# Community PR triage report — ansible-ui

| Field | Value |
| --- | --- |
| **Snapshot date** | 2026-11-17 |
| **Filter** | [Open PRs with `community` label](https://github.com/ansible/ansible-ui/pulls?q=is%3Apr+state%3Aopen+label%3Acommunity) |
| **Total open** | 21 |
| **GitHub data** | Authenticated API (`GH_ANSIBLE_UI_TOKEN`) |
| **Jira data** | `JIRA_URL` — **Priority** and **Affects version** (`versions`) per key in PR title/body |
| **PRs with Jira key(s)** | 13/21 |
| **Jira keys resolved via API** | 14/14 unique keys |

Community volume is concentrated: **swatinarvekar (6)**, **demonpig (3)**, **pshekhaw (2)**; the rest are one PR each. Many carry **`pr reviewed using repo skills`**. **`waiting-on-author`** appears on 14/21 — most of the queue is feedback-pending, not unreviewed.

---

## Executive summary

| Bucket | Count | Team action |
| --- | ---: | --- |
| Ready for maintainer review (no `waiting-on-author`) | 7 | Assign reviewers this week; prioritize XS/S bug fixes |
| Author follow-up required | 14 | Triage stale vs. one nudge from merge |
| Merge conflicts (`mergeable_state: dirty`) | 4 | Author rebase before deep review |
| Cross-cutting / framework | 4 | Framework + i18n owners |
| Large features / coordination | 3 | Dedicated design + API dependency review |

**Dirty merge (at snapshot):** [#3552](https://github.com/ansible/ansible-ui/pull/3552), [#3865](https://github.com/ansible/ansible-ui/pull/3865), [#3767](https://github.com/ansible/ansible-ui/pull/3767), [#3761](https://github.com/ansible/ansible-ui/pull/3761)

**Jira note:** All linked keys resolved via REST at snapshot time. Highest **Priority** in queue: **Major** — [AAP-100265](https://redhat.atlassian.net/browse/AAP-100265) (Hub collection browse, 2.6/2.7). [#3827](https://github.com/ansible/ansible-ui/pull/3827) also references [AAP-99473](https://redhat.atlassian.net/browse/AAP-99473) (**Closed**).

---

## Jira linkage (Priority & Affects version)

Keys are extracted from each PR **title and description**. When a PR lists multiple keys, Priority and Affects version are shown per key.

| PR | Jira key(s) | Priority | Affects version(s) | Notes |
| ---: | --- | --- | --- | --- |
| [#3911](https://github.com/ansible/ansible-ui/pull/3911) | [AAP-93628](https://redhat.atlassian.net/browse/AAP-93628) | AAP-93628: Normal | AAP-93628: 2.6, 2.6.20260701 | **AAP-93628:** Status Backlog — Host selection checkboxes are missing in constructed inventories (reg... |
| [#3908](https://github.com/ansible/ansible-ui/pull/3908) | [AAP-65130](https://redhat.atlassian.net/browse/AAP-65130) | AAP-65130: Normal | AAP-65130: 2.6 | **AAP-65130:** Status Backlog — Cannot upload custom logo in AAP2.6 |
| [#3902](https://github.com/ansible/ansible-ui/pull/3902) | [AAP-93673](https://redhat.atlassian.net/browse/AAP-93673) | AAP-93673: Normal | AAP-93673: 2.6 | **AAP-93673:** Status Backlog —  [UI] "Clone Template" button fails silently without user-facing erro... |
| [#3881](https://github.com/ansible/ansible-ui/pull/3881) | — | — | — | No Jira key in PR title/body |
| [#3874](https://github.com/ansible/ansible-ui/pull/3874) | [AAP-99022](https://redhat.atlassian.net/browse/AAP-99022) | AAP-99022: Normal | AAP-99022: 2.6 | **AAP-99022:** Status New — Cannot filter the management tasks by "name" under Automation Content |
| [#3865](https://github.com/ansible/ansible-ui/pull/3865) | [AAP-101258](https://redhat.atlassian.net/browse/AAP-101258) | AAP-101258: Normal | AAP-101258: — | **AAP-101258:** Status New — Native Boolean Survey Answer Type |
| [#3848](https://github.com/ansible/ansible-ui/pull/3848) | [AAP-99868](https://redhat.atlassian.net/browse/AAP-99868) | AAP-99868: Normal | AAP-99868: 2.6 | **AAP-99868:** Status Backlog — Let the textarea size in surveys be adjustable so multi-line answers ... |
| [#3843](https://github.com/ansible/ansible-ui/pull/3843) | [AAP-100265](https://redhat.atlassian.net/browse/AAP-100265) | AAP-100265: Major | AAP-100265: 2.6, 2.7 | **AAP-100265:** Status Backlog — BUG - Private Automation Hub: Browse version selection drops collecti... |
| [#3840](https://github.com/ansible/ansible-ui/pull/3840) | [AAPRFE-3174](https://redhat.atlassian.net/browse/AAPRFE-3174) | AAPRFE-3174: Normal | AAPRFE-3174: 2.6, 2.7 | **AAPRFE-3174:** Status New — Add dynamic/live search filtering to the Organizations page  |
| [#3827](https://github.com/ansible/ansible-ui/pull/3827) | [AAP-85721](https://redhat.atlassian.net/browse/AAP-85721), [AAP-99473](https://redhat.atlassian.net/browse/AAP-99473) | AAP-85721: Normal; AAP-99473: Undefined | AAP-85721: 2.6, 2.7; AAP-99473: 2.7 | **AAP-85721:** Status Backlog — Deleting a resource in use by another resource no longer shows a warn... · **AAP-99473:** Status Closed — Deleting a credential succeeds when the credential is used by a project |
| [#3770](https://github.com/ansible/ansible-ui/pull/3770) | — | — | — | No Jira key in PR title/body |
| [#3767](https://github.com/ansible/ansible-ui/pull/3767) | — | — | — | No Jira key in PR title/body |
| [#3761](https://github.com/ansible/ansible-ui/pull/3761) | [AAP-66504](https://redhat.atlassian.net/browse/AAP-66504) | AAP-66504: Minor | AAP-66504: 2.5, 2.6, 2.7 | **AAP-66504:** Status Backlog — "Copy to clipboard" button has various results |
| [#3752](https://github.com/ansible/ansible-ui/pull/3752) | — | — | — | No Jira key in PR title/body |
| [#3740](https://github.com/ansible/ansible-ui/pull/3740) | [AAPRFE-409](https://redhat.atlassian.net/browse/AAPRFE-409) | AAPRFE-409: Undefined | AAPRFE-409: 2.3, 2.6, 2.7 | **AAPRFE-409:** Status Backlog — Allow users to clear the galaxy cache |
| [#3706](https://github.com/ansible/ansible-ui/pull/3706) | [AAP-65215](https://redhat.atlassian.net/browse/AAP-65215) | AAP-65215: Normal | AAP-65215: 2.6 | **AAP-65215:** Status Backlog — Workflow Job Template node tags are multiplied and cannot be cleared ... |
| [#3702](https://github.com/ansible/ansible-ui/pull/3702) | — | — | — | No Jira key in PR title/body |
| [#3687](https://github.com/ansible/ansible-ui/pull/3687) | [AAP-95292](https://redhat.atlassian.net/browse/AAP-95292) | AAP-95292: Normal | AAP-95292: 2.6.20261019, 2.7.20261005 | **AAP-95292:** Status New — Workflow Job Template extra_vars UI truncates long numeric strings (1... |
| [#3686](https://github.com/ansible/ansible-ui/pull/3686) | — | — | — | No Jira key in PR title/body |
| [#3680](https://github.com/ansible/ansible-ui/pull/3680) | — | — | — | No Jira key in PR title/body |
| [#3552](https://github.com/ansible/ansible-ui/pull/3552) | — | — | — | No Jira key in PR title/body |

### Jira issues referenced (deduplicated)

| Key | Priority | Affects version(s) | Status | Summary |
| --- | --- | --- | --- | --- |
| [AAP-100265](https://redhat.atlassian.net/browse/AAP-100265) | Major | 2.6, 2.7 | Backlog | BUG - Private Automation Hub: Browse version selection drops collection path parameters, causing Documentation 404 |
| [AAP-101258](https://redhat.atlassian.net/browse/AAP-101258) | Normal | — | New | Native Boolean Survey Answer Type |
| [AAP-65130](https://redhat.atlassian.net/browse/AAP-65130) | Normal | 2.6 | Backlog | Cannot upload custom logo in AAP2.6 |
| [AAP-65215](https://redhat.atlassian.net/browse/AAP-65215) | Normal | 2.6 | Backlog | Workflow Job Template node tags are multiplied and cannot be cleared when "Prompt on launch" is enabled |
| [AAP-66504](https://redhat.atlassian.net/browse/AAP-66504) | Minor | 2.5, 2.6, 2.7 | Backlog | "Copy to clipboard" button has various results |
| [AAP-85721](https://redhat.atlassian.net/browse/AAP-85721) | Normal | 2.6, 2.7 | Backlog | Deleting a resource in use by another resource no longer shows a warning in AAP 2.6/2.7 |
| [AAP-93628](https://redhat.atlassian.net/browse/AAP-93628) | Normal | 2.6, 2.6.20260701 | Backlog | Host selection checkboxes are missing in constructed inventories (regression from AAP 2.4) |
| [AAP-93673](https://redhat.atlassian.net/browse/AAP-93673) | Normal | 2.6 | Backlog |  [UI] "Clone Template" button fails silently without user-facing error feedback on permission/RBAC mismatch |
| [AAP-95292](https://redhat.atlassian.net/browse/AAP-95292) | Normal | 2.6.20261019, 2.7.20261005 | New | Workflow Job Template extra_vars UI truncates long numeric strings (16+ digits), unlike standalone Job Templates |
| [AAP-99022](https://redhat.atlassian.net/browse/AAP-99022) | Normal | 2.6 | New | Cannot filter the management tasks by "name" under Automation Content |
| [AAP-99473](https://redhat.atlassian.net/browse/AAP-99473) | Undefined | 2.7 | Closed | Deleting a credential succeeds when the credential is used by a project |
| [AAP-99868](https://redhat.atlassian.net/browse/AAP-99868) | Normal | 2.6 | Backlog | Let the textarea size in surveys be adjustable so multi-line answers show fully |
| [AAPRFE-3174](https://redhat.atlassian.net/browse/AAPRFE-3174) | Normal | 2.6, 2.7 | New | Add dynamic/live search filtering to the Organizations page  |
| [AAPRFE-409](https://redhat.atlassian.net/browse/AAPRFE-409) | Undefined | 2.3, 2.6, 2.7 | Backlog | Allow users to clear the galaxy cache |

---

## Fast path — assign reviewers (7 PRs)

Small, scoped, mostly **`risk:low`** (or test-only), **not** `waiting-on-author`. Suitable for a single “community batch” review block.

| PR | Title | Area | Size | Jira | Priority | Affects version | Notes |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| [#3911](https://github.com/ansible/ansible-ui/pull/3911) | Constructed inventory host checkboxes (AAP-93628) | Controller | XS | [AAP-93628](https://redhat.atlassian.net/browse/AAP-93628) | Normal | 2.6, 2.6.20260701 | Regression vs 2.4 |
| [#3908](https://github.com/ansible/ansible-ui/pull/3908) | Platform custom logo upload (AAP-65130) | Platform | S | [AAP-65130](https://redhat.atlassian.net/browse/AAP-65130) | Normal | 2.6 | File upload + data URL |
| [#3902](https://github.com/ansible/ansible-ui/pull/3902) | Error toast on duplicate template failure (AAP-93673) | Controller | M | [AAP-93673](https://redhat.atlassian.net/browse/AAP-93673) | Normal | 2.6 | **Missing risk analysis** label |
| [#3881](https://github.com/ansible/ansible-ui/pull/3881) | Restore overview hosts Ready/Failed E2E | Playwright | XS | — | — | — | `e2e: running` |
| [#3874](https://github.com/ansible/ansible-ui/pull/3874) | Hub task name exact filter (AAP-99022) | Hub | XS | [AAP-99022](https://redhat.atlassian.net/browse/AAP-99022) | Normal | 2.6 | API rejects `name__icontains` on 2.6 |
| [#3840](https://github.com/ansible/ansible-ui/pull/3840) | Organizations live/async search (AAPRFE-3174) | Platform | M | [AAPRFE-3174](https://redhat.atlassian.net/browse/AAPRFE-3174) | Normal | 2.6, 2.7 | Enhancement |
| [#3827](https://github.com/ansible/ansible-ui/pull/3827) | Warn before deleting JT used by workflows (AAP-85721) | Controller | S | [AAP-85721](https://redhat.atlassian.net/browse/AAP-85721) | Normal | 2.6, 2.7 | 2.4 behavior restore |

**Reviewer routing:** `controller` → AWX UI; `HUB` → Hub; `platform` → Gateway/Platform; Playwright-only → E2E maintainers.

**Batch tip:** [#3911](https://github.com/ansible/ansible-ui/pull/3911), [#3908](https://github.com/ansible/ansible-ui/pull/3908), [#3874](https://github.com/ansible/ansible-ui/pull/3874), [#3827](https://github.com/ansible/ansible-ui/pull/3827) are all **swatinarvekar** — one reviewer can cover several in one pass.

---

## By product / workspace

### Controller (AWX)

| PR | Title / theme | Size | Status |
| ---: | --- | --- | --- |
| [#3911](https://github.com/ansible/ansible-ui/pull/3911) | Constructed inventory checkboxes | XS | Fast path |
| [#3902](https://github.com/ansible/ansible-ui/pull/3902) | Duplicate template error toast | M | Fast path |
| [#3827](https://github.com/ansible/ansible-ui/pull/3827) | Delete JT in-use warning | S | Fast path |
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
| [#3874](https://github.com/ansible/ansible-ui/pull/3874) | Task management exact name filter | Fast path |
| [#3843](https://github.com/ansible/ansible-ui/pull/3843) | Collection browse / version URL (AAP-100265) | `waiting-on-author`; missing risk analysis |

### Platform

| PR | Title | Status |
| ---: | --- | --- |
| [#3908](https://github.com/ansible/ansible-ui/pull/3908) | Custom logo upload | Fast path |
| [#3840](https://github.com/ansible/ansible-ui/pull/3840) | Organizations async filters | Fast path |

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
| [#3881](https://github.com/ansible/ansible-ui/pull/3881) | Overview hosts Ready/Failed redirect E2E | Fast path |

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

## Suggested meeting agenda (30–45 min)

1. Assign owners for the **7 fast-path** PRs; target XS/S merges within 1–2 sprints.
2. **Survey track** — one owner for #3552 vs #3865 (scope, API order, split strategy).
3. **Framework slot** — #3680, #3848, #3761 (after rebase): one framework reviewer + cross-product smoke.
4. **Waiting-on-author sweep** (14 PRs): CI, conflicts, product question, or nudge-only?
5. **Contributor load** — swatinarvekar backlog: batch vs sequential merge.

---

## Reviewer assignment matrix (starter)

| Expertise | PR numbers |
| --- | --- |
| AWX / Controller | 3911, 3902, 3827, 3770, 3706, 3687, 3686, 3740, 3865, 3552 |
| Hub | 3874, 3843 |
| Platform / Gateway | 3908, 3840 |
| EDA | 3752, 3706 |
| Framework + i18n | 3680, 3848, 3761, 3702, 3752 |
| Playwright | 3881 |
| Build / security | 3767 |

---

## Priority: merge five this month

1. [#3911](https://github.com/ansible/ansible-ui/pull/3911) — user-visible regression, tiny diff
2. [#3908](https://github.com/ansible/ansible-ui/pull/3908) — settings bug, small
3. [#3874](https://github.com/ansible/ansible-ui/pull/3874) — Hub filter 400
4. [#3827](https://github.com/ansible/ansible-ui/pull/3827) — destructive-action safety
5. [#3702](https://github.com/ansible/ansible-ui/pull/3702) **or** [#3840](https://github.com/ansible/ansible-ui/pull/3840) — docs vs platform bandwidth

**Defer until rebase/plan:** #3552, #3865, #3767, #3761

---

## Full inventory

| PR | Title | Author | Jira key(s) | Priority | Affects version(s) | Waiting on author | Conflicts | Link |
| ---: | --- | --- | --- | --- | --- | :---: | :---: | --- |
| 3911 | fix(awx): show host checkboxes for constructed inventories (AAP-93628) | swatinarvekar  | [AAP-93628](https://redhat.atlassian.net/browse/AAP-93628) | Normal | 2.6, 2.6.20260701 | | | [PR](https://github.com/ansible/ansible-ui/pull/3911) |
| 3908 | fix(platform): enable custom logo file upload (AAP-65130) | swatinarvekar  | [AAP-65130](https://redhat.atlassian.net/browse/AAP-65130) | Normal | 2.6 | | | [PR](https://github.com/ansible/ansible-ui/pull/3908) |
| 3902 | AAP-93673: show error toast when duplicate template fails | pshekhaw  | [AAP-93673](https://redhat.atlassian.net/browse/AAP-93673) | Normal | 2.6 | | | [PR](https://github.com/ansible/ansible-ui/pull/3902) |
| 3881 | test(e2e): restore overview hosts Ready/Failed redirect coverage | lgalis | — | — | — | | | [PR](https://github.com/ansible/ansible-ui/pull/3881) |
| 3874 | fix: use exact name filter for Hub task management (AAP-99022) | swatinarvekar  | [AAP-99022](https://redhat.atlassian.net/browse/AAP-99022) | Normal | 2.6 | | | [PR](https://github.com/ansible/ansible-ui/pull/3874) |
| 3865 | AAP-101258: feat: support boolean survey answers in UI | chadmf  | [AAP-101258](https://redhat.atlassian.net/browse/AAP-101258) | Normal | — | Yes | Yes | [PR](https://github.com/ansible/ansible-ui/pull/3865) |
| 3848 | AAP-99868: grow survey textarea for multi-line defaults | shrsingh-eng  | [AAP-99868](https://redhat.atlassian.net/browse/AAP-99868) | Normal | 2.6 | Yes | | [PR](https://github.com/ansible/ansible-ui/pull/3848) |
| 3843 | fix(hub): keep the selected collection when browsing versions (AAP-100265) | snehald1241  | [AAP-100265](https://redhat.atlassian.net/browse/AAP-100265) | Major | 2.6, 2.7 | Yes | | [PR](https://github.com/ansible/ansible-ui/pull/3843) |
| 3840 | AAPRFE-3174: Add dynamic/live search filtering to Organizations page | pshekhaw  | [AAPRFE-3174](https://redhat.atlassian.net/browse/AAPRFE-3174) | Normal | 2.6, 2.7 | | | [PR](https://github.com/ansible/ansible-ui/pull/3840) |
| 3827 | AAP-85721: Warn before deleting job templates in use by workflows | swatinarvekar  | [AAP-85721](https://redhat.atlassian.net/browse/AAP-85721), [AAP-99473](https://redhat.atlassian.net/browse/AAP-99473) | Normal (85721); Undefined (99473) | 2.6, 2.7 (85721); 2.7 (99473) | | | [PR](https://github.com/ansible/ansible-ui/pull/3827) |
| 3770 | fix(awx): allow clearing schedule limit | demonpig | — | — | — | Yes | | [PR](https://github.com/ansible/ansible-ui/pull/3770) |
| 3767 | chore(deps): fix npm audit findings | sasas-cloud | — | — | — | Yes | Yes | [PR](https://github.com/ansible/ansible-ui/pull/3767) |
| 3761 | Fix copy-to-clipboard format selection (AAP-66504) | abhishek-paygavhan  | [AAP-66504](https://redhat.atlassian.net/browse/AAP-66504) | Minor | 2.5, 2.6, 2.7 | Yes | Yes | [PR](https://github.com/ansible/ansible-ui/pull/3761) |
| 3752 | Update EDA rulebook activation help text for project sync restart | lennysh | — | — | — | Yes | | [PR](https://github.com/ansible/ansible-ui/pull/3752) |
| 3740 | Add UI for galaxy_update_on_launch project setting | jonnyfiveiq  | [AAPRFE-409](https://redhat.atlassian.net/browse/AAPRFE-409)| Undefined | 2.3, 2.6, 2.7 | Yes | | [PR](https://github.com/ansible/ansible-ui/pull/3740) |
| 3706 | fix: persist cleared workflow node job/skip tags (AAP-65215) | swatinarvekar  | [AAP-65215](https://redhat.atlassian.net/browse/AAP-65215) | Normal | 2.6 | Yes | | [PR](https://github.com/ansible/ansible-ui/pull/3706) |
| 3702 | docs: add translation contribution guide | demonpig | — | — | — | Yes | | [PR](https://github.com/ansible/ansible-ui/pull/3702) |
| 3687 | fix: preserve WJT extra_vars numeric precision (AAP-95292) | swatinarvekar | [AAP-95292](https://redhat.atlassian.net/browse/AAP-95292) | Normal | 2.6.20261019, 2.7.20261005 | Yes | | [PR](https://github.com/ansible/ansible-ui/pull/3687) |
| 3686 | fix: project status link missing and inventory source last job status link malformed | siddhipatil01 | — | — | — | Yes | | [PR](https://github.com/ansible/ansible-ui/pull/3686) |
| 3680 | feat(framework): add language preference setting | demonpig | — | — | — | Yes | | [PR](https://github.com/ansible/ansible-ui/pull/3680) |
| 3552 | Feature/conditional survey | kenancakir | — | — | — | Yes | Yes | [PR](https://github.com/ansible/ansible-ui/pull/3552) |

---
## Regenerating this report

Credential env vars are listed in `.cursor/rules/creds.mdc` (`GH_ANSIBLE_UI_TOKEN`, `JIRA_URL`, `JIRA_EMAIL`, `JIRA_API_TOKEN`).

Refresh **Jira linkage** and inventory columns (re-run against live GitHub + Jira):

```bash
python3 reports/generate-community-pr-triage.py \
  --output reports/community-pr-triage-$(date +%Y-%m-%d).md
```

The generator writes the Jira-centric tables; merge into the narrative sections of this doc or extend the script to emit the full triage template.

GitHub-only snapshot:

```bash
gh pr list --repo ansible/ansible-ui --label community --state open --limit 100 \
  --json number,title,author,labels,additions,deletions,changedFiles,url,isDraft,updatedAt,body
```
