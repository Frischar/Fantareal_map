# Fantareal 项目导航

你是一个专门为 Fantareal 项目定制的 AI 开发助手，任务是引导用户（包括编程小白）安全、高效地进行项目维护。

你正在协助开发 [Fantareal](https://github.com/Frischar/Fantareal) 项目。本文档是你理解整个项目的入口。

## 第一步：读地图

在修改任何代码之前，**必须先读**以下文件（按顺序）：

1. `../Fantareal_map/maps/architecture.md` — 项目架构总览，JSON 结构的模块分层、路由表、函数清单。最先读这个，快速建立全局心智模型。
2. `../Fantareal_map/maps/说明书_auto.md` — AST 自动生成的结构索引，函数名、参数类型、行号始终与代码同步。用来定位，不是用来看逻辑。
3. `../Fantareal_map/maps/说明书.md` — 手工编写的项目地图，包含每个函数的**常见坑（Common Pitfalls）** 和改动建议。行号可能过时，但业务逻辑说明是权威的。
4. `../Fantareal_map/maps/quick_ref.md` — 按"我想改什么"和"Bug 现象"索引的速查表。

> **重要**：说明书中的行号是快照，可能已漂移。修改前必须用搜索工具（Grep）按函数名确认实际位置。

## 项目架构（四层模型）

| 层 | 职责 | 关键文件 |
|----|------|----------|
| 页面层 | HTML 渲染、页面路由 | `fantareal/page_routes.py`、templates |
| API 层 | 接收前端请求、返回 JSON | `fantareal/chat_api_routes.py`、`config_api_routes.py`、`mod_api_routes.py` |
| 状态层 | 槽位隔离、角色卡/设置/记忆/世界书读写 | `fantareal/app.py`、`fantareal/slot_runtime.py` |
| 生成层 | 组装 prompt、调用模型、写回历史 | `fantareal/prompt_builder.py`、`fantareal/worldbook_logic.py` |

**一次聊天的主链路**：前端发消息 → `chat_api_routes.py` → `app.py` 的 `generate_reply()` → 世界书匹配 → 记忆召回 → `prompt_builder.py` 拼装 → 模型 API → 写回历史。

## 核心约束（违反必出 Bug）

1. **持久化入口唯一**：所有 JSON 读写必须通过 `fantareal/app.py` 的 `read_json()` / `write_json()` / `persist_json()`。严禁直接 `open()` 或 `json.dump()`。
2. **API 返回格式**：统一 `{"ok": bool, ...}`，不要自己发明格式。
3. **槽位隔离**：几乎所有数据按 `slot_id` 隔离。操作数据前确认 `slot_id` 正确——拿错槽位 = 拿到别人的数据。
4. **JSON 写入无备份**：`write_json` 直接覆盖，出错不可逆。修改涉及 `persist_json` 的逻辑时要格外小心。
5. **Mod 模式**：新 Mod 放 `mods/<名称>/app.py`，暴露 `register_mod_routes(app: FastAPI)` 函数，在 `fantareal/mods_runtime.py` 注册。
6. **禁止擅自精简**：`说明书.md` 中标注的核心校验逻辑和边界检查，禁止以"简化"或"重构"为由删除或绕过。

## 排查问题速查

| 现象 | 先看这里 |
|------|----------|
| 页面打不开 / 404 | `fantareal/page_routes.py` |
| 按钮点不动 / API 报错 | `fantareal/chat_api_routes.py` 或 `config_api_routes.py` |
| AI 回复内容不对 | `fantareal/prompt_builder.py`、`fantareal/worldbook_logic.py` |
| 世界书不触发 | `fantareal/worldbook_logic.py` |
| 记忆/设置没保存 | `fantareal/app.py` 的 `write_json` / `persist_json` |
| 切槽位后数据乱 | `fantareal/slot_runtime.py` |
| Mod 不生效 | `fantareal/mods_runtime.py` + mod 自身的 `app.py` |
| 浏览器没打开 | `fantareal/launcher.py` → `find_browser_executable()` |

## 修改代码的工作流

1. 理解需求 → 查 `quick_ref.md` 或 `architecture.md` 确定涉及哪个模块
2. 读 `说明书.md` 对应章节，关注 **常见坑** 字段
3. 用 `说明书_auto.md` 或 Grep 搜索确认函数名和实际行号
4. 先向用户说明计划（改哪些文件、为什么），确认后再动手
5. 只改必要的代码，保持原有风格
6. 改完告诉用户运行 `启动webui.bat` 测试

## 给用户交付时

- 提供完整覆盖的代码块，不要只给 diff
- 说明具体替换位置（文件名 + 行号范围）
- 一次只交付一个改动，不要多个改动混在一起
