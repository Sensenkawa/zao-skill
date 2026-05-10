# Design Principles

> Load when designing a new skill, reviewing an existing skill against best practices, or upgrading a skill. These are the foundational rules that every effective skill must follow.

## 1. Concise is Key

The context window is a shared resource. Skills compete with system prompts, conversation history, other skills' metadata, and user requests.

**Default assumption: the assistant is already very smart.** Only add context the assistant doesn't already have. Challenge each piece of information: "Does the assistant really need this explanation?" and "Does this paragraph justify its token cost?"

Prefer concise examples over verbose explanations.

### Anti-patterns

- Explaining what a skill is to an assistant that has already triggered this skill
- Documenting basic concepts the assistant already knows
- Including "when to use" guidance in body instead of frontmatter description
- Creating auxiliary files like README, CHANGELOG, INSTALLATION_GUIDE

## 2. Set Appropriate Degrees of Freedom

Match specificity to the task's fragility and variability:

- **High freedom (text instructions)**: When multiple approaches are valid and decisions depend on context
- **Medium freedom (pseudocode / parameterized scripts)**: When a preferred pattern exists but variation is acceptable
- **Low freedom (specific scripts, few parameters)**: When operations are fragile, error-prone, or require strict consistency

Think of the assistant as exploring a path: a narrow bridge with cliffs needs specific guardrails (low freedom), while an open field allows many routes (high freedom).

## 3. Progressive Disclosure

Three-level loading to manage context efficiently:

1. **Metadata (name + description)** — Always in context (~100 words), determines triggering
2. **SKILL.md body** — Loaded when skill triggers; keep under 500 lines
3. **Bundled resources** — Loaded as needed; unlimited because scripts execute without entering context

### Key patterns

**Pattern 1: High-level guide with references**
```markdown
# PDF Processing

## Quick start
Extract text with pdfplumber: [code example]

## Advanced features
- **Form filling**: See FORMS.md
- **API reference**: See REFERENCE.md
```

The assistant loads FORMS.md or REFERENCE.md only when needed.

**Pattern 2: Domain-specific organization**
```
bigquery-skill/
└── references/
    ├── finance.md   (revenue, billing)
    ├── sales.md     (pipeline, metrics)
    └── product.md   (usage, features)
```

When a user asks about sales metrics, the assistant only reads sales.md.

**Pattern 3: Conditional details**
```markdown
# DOCX Processing

For simple edits, modify the XML directly.
**For tracked changes**: See REDLINING.md
**For OOXML details**: See OOXML.md
```

The assistant reads REDLINING.md or OOXML.md only when the user needs those features.

### Guidelines

- Keep all references one level deep from SKILL.md — no nested reference chains
- Structure longer reference files — For files longer than 100 lines, include a table of contents at the top so the assistant can see the full scope when previewing.

## 4. Self-Consistency

This skill must follow its own rules. Every principle, every structural requirement, every validation rule applies here first.

- **Text instructions = Medium/High freedom**: When the assistant should adapt based on context
- **Scripts = Low freedom**: For deterministic, error-prone, or repetitive operations
- **References = Freedom enabler**: Provide detailed knowledge the assistant loads when needed, keeping the base skill lean
- **This SKILL.md**: Must stay under 500 lines, follow progressive disclosure, and be concise
