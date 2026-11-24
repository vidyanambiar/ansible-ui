# Community PR triage report — ansible-ui

| Field | Value |
| --- | --- |
| **Snapshot date** | 2026-11-24 |
| **Filter** | [Open PRs with `community` label](https://github.com/ansible/ansible-ui/pulls?q=is%3Apr+state%3Aopen+label%3Acommunity) |
| **Total open** | 24 |
| **GitHub data** | GitHub (`gh api`, authenticated as chai-bot) |
| **Jira data** | Jira REST (`https://redhat.atlassian.net`) |
| **PRs with GitHub assignee** | 17/24 |
| **Unassigned, ready for review** | 4 |
| **PRs with Jira key(s)** | 16/24 |
| **Jira keys resolved via API** | 17/17 unique keys |

## Community triage process

Use this report in a **UI foundation pod** meeting to **assign GitHub assignees** on
`community` PRs that are **ready for maintainer review**, then track assigned work between
meetings.

### Jira-linked PRs (issue key in PR title/body)

These are often **customer bug fixes**. In the meeting:

1. A UI foundation pod member becomes the **GitHub assignee** on the PR.
2. That person **claims the linked Jira issue(s)** and shepherds the work to completion.
3. **Author communication happens in Jira**, not on the PR thread (more effective for this queue).
4. The assignee **opens and drives any needed backport PRs** through review and merge.

### PRs without a Jira key in the PR text

1. A UI team member is set as **GitHub assignee** and owns **code review and merge**.
2. The assignee **opens and drives backport PRs** when applicable.

The tables below are generated from live GitHub **assignee** data.

---

## Ready for review — assign in meeting

Pick **GitHub assignees** on PRs that are review-ready. **Fast path** = batch-friendly 
(`risk:low`, review-ready; Jira-linked PRs need resolved priority below **Major**). 
Linked Jira without snapshot/priority is **not** fast path—still track customer work.
Fast-path rows appear here **only while unassigned**; once assigned, batch-review via
**Assigned — follow-up** (Fast path column).

### Needs assignee (4)

| PR | Fast path | Title | Track | Jira | Priority | Notes |
| ---: | :---: | --- | --- | --- | --- | --- |
| [#3932](https://github.com/ansible/ansible-ui/pull/3932) | — | AAP-102151: Include image tag in EE Images podman pul... | Jira-linked | [AAP-102151](https://redhat.atlassian.net/browse/AAP-102151) | Major | — |
| [#3843](https://github.com/ansible/ansible-ui/pull/3843) | — | fix(hub): keep the selected collection when browsing ... | Jira-linked | [AAP-100265](https://redhat.atlassian.net/browse/AAP-100265) | Major | add `risk:*` before merge if required |
| [#3931](https://github.com/ansible/ansible-ui/pull/3931) | — | AAP-102729 Fix authenticator type filter reported as ... | Jira-linked | [AAP-102729](https://redhat.atlassian.net/browse/AAP-102729) | Normal | add `risk:*` before merge if required |
| [#3929](https://github.com/ansible/ansible-ui/pull/3929) | — | AAP-102995 Add minHeight prop to DataEditor and PageF... | Jira-linked | [AAP-102995](https://redhat.atlassian.net/browse/AAP-102995) | Undefined | — |

### Fast path — already assigned (2)

| Assignee | PRs (batch review) |
| --- | --- |
| @vidyanambiar | [#3911](https://github.com/ansible/ansible-ui/pull/3911), [#3908](https://github.com/ansible/ansible-ui/pull/3908) |

_3 other open community PR(s) have no assignee but are **not** review-ready (waiting on author and/or merge conflicts) — assign when review-ready._

## Assigned — follow-up (17 PRs)

GitHub assignee already set — check Jira ownership, author status, backports.
Use **Fast path** to batch small review-ready PRs under the same assignee.

| PR | Assignee | Fast path | Track | Jira | Priority | Waiting on author |
| ---: | --- | :---: | --- | --- | --- | :---: |
| [#3874](https://github.com/ansible/ansible-ui/pull/3874) | @acruzgon | — | Jira-linked | [AAP-99022](https://redhat.atlassian.net/browse/AAP-99022) | Normal | Yes |
| [#3840](https://github.com/ansible/ansible-ui/pull/3840) | @acruzgon | — | Jira-linked | [AAPRFE-3174](https://redhat.atlassian.net/browse/AAPRFE-3174) | Normal | Yes |
| [#3827](https://github.com/ansible/ansible-ui/pull/3827) | @acruzgon | — | Jira-linked | [AAP-85721](https://redhat.atlassian.net/browse/AAP-85721), [AAP-99473](https://redhat.atlassian.net/browse/AAP-99473) | Normal; Undefined | Yes |
| [#3706](https://github.com/ansible/ansible-ui/pull/3706) | @acruzgon | — | Jira-linked | [AAP-65215](https://redhat.atlassian.net/browse/AAP-65215) | Normal | Yes |
| [#3761](https://github.com/ansible/ansible-ui/pull/3761) | @acruzgon | — | Jira-linked | [AAP-66504](https://redhat.atlassian.net/browse/AAP-66504) | Minor | Yes |
| [#3740](https://github.com/ansible/ansible-ui/pull/3740) | @acruzgon | — | Jira-linked | [AAPRFE-409](https://redhat.atlassian.net/browse/AAPRFE-409) | Undefined | Yes |
| [#3767](https://github.com/ansible/ansible-ui/pull/3767) | @acruzgon | — | Community (no Jira in PR) | — | — | Yes |
| [#3752](https://github.com/ansible/ansible-ui/pull/3752) | @acruzgon | — | Community (no Jira in PR) | — | — | Yes |
| [#3687](https://github.com/ansible/ansible-ui/pull/3687) | @lgalis | — | Jira-linked | [AAP-95292](https://redhat.atlassian.net/browse/AAP-95292) | Normal | Yes |
| [#3770](https://github.com/ansible/ansible-ui/pull/3770) | @lgalis | — | Community (no Jira in PR) | — | — | Yes |
| [#3702](https://github.com/ansible/ansible-ui/pull/3702) | @lgalis | — | Community (no Jira in PR) | — | — | Yes |
| [#3686](https://github.com/ansible/ansible-ui/pull/3686) | @lgalis | — | Community (no Jira in PR) | — | — | Yes |
| [#3680](https://github.com/ansible/ansible-ui/pull/3680) | @lgalis | — | Community (no Jira in PR) | — | — | Yes |
| [#3552](https://github.com/ansible/ansible-ui/pull/3552) | @lgalis | — | Community (no Jira in PR) | — | — | Yes |
| [#3911](https://github.com/ansible/ansible-ui/pull/3911) | @vidyanambiar | Yes | Jira-linked | [AAP-93628](https://redhat.atlassian.net/browse/AAP-93628) | Normal |  |
| [#3908](https://github.com/ansible/ansible-ui/pull/3908) | @vidyanambiar | Yes | Jira-linked | [AAP-65130](https://redhat.atlassian.net/browse/AAP-65130) | Normal |  |
| [#3902](https://github.com/ansible/ansible-ui/pull/3902) | @vidyanambiar | — | Jira-linked | [AAP-93673](https://redhat.atlassian.net/browse/AAP-93673) | Normal |  |

---

Jira keys are parsed from each PR **title and body** (`PROJ-123` pattern). The **Jira linkage** section lists only PRs that reference Jira in the PR text; PRs with no key in title/body are omitted from the Jira linkage table.

**API vs browser:** Jira Cloud returns **HTTP 404** when an issue is missing *or* when the API token lacks **Browse** permission. A `AAP-*` key that opens in the browser may still show as 404 in this report until the token can browse the **AAP** defect project (not only **AAPRFE**).

---

## Jira linkage (Priority & Affects version)

PRs that **link Jira in the PR** (issue key in title or body). Sorted by highest linked **Priority**, then PR #. Multiple keys per PR use `;` in Priority / Affects version (same order as the Jira key column).

| PR | Jira key(s) | Priority | Affects version(s) | Notes |
| ---: | --- | --- | --- | --- |
| [#3932](https://github.com/ansible/ansible-ui/pull/3932) | [AAP-102151](https://redhat.atlassian.net/browse/AAP-102151) | Major | 2.7 | Status Backlog — [UI] EE Images tab podman pull copy omits image tag in AAP 2.7 (regre... |
| [#3843](https://github.com/ansible/ansible-ui/pull/3843) | [AAP-100265](https://redhat.atlassian.net/browse/AAP-100265) | Major | 2.6, 2.7 | Status Backlog — BUG - Private Automation Hub: Browse version selection drops collecti... |
| [#3931](https://github.com/ansible/ansible-ui/pull/3931) | [AAP-102729](https://redhat.atlassian.net/browse/AAP-102729) | Normal | 2.6, 2.7 | Status Backlog — BUG - AAP UI authenticator type filter returns no results for existin... |
| [#3911](https://github.com/ansible/ansible-ui/pull/3911) | [AAP-93628](https://redhat.atlassian.net/browse/AAP-93628) | Normal | 2.6, 2.6.20260701 | Status In Progress — Host selection checkboxes are missing in constructed inventories (reg... |
| [#3908](https://github.com/ansible/ansible-ui/pull/3908) | [AAP-65130](https://redhat.atlassian.net/browse/AAP-65130) | Normal | 2.6 | Status In Progress — Cannot upload custom logo in AAP2.6 |
| [#3902](https://github.com/ansible/ansible-ui/pull/3902) | [AAP-93673](https://redhat.atlassian.net/browse/AAP-93673) | Normal | 2.6 | Status In Progress —  [UI] "Clone Template" button fails silently without user-facing erro... |
| [#3874](https://github.com/ansible/ansible-ui/pull/3874) | [AAP-99022](https://redhat.atlassian.net/browse/AAP-99022) | Normal | 2.6 | Status New — Cannot filter the management tasks by "name" under Automation Content |
| [#3865](https://github.com/ansible/ansible-ui/pull/3865) | [AAP-101258](https://redhat.atlassian.net/browse/AAP-101258) | Normal | — | Status New — Native Boolean Survey Answer Type |
| [#3848](https://github.com/ansible/ansible-ui/pull/3848) | [AAP-99868](https://redhat.atlassian.net/browse/AAP-99868) | Normal | 2.6 | Status Backlog — Let the textarea size in surveys be adjustable so multi-line answers ... |
| [#3840](https://github.com/ansible/ansible-ui/pull/3840) | [AAPRFE-3174](https://redhat.atlassian.net/browse/AAPRFE-3174) | Normal | 2.6, 2.7 | Status New — Add dynamic/live search filtering to the Organizations page  |
| [#3827](https://github.com/ansible/ansible-ui/pull/3827) | [AAP-85721](https://redhat.atlassian.net/browse/AAP-85721), [AAP-99473](https://redhat.atlassian.net/browse/AAP-99473) | Normal; Undefined | 2.6, 2.7; 2.7 | **AAP-85721:** Status Backlog — Deleting a resource in use by another resource no longer shows a warn... · **AAP-99473:** Status Closed — Deleting a credential succeeds when the credential is used by a project |
| [#3706](https://github.com/ansible/ansible-ui/pull/3706) | [AAP-65215](https://redhat.atlassian.net/browse/AAP-65215) | Normal | 2.6 | Status Backlog — Workflow Job Template node tags are multiplied and cannot be cleared ... |
| [#3687](https://github.com/ansible/ansible-ui/pull/3687) | [AAP-95292](https://redhat.atlassian.net/browse/AAP-95292) | Normal | 2.6.20261019, 2.7.20261005 | Status New — Workflow Job Template extra_vars UI truncates long numeric strings (1... |
| [#3761](https://github.com/ansible/ansible-ui/pull/3761) | [AAP-66504](https://redhat.atlassian.net/browse/AAP-66504) | Minor | 2.5, 2.6, 2.7 | Status Backlog — "Copy to clipboard" button has various results |
| [#3929](https://github.com/ansible/ansible-ui/pull/3929) | [AAP-102995](https://redhat.atlassian.net/browse/AAP-102995) | Undefined | — | Status New — [UI] Framework: add minHeight prop to DataEditor and PageFormDataEditor |
| [#3740](https://github.com/ansible/ansible-ui/pull/3740) | [AAPRFE-409](https://redhat.atlassian.net/browse/AAPRFE-409) | Undefined | 2.3, 2.6, 2.7 | Status Backlog — Allow users to clear the galaxy cache |

---

## Regenerating this report

Chai-bot: see `community-pr-triage/references/chai-bot.md`. Local dev may use `--github-via token` and `--jira-via env` (optional).
