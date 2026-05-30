# Verification Guide

## Two Complementary Layers

Generally, devise your verification by dividing into two complementary layers:
- **Script** — deterministic, regex‑able: line counts, syntax, reference existence, table format
- **Checklist** — requires reading content: conciseness, duplication, rules compliance. Each item is a yes/no question, one dimension each

## Design Rules

- Only check against rules stated in the skill's text. Don't invent standards.
- The Evidence column stays empty — the agent fills it after inspecting its own output.
- Every finding cites the specific line number. No vague claims.
- Set up **Scope-lock** :
    - Polish how the skill works, don't change what it does. No new capabilities, no new dependencies.
    - Every finding must cite the specific line number. No vague claims.
    - Don't apply changes without user confirmation and git commit.

## Loop Structure

   Run script → fix FAILs → run checklist and fill Evidence → discuss  and fix gaps → re‑run 
   Stop when: zero FAILs + all Evidence filled + user approves

## Output

Save the summary to `<skill-name>/.wip/validation-N-summary.md` 

> For exit verification, if some verifications have already been embedded in the workflow and outputs, you don't need to repeat them. Add only additional checks if needed.

