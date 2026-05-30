# Skill Evolution

Load when: Phase 5 (Evolution in Usage) triggers, or when adding/reviewing gotchas and success patterns.

## Purpose

Store all practical experience from real usage. Gotchas capture failures;
Success Patterns capture what worked well. This skill evolves through both.

## How to use this file

**Trigger**: After any run with a repeatable fix or a config/workflow
change that improves results → propose a new entry for user approval.
If uneventful, skip.

**Workflow:**
- Commit baseline before changes
- Helped → Success Patterns entry. Worse → undo and log as gotcha
- **Approval**: SKILL.md table updates require user approval.
  Entries here (full archive) are just recording — no approval needed

**Main SKILL.md**: Keep 3 most critical Gotchas and 3 most recent
Success Patterns in SKILL.md. This file holds the full archive.

**What to record vs Gotchas** (some items could go either way):
- Parameter tuning that improved performance — **Success Pattern**
- Workflow redesign that proved reliable — **Success Pattern**
- Any eventful experience that made this skill better — **Success Pattern**
- Failures with a repeatable fix — **Gotcha**
- Trivial changes (e.g., fixing a typo) — **neither**

## Gotchas Archive
| ID | Date | Issue / Symptom | Fix |
|----|------|-----------------|-----|

## Success Patterns
> Free-form entries. Record what worked, why, and what was learned.
> Each entry starts with `### YYYY-MM-DD — summary`; context inline.

### YYYY-MM-DD — (example) Increased response accuracy
By adjusting the temperature parameter from 0.7 to 0.3 for factual
queries, accuracy improved from 82% to 94%. The change was validated
across 3 different skill types. Lower temperature may not work well
for creative tasks — keep that in mind.

...
