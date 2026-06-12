```json
{
  "用户输入": "当前一句话",
  "检索": "召回相关记忆 + 匹配世界书",
  "打包": "预设 + 角色卡 + 世界书 + 记忆 + 用户资料 + 历史 + 约束（含宏变量替换）",
  "调用": "OpenAI 兼容模型接口（支持多 Provider 路由转发 / failover）",
  "写回": "聊天历史 / 运行时状态 / 导出文件"
}
```

---

## 1. 项目分层

```json
{
  "入口层": ["app.py（兼容入口）", "fantareal/launcher.py"],
  "页面层": ["fantareal/page_routes.py", "templates/"],
  "接口层": ["fantareal/chat_api_routes.py", "fantareal/config_api_routes.py", "fantareal/mod_api_routes.py"],
  "业务层": [
    "fantareal/app.py",
    "fantareal/prompt_builder.py",
    "fantareal/worldbook_logic.py",
    "fantareal/memory_merge_logic.py",
    "fantareal/workshop_logic.py",
    "fantareal/slot_runtime.py",
    "fantareal/preset_rules.py",
    "fantareal/macro_variables.py",
    "fantareal/route_forwarding.py"
  ],
  "插件层": ["mods/*/app.py", "fantareal/mods_runtime.py"],
  "模型层": ["fantareal/app_models.py"],
  "应用层": ["game/Tea Party/"],
  "数据层": ["data/", "cards/", "exports/", "static/", "assets/"]
}
```

> 📌 **新模块**：`macro_variables.py` 负责 Prompt 宏变量替换；`route_forwarding.py` 负责多 Provider 路由转发 / failover / Key 轮换。
> 📌 **新应用**：`game/Tea Party/` 是一个独立游戏子项目（派对彩带大对决）。

---

## 2. 入口与装配

### 2.1 根目录 `app.py`

根目录 `app.py` 只是兼容入口，方便：

- `uvicorn app:app`
- 封包启动器
- 某些旧脚本调用

真正核心都在 [fantareal/app.py](fantareal/app.py)。

### 2.2 `fantareal/launcher.py` 的职责

桌面启动器，用户双击 `启动webui.bat` 时：

- 找空闲端口（`is_port_open` / `get_free_port`）
- 启动 uvicorn（`start_local_server`）
- 等端口连通（`wait_for_port`）
- 用浏览器 app 模式打开（`launch_app_window`）

### 2.3 `fantareal/app.py` 的职责

整个项目的"总装配器"：

- 决定运行目录（`get_runtime_base_dir`）
- 初始化数据目录（`bootstrap_runtime_layout`）
- 定义默认配置（`DEFAULT_PERSONA` / `DEFAULT_SETTINGS`）
- 读取和保存 JSON 数据（`read_json` / `write_json` / `persist_json`）
- 处理上传、导出、迁移
- 创建 FastAPI 应用
- 把页面路由、API 路由、插件路由挂进去
- 暴露 `route_ctx` 给其它模块使用

主链路上 `generate_reply()` 负责一次完整回复的总封装。

---

## 3. 页面路由索引

页面路由集中在 `fantareal/page_routes.py`。

### 3.1 主页面

| 路径 | 页面 | 作用 |
|---|---|---|
| `/` | 跳转 | 自动跳转到聊天页 |
| `/chat` | 聊天页 | 主对话界面 |

### 3.2 配置页

| 路径 | 页面 | 作用 |
|---|---|---|
| `/config` | 全局设置 | 全局运行参数 |
| `/config/user` | 用户设定 | 用户资料 |
| `/config/workshop` | 创意工坊 | 阶段、触发、资源 |
| `/config/card` | 角色卡 | 当前人设与卡片管理 |
| `/config/preset` | 预设 | prompt 预设管理 |
| `/config/memory` | 记忆 | 原记忆 / 合并记忆 / 大纲 |
| `/config/worldbook` | 世界书设置 | 世界书总配置 |
| `/config/worldbook/entries` | 词条管理 | 世界书条目编辑 |
| `/config/sprite` | 立绘管理 | 差分立绘与头像 |
| `/config/about` | 关于页 | 项目信息 |

### 3.3 插件页

| 路径 | 页面 | 作用 |
|---|---|---|
| `/mods/{mod_slug}` | 插件宿主页 | 统一壳页面 |
| `/mods/{mod_slug}/app/` | 插件应用页 | 插件自己的 WebUI |

