---
name: zao-skill
description: >-
  Guide for creating effective skills that extend AI agent capabilities.
  Use when users request to:
  (1) Create a new skill from scratch,
  (2) Update or improve an existing skill,
  (3) Review or validate skill quality against best practices,
  (4) Package a skill for distribution,
  (5) Learn skill design principles or structure conventions.
  Covers full lifecycle: alignment, drafting, validation, packaging, and iteration.
---

# Zao Skill

Skills are modular packages that provide specialized knowledge, workflows, and tools to AI agents.
This skill guides the creation, review, and maintenance of effective skills.

## Core Principles

### 1. Concise is Key

**Default assumption: the agent is already smart.** Only add context it doesn't have. The context window is a public good. Every token in your skill competes for the agent’s attention with conversation history, system context, and other active skills. Focus on what the agent wouldn’t know without your skill.

**Prefer concise examples over verbose explanations.** Challenge each piece in your skill: "Does the agent really need this explanation?" or “Would the agent get this wrong without this instruction?” If the answer is no, cut it. 

### 2. Set Appropriate Degrees of Freedom？？？

Match the specificity of your instructions to the fragility of the task. Most skills have a mix. Calibrate each part independently.

**High freedom (text-based instructions)**: Use when multiple approaches are valid, decisions depend on context, or heuristics guide the approach.

**Medium freedom (pseudocode or scripts with parameters)**: Use when a preferred pattern exists, some variation is acceptable, or configuration affects behavior.

**Low freedom (specific scripts, few parameters)**: Use when operations are fragile and error-prone, consistency is critical, or a specific sequence must be followed.

For flexible instructions, explaining the why can be more effective than rigid directives — an agent that understands the purpose behind an instruction makes better context-dependent decisions.

Be prescriptive when operations are fragile, consistency matters, or a specific sequence must be followed

Think of the agent as exploring a path: a narrow bridge with cliffs needs specific guardrails (low freedom), while an open field allows many routes (high freedom).

Aim for moderate detail

### Anatomy of a Skill

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description required)
│   └── Markdown instructions
└── Bundled Resources (optional)
    ├── scripts/    - Executable code for deterministic/repetitive tasks
    ├── references/ - Docs loaded into context as needed
    └── assets/     - Files used in output (templates, icons, fonts)
