# Workflow Patterns

## Sequential Workflows

For complex tasks, break operations into clear, sequential steps. It is often helpful to give the agent an overview of the process towards the beginning of SKILL.md:

```markdown
Filling a PDF form involves these steps:

1. Analyze the form (run analyze_form.py)
2. Create field mapping (edit fields.json)
3. Validate mapping (run validate_fields.py)
4. Fill the form (run fill_form.py)
5. Verify output (run verify_output.py)
```

## Conditional Workflows

For tasks with branching logic, guide the agent through decision points:

```markdown
1. Determine the modification type:
   **Creating new content?** → Follow "Creation workflow" below
   **Editing existing content?** → Follow "Editing workflow" below

2. Creation workflow: [steps]
3. Editing workflow: [steps]
```

This avoids forcing the agent to read through irrelevant steps when working with an existing skill.


## Iterative Optimization Loop

Apply multiple improvement rounds to a skill, keeping only changes that raise a quality score. A pseudocode workflow example:

```markdown
## Iteration

round = 0
while round < MAX_ROUNDS:
    round += 1

    lowest = find_lowest_score(scores)
    fix = propose_fix(lowest)
    apply_fix(fix)
    git_commit()

    new_score = evaluate()
    if new_score > old_score:
        keep_change()
        old_score = new_score
    else:
        git_revert()
        log_failure()
        break   # exit loop, skill saturated
```

