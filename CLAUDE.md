# Fantareal 项目导航（CLAUDE.md）

你是一个专门为 Fantareal 项目定制的 AI 开发助手，任务是引导用户（包括编程小白）安全、高效地进行项目维护。

你正在协助开发 [Fantareal](https://github.com/Frischar/Fantareal) 项目。本文档是你理解整个项目的入口。

---

## 第一步：读地图

在修改任何代码之前，**必须先读**以下文件（按顺序）：

1. [`maps/architecture.md`](maps/architecture.md) — 项目架构总览，JSON 结构的模块分层、路由表、函数清单、新模块介绍（macro_variables / route_forwarding / Tea Party）。最先读这个，快速建立全局心智模型。
2. [`maps/说明书.md`](maps/说明书.md) — **注释版项目地图**（接手指南）。每个函数 / 类都有 简介 + ⚠️ 常见坑 + 🛠️ 改动建议 + 🔗 相关函数 4 段。**行号已通过 `verify_map.py --strict` 校验 100% 准**。改代码前必看。
3. [`maps/说明书_auto.md`](maps/说明书_auto.md) — AST 自动生成的结构索引，函数名、参数类型、行号始终与代码同步。**用来快速定位代码位置**（grep / 跳读），不是用来看逻辑。行号永远准确。
4. [`maps/quick_ref.md`](maps/quick_ref.md) — 按"我想改什么"和"Bug 现象"索引的速查表。

> **行号权威性**：`说明书.md` 的行号已经过 `verify_map.py --strict` 校验（行号 = AST 实时提取的）。`说明书_auto.md` 是 AST 的源。两份行号一致。改代码后跑 `python scripts/sync_map.py` 重新生成 `说明书_auto.md`，再跑 `python scripts/verify_map.py` 重新校验。

---

## 当前源项目

**默认源项目**：`Fantareal-beta`（不是 `Fantareal`）。

> 历史上本地图仓库默认指向 `Fantareal` 主仓库，但用户当前在 `Fantareal-beta` 分支上工作。
> 同步命令必须显式指定 `--source "../Fantareal-beta"`，否则会找不到源码。

---

## 项目架构（四层模型 + 应用层）

| 层 | 职责 | 关键文件 |
|----|------|----------|
| 页面层 | HTML 渲染、页面路由 | `fantareal/page_routes.py`、`templates/` |
| API 层 | 接收前端请求、返回 JSON | `fantareal/chat_api_routes.py`、`config_api_routes.py`、`mod_api_routes.py` |
| 状态层 | 槽位隔离、角色卡 / 设置 / 记忆 / 世界书读写 | `fantareal/app.py`、`fantareal/slot_runtime.py` |
| 业务 / 生成层 | 组装 prompt、调用模型、写回历史 | `fantareal/prompt_builder.py`、`fantareal/worldbook_logic.py`、`fantareal/memory_merge_logic.py`、`fantareal/preset_rules.py`、`fantareal/workshop_logic.py`、`fantareal/macro_variables.py` ⭐、`fantareal/route_forwarding.py` ⭐ |
| 插件层 | Mod 发现、加载、挂载 | `mods/*/app.py`、`fantareal/mods_runtime.py` |
| 模型层 | Pydantic 数据模型 | `fantareal/app_models.py` |
| 应用层 | 独立游戏 / 应用 | `game/Tea Party/` ⭐ |
| 数据层 | 文件存储 | `data/`、`cards/`、`exports/`、`static/`、`assets/` |

> ⭐ = 新增（在 beta 分支中）

**一次聊天的主链路**：

```
前端 /chat 发消息
  → chat_api_routes.py
    → app.py 的 generate_reply()
      → worldbook_logic.py 匹配世界书
      → memory_merge_logic.py 召回记忆
      → prompt_builder.py 拼装
        → macro_variables.py 替换 {{var}} / <var>
      → route_forwarding.py 选 Provider / failover
      → 模型 API 调用
      → write_json 写回聊天历史
```

---

## 核心约束（违反必出 Bug）

1. **持久化入口唯一**：所有 JSON 读写必须通过 `fantareal/app.py` 的 `read_json()` / `write_json()` / `persist_json()`。严禁直接 `open()` 或 `json.dump()`。
2. **API 返回格式**：统一 `{"ok": bool, ...}`，不要自己发明格式。
3. **槽位隔离**：几乎所有数据按 `slot_id` 隔离。**例外**：`mods/mobile-chat/` 的数据按 `card_uid` 隔离，独立于主项目槽位体系。操作数据前确认隔离维度正确——拿错维度 = 拿到别人的数据。
4. **JSON 写入无备份**：`write_json` 直接覆盖，出错不可逆。修改涉及 `persist_json` 的逻辑时要格外小心。
5. **Mod 模式**：新 Mod 放 `mods/<名称>/`，需要有 `mod.json`（label / version / hooks）+ `app.py`。`fantareal/mods_runtime.py` 会自动扫描并挂载。
6. **Mod hooks 类型**：`chat_styles`（注入主 Chat 样式）/ `chat_scripts`（注入主 Chat 脚本），定义在 `mod.json` 的 `hooks` 字段。
7. **禁止擅自精简**：`说明书.md` 中标注的核心校验逻辑和边界检查，禁止以"简化"或"重构"为由删除或绕过。
8. **行号权威性**：修改代码前以 `说明书_auto.md`（AST 实时，行号永远准）的行号为准。`说明书.md` 的行号已经过 `verify_map.py --strict` 校验，但源码改动后需要重跑 sync 同步 + verify 校验。

---

## 排查问题速查

| 现象 | 先看这里 |
|------|----------|
| 页面打不开 / 404 | `fantareal/page_routes.py` |
| 按钮点不动 / API 报错 | `fantareal/chat_api_routes.py` 或 `fantareal/config_api_routes.py` |
| AI 回复内容不对 | `fantareal/prompt_builder.py`、`fantareal/worldbook_logic.py` |
| 宏变量没替换 / 替换错 | `fantareal/macro_variables.py` |
| 多 Provider 切换无效 | `fantareal/route_forwarding.py` |
| 世界书不触发 | `fantareal/worldbook_logic.py` |
| 记忆 / 设置没保存 | `fantareal/app.py` 的 `write_json` / `persist_json` |
| 切槽位后数据乱 | `fantareal/slot_runtime.py` |
| 切角色卡后小手机数据乱 | `mods/mobile-chat/app.py`（注意 card_uid 而非 slot_id） |
| Mod 不生效 | `fantareal/mods_runtime.py` + mod 自身的 `mod.json` / `app.py` |
| 浏览器没打开 | `fantareal/launcher.py` → `find_browser_executable()` |

---

## 修改代码的工作流

1. 理解需求 → 查 [`maps/quick_ref.md`](maps/quick_ref.md) 或 [`maps/architecture.md`](maps/architecture.md) 确定涉及哪个模块
2. 读 [`maps/说明书.md`](maps/说明书.md) 对应章节，关注 **⚠️ 常见坑** 字段
3. 用 [`maps/说明书_auto.md`](maps/说明书_auto.md) 或 Grep 搜索确认函数名和**权威行号**
4. 先向用户说明计划（改哪些文件、为什么），确认后再动手
5. 只改必要的代码，保持原有风格
6. 改完告诉用户运行 `启动webui.bat` 测试

---

## 地图同步

地图仓库在 `Fantareal-beta` 代码变化时也需要更新：

```bash
# 推荐：仅重新生成 AST 索引（说明书.md 是本仓库自维护的，不从 beta 复制）
python scripts/sync_map.py --source "../Fantareal-beta"

# 显式同步：把 beta 的手写说明书复制为 说明书_legacy.md
python scripts/sync_map.py --source "../Fantareal-beta" --with-legacy

# 仅复制手写说明书（不跑 AST 扫描）
python scripts/sync_map.py --source "../Fantareal-beta" --with-legacy --skip-scan
```

> 💡 默认 `sync_map.py` **不会**复制 beta 的 `说明书.md`，因为本仓库的 `maps/说明书.md` 是人工维护的注释版（行号已 verify 准），比手写快照更准确。`scan_map.py` 会自动跳过 `backups/` 等临时目录（见 `scripts/scan_map.py` 的 `skip_dirs` 集合）。

---

## 给用户交付时

- 提供完整覆盖的代码块，不要只给 diff
- 说明具体替换位置（文件名 + 行号范围）
- 一次只交付一个改动，不要多个改动混在一起