```

Only include what the agent needs to do the job. Do NOT create README, CHANGELOG, INSTALLATION_GUIDE, or other auxiliary files.

### 3. Progressive Disclosure
Skills use a three-level loading system and should be structured to take advantage of this:

 1. Metadata (name + description) - Always in context (~100 words)
 2. SKILL.md body - In context whenever skill triggers (<500 lines ideal)
 3. Bundled resources - As needed (unlimited, scripts can execute without loading)

#### Guidelines

- Keep SKILL.md under 500 lines; if approaching this limit, split into Bundled Resources and link them from SKILL.md with clear "when to read" guidance
- Keep file references one level deep from SKILL.md and for large reference files (>300 lines), include a table of contents
- Avoid duplication: Each reference must add genuinely new value — never repeat what SKILL.md already says.
- The agent reads only the relevant reference file. So keep reference files focused.
- 
#### Example: Domain organization
When a skill supports multiple domains/frameworks, organize by variant:
cloud-deploy/
├── SKILL.md (workflow + selection)
└── references/
    ├── aws.md
    ├── gcp.md
    └── azure.md

## Skill Creation Process

Choose your entry point based on user's need:

- **Creating a new skill?** → Start at Phase 1
- **Updating or reviewing an existing skill?** → Jump to Drafting
- **Just validating or packaging?** → Jump to Validate & Package

//总要test不写skill自己跑是不是也行，太简单or太复杂，合并gril      
// trigger scenarios, ...Proactively ask questions about edge cases, input/output formats, example files, success criteria, and dependencies. Wait to write test prompts until you've got this part ironed out.
Skip this step only when usage patterns are already clearly understood.

### Phase 1: Pre-Creation Alignment

#### Step 1. Understand intent and extract workflow
   - Ask the user to clarify domain, use cases, and practical tasks/functionality, one question at a time.
   - Check whether the current conversation already contains a workflow to capture (e.g., "turn this into a skill"):
     - **If yes**: Extract successful steps, corrections, input/output formats, tools, and any project‑specific facts, conventions, or constraints. Write this as `wip/workflow-extraction.md`.
     - **If not**: Suggest that the user complete a real task in conversation first, then crystalize it in `wip/workflow-extraction.md`.
   - Confirm your understanding with the user before proceeding.

#### Step 2. Search for similar skills and decide direction
   - Based on the confirmed understanding, search local repos and online platforms for matching skills. Follow `references/skillSearchList.md` for the full search strategy.
   - Read `ref-skills/_summary.md` and review the SKILL.md copies in `ref-skills/`.
   - **If similar skills exist**:
     → Present your recommendation to the user. Clarify differences, and discuss one decision at a time — walk down each branch of the design tree, resolving dependencies step by step.
     → Reach a shared understanding on how to extend or modify the ref skills, together with workflow-extraction.md (if there is), then proceed to **Drafting**.
   - **If no similar skills found, or the user chooses not to use them**:
     → Proceed to **Drafting**, using the workflow extraction from Step 1 as input.
//现在看起来都是去drafting嘛
//Skip this phase only when usage patterns are already clearly understood.

//+claude plus：you can also run the skill description improver, which we have a whole separate script for, to optimize the triggering of the skill.

### Phase 2: Draft the Skill

Write the SKILL.md and any bundled resources in a single flow://？？？？

1. **Set up the directory** — Create `skill-name/` with `SKILL.md`. Optionally, run `scripts/init_skill.py <name> --path <dir>` to generate a template with example files.
//都可以删掉？----更新skill git manager
2. **Write bundled resources** — Create scripts, references, and assets as the workflow demands. Test scripts by actually running them. Delete unneeded files. Not every skill needs all three resource types — only create what the workflow requires.
//-----pocock，2.0提及了吗？其他两个呢。前面还是后面
   - SKILL.md with concise instructions
   - Additional reference files if content exceeds 500 lines
   - Utility scripts if deterministic operations needed

3. **Write SKILL.md**:
   - **Frontmatter**: `name` in kebab-case, `description` with BOTH what the skill does AND specific trigger scenarios (numbered list). All "when to use" info goes in description — not in body. Optional fields (`license`, `metadata`, `compatibility`) are rarely needed; only include them with clear purpose.
   - **Body**: Imperative form. Keep under 500 lines. Only operational instructions — teaching material goes in references.

4. **Validate as you go**: Run `scripts/quick_validate.py <skill-dir>` after significant edits for fast feedback. See references/output-patterns.md and references/workflows.md for design patterns (output formats, workflow structures).

If updating an existing skill, skip directory creation and work directly on the existing files.

### Phase 3: Validate & Package

When the skill is complete, package it for distribution:

```bash
scripts/package_skill.py <path/to/skill-folder> [output-directory]
```

This automatically runs full validation (frontmatter, naming, structure, description quality) before packaging. If validation fails, fix errors and re-run. On success, creates a `<skill-name>.skill` file.

### Phase 4: Iterate

After real usage, collect feedback and improve:

1. Use the skill on real tasks and note struggles or inefficiencies
2. Identify what to update in SKILL.md or bundled resources
3. Implement changes, re-validate (`quick_validate.py`), re-package if distributing
4. Test again

Common iteration triggers: missing trigger scenarios in description, overly long SKILL.md body that should be split to references, script bugs discovered in real use, or missing edge cases.

## Detailed Guides

Load these references when the corresponding scenario arises:

- **Scenario walkthroughs** — See [references/scenarios.md](references/scenarios.md) for end-to-end demonstrations (creating from scratch, updating existing, packaging only) with concrete examples. Load when stuck or learning by example.
- **Design patterns** — See [references/output-patterns.md](references/output-patterns.md) for output templates and [references/workflows.md](references/workflows.md) for workflow patterns (sequential, conditional, entry-point). Load when choosing output formats or process structures.
