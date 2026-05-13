# Design Principles

> Load when designing a new skill or reviewing one against best practices.
> For the core statements of each principle, see Core Principles in SKILL.md.
> This file covers the details, anti-patterns, and patterns that don't fit in a one-liner.

## 1. Concise is Key

Challenge every piece of information. Prefer concise examples over verbose explanations.

### Anti-patterns

- Explaining what a skill is to an assistant that has already triggered this skill
- Documenting basic concepts the assistant already knows
- Including "when to use" guidance in body instead of frontmatter description
- Creating auxiliary files like README, CHANGELOG, INSTALLATION_GUIDE
- Repeating the same information in both SKILL.md and a reference file

## 2. Set Appropriate Degrees of Freedom

Match specificity to the task's fragility and variability:

| Freedom | Format | When |
|---------|--------|------|
| High | Text instructions | Multiple valid approaches, decisions depend on context |
| Medium | Pseudocode / parameterized scripts | Preferred pattern exists, some variation acceptable |
| Low | Specific scripts, few params | Fragile operations, consistency critical |

Think of the assistant as exploring a path: a narrow bridge with cliffs needs specific guardrails (low freedom), while an open field allows many routes (high freedom).

## 3. Progressive Disclosure + No Duplication

Three-level loading:
1. **Metadata** (name + description) — Always in context, determines triggering
2. **SKILL.md body** — Loaded when skill triggers; keep under 500 lines
3. **Bundled resources** — Loaded as needed

**The duplication rule**: A reference file must add genuinely new value. If it merely repeats what SKILL.md already says, it wastes context without benefit. Information lives in exactly one place — choose SKILL.md for core workflow, references for deep domain material. When in doubt, ask: "If SKILL.md already says this, what does this reference add?"

### When to split

- Content has **distinct domains** (e.g., finance vs sales schemas) → separate reference files
- SKILL.md approaching **500 lines** → split non-core content into references
- **Otherwise**: keep content in SKILL.md. An unnecessary reference is worse than a slightly longer SKILL.md.

### Progressive disclosure patterns

**Pattern 1: High-level guide with references**
```markdown
# PDF Processing
## Quick start
Extract text with pdfplumber: [code example]

## Advanced features
- **Form filling**: See FORMS.md
- **API reference**: See REFERENCE.md
```

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

### Guidelines

- Keep all references one level deep from SKILL.md — no nested reference chains
- For reference files >300 lines, include a table of contents at the top
- Reference files clearly from SKILL.md with guidance on when to load them

## 4. Self-Consistency

This skill must follow its own rules. Every principle, every structural requirement, every validation rule applies here first. The rules this skill teaches are applied to this skill itself — no exceptions.