### 3.4 页面导航分组

左侧导航在 `templates/_grouped_nav.html` 中分成：

- 聊天
- 设置
- 人设
- 世界书
- 插件
- 关于

---

## 4. 路由文件职责

| 路由文件 | 关键函数 | 行号 |
|---|---|---|
| `fantareal/page_routes.py` | `register_page_routes` | 见 说明书_auto.md |
| | `build_chat_template_context` | |
| | `_opening_message_from_persona` | |
| `fantareal/chat_api_routes.py` | `register_chat_api_routes` | |
| | `api_chat` / `api_chat_stream` | |
| | `api_get_history` | |
| | `api_edit_user_message` | |
| | `api_reroll_assistant_message` | |
| | `api_chat_prompt_preview` | |
| | `api_end_conversation` | |
| | `api_reset` / `api_export_history` | |
| `fantareal/config_api_routes.py` | `register_config_api_routes` | |
| | `api_get_settings` / `api_save_settings` | |
| | `strip_json_comments` / `parse_json_import_payload` | |
| `fantareal/mod_api_routes.py` | `register_mod_api_routes` | |
| | `/api/mods` / `/api/mods/{mod_slug}` | |
| `fantareal/mods_runtime.py` | `discover_mods` | 第 89 行 |
| | `load_mod_app` | 第 116 行 |
| | `mount_discovered_mods` | 第 132 行 |
| | `find_mod` | 第 144 行 |
| | `slugify_mod_name` / `read_mod_manifest` | |
| | `normalize_hook_url` / `normalize_hooks` | |

---

## 5. 主模块函数总览

> 行号均为源码实际行号，由 `scripts/scan_map.py` 自动提取，永远准确。
> 详细签名 / 嵌套方法 / Pydantic 字段请看 [maps/说明书_auto.md](说明书_auto.md)。

### 5.1 `fantareal/app.py`（233 个函数 / 1 个类）

**最大文件，项目大脑。** 关键函数分组：

- **运行目录**：`get_runtime_base_dir`（L86）/ `get_resource_dir` / `bootstrap_runtime_layout`
- **默认数据**：`default_role_card` / `default_user_profile` / `default_creative_workshop` / `default_preset_store` / `DEFAULT_PERSONA` / `DEFAULT_SETTINGS`
- **JSON 读写**：`load_env_file` / `read_json` / `write_json` / `persist_json` / `parse_bool` / `clamp_int` / `clamp_float`
- **清洗函数**：`sanitize_settings` / `sanitize_tags` / `sanitize_memories` / `sanitize_slot_id` / `sanitize_slot_registry` 等
- **槽位路径**：`get_slot_registry` / `get_active_slot_id` / `get_slot_dir` / `persona_path` / `conversation_path` / `settings_path` 等
- **角色卡**：`get_persona` / `parse_role_card_json` / `extract_role_card_payload` / `build_persona_from_role_card` / `apply_role_card`
- **记忆 / 世界书 / 卡片**：`get_memories` / `get_worldbook_store` / `get_worldbook_entries` / `get_current_card`
- **上传资源**：`save_image_upload_for_slot` / `save_workshop_asset_upload` / `save_workshop_state`
- **运行时配置**：`get_runtime_chat_config` / `get_runtime_embedding_config` / `get_runtime_rerank_config`
- **网络请求**：`build_api_url` / `build_headers` / `request_json` / `fetch_available_models` / `request_model_reply` / `stream_model_reply` / **`generate_reply`**（主入口）
- **世界书运行**：`match_worldbook_entries` / `enforce_worldbook_fact_in_reply` 等 30+ 个内部函数
- **记忆召回**：`retrieve_memories` / `build_conversation_transcript` / `summarize_conversation_to_memory` / `archive_current_conversation`
- **回复拆分**：`extract_reasoning_field` / `combine_think_parts` / `extract_reply_parts` / `compose_full_reply`
- **日志**：`make_access_style` / `format_access_log` / `chinese_access_log`

### 5.2 `fantareal/app_models.py`（50 个 Pydantic 类）

所有 Pydantic 请求 / 响应模型集中在这里。关键类：

