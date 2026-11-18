# Community PR triage report — ansible-ui

| Field | Value |
| --- | --- |
| **Snapshot date** | 2026-11-17 |
| **Filter** | [Open PRs with `community` label](https://github.com/ansible/ansible-ui/pulls?q=is%3Apr+state%3Aopen+label%3Acommunity) |
| **Total open** | 21 |
| **GitHub data** | Authenticated API (`GH_ANSIBLE_UI_TOKEN`) — includes PR **assignees** and labels |
| **Jira data** | `JIRA_URL` — **Priority** and **Affects version** (`versions`) per key in PR title/body |
| **PRs with GitHub assignee** | 18/21 |
| **Unassigned, ready for review** | 1 |
| **PRs with Jira key(s)** | 13/21 |
| **Jira keys resolved via API** | 14/14 unique keys |

## Community triage process

Use this report in a **UI foundation pod** meeting to **assign GitHub assignees** on `community` PRs that are **ready for maintainer review**, then track assigned work between meetings.

### Jira-linked PRs (issue key in PR title/body)

These are often **customer bug fixes**. In the meeting:

1. A UI foundation pod member becomes the **GitHub assignee** on the PR.
2. That person **claims the linked Jira issue(s)** and shepherds the work to completion.
3. **Author communication happens in Jira**, not on the PR thread (more effective for this queue).
4. The assignee **opens and drives any needed backport PRs** through review and merge.

### PRs without a Jira key in the PR text

1. A UI team member is set as **GitHub assignee** and owns **code review and merge**.
2. The assignee **opens and drives backport PRs** when applicable.

Assignee columns below come from live GitHub data (regenerate with `reports/generate-community-pr-triage.py`).

---

## Ready for review — assign in meeting

Pick **GitHub assignees** on review-ready PRs in the meeting. **Fast path** = batch-friendly (`risk:low` or small Jira fix, not waiting on author, Jira priority below **Major**). Fast path is listed here **only while unassigned**; once assigned, batch-review under **Assigned — follow-up**.

### Needs assignee (1)

| PR | Fast path | Title | Track | Jira | Priority | Notes |
| ---: | :---: | --- | --- | --- | --- | --- |
| [#3843](https://github.com/ansible/ansible-ui/pull/3843) | — | fix(hub): keep collection when browsing versions (AAP-100265) | Jira-linked | [AAP-100265](https://redhat.atlassian.net/browse/AAP-100265) | Major | add `risk:*` before merge; **Major** Jira — not fast path |

### Fast path — already assigned (7)

| Assignee | PRs (batch review) |
| --- | --- |
| @acruzgon | [#3874](https://github.com/ansible/ansible-ui/pull/3874), [#3840](https://github.com/ansible/ansible-ui/pull/3840), [#3827](https://github.com/ansible/ansible-ui/pull/3827) |
| @vidyanambiar | [#3911](https://github.com/ansible/ansible-ui/pull/3911), [#3908](https://github.com/ansible/ansible-ui/pull/3908), [#3902](https://github.com/ansible/ansible-ui/pull/3902), [#3881](https://github.com/ansible/ansible-ui/pull/3881) |

_2 other open community PRs have no assignee but are **not** review-ready (`waiting-on-author` and/or merge conflicts on [#3865](https://github.com/ansible/ansible-ui/pull/3865), [#3848](https://github.com/ansible/ansible-ui/pull/3848)) — assign when review-ready._

---

## Assigned — follow-up (18 PRs)

GitHub assignee already set — check Jira ownership, author status, backports. **Fast path** = batch small review-ready PRs under the same assignee.

| PR | Assignee | Fast path | Track | Jira | Priority | Waiting on author |
| ---: | --- | :---: | --- | --- | --- | :---: |
| [#3874](https://github.com/ansible/ansible-ui/pull/3874) | @acruzgon | Yes | Jira-linked | [AAP-99022](https://redhat.atlassian.net/browse/AAP-99022) | Normal | |
| [#3840](https://github.com/ansible/ansible-ui/pull/3840) | @acruzgon | Yes | Jira-linked | [AAPRFE-3174](https://redhat.atlassian.net/browse/AAPRFE-3174) | Normal | |
| [#3827](https://github.com/ansible/ansible-ui/pull/3827) | @acruzgon | Yes | Jira-linked | [AAP-85721](https://redhat.atlassian.net/browse/AAP-85721), [AAP-99473](https://redhat.atlassian.net/browse/AAP-99473) | Normal; Undefined | |
| [#3767](https://github.com/ansible/ansible-ui/pull/3767) | @acruzgon | — | Community (no Jira in PR) | — | — | Yes |
| [#3761](https://github.com/ansible/ansible-ui/pull/3761) | @acruzgon | — | Jira-linked | [AAP-66504](https://redhat.atlassian.net/browse/AAP-66504) | Minor | Yes |
| [#3752](https://github.com/ansible/ansible-ui/pull/3752) | @acruzgon | — | Community (no Jira in PR) | — | — | Yes |
| [#3740](https://github.com/ansible/ansible-ui/pull/3740) | @acruzgon | — | Jira-linked | [AAPRFE-409](https://redhat.atlassian.net/browse/AAPRFE-409) | Undefined | Yes |
| [#3706](https://github.com/ansible/ansible-ui/pull/3706) | @acruzgon | — | Jira-linked | [AAP-65215](https://redhat.atlassian.net/browse/AAP-65215) | Normal | Yes |
| [#3770](https://github.com/ansible/ansible-ui/pull/3770) | @lgalis | — | Community (no Jira in PR) | — | — | Yes |
| [#3702](https://github.com/ansible/ansible-ui/pull/3702) | @lgalis | — | Community (no Jira in PR) | — | — | Yes |
| [#3687](https://github.com/ansible/ansible-ui/pull/3687) | @lgalis | — | Jira-linked | [AAP-95292](https://redhat.atlassian.net/browse/AAP-95292) | Normal | Yes |
| [#3686](https://github.com/ansible/ansible-ui/pull/3686) | @lgalis | — | Community (no Jira in PR) | — | — | Yes |
| [#3680](https://github.com/ansible/ansible-ui/pull/3680) | @lgalis | — | Community (no Jira in PR) | — | — | Yes |
| [#3552](https://github.com/ansible/ansible-ui/pull/3552) | @lgalis | — | Community (no Jira in PR) | — | — | Yes |
| [#3911](https://github.com/ansible/ansible-ui/pull/3911) | @vidyanambiar | Yes | Jira-linked | [AAP-93628](https://redhat.atlassian.net/browse/AAP-93628) | Normal | |
| [#3908](https://github.com/ansible/ansible-ui/pull/3908) | @vidyanambiar | Yes | Jira-linked | [AAP-65130](https://redhat.atlassian.net/browse/AAP-65130) | Normal | |
| [#3902](https://github.com/ansible/ansible-ui/pull/3902) | @vidyanambiar | Yes | Jira-linked | [AAP-93673](https://redhat.atlassian.net/browse/AAP-93673) | Normal | |
| [#3881](https://github.com/ansible/ansible-ui/pull/3881) | @vidyanambiar | Yes | Community (no Jira in PR) | — | — | |

---

Community volume is concentrated: **swatinarvekar (6)**, **demonpig (3)**, **pshekhaw (2)**; the rest are one PR each. Many carry **`pr reviewed using repo skills`**. **`waiting-on-author`** appears on 14/21 — most of the queue is feedback-pending, not unreviewed.

---

## Executive summary

| Bucket | Count | Team action |
| --- | ---: | --- |
| Ready for maintainer review (no `waiting-on-author`) | 8 | Assign reviewers this week; prioritize XS/S bug fixes |
| Author follow-up required | 14 | Triage stale vs. one nudge from merge |
| Merge conflicts (`mergeable_state: dirty`) | 4 | Author rebase before deep review |
| Cross-cutting / framework | 4 | Framework + i18n owners |
| Large features / coordination | 3 | Dedicated design + API dependency review |

**Dirty merge (at snapshot):** [#3552](https://github.com/ansible/ansible-ui/pull/3552), [#3865](https://github.com/ansible/ansible-ui/pull/3865), [#3767](https://github.com/ansible/ansible-ui/pull/3767), [#3761](https://github.com/ansible/ansible-ui/pull/3761)

**Jira note:** All linked keys resolved via REST at snapshot time. Highest **Priority** in queue: **Major** — [AAP-100265](https://redhat.atlassian.net/browse/AAP-100265) (Hub collection browse, 2.6/2.7). [#3827](https://github.com/ansible/ansible-ui/pull/3827) also references [AAP-99473](https://redhat.atlassian.net/browse/AAP-99473) (**Closed**).

---

## Jira linkage (by Jira priority)

Community PRs that **reference Jira in the PR** — an issue key (`PROJ-123`) in the **title or body**. Columns are filled from Jira (**Priority**, **Affects version**, status/summary). Sorted by highest linked **Priority**, then PR #. PRs with **no Jira key in the PR text** are omitted.

| PR | Jira | Priority | Affects version | Jira status / summary |
| ---: | --- | --- | --- | --- |
| [#3843](https://github.com/ansible/ansible-ui/pull/3843) | [AAP-100265](https://redhat.atlassian.net/browse/AAP-100265) | Major | 2.6, 2.7 | Status Backlog — BUG - Private Automation Hub: Browse version selection drops collecti... |
| [#3911](https://github.com/ansible/ansible-ui/pull/3911) | [AAP-93628](https://redhat.atlassian.net/browse/AAP-93628) | Normal | 2.6, 2.6.20260701 | Status Backlog — Host selection checkboxes are missing in constructed inventories (reg... |
| [#3908](https://github.com/ansible/ansible-ui/pull/3908) | [AAP-65130](https://redhat.atlassian.net/browse/AAP-65130) | Normal | 2.6 | Status Backlog — Cannot upload custom logo in AAP2.6 |
| [#3902](https://github.com/ansible/ansible-ui/pull/3902) | [AAP-93673](https://redhat.atlassian.net/browse/AAP-93673) | Normal | 2.6 | Status Backlog —  [UI] "Clone Template" button fails silently without user-facing erro... |
| [#3874](https://github.com/ansible/ansible-ui/pull/3874) | [AAP-99022](https://redhat.atlassian.net/browse/AAP-99022) | Normal | 2.6 | Status New — Cannot filter the management tasks by "name" under Automation Content |
| [#3865](https://github.com/ansible/ansible-ui/pull/3865) | [AAP-101258](https://redhat.atlassian.net/browse/AAP-101258) | Normal | — | Status New — Native Boolean Survey Answer Type |
| [#3848](https://github.com/ansible/ansible-ui/pull/3848) | [AAP-99868](https://redhat.atlassian.net/browse/AAP-99868) | Normal | 2.6 | Status Backlog — Let the textarea size in surveys be adjustable so multi-line answers ... |
| [#3840](https://github.com/ansible/ansible-ui/pull/3840) | [AAPRFE-3174](https://redhat.atlassian.net/browse/AAPRFE-3174) | Normal | 2.6, 2.7 | Status New — Add dynamic/live search filtering to the Organizations page  |
| [#3827](https://github.com/ansible/ansible-ui/pull/3827) | [AAP-85721](https://redhat.atlassian.net/browse/AAP-85721), [AAP-99473](https://redhat.atlassian.net/browse/AAP-99473) | Normal; Undefined | 2.6, 2.7; 2.7 | **AAP-85721:** Status Backlog — Deleting a resource in use by another resource no longer shows a warn... · **AAP-99473:** Status Closed — Deleting a credential succeeds when the credential is used by a project |
| [#3706](https://github.com/ansible/ansible-ui/pull/3706) | [AAP-65215](https://redhat.atlassian.net/browse/AAP-65215) | Normal | 2.6 | Status Backlog — Workflow Job Template node tags are multiplied and cannot be cleared ... |
| [#3687](https://github.com/ansible/ansible-ui/pull/3687) | [AAP-95292](https://redhat.atlassian.net/browse/AAP-95292) | Normal | 2.6.20261019, 2.7.20261005 | Status New — Workflow Job Template extra_vars UI truncates long numeric strings (1... |
| [#3761](https://github.com/ansible/ansible-ui/pull/3761) | [AAP-66504](https://redhat.atlassian.net/browse/AAP-66504) | Minor | 2.5, 2.6, 2.7 | Status Backlog — "Copy to clipboard" button has various results |
| [#3740](https://github.com/ansible/ansible-ui/pull/3740) | [AAPRFE-409](https://redhat.atlassian.net/browse/AAPRFE-409) | Undefined | 2.3, 2.6, 2.7 | Status Backlog — Allow users to clear the galaxy cache |

---

## By product / workspace

### Controller (AWX)

| PR | Title / theme | Size | Status |
| ---: | --- | --- | --- |
| [#3911](https://github.com/ansible/ansible-ui/pull/3911) | Constructed inventory checkboxes | XS | Assigned; fast path |
| [#3902](https://github.com/ansible/ansible-ui/pull/3902) | Duplicate template error toast | M | Assigned; fast path |
| [#3827](https://github.com/ansible/ansible-ui/pull/3827) | Delete JT in-use warning | S | Assigned; fast path |
| [#3770](https://github.com/ansible/ansible-ui/pull/3770) | Allow clearing schedule limit | XS | `waiting-on-author`; `e2e: pending` |
| [#3706](https://github.com/ansible/ansible-ui/pull/3706) | Persist cleared workflow node tags (AAP-65215) | S | `waiting-on-author`; save-path after #3705 |
| [#3687](https://github.com/ansible/ansible-ui/pull/3687) | WJT `extra_vars` numeric precision (AAP-95292) | XS | `waiting-on-author`; minimal tests |
| [#3686](https://github.com/ansible/ansible-ui/pull/3686) | Project / inventory source status links | S | `waiting-on-author`; larger diff (~297 lines) |
| [#3740](https://github.com/ansible/ansible-ui/pull/3740) | `galaxy_update_on_launch` UI | S | `waiting-on-author`; merge clean |
| [#3865](https://github.com/ansible/ansible-ui/pull/3865) | Boolean survey answers (AAP-101258) | M | **Dirty**; depends on [AWX #16782](https://github.com/ansible/awx/pull/16782) |
| [#3552](https://github.com/ansible/ansible-ui/pull/3552) | Conditional / dynamic surveys | L | **Dirty**; ~1.8k LOC; reviewers: `h-kataria`, `redhat-chai-bot` |

**Survey track:** Treat [#3552](https://github.com/ansible/ansible-ui/pull/3552) and [#3865](https://github.com/ansible/ansible-ui/pull/3865) as one program. Do not merge [#3865](https://github.com/ansible/ansible-ui/pull/3865) until AWX API lands.

### Hub

| PR | Title | Status |
| ---: | --- | --- |
| [#3874](https://github.com/ansible/ansible-ui/pull/3874) | Task management exact name filter | Assigned; fast path |
| [#3843](https://github.com/ansible/ansible-ui/pull/3843) | Collection browse / version URL (AAP-100265) | **Needs assignee**; Major Jira; missing `risk:*` |

### Platform

| PR | Title | Status |
| ---: | --- | --- |
| [#3908](https://github.com/ansible/ansible-ui/pull/3908) | Custom logo upload | Assigned; fast path |
| [#3840](https://github.com/ansible/ansible-ui/pull/3840) | Organizations async filters | Assigned; fast path |

### EDA

| PR | Title | Status |
| ---: | --- | --- |
| [#3752](https://github.com/ansible/ansible-ui/pull/3752) | Rulebook activation help text | `waiting-on-author`; 16 locale files; reviewers requested |
| [#3706](https://github.com/ansible/ansible-ui/pull/3706) | Workflow node tags clear | `waiting-on-author`; also controller-related |

### Framework / shared UI

| PR | Title | Risk / status |
| ---: | --- | --- |
| [#3848](https://github.com/ansible/ansible-ui/pull/3848) | Survey textarea multi-line defaults (`PageFormTextArea`) | `risk:medium`; stale since 2026-11-02 |
| [#3761](https://github.com/ansible/ansible-ui/pull/3761) | Copy-to-clipboard YAML/JSON (AAP-66504) | **Dirty**; `waiting-on-author` |
| [#3680](https://github.com/ansible/ansible-ui/pull/3680) | User language preference | `risk:medium`; merge clean; ~789 LOC |

Deliver framework behavior with dedicated framework review per repository policy.

### Docs and dependencies

| PR | Title | Status |
| ---: | --- | --- |
| [#3702](https://github.com/ansible/ansible-ui/pull/3702) | Translation contribution guide | Merge clean; docs-only quick-approve candidate |
| [#3767](https://github.com/ansible/ansible-ui/pull/3767) | npm audit (dompurify, js-yaml, nanoid, vite) | **Dirty**; build/security owner |

### Tests only

| PR | Title | Status |
| ---: | --- | --- |
| [#3881](https://github.com/ansible/ansible-ui/pull/3881) | Overview hosts Ready/Failed redirect E2E | Assigned; fast path |

---

## Blockers checklist

| Signal | PRs | Action |
| --- | --- | --- |
| Merge conflicts | #3552, #3865, #3767, #3761 | Rebase on `main` before deep review |
| Missing risk analysis | #3902, #3865, #3843 | Add risk section before merge |
| External API dependency | #3865 | Block until [AWX #16782](https://github.com/ansible/awx/pull/16782) merges |
| Weak test signal | #3687 | Minimal regression test or documented manual QA |
| Stale (2+ weeks at snapshot) | #3848, #3843, #3687 | Ping author or apply stale policy |
| Recently updated | #3911, #3908, #3865, #3767, #3552 | Prioritize reviewer bandwidth |

---

## Regenerating this report

Credential env vars are listed in `.cursor/rules/creds.mdc` (`GH_ANSIBLE_UI_TOKEN`, `JIRA_URL`, `JIRA_EMAIL`, `JIRA_API_TOKEN`).

Refresh **assignee tables** and **Jira linkage** (re-run against live GitHub + Jira):

```bash
source ~/.zshenv
python3 reports/generate-community-pr-triage.py \
  --output reports/community-pr-triage-$(date +%Y-%m-%d).md
```

The generator writes process text, **Ready for review — assign in meeting** / **Assigned — follow-up**, and Jira linkage tables. Merge into the narrative sections of this doc or extend the script to emit the full triage template.

GitHub-only snapshot:

```bash
gh pr list --repo ansible/ansible-ui --label community --state open --limit 100 \
  --json number,title,author,labels,additions,deletions,changedFiles,url,isDraft,updatedAt,body
```
