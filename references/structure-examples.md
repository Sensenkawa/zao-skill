# Structure Design Patterns

Two-level decision guide for organizing a skill's content:
**Part 1** helps choose the overall body architecture. **Part 2** helps design the steps within the workflow section.

---

## Part 1: Body Architecture — Choosing the Overall Structure

Standard Sections (Overview / Top Reminders / Workflows / Guardrails / Verification) are a recommended starting point, not a rigid template. Adapt the layout when the skill's nature calls for a different organization. Common patterns:

### 1. Workflow-Based (best for sequential processes)

Use when the skill has clear step-by-step procedures that follow a fixed order.

- **Example:** DOCX skill with "Workflow Decision Tree" → "Reading" → "Creating" → "Editing"
- **Structure:** Overview → Workflow Decision Tree → Step 1 → Step 2 → ...
- **Fits when:** One primary task with ordered sub-steps; each step depends on the previous

### 2. Task-Based (best for tool collections)

Use when the skill offers multiple independent operations that don't depend on each other.

- **Example:** PDF skill with "Quick Start" → "Merge PDFs" → "Split PDFs" → "Extract Text"
- **Structure:** Overview → Quick Start → Task Category 1 → Task Category 2 → ...
- **Fits when:** Several loosely-related capabilities; user picks one per invocation

### 3. Capabilities-Based (best for integrated systems)

Use when the skill provides interrelated features that form a coherent system.

- **Example:** Product Management with "Core Capabilities" → numbered capability list
- **Structure:** Overview → Core Capabilities → ### 1. Feature → ### 2. Feature → ...
- **Fits when:** Multiple features that work together; users may chain several in one session

### 4. Reference/Guidelines (best for standards or specifications)

Use for brand guidelines, coding standards, API specs, or fixed requirements — situations where the skill is a lookup resource, not a process.

- **Example:** Brand styling with "Brand Guidelines" → "Colors" → "Typography" → "Features"
- **Structure:** Overview → Topic 1 → Topic 2 → ... (flat, no ordered workflow)
- **Fits when:** The skill is consumed as reference material; no sequential navigation needed

**Patterns can be combined.** Most skills blend approaches — start with task-based grouping, add workflow detail for complex operations.

---

## Part 2: Step Design — Writing the Workflow Steps

Once the body architecture is chosen, design the individual steps within the process section. Three common step patterns:

### Sequential Steps

For complex tasks, break operations into clear, ordered steps. Give the agent an overview early:

```
Filling a PDF form involves these steps:

1. Analyze the form (run analyze_form.py)
2. Create field mapping (edit fields.json)
3. Validate mapping (run validate_fields.py)
4. Fill the form (run fill_form.py)
5. Verify output (run verify_output.py)
```

### Conditional Branching

For tasks with decision points, guide the agent through branches:

```
1. Determine the modification type:
   **Creating new content?** → Follow "Creation workflow" below
   **Editing existing content?** → Follow "Editing workflow" below

2. Creation workflow: [steps]
3. Editing workflow: [steps]
```

This avoids forcing the agent to read irrelevant steps.

### Iterative Optimization Loop

For quality-improvement cycles, use pseudocode to express the logic precisely:

```
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