| 类 | 行号 | 作用 |
|---|---|---|
| `ChatRequest` | L9 | 聊天请求 |
| `ChatHistoryEditRequest` | L14 | 编辑消息 |
| `ChatHistoryRerollRequest` | L19 | 重 roll 消息 |
| `PersonaPayload` | L33 | 角色人设 |
| `SettingsPayload` | L39 | 全局设置 |
| `MemoryItemPayload` / `MemoryListPayload` | L73 / L81 | 原记忆 |
| `MergedMemoryItemPayload` / `MergedMemoryListPayload` | L85 / | 合并记忆 |
| `MemoryOutlineItemPayload` | | 记忆大纲 |
| `MemoryMergePayload` | | 手动合并参数 |
| `UserProfilePayload` | | 用户资料 |
| `WorldbookEntryPayload` | L178 附近 | 世界书词条 |
| `WorldbookSettingsPayload` / `WorldbookPayload` | | 世界书总配置 |
| `PresetPromptPayload` / `PresetStorePayload` 等 | | 预设相关 |
| `SlotState` / `SlotMetadata` / `SlotChatMessage` 等 | | 槽位运行态 |
| `ScenarioBundle` / `ScenarioBundleImportPayload` | | 场景导出包 |

### 5.3 `fantareal/prompt_builder.py`（50 个函数）

把内容打包成 LLM 输入的核心。关键函数：

- `configure_prompt_builder`（依赖注入）
- `build_worldbook_prompt`（世界书拼装）
- `build_retrieval_prompt`（召回记忆）
- `build_memory_recap_prompt`（长期记忆）
- `build_user_profile_prompt`（用户资料）
- `build_sprite_prompt`（sprite 输出规则）
- `filter_prompt_history`（过滤历史）
- `build_conversation_transcript`（历史转录）
- **`build_prompt_package`**（总打包入口）
- **`build_messages`**（直接取 messages 数组）

打包顺序见第 9 节。

### 5.4 `fantareal/worldbook_logic.py`（21 个函数）

- 关键词匹配：`keyword_matches_query`
- 触发别名拆分：`split_trigger_aliases`
- 注入位置 / 角色 / 深度 / 顺序 / 提示层规范化
- **`match_worldbook_entries`**（核心匹配）
- **`enforce_worldbook_fact_in_reply`**（输出守卫）

### 5.5 `fantareal/memory_merge_logic.py`（25 个函数）

- 合并数据读取：`get_merged_memories` / `save_merged_memories` / `get_memory_outline` / `save_memory_outline`
- 模型合并：`build_memory_merge_prompt` / `request_memory_merge_with_model`
- 兜底合并：`_fallback_merge_result`
- 解析：`_parse_merge_response_json`
- **核心**：`merge_memories_to_outline`

### 5.6 `fantareal/workshop_logic.py`（23 个函数）

- 创意工坊规范化与默认值
- `workshop_effective_fields` / `get_workshop_stage` / `get_workshop_stage_label`
- 触发匹配：`workshop_rule_matches_trigger` / `build_workshop_trigger_token`
- **核心**：`select_workshop_match`

### 5.7 `fantareal/slot_runtime.py`（25 个函数 / 1 个类）

主类：`SlotRuntimeService`。负责：

- 读 snapshot
- 猜时间
- 标准化聊天历史
- 构建 summary buffer
- 构建 active preset / variable store / runtime media
- 构建完整 slot state

### 5.8 `fantareal/preset_rules.py`（33 个函数）

- 预设模块常量：`DEFAULT_PRESET_MODULES` / `RUNTIME_ONLY_PRESET_MODULES` / `PRESET_MODULE_RULES` / `PRESET_MODULE_MUTEX`
- 预设 CRUD：`create_preset_in_store` / `activate_preset_in_store` / `duplicate_preset_in_store` / `delete_preset_from_store`
- 拼装：`build_preset_prompt_from_preset` / `build_preset_output_guard_from_preset`

### 5.9 `fantareal/macro_variables.py`（11 个函数）⭐ 新

Prompt 宏变量替换。支持的语法：

- `{{var_name}}` 和 `{{var_name:modifier}}`（如 `{{user_name}}` / `{{user_name:default}}`）
- `<var_name>`（如 `<user>`）
- 别名表：`user` / `user_name` / `char` / `char_name`

关键函数：

