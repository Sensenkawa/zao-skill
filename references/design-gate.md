# Step 1 Interview & Judgment Protocol

Load when the user describes a skill need but no workflow exists yet.

## Interview

1. Interview to clarify use cases, tasks, and domain.

2. Grill relentlessly — walk down every branch of the design tree. One question at a time.
   For each, give your recommended answer. Resolve dependencies before moving on.

3. Once the picture is clear, give your independent judgment:
   - Is a skill even useful here, or would the agent do fine without it?
   - Too trivial for a skill or too complex for one skill?
     If complex, propose a breakdown. Focus on the first piece to start or to stop.
     Keep the rest as candidates.

4. If the idea passes: for the current piece, suggest completing a real task in conversation,
   as a living document; do not clean intermediate notes.
   This crystalizes the workflow to the output file — triggers, I/O, edge cases, failures, tools, conventions.
