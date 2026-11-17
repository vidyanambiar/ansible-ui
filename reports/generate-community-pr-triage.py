#!/usr/bin/env python3
"""Generate community PR triage markdown with Jira Priority and Affects version.

Requires: GH_ANSIBLE_UI_TOKEN, JIRA_URL, JIRA_EMAIL, JIRA_API_TOKEN
(see .cursor/creds.mdc)

Usage:
  python3 reports/generate-community-pr-triage.py \
    --output reports/community-pr-triage-YYYY-MM-DD.md
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import date
from typing import Any

ISSUE_KEY_PATTERN = re.compile(r"\b([A-Z][A-Z0-9_]*-\d+)\b")
SKIP_KEY_PREFIXES = ("CVE-",)


def env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        print(f"Missing required environment variable: {name}", file=sys.stderr)
        sys.exit(1)
    return value


def gh_headers(token: str) -> dict[str, str]:
    return {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }


def jira_headers(email: str, token: str) -> dict[str, str]:
    auth = base64.b64encode(f"{email}:{token}".encode()).decode()
    return {"Accept": "application/json", "Authorization": f"Basic {auth}"}


def http_json(request: urllib.request.Request) -> Any:
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.load(response)


def fetch_community_prs(token: str) -> list[dict[str, Any]]:
    url = "https://api.github.com/repos/ansible/ansible-ui/pulls?state=open&per_page=100"
    pulls = http_json(urllib.request.Request(url, headers=gh_headers(token)))
    return [p for p in pulls if any(label.get("name") == "community" for label in p.get("labels", []))]


def extract_jira_keys(title: str, body: str | None) -> list[str]:
    text = f"{title}\n{body or ''}"
    keys: list[str] = []
    for match in ISSUE_KEY_PATTERN.finditer(text):
        key = match.group(1)
        if any(key.startswith(prefix) for prefix in SKIP_KEY_PREFIXES):
            continue
        if key not in keys:
            keys.append(key)
    return keys


def fetch_jira_issue(
    jira_url: str, headers: dict[str, str], issue_key: str
) -> dict[str, Any]:
    url = f"{jira_url.rstrip('/')}/rest/api/3/issue/{issue_key}?fields=summary,priority,versions,status"
    request = urllib.request.Request(url, headers=headers)
    try:
        data = http_json(request)
    except urllib.error.HTTPError as error:
        return {"key": issue_key, "found": False, "error": error.code}

    fields = data.get("fields", {})
    versions = [version.get("name", "") for version in fields.get("versions") or []]
    priority = (fields.get("priority") or {}).get("name") or ""
    status = (fields.get("status") or {}).get("name") or ""
    return {
        "key": issue_key,
        "found": True,
        "summary": fields.get("summary", ""),
        "priority": priority,
        "affects_versions": [version for version in versions if version],
        "status": status,
        "browse_url": f"{jira_url.rstrip('/')}/browse/{issue_key}",
    }


def format_versions(versions: list[str]) -> str:
    return ", ".join(versions) if versions else "—"


def primary_jira_row(keys: list[str], jira: dict[str, dict[str, Any]]) -> tuple[str, str, str, str]:
    if not keys:
        return "—", "—", "—", "No Jira key in PR title/body"

    priorities: list[str] = []
    version_groups: list[str] = []
    statuses: list[str] = []
    missing: list[str] = []

    for key in keys:
        issue = jira.get(key, {"found": False})
        if not issue.get("found"):
            missing.append(key)
            continue
        priority = issue.get("priority") or "—"
        versions = format_versions(issue.get("affects_versions") or [])
        priorities.append(f"{key}: {priority}")
        version_groups.append(f"{key}: {versions}")
        statuses.append(f"{key}: {issue.get('status', '—')}")

    key_col = ", ".join(keys)
    if missing and not priorities:
        return key_col, "—", "—", f"Not found in Jira ({', '.join(missing)})"

    note_parts: list[str] = []
    if missing:
        note_parts.append(f"Not found: {', '.join(missing)}")
    if priorities:
        note_parts.append("; ".join(statuses))
    return key_col, "; ".join(priorities) if priorities else "—", "; ".join(version_groups) if version_groups else "—", " | ".join(note_parts)


def render_report(snapshot: str, prs: list[dict[str, Any]], jira: dict[str, dict[str, Any]]) -> str:
    linked = sum(1 for pr in prs if pr["jira_keys"])
    resolved = sum(1 for pr in prs if any(jira.get(k, {}).get("found") for k in pr["jira_keys"]))

    lines: list[str] = [
        "# Community PR triage report — ansible-ui",
        "",
        "| Field | Value |",
        "| --- | --- |",
        f"| **Snapshot date** | {snapshot} |",
        "| **Filter** | [Open PRs with `community` label](https://github.com/ansible/ansible-ui/pulls?q=is%3Apr+state%3Aopen+label%3Acommunity) |",
        f"| **Total open** | {len(prs)} |",
        "| **GitHub data** | `GH_ANSIBLE_UI_TOKEN` |",
        "| **Jira data** | `JIRA_URL` — fields: **Priority**, **Affects version** (`versions`) |",
        f"| **PRs with Jira key(s)** | {linked}/{len(prs)} |",
        f"| **Jira keys resolved** | {resolved} issue lookup(s) across PRs |",
        "",
        "Jira keys are parsed from each PR **title and body** (`PROJ-123` pattern). When multiple keys appear on one PR, Priority and Affects version are shown per key.",
        "",
        "---",
        "",
        "## Jira linkage (Priority & Affects version)",
        "",
        "| PR | Jira key(s) | Priority | Affects version(s) | Notes |",
        "| ---: | --- | --- | --- | --- |",
    ]

    for pr in sorted(prs, key=lambda item: item["number"], reverse=True):
        keys, priority, versions, notes = primary_jira_row(pr["jira_keys"], jira)
        title = pr["title"].replace("|", "\\|")
        lines.append(
            f"| [#{pr['number']}](https://github.com/ansible/ansible-ui/pull/{pr['number']}) "
            f"| {keys} | {priority} | {versions} | {notes} |"
        )

    lines.extend(
        [
            "",
            "### Jira issues referenced (deduplicated)",
            "",
            "| Key | Priority | Affects version(s) | Status | Summary |",
            "| --- | --- | --- | --- | --- |",
        ]
    )

    for key in sorted(jira.keys()):
        issue = jira[key]
        if issue.get("found"):
            lines.append(
                f"| [{key}]({issue.get('browse_url', '')}) | {issue.get('priority', '—')} "
                f"| {format_versions(issue.get('affects_versions') or [])} | {issue.get('status', '—')} "
                f"| {issue.get('summary', '').replace('|', '\\|')} |"
            )
        else:
            lines.append(f"| {key} | — | — | Not found ({issue.get('error', '?')}) | — |")

    lines.extend(
        [
            "",
            "---",
            "",
            "## Full inventory (with Jira)",
            "",
            "| PR | Title | Author | Jira key(s) | Priority | Affects version(s) | Link |",
            "| ---: | --- | --- | --- | --- | --- | --- |",
        ]
    )

    for pr in sorted(prs, key=lambda item: item["number"], reverse=True):
        keys, priority, versions, _ = primary_jira_row(pr["jira_keys"], jira)
        title = pr["title"].replace("|", "\\|")
        lines.append(
            f"| {pr['number']} | {title} | {pr['author']} | {keys} | {priority} | {versions} "
            f"| [PR](https://github.com/ansible/ansible-ui/pull/{pr['number']}) |"
        )

    lines.extend(
        [
            "",
            "---",
            "",
            "## Regenerating this report",
            "",
            "Set credentials per `.cursor/creds.mdc`, then:",
            "",
            "```bash",
            "python3 reports/generate-community-pr-triage.py \\",
            f"  --output reports/community-pr-triage-{snapshot}.md",
            "```",
            "",
            "**Note:** If `AAP-*` keys return Jira 404, those issues may be outside your Jira project scope",
            "or not migrated to `redhat.atlassian.net`. `AAPRFE-*` keys typically resolve for contributors",
            "with AAP RFE project access.",
            "",
        ]
    )

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        default=f"reports/community-pr-triage-{date.today().isoformat()}.md",
        help="Output markdown path",
    )
    parser.add_argument("--snapshot", default=date.today().isoformat(), help="Snapshot date (YYYY-MM-DD)")
    args = parser.parse_args()

    gh_token = env("GH_ANSIBLE_UI_TOKEN")
    jira_url = env("JIRA_URL")
    jira_email = env("JIRA_EMAIL")
    jira_token = env("JIRA_API_TOKEN")
    headers = jira_headers(jira_email, jira_token)

    pulls = fetch_community_prs(gh_token)
    pr_rows: list[dict[str, Any]] = []
    all_keys: set[str] = set()

    for pull in pulls:
        keys = extract_jira_keys(pull.get("title", ""), pull.get("body"))
        all_keys.update(keys)
        pr_rows.append(
            {
                "number": pull["number"],
                "title": pull.get("title", ""),
                "author": pull.get("user", {}).get("login", ""),
                "jira_keys": keys,
            }
        )

    jira: dict[str, dict[str, Any]] = {}
    for key in sorted(all_keys):
        time.sleep(0.12)
        jira[key] = fetch_jira_issue(jira_url, headers, key)

    markdown = render_report(args.snapshot, pr_rows, jira)
    with open(args.output, "w", encoding="utf-8") as handle:
        handle.write(markdown)
    print(f"Wrote {args.output} ({len(pr_rows)} PRs, {len(all_keys)} Jira keys)")


if __name__ == "__main__":
    main()