- `_clean_text` / `_normalize_role_id`（L18 / L22）
- `_split_aliases`（L30）
- `_role_from_persona` / `_roles_from_card` / `_format_cast`
- **`build_macro_context`**（L100，构建上下文）
- **`render_macro_variables`**（L133，单段文本替换）
- `render_prompt_segments_with_macros`（L202）
- `render_messages_with_macros`（L253，多消息批量替换）

### 5.10 `fantareal/route_forwarding.py`（33 个函数 / 1 个类）⭐ 新

多 Provider 路由转发 / failover / Key 轮换。

关键常量：

- `DEFAULT_ROUTE_FORWARDING_CONFIG`
- `RETRY_STATUS_CODES = {408, 409, 425, 429}`
- `KNOWN_ENDPOINT_SUFFIXES = ("chat/completions", "messages", "embeddings", "rerank", "rerank/compress")`

关键函数 / 类：

- `sanitize_provider` / `sanitize_route_forwarding_config`
- `should_retry_status_code` / `endpoint_suffix_from_url`
- `build_forward_url` / `is_external_http_url` / `provider_keys`
- **`class RouteForwardingRuntime`**（L147，路由运行时）
- 钩子深度用 `contextvars.ContextVar` 控制，防递归

---

## 6. 插件模块总览

`mods_runtime.py` 自动发现、加载、挂载。`mod.json` 示例：

```json
{
  "label": "小手机",
  "version": "4.5.0-alpha.1",
  "hooks": {
    "chat_styles": ["/static/mobile-chat-ui.css?v=..."],
    "chat_scripts": ["/static/mobile-chat-chat.js?v=..."]
  }
}
```

> 💡 **mod.json hooks 类型**：`chat_styles` 注入主 Chat 样式，`chat_scripts` 注入主 Chat 脚本（见 6.x 节）。

### 6.1 `mods/worldbook maker/app.py`（47 个函数 / 6 个类）

世界书生成工具。提供"关键词 → 词条"的自动生成。

### 6.2 `mods/soul weaver/app.py`（75 个函数）

余音：叙事 / 情绪分析 / 内心独白生成。负责从聊天历史中提取情绪、主题、叙事线索。

### 6.3 `mods/status panel/app.py`（45 个函数 / 4 个类）

游玩状态栏：角色情绪、场景信息、好感度、体力等可视化状态面板。

### 6.4 `mods/card writer/app.py`（125 个函数 / 7 个类）

古法写卡器：角色卡编辑、生成、审阅、辅助写作、导出导入。

关键类 / 函数：

- `CardCompiler`（编译项目成目标结构）
- `build_copilot_prompt_text` / `request_copilot_review` / `build_copilot_candidate`
- `normalize_project` / `project_from_payload`

### 6.5 `mods/tavern-card-converter/app.py`（16 个函数 / 2 个类）

酒馆卡转换器：SillyTavern 格式 ↔ Fantareal 格式。

### 6.6 `mods/mobile-chat/app.py`（387 个函数 / 32 个类）⭐ 大 Mod

**小手机**：独立于主 Chat 的群聊与轻应用插件，v4.5.0-alpha.1。

主要能力：

- 主 Chat 内的悬浮球、手机面板和轻应用
- 独立的小手机后台管理页面
- 群聊、消息、角色资料
- 动态、论坛、直播、邮箱、日记、日程
- 通知与电话会话
- Prompt 构建和模型调用
- 4 套主题：`modern` / `social` / `xianxia` / `apocalypse`

数据按 `card_uid` 隔离（非 slot_id）。详细架构见 [docs/mobile-chat-architecture.md](../Fantareal-beta/docs/mobile-chat-architecture.md)。

### 6.7 `mods/state_journal/app.py`（265 个函数 / 1 个类）⭐ 新 Mod

**心笺**：AI 结构化状态记录与幕笺展示工具，v2.0.9。

主要能力：

- 角色配置（character_status.json）
- 关系记录（relationship.json）
- 内置模板（templates_builtin/）
- 美化包支持（beauty_packs/）
- 主 Chat 注入：`chat_scripts` 钩子

自带文档（`mods/state_journal/docs/`）：

- 心笺使用说明
- 心笺 v2.0 稳定版说明
- 如何添加新的模板字段
- 如何制作心笺美化包

---

## 7. 应用层：`game/Tea Party/`

独立的游戏子项目：**派对彩带大对决**。纯逻辑、无 I/O。

