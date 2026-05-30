# Design Gate

## Part 1 — Init Design
Load when Phase 1 Step 1 has no existing workflow.

### Interview and Crystalize the workflow

1. Interview to clarify use cases, tasks, and domain — **one question at a time**

2. **Grill systematically**  — walk down every branch of the design tree. One question at a time.
   For each, give your recommended answer. Resolve dependencies before moving on.

3. Once the picture is clear, give your **independent judgment**:
   - Is a skill even useful here, or would the agent do fine without it?
   - Is it too trivial for a skill? (If yes → stop; handle conversationally.)
   - Is it too complex for one skill?  
     If complex, propose a breakdown. Focus on the **first piece** to start.  
     Keep the remaining pieces as a todo list in `<skill-name>/.wip/`.

4. If the idea passes (skill is useful and appropriately scoped):
   - Suggest that the user complete a **real task** in conversation to crystallize the workflow.
   - Capture: triggers, input/output formats, example files, success criteria, edge cases, failures/corrections, tools, project‑specific facts/conventions/constraints.
   - Keep the conversation as a **living document**; do not clean intermediate notes.


## Part 2 — Refine Design
Load when Phase 1 Step 2 user chooses "Refine".

- Clarify differences between the existing skill(s) and the user's intent (from Step 1 workflow extraction).
- Recommend which skill(s) to base on, borrow from, or discard.
- Discuss one decision at a time. Walk down each branch, resolve dependencies and fill gaps.
- Confirm shared understanding and append refinement decisions to the Design Context section in `workflow-extraction.md`.
