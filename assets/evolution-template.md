# Skill Evolution — Full Archive

## How to Use This File

This file stores the **complete archive** of gotchas and success patterns for this skill.
The most critical current entries are summarized in SKILL.md's tables — this file holds everything else.

### Trigger

- **If the agent platform supports editing skills mid-conversation** (e.g., Hermes with `skill_manage`)
  → Record new discoveries immediately, before context is lost
- **Otherwise**
  → Check at the end of each run (Exit Verification) and record any new insights

### Record Flow

```
New insight discovered
  → Add to SKILL.md's Critical Gotchas or Success Patterns table (default location)
  → When the table exceeds 5 rows, move older entries here as narrative records
  → If the insight is a reference document (diagnosis, comparison, architecture analysis),
    create references/<topic>.md instead
```

### What to Record

- **Gotcha** — a failure with a repeatable fix. Record the symptom, root cause, and the fix.
- **Success Pattern** — a workflow or approach that proved reliably better. Record the change, the context, and the result.
- **Neither** — trivial changes (typos, one-line updates). No recording needed.

---

## Reference Index

| File | Topic |
|------|-------|
| _(Add a row for each reference file created)_ | |

---

## Gotchas Archive

### YYYY-MM-DD — [G01] Title
**Issue:**
**Root cause:**
**Fix:**

### YYYY-MM-DD — [G02] Title
**Issue:**
**Root cause:**
**Fix:**

---

## Success Patterns Archive

### YYYY-MM-DD — Title
Describe what changed, the context, and the outcome.

### YYYY-MM-DD — Title
Describe what changed, the context, and the outcome.