```
game/Tea Party/
├─ __init__.py          导出 PartyGame 与模型
├─ engine.py            36 个函数 / 1 个类（PartyGame）
├─ models.py            12 个函数 / 11 个类（GameMode / PlayerState / ...）
├─ ai_opponent.py       3 个函数
├─ ai_instructions.py   2 个函数
├─ test_verify.py       4 个函数
├─ pictures/            美术资源
└─ sounds/              音效资源
```

主类：

- `PartyGame`（L58）：游戏引擎核心
- `MAX_ITEM_SLOTS` / `ActionResult` / `BattleLogEntry` / `CannonState` / `GameEvent` / `GameMode` / `GamePhase` / `ItemType` / `PlayerState` / `RoundType` / `Target`

---

## 8. `fantareal/app.py` 里的主要配置默认值

### 8.1 路径类

```json
{
  "DATA_DIR": "data/",
  "SLOTS_DIR": "data/slots/",
  "STATIC_DIR": "static/",
  "TEMPLATES_DIR": "templates/",
  "UPLOAD_DIR": "static/uploads/",
  "SPRITES_DIR": "static/sprites/",
  "CARDS_DIR": "cards/",
  "MODS_DIR": "mods/",
  "EXPORT_DIR": "exports/"
}
```

### 8.2 模型 / 上传类

```json
{
  "MAX_UPLOAD_SIZE_BYTES": 10485760,
  "MAX_BACKGROUND_UPLOAD_SIZE_BYTES": 31457280,
  "MAX_WORKSHOP_UPLOAD_SIZE_BYTES": 26214400,
  "MAX_FONT_UPLOAD_SIZE_BYTES": 5242880,
  "REQUEST_RETRY_ATTEMPTS": 5,
  "REQUEST_RETRY_BASE_DELAY_SECONDS": 1.0
}
```

### 8.3 槽位 / Persona 默认值

```json
{
  "GLOBAL_RUNTIME_ID": "global_workspace",
  "GLOBAL_RUNTIME_NAME": "当前记忆",
  "LEGACY_SLOT_IDS": ["slot_1", "slot_2", "slot_3"],
  "DEFAULT_SLOT_IDS": ["global_workspace"],
  "DEFAULT_PERSONA": {
    "name": "Xuxu",
    "system_prompt": "You are a gentle, patient, and attentive AI companion. Respond naturally, show care, and avoid overly templated phrasing.",
    "greeting": "What would you like to talk about today? I am here with you."
  }
}
```

### 8.4 聊天默认设置 `DEFAULT_SETTINGS`

```json
{
  "llm_base_url": "",
  "llm_api_key": "",
  "llm_model": "",
  "theme": "light",
  "temperature": 0.85,
  "history_limit": 20,
  "request_timeout": 120,
  "demo_mode": false,
  "ui_opacity": 0.84,
  "background_image_url": "",
  "background_overlay": 0.42,
  "font_family_url": "",
  "font_family_name": "",
  "font_size": 15,
  "font_weight": 400,
  "font_color": "",
  "embedding_base_url": "",
  "embedding_api_key": "",
  "embedding_model": "",
  "embedding_fields": ["title", "content", "tags"],
  "retrieval_top_k": 4,
  "rerank_enabled": false,
  "rerank_base_url": "",
  "rerank_api_key": "",
  "rerank_model": "",
  "rerank_top_n": 3,
  "sprite_enabled": false,
  "sprite_base_path": "/static/sprites",
  "memory_summary_length": "medium",
  "memory_summary_max_chars": 520
}
```

### 8.5 你最容易问到的字段

- `history_limit`：最近聊天记录最多多少轮送进 prompt
- `retrieval_top_k`：召回记忆最多取多少条
- `embedding_fields`：哪些字段参与记忆向量化
- `memory_summary_max_chars`：记忆摘要最大长度
- `sprite_enabled`：是否启用 sprite tag
- `demo_mode`：没配模型时是否走演示模式

---

## 9. `fantareal/prompt_builder.py` 的输入顺序

`build_prompt_package()` 的输入拼装顺序（重要！）：

