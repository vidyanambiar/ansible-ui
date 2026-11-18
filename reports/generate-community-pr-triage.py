#!/usr/bin/env python3
"""Generate community PR triage markdown with Jira Priority and Affects version.

Requires: GH_ANSIBLE_UI_TOKEN, JIRA_URL, JIRA_EMAIL, JIRA_API_TOKEN
(see .cursor/rules/creds.mdc — use REST API, not /browse/)

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


def jira_rest_issue_url(jira_url: str, issue_key: str, fields: str) -> str:
    base = jira_url.rstrip("/")
    return f"{base}/rest/api/3/issue/{issue_key}?fields={fields}"


def jira_browse_url(jira_url: str, issue_key: str) -> str:
    return f"{jira_url.rstrip('/')}/browse/{issue_key}"


def verify_jira_access(jira_url: str, email: str, token: str) -> None:
    """Fail fast when the token cannot read a representative AAP defect issue."""
    headers = jira_headers(email, token)
    probe_key = "AAP-93628"
    public_key = "AAPRFE-3174"
    probe_url = jira_rest_issue_url(jira_url, probe_key, "priority,versions")
    request = urllib.request.Request(probe_url, headers=headers)
    try:
        http_json(request)
        print(f"Jira: API token can read {probe_key}.", file=sys.stderr)
        return
    except urllib.error.HTTPError as error:
        if error.code != 404:
            print(
                f"Jira: probe {probe_key} returned HTTP {error.code}; continuing.",
                file=sys.stderr,
            )
            return

    public_url = jira_rest_issue_url(jira_url, public_key, "summary")
    public_anonymous = False
    try:
        http_json(urllib.request.Request(public_url, headers={"Accept": "application/json"}))
        public_anonymous = True
    except urllib.error.HTTPError:
        pass

    print(
        f"Jira: cannot read {probe_key} via REST (HTTP 404). "
        f"Browse URL works in SSO browser: {jira_browse_url(jira_url, probe_key)}",
        file=sys.stderr,
    )
    if public_anonymous:
        print(
            "Jira: AAPRFE issues may work without token access; AAP defect issues need "
            "Browse on project AAP for the API token user. See .cursor/rules/creds.mdc",
            file=sys.stderr,
        )


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
    browse_url = jira_browse_url(jira_url, issue_key)
    url = jira_rest_issue_url(jira_url, issue_key, "summary,priority,versions,status")
    request = urllib.request.Request(url, headers=headers)
    try:
        data = http_json(request)
    except urllib.error.HTTPError as error:
        # Jira Cloud uses 404 for both missing issues and missing Browse permission.
        return {
            "key": issue_key,
            "found": False,
            "error": error.code,
            "access_denied_likely": error.code == 404,
            "browse_url": browse_url,
        }

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
        "browse_url": browse_url,
    }


def unresolved_jira_label(issue: dict[str, Any]) -> str:
    if issue.get("error") == 404:
        return "No API access (404)"
    return f"Unresolved (HTTP {issue.get('error', '?')})"


def unresolved_jira_note(issue: dict[str, Any]) -> str:
    browse_url = issue.get("browse_url", "")
    if issue.get("error") == 404:
        return (
            f"[View in Jira]({browse_url}) — Priority/Affects not returned by API "
            f"(open in browser or grant token Browse on AAP)"
        )
    return f"[View in Jira]({browse_url}) — API HTTP {issue.get('error', '?')}"


def format_versions(versions: list[str]) -> str:
    return ", ".join(versions) if versions else "—"


# Lower number = higher urgency (Jira default names at Red Hat).
PRIORITY_RANK: dict[str, int] = {
    "Blocker": 0,
    "Critical": 1,
    "Major": 2,
    "High": 3,
    "Normal": 4,
    "Minor": 5,
    "Low": 6,
    "Trivial": 7,
    "Undefined": 8,
}


def priority_rank(priority_name: str | None) -> int:
    if not priority_name or priority_name == "—":
        return 9
    return PRIORITY_RANK.get(priority_name, 8)


def best_priority_for_keys(keys: list[str], jira: dict[str, dict[str, Any]]) -> int:
    ranks = [
        priority_rank(jira.get(key, {}).get("priority"))
        for key in keys
        if jira.get(key, {}).get("found")
    ]
    return min(ranks) if ranks else 9


def format_priority_column(keys: list[str], jira: dict[str, dict[str, Any]]) -> str:
    values: list[str] = []
    for key in keys:
        issue = jira.get(key, {})
        if not issue.get("found"):
            continue
        values.append(issue.get("priority") or "—")
    return "; ".join(values) if values else "—"


def format_affects_column(keys: list[str], jira: dict[str, dict[str, Any]]) -> str:
    values: list[str] = []
    for key in keys:
        issue = jira.get(key, {})
        if not issue.get("found"):
            continue
        values.append(format_versions(issue.get("affects_versions") or []))
    return "; ".join(values) if values else "—"


def format_jira_key_links(
    keys: list[str], jira: dict[str, dict[str, Any]], jira_url: str
) -> str:
    if not keys:
        return "—"
    links: list[str] = []
    for key in keys:
        issue = jira.get(key, {})
        browse_url = issue.get("browse_url") or jira_browse_url(jira_url, key)
        links.append(f"[{key}]({browse_url})")
    return ", ".join(links)


def issue_row_note(key: str, issue: dict[str, Any], jira_url: str, *, multi: bool) -> str:
    if issue.get("found"):
        summary = (issue.get("summary") or "").replace("|", "\\|")
        if len(summary) > 72:
            summary = f"{summary[:69]}..."
        prefix = f"**{key}:** " if multi else ""
        return f"{prefix}Status {issue.get('status', '—')} — {summary}"
    if not issue.get("browse_url"):
        issue = {
            **issue,
            "browse_url": jira_browse_url(jira_url, key),
        }
    return f"**{key}:** {unresolved_jira_note(issue)}"


def primary_jira_row(
    keys: list[str], jira: dict[str, dict[str, Any]], jira_url: str
) -> tuple[str, str, str, str]:
    if not keys:
        return "—", "—", "—", "No Jira key in PR title/body"

    key_col = format_jira_key_links(keys, jira, jira_url)
    multi = len(keys) > 1
    note_parts = [
        issue_row_note(key, jira.get(key, {"found": False, "key": key}), jira_url, multi=multi)
        for key in keys
    ]
    priority_col = format_priority_column(keys, jira)
    version_col = format_affects_column(keys, jira)
    notes_col = " · ".join(note_parts)
    return key_col, priority_col, version_col, notes_col


def render_report(
    snapshot: str, prs: list[dict[str, Any]], jira: dict[str, dict[str, Any]], jira_url: str
) -> str:
    linked = sum(1 for pr in prs if pr["jira_keys"])
    resolved_keys = sum(1 for issue in jira.values() if issue.get("found"))

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
        f"| **Jira keys resolved via API** | {resolved_keys}/{len(jira)} unique keys |",
        "",
        "Jira keys are parsed from each PR **title and body** (`PROJ-123` pattern). "
        "Rows are sorted by **highest Jira Priority** on the linked issue(s), then PR number (newest first). "
        "PRs with multiple keys use `;` in Priority / Affects version (same order as Jira key column).",
        "",
        "**API vs browser:** Jira Cloud returns **HTTP 404** when an issue is missing *or* when the API token lacks **Browse** permission. A `AAP-*` key that opens in the browser may still show as 404 in this report until the token can browse the **AAP** defect project (not only **AAPRFE**).",
        "",
        "---",
        "",
        "## Jira linkage (Priority & Affects version)",
        "",
        "| PR | Jira key(s) | Priority | Affects version(s) | Notes |",
        "| ---: | --- | --- | --- | --- |",
    ]

    def sort_pr_for_jira(item: dict[str, Any]) -> tuple[int, int]:
        rank = best_priority_for_keys(item["jira_keys"], jira)
        return (rank, -item["number"])

    for pr in sorted(prs, key=sort_pr_for_jira):
        keys, priority, versions, notes = primary_jira_row(pr["jira_keys"], jira, jira_url)
        lines.append(
            f"| [#{pr['number']}](https://github.com/ansible/ansible-ui/pull/{pr['number']}) "
            f"| {keys} | {priority} | {versions} | {notes} |"
        )

    lines.extend(
        [
            "",
            "---",
            "",
            "## Full inventory (with Jira)",
            "",
            "| PR | Title | Author | Jira key(s) | Priority | Affects version(s) | Notes | Link |",
            "| ---: | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )

    for pr in sorted(prs, key=lambda item: item["number"], reverse=True):
        keys, priority, versions, notes = primary_jira_row(pr["jira_keys"], jira, jira_url)
        title = pr["title"].replace("|", "\\|")
        lines.append(
            f"| {pr['number']} | {title} | {pr['author']} | {keys} | {priority} | {versions} "
            f"| {notes} | [PR](https://github.com/ansible/ansible-ui/pull/{pr['number']}) |"
        )

    lines.extend(
        [
            "",
            "---",
            "",
            "## Regenerating this report",
            "",
            "Set credentials per `.cursor/rules/creds.mdc`, then:",
            "",
            "```bash",
            "python3 reports/generate-community-pr-triage.py \\",
            f"  --output reports/community-pr-triage-{snapshot}.md",
            "```",
            "",
            "**Note:** If `AAP-*` keys return Jira **404**, the issue often still exists at",
            "`https://redhat.atlassian.net/browse/<KEY>` in your browser — grant the API token user",
            "**Browse** on the **AAP** defect project, or regenerate with a personal token tied to that account.",
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
    parser.add_argument(
        "--skip-jira-probe",
        action="store_true",
        help="Skip startup check for AAP defect REST access",
    )
    args = parser.parse_args()

    gh_token = env("GH_ANSIBLE_UI_TOKEN")
    jira_url = env("JIRA_URL")
    jira_email = env("JIRA_EMAIL")
    jira_token = env("JIRA_API_TOKEN")
    headers = jira_headers(jira_email, jira_token)
    if not args.skip_jira_probe:
        verify_jira_access(jira_url, jira_email, jira_token)

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

    markdown = render_report(args.snapshot, pr_rows, jira, jira_url)
    with open(args.output, "w", encoding="utf-8") as handle:
        handle.write(markdown)
    print(f"Wrote {args.output} ({len(pr_rows)} PRs, {len(all_keys)} Jira keys)")


if __name__ == "__main__":
    main()