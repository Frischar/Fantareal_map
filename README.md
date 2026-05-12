# Fantareal 开发地图

这是 [Fantareal](https://github.com/Frischar/Fantareal) 的**开发导航仓库**。你不会编程也能修 Bug、加 Mod——Git 克隆下来，用 AI 工具打开，第一句话让它读这份文档就行。

## 原理

AI 编程工具不会自动理解你的项目。这个仓库提供了一份精确到每个函数的**项目地图**（`maps/说明书.md` + `maps/说明书_auto.md`），AI 读完就知道每个功能在哪个文件的第几行。你只需要说人话，AI 负责定位代码、修改、解释。

## 环境准备

### 1. 装 Git 和 Python

- [git-scm.com](https://git-scm.com) 下载 Git，一路下一步
- [python.org](https://python.org) 下载 Python 3.11+，**安装时勾选 "Add Python to PATH"**

### 2. 克隆仓库

在你想放项目的文件夹里打开终端：

```bash
git clone https://github.com/Frischar/Fantareal.git
git clone https://github.com/Frischar/Fantareal_map.git
```

最终目录结构：

```
文件夹/
├── Fantareal/          ← 主项目（代码）
└── Fantareal_map/      ← 地图仓库（文档）
```

### 3. 装 AI 编程工具

挑一个你顺手的：

| 工具 | 适合谁 | 怎么装 |
|------|--------|--------|
| **VS Code + Claude Code 插件**（推荐） | 大多数人，有图形界面 | VS Code 扩展商店搜 `Claude Code` 安装 |
| **Claude Code CLI** | 习惯终端的人 | 终端跑 `npm install -g @anthropic-ai/claude-code` |
| **Codex** | 已有 Codex 账号的人 | [codex.openai.com](https://codex.openai.com) 下载客户端 |
| **Cursor / Windsurf / 其他** | 用惯哪个用哪个 | 各自官网下载 |

## 怎么用

用 AI 工具打开 `Fantareal/` 文件夹，第一句话：

> 先读 ../Fantareal_map/CLAUDE.md，然后告诉我你准备好了。

之后直接说大白话：

| 你想做的事 | 这样说 |
|-----------|--------|
| 修 Bug | 「XXX 功能出错了，帮我找原因」 |
| 加 Mod | 「参考 mods/card writer 的结构，帮我新建一个 XXX Mod」 |
| 调参数 | 「把 AI 回复的温度默认值从 0.8 改成 0.6」 |
| 理解代码 | 「XXX 功能是怎么实现的？」 |

### VS Code + Claude Code 插件

1. VS Code 打开 `Fantareal/` 文件夹
2. `Ctrl+Shift+P` → `Claude Code: Open in New Tab`
3. 输入上面那句指令，然后等 AI 说准备好了

### CLI

```bash
cd Fantareal
claude
# 输入：先读 ../Fantareal_map/CLAUDE.md，然后告诉我你准备好了。
```

## 目录结构

```
Fantareal_map/
├── README.md              ← 你正在看的文件
├── CLAUDE.md              ← AI 自动读取的项目导航
├── maps/
│   ├── architecture.md     ← 架构总览（JSON 结构，适合 AI 快速建立全局认知）
│   ├── 说明书.md           ← 手工编写，含踩坑指南（行号可能过时，看逻辑用）
│   ├── 说明书_auto.md      ← AST 自动生成，行号永远准确（定位用）
│   └── quick_ref.md       ← 常用操作速查
└── scripts/
    ├── scan_map.py        ← AST 扫描器：自动提取所有函数/类/行号
    └── sync_map.py        ← 一键同步：复制说明书 + 运行扫描
```

## 更新地图

主项目代码更新后，运行一次：

```bash
cd Fantareal_map
python scripts/sync_map.py
```

这会做两件事：
1. 从主项目复制 `说明书.md`
2. 运行 AST 扫描器生成 `说明书_auto.md`（行号重新提取）

每次改完代码顺手跑一下就行

## 常见问题

**Q: AI 改错了怎么办？**
A: 用 `git diff` 看改动，`git checkout -- 文件名` 撤销。改之前让 AI 先说明要改什么，确认了再让它动手。

**Q: 我完全不懂代码，能改吗？**
A: 简单的改参数、加静态内容可以。涉及逻辑的修改，让 AI 先解释清楚，每次只改一小步，改完跑起来看看效果。

**Q: AI 说找不到某个函数？**
A: 地图可能没更新，先跑一下 `python scripts/sync_map.py`。如果还找不到，让 AI 用函数名搜索。

**Q: 三个地图文件有什么区别？**
A: `architecture.md` 是架构总览（JSON 结构，按模块分层，适合 AI 快速建立全局认知）；`说明书_auto.md` 是 AST 自动提取的（函数名、行号、参数类型永远准确，但踩坑指南是空的）；`说明书.md` 是手工写的（有踩坑指南和改动建议，但行号可能过时，我会不定期更新说明书）。AI 应该按 `architecture.md` → `说明书_auto.md` → `说明书.md` 的顺序读。
