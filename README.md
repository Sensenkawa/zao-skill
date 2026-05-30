# zao-skill

AI 为 AI 创造技能的元技能框架。

默认技能创建器 v0.1.0 版。本技能新增**设计流、规范步骤流、引入迭代流**，让技能跨平台可继承。

## 工作流概览

```
Start → User Need?
   ├─ Create new skill              → Phase 1: Design
   ├─ Draft / update / edit skill   → Phase 2: Drafting
   ├─ Review / validate             → Phase 3: Validation
   └─ Package for release           → Phase 4: Packaging
After any run → Evolution in Usage (self-improve)
```

## 特性

- **Design Gate**: 意图理解 → 相似技能搜索 → 设计提炼
- **规范化创作**: 严格定义 Frontmatter + Standard Sections + Bundled Resources
- **自动化验证**: 25+ 项静态检查（quick_validate.py）
- **Self-Evolution**: Success Patterns 自由记录经验，Gotchas 归档失败
- **跨平台**: 兼容 WorkBuddy / ClawPro / Codex / OpenClaw

## 快速开始

```bash
# 验证 skill
python scripts/quick_validate.py <skill-dir>

# 打包发布
python scripts/package_skill.py <skill-dir>
```

## 安装

将 `zao-skill` 目录放入你的 Agent 平台 skill 目录：

- **WorkBuddy**: `~/.workbuddy/skills/`
- **QClaw / OpenClaw**: `~/.openclaw/skills/`

## License

Apache 2.0
