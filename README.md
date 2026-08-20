# Agent Skills

A collection of reusable Agent Skills for Codex, Antigravity, Claude Code, Cursor, and other agents that support the Agent Skills format.

这是一个 Agent Skills 集合，面向 Codex、Antigravity、Claude Code、Cursor 以及其他支持 Agent Skills 格式的 Agent。

## Available skills

| Skill | Purpose |
| --- | --- |
| `clarify` | 厘清模糊表达，纠正术语与概念偏差，在必要时对齐含义。 |
| `vocab-story-generator` | 灵活解析不同软件导出的英文单词、短语和短句，排除历史已用条目后续写格式统一的情境助记文章。 |
| `cantonese-vocab-story-generator` | 把粤语词语、短语和短句转化为现代香港口语故事，并支持历史去重、增量续写与完整覆盖核验。 |

## Repository structure

```text
agent-skills/
├── README.md
└── skills/
    ├── clarify/
    │   └── SKILL.md
    ├── vocab-story-generator/
    │   └── SKILL.md
    └── cantonese-vocab-story-generator/
        └── SKILL.md
```

## Install

Replace `<github-user>` with the GitHub account that owns the repository.

List the available skills:

```powershell
npx skills add <github-user>/agent-skills --list
```

Install one skill interactively:

```powershell
npx skills add <github-user>/agent-skills --skill clarify
```

Install `clarify` globally for Codex and Antigravity:

```powershell
npx skills add <github-user>/agent-skills --skill clarify -g -a codex -a antigravity
```

If PowerShell blocks `npx.ps1`, run the same command with `npx.cmd` instead of `npx`.

## Compatibility

Each skill uses the portable `SKILL.md` format with YAML frontmatter. Basic instructions are designed to work across compatible agents, while installation paths and agent-specific features may vary by host and version.