```json
{
  "预设": "preset_prompt",
  "世界书前置": "before_char_defs",
  "角色卡": "system_prompt",
  "稳定世界书": "stable",
  "后置世界书": "after_char_defs",
  "长期记忆": "memory_recap_prompt",
  "用户资料": "user_profile_prompt",
  "当前状态世界书": "current_state",
  "召回记忆": "retrieval_prompt",
  "动态世界书": "dynamic",
  "世界书问答守卫": "worldbook_answer_guard",
  "sprite / 输出约束": "sprite_prompt",
  "最近聊天记录": "recent_history_text",
  "最终输出守卫": "preset_output_guard_prompt + worldbook_output_guard_prompt",
  "用户输入": "clean_user_message"
}
```

---

## 10. `fantareal/worldbook_logic.py` 默认值

```json
{
  "enabled": true,
  "debug_enabled": false,
  "max_hits": 3,
  "default_case_sensitive": false,
  "default_whole_word": false,
  "default_match_mode": "any",
  "default_secondary_mode": "all",
  "default_entry_type": "keyword",
  "default_group_operator": "and",
  "default_chance": 100,
  "default_sticky_turns": 0,
  "default_cooldown_turns": 0,
  "default_insertion_position": "after_char_defs",
  "default_injection_depth": 0,
  "default_injection_role": "system",
  "default_injection_order": 100,
  "default_prompt_layer": "follow_position",
  "recursive_scan_enabled": false,
  "recursion_max_depth": 2
}
```

---

## 11. 数据怎么分

```json
{
  "data/": ["全局设置", "记忆", "世界书", "预设", "槽位运行状态", "导出缓存"],
  "cards/": ["角色卡源文件"],
  "exports/": ["导出产物"],
  "static/": ["上传图片", "立绘", "前端静态资源"],
  "assets/": ["示例数据", "模板资源", "说明素材"],
  "mods/": ["各插件自己的数据和页面"]
}
```

> 📌 **小手机的数据是按 `card_uid` 隔离的**，独立于主项目的 `slot_id` 隔离体系。

---

## 12. 页面检索速查

| 想找 | 路径 / 文件 |
|---|---|
| 聊天 | `/chat` |
| 记忆 | `/config/memory` |
| 世界书 | `/config/worldbook` |
| 世界书词条 | `/config/worldbook/entries` |
| 预设 | `/config/preset` |
| 角色卡 | `/config/card` |
| 用户资料 | `/config/user` |
| 工坊 | `/config/workshop` |
| 关于 | `/config/about` |
| 插件 | `/mods/{slug}` |
| 聊天接口 | `fantareal/chat_api_routes.py` |
| 配置接口 | `fantareal/config_api_routes.py` |
| 页面壳 | `fantareal/page_routes.py` |
| 插件发现 | `fantareal/mods_runtime.py` |
| 插件专属 API | `mods/*/app.py` |
| Prompt 打包 | `fantareal/prompt_builder.py` |
| 宏变量替换 | `fantareal/macro_variables.py` ⭐ |
| 多 Provider 路由 | `fantareal/route_forwarding.py` ⭐ |
| 记忆合并 | `fantareal/memory_merge_logic.py` |
| 世界书匹配 | `fantareal/worldbook_logic.py` |
| 预设拼装 | `fantareal/preset_rules.py` |
| 工坊规则 | `fantareal/workshop_logic.py` |
| 槽位状态 | `fantareal/slot_runtime.py` |
| 数据模型 | `fantareal/app_models.py` |

---

## 13. 地图文件分工

| 文件 | 角色 | 准确性 |
|---|---|---|
| `maps/architecture.md`（本文件） | 架构总览 / 路由表 / 函数清单 / 默认值 | 手写 + 引用 auto |
| `maps/说明书.md` | **注释版项目地图**（1,553 entry），含简介 / ⚠️ 常见坑 / 🛠️ 改动建议 / 🔗 相关函数 | 行号已通过 `verify_map.py --strict` 校验 100% 准 |
| `maps/说明书_auto.md` | AST 提取的函数 / 类 / 行号索引 | **行号永远准确**（AST 源） |
| `maps/quick_ref.md` | "我想改什么" / "Bug 现象" 速查 | 手写 |

> 📌 **使用顺序**：先读 `architecture.md`（建立全局认知）→ 读 `说明书.md`（看常见坑 / 改动建议）→ 查 `说明书_auto.md`（定位代码 / 跳读）→ 翻 `quick_ref.md`（速查）。
>
> 改完代码后跑 `python scripts/sync_map.py --source "../Fantareal-beta"` 重新生成 `说明书_auto.md`，再跑 `python scripts/verify_map.py --strict` 校验行号一致性。
