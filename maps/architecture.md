```json
{
  "用户输入": "当前一句话",
  "检索": "召回相关记忆 + 匹配世界书",
  "打包": "预设 + 角色卡 + 世界书 + 记忆 + 用户资料 + 历史 + 约束",
  "调用": "OpenAI 兼容模型接口",
  "写回": "聊天历史 / 运行时状态 / 导出文件"
}
```

---

## 1. 项目分层

```json
{
  "入口层": ["根目录 app.py", "fantareal/app.py", "fantareal/launcher.py"],
  "页面层": ["fantareal/page_routes.py", "templates/"],
  "接口层": ["fantareal/chat_api_routes.py", "fantareal/config_api_routes.py", "fantareal/mod_api_routes.py"],
  "业务层": ["fantareal/prompt_builder.py", "fantareal/worldbook_logic.py", "fantareal/memory_merge_logic.py", "fantareal/workshop_logic.py", "fantareal/slot_runtime.py", "fantareal/preset_rules.py"],
  "插件层": ["mods/*/app.py", "fantareal/mods_runtime.py"],
  "模型层": ["fantareal/app_models.py"],
  "数据层": ["data/", "cards/", "exports/", "static/", "assets/" ]
}
```

---

## 2. 入口和装配

### 2.1 根目录 `app.py`

根目录 `app.py` 只是兼容入口，方便：

- `uvicorn app:app`
- 封包启动器
- 某些旧脚本调用

真正核心都在 [fantareal/app.py](fantareal/app.py)。

### 2.2 `fantareal/app.py` 的职责

它是整个项目的“总装配器”，主要做这些事：

- 决定运行目录
- 初始化数据目录
- 定义默认配置
- 定义默认角色卡 / 默认人设 / 默认运行状态
- 读取和保存 JSON 数据
- 处理上传、导出、迁移
- 提供聊天、记忆、世界书、工坊、预设等共享函数
- 创建 `FastAPI` 应用
- 把页面路由、API 路由、插件路由挂进去
- 暴露 `route_ctx` 给其它模块使用

最后把这些模块接起来：

- [fantareal/page_routes.py](fantareal/page_routes.py)
- [fantareal/config_api_routes.py](fantareal/config_api_routes.py)
- [fantareal/chat_api_routes.py](fantareal/chat_api_routes.py)
- [fantareal/mod_api_routes.py](fantareal/mod_api_routes.py)
- [fantareal/mods_runtime.py](fantareal/mods_runtime.py)

---

## 3. 页面路由索引

页面路由集中在 [fantareal/page_routes.py](fantareal/page_routes.py)。

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

左侧导航在 [templates/_grouped_nav.html](templates/_grouped_nav.html) 中分成：

- 聊天
- 设置
- 人设
- 世界书
- 插件
- 关于

---

## 4. 路由文件职责

### 4.1 `page_routes.py`

负责把模板页面暴露成路由。

它会把：

- 当前角色卡
- 当前记忆
- 当前设置
- 当前工坊状态
- 当前预设
- 当前世界书
- 当前插件状态

打包成模板上下文。

#### 里面的主要 `def`

- `register_page_routes(app, templates, ctx)`
  - 注册所有页面路由
- `_opening_message_from_persona(persona)`
  - 取角色卡开场白
- `_summary_buffer_content(slot_id)`
  - 读取槽位摘要缓冲区
- `_has_workshop_progress(workshop_state)`
  - 判断工坊是否已有进度
- `_should_show_opening_message(...)`
  - 决定聊天页是否显示开场白
- `_should_show_workshop_opening(...)`
  - 决定是否显示工坊开场页
- `build_chat_template_context()`
  - 组装聊天页模板上下文

### 4.2 `chat_api_routes.py`

负责聊天相关接口。

#### 主要 `def`

- `register_chat_api_routes(app, ctx)`
  - 注册聊天 API
- `api_get_history()`
  - 获取聊天历史
- `api_edit_user_message()`
  - 编辑用户消息
- `api_reroll_assistant_message()`
  - 从历史消息重 roll
- `api_chat()`
  - 一次性聊天请求
- `api_chat_prompt_preview()`
  - 只预览 prompt，不发模型
- `api_chat_stream()`
  - 流式聊天接口
- `api_end_conversation()`
  - 结束会话并归档
- `api_reset()`
  - 清空聊天 / 工坊状态
- `api_export_history()`
  - 导出聊天历史

### 4.3 `config_api_routes.py`

负责所有配置数据的读写、导入、导出、测试。

#### 主要 `def`

- `strip_json_comments(raw_text)`
  - 去掉 JSON 注释
- `parse_json_import_payload(raw_json, label)`
  - 解析带注释的导入 JSON
- `_worldbook_field_present(row, key)`
  - 判断世界书字段是否真的存在
- `_apply_worldbook_import_options(...)`
  - 导入世界书时补默认注入参数
- `register_config_api_routes(app, ctx)`
  - 注册所有配置 API

### 4.4 `mod_api_routes.py`

只负责插件信息查询。

#### 主要 `def`

- `register_mod_api_routes(app, ctx)`
  - 注册插件查询接口
- `/api/mods`
  - 列出已发现插件
- `/api/mods/{mod_slug}`
  - 查询单个插件信息

### 4.5 `mods_runtime.py`

负责发现、加载和挂载插件。

#### 主要 `def`

- `slugify_mod_name(name)`
  - 把目录名转成 slug
- `read_mod_manifest(directory)`
  - 读插件 `mod.json`
- `normalize_hook_url(mount_path, value)`
  - 规范插件钩子 URL
- `normalize_hooks(mount_path, raw)`
  - 规范插件钩子配置
- `discover_mods(mods_dir)`
  - 找出所有插件目录
- `load_mod_app(spec)`
  - 动态加载插件 FastAPI app
- `mount_discovered_mods(app, mods_dir)`
  - 挂载所有插件
- `find_mod(mods, slug)`
  - 从插件列表里找某个插件

---

## 5. 主模块函数总览

下面按模块把 **所有顶层 `def` / `class` 的职责** 做一轮说明。

---

# 6. `fantareal/app.py` 函数总览

这个文件最长，实际是项目的大脑。

---

## 6.1 运行目录与基础设施

- `get_runtime_base_dir()`
  - 决定运行目录
  - 打包后优先放到可写目录
- `get_resource_dir()`
  - 读取资源目录
- `bootstrap_runtime_layout()`
  - 初始化目录结构
- `default_slot_registry()`
  - 生成默认槽位注册表
- `default_sprite_base_path_for_slot()`
  - 返回立绘默认路径
- `sprite_dir_path()`
  - 立绘目录路径
- `sanitize_sprite_filename_tag()`
  - 清理立绘文件名标签
- `list_sprite_assets()`
  - 列出立绘资源
- `remove_upload_variants()`
  - 清理上传资源的派生文件
- `avatar_upload_url()`
  - 头像资源 URL
- `workshop_asset_dir()` / `workshop_asset_url()`
  - 工坊资源路径和 URL

---

## 6.2 默认数据

### 默认角色

- `default_role_card()`
  - 生成空角色卡默认结构

### 默认用户资料

- `default_user_profile()`
  - 生成默认用户资料

### 默认工坊状态

- `default_creative_workshop()`
  - 生成工坊默认结构
- `default_workshop_state()`
  - 生成工坊运行状态默认值
- `reset_workshop_state()`
  - 重置工坊状态

### 默认预设

- `default_preset_store()`
  - 生成默认预设仓库
- `sanitize_preset_store()`
  - 清理预设仓库数据
- `get_preset_store()`
  - 读取预设仓库
- `save_preset_store()`
  - 保存预设仓库
- `get_active_preset()`
  - 获取当前激活预设
- `build_preset_prompt()`
  - 生成最终预设 prompt
- `get_active_preset_module_labels()`
  - 获取已启用模块名
- `build_preset_debug_payload()`
  - 生成预设调试信息

### 默认设置

- `DEFAULT_PERSONA`
  - 默认角色人格
- `DEFAULT_SETTINGS`
  - 默认全局设置

---

## 6.3 JSON 和配置读写

- `load_env_file()`
  - 读取 `.env`
- `read_json()`
  - 读 JSON
- `write_json()`
  - 写 JSON
- `persist_json()`
  - 保险式保存 JSON
- `parse_bool()`
  - 解析布尔值
- `clamp_int()`
  - 整数限幅
- `clamp_float()`
  - 浮点数限幅
- `sanitize_background_image_url()`
  - 规范背景图 URL
- `sanitize_font_url()`
  - 规范字体 URL
- `sanitize_font_color()`
  - 规范字体颜色
- `sanitize_embedding_fields()`
  - 规范 embedding 字段列表
- `sanitize_settings()`
  - 清理全局设置
- `sanitize_tags()`
  - 清理标签列表
- `sanitize_memories()`
  - 清理记忆条目
- `sanitize_slot_id()`
  - 清理槽位 ID
- `sanitize_legacy_slot_id()`
  - 清理旧槽位 ID
- `sanitize_slot_registry()`
  - 清理槽位注册表

---

## 6.4 槽位和数据路径

- `get_slot_registry()`
  - 读槽位注册表
- `save_slot_registry()`
  - 保存槽位注册表
- `get_active_slot_id()`
  - 当前激活槽位
- `get_slot_name()`
  - 槽位名称
- `slot_summary()`
  - 槽位摘要
- `get_slot_dir()`
  - 槽位目录
- `persona_path()`
  - 角色卡路径
- `legacy_slot_dir()`
  - 旧槽位目录
- `legacy_persona_path()`
  - 旧角色卡路径
- `global_persona_path()`
  - 全局角色卡路径
- `conversation_path()`
  - 聊天历史路径
- `settings_path()`
  - 设置路径
- `memories_path()`
  - 记忆路径
- `worldbook_path()`
  - 世界书路径
- `current_card_path()`
  - 当前角色卡路径
- `legacy_current_card_path()`
  - 旧角色卡路径
- `global_current_card_path()`
  - 全局当前角色卡路径
- `workshop_state_path()`
  - 工坊状态路径
- `user_profile_path()`
  - 用户资料路径

---

## 6.5 角色卡与人设

- `get_persona()`
  - 读取当前角色人设
- `read_role_card_text()`
  - 读取角色卡文本
- `list_role_card_files()`
  - 列出角色卡文件
- `parse_role_card_json()`
  - 解析角色卡 JSON
- `repair_deepseek_card_json()`
  - 修复某些角色卡格式
- `extract_role_card_payload()`
  - 提取角色卡结构
- `build_persona_from_role_card()`
  - 从角色卡构造 persona
- `build_memories_from_role_card()`
  - 从角色卡构造初始记忆
- `apply_role_card()`
  - 应用新角色卡
- `save_workshop_card()`
  - 保存工坊关联卡

---

## 6.6 用户资料

- `sanitize_user_profile()`
  - 清理用户资料
- `get_user_profile()`
  - 获取用户资料
- `save_user_profile()`
  - 保存用户资料
- `get_role_avatar_url()`
  - 获取角色头像 URL

---

## 6.7 记忆、世界书、卡片

- `get_memories()`
  - 读取原记忆
- `save_memories()`
  - 保存原记忆
- `get_worldbook()`
  - 读取世界书旧式结构
- `get_worldbook_store()`
  - 读取世界书仓库
- `get_worldbook_entries()`
  - 读取世界书条目
- `get_worldbook_settings()`
  - 读取世界书设置
- `save_worldbook()`
  - 保存世界书旧式结构
- `save_worldbook_store()`
  - 保存世界书仓库
- `save_worldbook_entries()`
  - 保存世界书条目
- `save_worldbook_settings()`
  - 保存世界书设置
- `get_current_card()`
  - 读取当前卡片

---

## 6.8 上传与资源

- `save_image_upload_for_slot()`
  - 保存图片上传并返回 URL
- `save_workshop_asset_upload()`
  - 保存工坊资源上传
- `save_workshop_state()`
  - 保存工坊状态
- `save_image_upload_for_slot()` 这类函数负责：
  - 限制大小
  - 检查类型
  - 写入目标目录
  - 回传可访问 URL

---

## 6.9 运行时配置

- `sanitize_runtime_overrides()`
  - 清理接口传入的运行时覆盖参数
- `resolve_runtime_value()`
  - 从覆盖值 / 设置 / 环境变量中选最终值
- `get_runtime_chat_config()`
  - 取聊天模型运行配置
- `get_runtime_embedding_config()`
  - 取 embedding 配置
- `get_runtime_rerank_config()`
  - 取 rerank 配置

---

## 6.10 网络请求和模型调用

- `build_api_url()`
  - 拼 OpenAI 兼容 API 地址
- `build_headers()`
  - 组请求头
- `should_retry_status_code()`
  - 判断 HTTP 是否该重试
- `request_json()`
  - 通用 JSON 请求
- `fetch_available_models()`
  - 拉模型列表
- `request_minimal_model_reply()`
  - 轻量测试模型回复
- `fetch_embeddings()`
  - 请求 embedding 向量
- `cosine_similarity()`
  - 计算相似度
- `rerank_documents()`
  - 重排相关文档
- `request_model_reply()`
  - 请求普通聊天回复
- `stream_model_reply()`
  - 流式聊天回复
- `generate_reply()`
  - 生成一次完整回复的总封装

---

## 6.11 世界书运行逻辑

- `default_worldbook_runtime_state()`
  - 世界书运行态默认结构
- `worldbook_runtime_state_path()`
  - 世界书运行态路径
- `sanitize_worldbook_runtime_state()`
  - 清理世界书运行态
- `get_worldbook_runtime_state()`
  - 读取运行态
- `save_worldbook_runtime_state()`
  - 保存运行态
- `_normalize_worldbook_insertion_position()`
  - 标准化注入位置
- `_normalize_worldbook_injection_role()`
  - 标准化注入角色
- `_normalize_worldbook_injection_depth()`
  - 标准化插入深度
- `_normalize_worldbook_injection_order()`
  - 标准化插入顺序
- `_normalize_worldbook_prompt_layer()`
  - 标准化 prompt 层级
- `_worldbook_position_priority()`
  - 世界书位置优先级
- `_worldbook_global_selection_sort_key()`
  - 全局选择排序键
- `_worldbook_bucket_sort_key()`
  - 分桶排序键
- `bucket_worldbook_matches()`
  - 把命中条目分层分桶
- `_worldbook_entry_sort_key()`
  - 条目排序键
- `_build_worldbook_runtime_debug_entries()`
  - 生成调试显示条目
- `_worldbook_alias_match_result()`
  - 别名匹配结果
- `_evaluate_worldbook_keyword_entry()`
  - 评估关键词词条
- `_worldbook_match_payload()`
  - 构造命中结果
- `_worldbook_recursive_seed_text()`
  - 递归扫描种子文本
- `_worldbook_runtime_state_row()`
  - 运行态行数据
- `_worldbook_debug_display_sort_key()`
  - 调试显示排序键
- `match_worldbook_entries()`
  - 匹配世界书条目
- `enforce_worldbook_fact_in_reply()`
  - 在回复中强制约束世界书事实

---

## 6.12 记忆召回和聊天文本

- `build_memory_text()`
  - 把记忆条目拼成可检索文本
- `retrieve_memories()`
  - 召回相关记忆
- `build_conversation_transcript()`
  - 把聊天历史转成 prompt 文本
- `fallback_memory_from_conversation()`
  - 从聊天中生成兜底记忆
- `request_conversation_summary_with_model()`
  - 请求模型总结对话
- `sanitize_memory_summary()`
  - 清理摘要文本
- `summarize_conversation_to_memory()`
  - 把对话归档成记忆
- `archive_current_conversation()`
  - 归档当前会话

---

## 6.13 语气、思考链和回复拆分

- `normalize_sprite_tag()`
  - 标准化 sprite tag
- `extract_sprite_tag()`
  - 从回复中提取 sprite tag
- `_stringify_model_text()`
  - 把模型内容统一转文本
- `extract_reasoning_field()`
  - 读取模型 reasoning 字段
- `combine_think_parts()`
  - 合并思考链文本
- `normalize_thought_markup()`
  - 规范 `<think>` 格式
- `extract_reply_parts()`
  - 拆分回复中的 sprite / think / visible 部分
- `compose_full_reply()`
  - 拼完整回复
- `extract_stream_visible_reply()`
  - 从流式片段里提取可见内容

---

## 6.14 调试与日志

- `flush_log_handlers()`
  - 刷新日志句柄
- `make_access_style()`
  - 决定访问日志颜色
- `format_access_log()`
  - 格式化访问日志
- `resolve_access_label()`
  - 把路径转成中文标签
- `build_worldbook_debug_payload()`
  - 生成世界书调试信息
- `chinese_access_log()`
  - HTTP 中间件日志

---

## 7. `app.py` 里的主要配置默认值

这一块最容易让人迷糊，所以单独列出来。

### 7.1 路径类默认值

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

### 7.2 模型 / 上传类默认值

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

### 7.3 角色和槽位默认值

```json
{
  "GLOBAL_RUNTIME_ID": "global_workspace",
  "GLOBAL_RUNTIME_NAME": "当前记忆",
  "LEGACY_SLOT_IDS": ["slot_1", "slot_2", "slot_3"],
  "DEFAULT_SLOT_IDS": ["global_workspace"]
}
```

### 7.4 聊天默认值

```json
{
  "DEFAULT_PERSONA": {
    "name": "Xuxu",
    "system_prompt": "You are a gentle, patient, and attentive AI companion. Respond naturally, show care, and avoid overly templated phrasing.",
    "greeting": "What would you like to talk about today? I am here with you."
  },
  "DEFAULT_SETTINGS": {
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
}
```

### 7.5 你最容易问到的几个字段

- `history_limit`
  - 最近聊天记录最多多少轮送进 prompt
- `retrieval_top_k`
  - 召回记忆最多取多少条
- `embedding_fields`
  - 哪些字段参与记忆向量化
- `memory_summary_max_chars`
  - 记忆摘要最大长度
- `sprite_enabled`
  - 是否启用 sprite tag
- `demo_mode`
  - 没配模型时是否走演示模式

---

## 8. `fantareal/app_models.py` 数据模型总览

这个文件基本就是所有接口请求/响应结构的定义。

### 8.1 聊天相关

- `ChatRequest`
  - `message: str`
  - `runtime_config: dict | None = None`
- `ChatHistoryEditRequest`
  - `message_index: int`
  - `content: str`
- `ChatHistoryRerollRequest`
  - `message_index: int`
- `PersonaPayload`
  - `name`, `system_prompt`, `greeting`

### 8.2 全局设置

- `SettingsPayload`
  - 全局聊天、样式、检索、sprite、记忆摘要参数
  - 默认值大多是空字符串、`False`、常用数字

### 8.3 记忆相关

- `MemoryItemPayload`
  - `id`, `title`, `content`, `tags`, `notes`
- `MemoryListPayload`
  - `items: list[MemoryItemPayload]`
- `MergedMemoryItemPayload`
  - 多了 `source_memory_ids`, `created_at`
- `MergedMemoryListPayload`
  - 合并记忆列表
- `MemoryOutlineItemPayload`
  - `summary`, `characters`, `relationship_progress`, `key_events`, `conflicts`, `next_hooks`
- `MemoryOutlineListPayload`
  - 记忆大纲列表
- `MemoryMergePayload`
  - 手动合并记忆时提交的参数

### 8.4 用户资料

- `UserProfilePayload`
  - `display_name`, `nickname`, `profile_text`, `notes`

### 8.5 世界书

- `WorldbookEntryPayload`
  - 世界书词条结构
  - 包含关键词、注入位置、递归、提示层级等
- `WorldbookSettingsPayload`
  - 世界书全局默认值
- `WorldbookPayload`
  - 词条 + 设置

### 8.6 预设

- `PresetPromptPayload`
- `PresetPromptGroupItemPayload`
- `PresetPromptGroupPayload`
- `PresetItemPayload`
- `PresetStorePayload`
- `PresetCreatePayload`
- `PresetActionPayload`
- `PresetImportPayload`

这些类一起负责：

- 预设块
- 预设组
- 选择状态
- 导入导出
- 激活 / 复制 / 删除

### 8.7 槽位 / 运行时

- `SaveSlotSelectPayload`
- `SaveSlotRenamePayload`
- `SaveSlotResetPayload`
- `SlotMetadata`
- `SlotChatMessage`
- `SlotSummaryBuffer`
- `SlotActivePreset`
- `SlotVariableStore`
- `SlotRuntimeMedia`
- `SlotEnvironmentState`
- `SlotWorldbookContext`
- `SlotState`
- `SlotForkPayload`
- `SlotSummaryBufferPayload`
- `SlotVariablePatchPayload`
- `DynamicWorldbookPreviewPayload`

这些类基本决定了“一个槽位运行状态长什么样”。

### 8.8 其它

- `ScenarioBundle`
  - 场景导出包
- `ScenarioBundleImportPayload`
  - 场景导入参数

---

## 9. `fantareal/prompt_builder.py`

这是“怎么把内容打包给 LLM”的核心。

### 9.1 主要 `def`

- `configure_prompt_builder(**deps)`
  - 注入依赖
- `_dep(name)`
  - 取必须依赖
- `_optional_dep(name)`
  - 取可选依赖
- `_extract_runtime_guard_from_preset(preset_prompt)`
  - 从预设里剥离运行时 guard
- `_worldbook_direct_question(user_message)`
  - 判断用户是否在直接问世界书
- `build_worldbook_prompt(matches, heading=...)`
  - 把世界书命中条目拼成文本
- `build_worldbook_answer_guard(user_message, matches)`
  - 直接问设定时用的回答守卫
- `build_retrieval_prompt(retrieved_items)`
  - 把召回记忆拼成文本
- `build_memory_recap_prompt(memories)`
  - 把长期记忆拼成文本
- `build_user_profile_prompt(user_profile)`
  - 把用户资料拼成文本
- `build_sprite_prompt(llm_config)`
  - sprite 输出规则
- `strip_thought_blocks(text)`
  - 去掉 `<think>` 块
- `_same_normalized_text(left, right)`
  - 对比规范化文本
- `_is_opening_only_message(item, persona)`
  - 判断是否为只用于 UI 的开场白
- `filter_prompt_history(history, persona)`
  - 过滤掉不该进 prompt 的历史
- `build_conversation_transcript(history, persona)`
  - 把历史转成 transcript
- `build_prompt_package(...)`
  - 总打包函数
- `build_messages(...)`
  - `build_prompt_package(...)["messages"]`

### 9.2 `build_prompt_package()` 的输入顺序

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

## 10. `fantareal/worldbook_logic.py`

负责世界书数据的清洗和匹配。

### 10.1 常量

`DEFAULT_WORLDBOOK_SETTINGS` 里定义了世界书默认值：

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

### 10.2 主要 `def`

- `default_worldbook_store()`
  - 世界书仓库默认结构
- `_clamp_int()`
  - 整数限幅
- `_normalize_yes_no_bool()`
  - 规范化布尔值
- `_normalize_match_mode()`
  - 规范化匹配模式
- `_normalize_entry_type()`
  - 规范化条目类型
- `_normalize_group_operator()`
  - 规范化组操作符
- `_normalize_insertion_position()`
  - 规范化注入位置
- `_normalize_injection_role()`
  - 规范化注入角色
- `_normalize_injection_depth()`
  - 规范化 in_chat 深度
- `_normalize_injection_order()`
  - 规范化注入顺序
- `_normalize_prompt_layer()`
  - 规范化提示层级
- `_normalize_recursion_depth()`
  - 规范化递归深度
- `sanitize_worldbook_settings(raw)`
  - 清理世界书设置
- `sanitize_worldbook_entry(raw, ...)`
  - 清理单条世界书词条
- `sanitize_worldbook_store(raw)`
  - 清理整个世界书仓库
- `sanitize_worldbook(raw)`
  - 旧式世界书兼容清理
- `normalize_match_text(text)`
  - 规范化用于匹配的文本
- `split_trigger_aliases(trigger)`
  - 拆分触发别名
- `keyword_matches_query(trigger, query, ...)`
  - 判断关键词是否命中

### 10.3 世界书作用

世界书决定了：

- 哪些词条能命中
- 命中时放在哪一层
- 是否递归扫描
- 是否进 in-chat
- 是否走输出守卫

---

## 11. `fantareal/preset_rules.py`

负责预设系统。

### 11.1 常量

- `DEFAULT_PRESET_MODULES`
  - 所有预设模块默认开关
- `RUNTIME_ONLY_PRESET_MODULES`
  - 只在运行时后处理的模块
- `V4F_OUTPUT_GUARD_MARKER`
  - 运行时 guard 标记
- `V4F_OUTPUT_GUARD_PROMPT`
  - V4F 稳定器提示词
- `PRESET_MODULE_RULES`
  - 每个模块的标签和 prompt
- `PRESET_MODULE_MUTEX`
  - 冲突模块互斥表

### 11.2 主要 `def`

- `parse_bool()`
  - 解析布尔
- `parse_int()`
  - 解析整数
- `generate_preset_id()`
  - 生成预设 ID
- `generate_prompt_group_id()`
  - 生成 prompt group ID
- `generate_prompt_group_item_id()`
  - 生成 prompt group item ID
- `default_extra_prompts()`
  - 默认额外提示块
- `default_prompt_groups()`
  - 默认提示组
- `default_single_preset()`
  - 默认单个预设结构
- `default_preset_store()`
  - 默认预设仓库
- `sanitize_prompt_item()`
  - 清理单条提示块
- `normalize_selection_mode()`
  - 规范组选择模式
- `sanitize_prompt_group_item()`
  - 清理组内项
- `sanitize_prompt_group()`
  - 清理提示组
- `apply_module_mutex()`
  - 处理模块互斥
- `sanitize_single_preset()`
  - 清理单个预设
- `sanitize_preset_store()`
  - 清理预设仓库
- `get_active_preset_from_store()`
  - 取激活预设
- `build_selected_prompt_group_blocks()`
  - 组装被选中的组内容
- `build_preset_prompt_from_preset()`
  - 把预设拼成最终 prompt
- `build_preset_output_guard_from_preset()`
  - 从预设生成输出守卫
- `build_preset_output_guard_from_store()`
  - 从整个仓库生成输出守卫
- `create_preset_in_store()`
  - 新建预设
- `activate_preset_in_store()`
  - 激活预设
- `duplicate_preset_in_store()`
  - 复制预设
- `delete_preset_from_store()`
  - 删除预设

### 11.3 预设怎么理解

预设就是一组“长期稳定的 prompt 规则”。

它既能：

- 影响整体写作风格
- 影响角色输出格式
- 影响 TTS / sprite / V4F 约束

也能通过模块控制更细粒度的行为。

---

## 12. `fantareal/workshop_logic.py`

负责创意工坊 / 阶段 / 动态场景 / 资源触发。

### 12.1 常量

- `DEFAULT_WORKSHOP_STAGE_LIMITS = {"aMax": 2, "bMax": 5}`
- `WORKSHOP_OPENING_ANIMATIONS`
- `WORKSHOP_OPENING_AFTER_MODES`
- `WORKSHOP_DYNAMIC_TRIGGER_TYPES`
- `WORKSHOP_DYNAMIC_REPEAT_MODES`
- `WORKSHOP_DYNAMIC_CONTENT_TYPES`
- `WORKSHOP_DYNAMIC_PRESENTATION_MODES`

### 12.2 主要 `def`

- `_parse_bool()`
  - 布尔解析
- `_clamp_int()`
  - 整数限幅
- `_clamp_float()`
  - 浮点限幅
- `_safe_text()`
  - 截断文本
- `normalize_workshop_opening_animation()`
  - 开场动画规范化
- `normalize_workshop_opening_after_mode()`
  - 开场后续模式规范化
- `default_workshop_opening()`
  - 开场默认值
- `default_workshop_ambience()`
  - 氛围默认值
- `default_dynamic_scene()`
  - 动态场景默认值
- `default_creative_workshop()`
  - 工坊默认结构
- `normalize_workshop_stage()`
  - 工坊阶段规范化
- `normalize_workshop_trigger_mode()`
  - 触发模式规范化
- `normalize_workshop_action_type()`
  - 动作类型规范化
- `normalize_dynamic_trigger_type()`
  - 动态触发类型规范化
- `normalize_dynamic_repeat_mode()`
  - 动态重复模式规范化
- `normalize_dynamic_content_type()`
  - 动态内容类型规范化
- `normalize_dynamic_presentation_mode()`
  - 动态表现模式规范化
- `sanitize_workshop_opening()`
  - 清理开场配置
- `sanitize_workshop_ambience()`
  - 清理氛围配置
- `sanitize_dynamic_scene()`
  - 清理动态场景
- `sanitize_creative_workshop_item()`
  - 清理单项工坊规则
- `sanitize_creative_workshop()`
  - 清理完整工坊配置
- `workshop_effective_fields()`
  - 计算有效字段
- `default_workshop_state()`
  - 生成工坊运行状态默认值
- `sanitize_workshop_state()`
  - 清理工坊状态
- `get_workshop_stage()`
  - 根据 temp 得出阶段
- `get_workshop_stage_label()`
  - 阶段标签
- `workshop_rule_matches_trigger()`
  - 判断规则是否触发
- `build_workshop_trigger_token()`
  - 构造触发 token
- `get_workshop_trigger_label()`
  - 触发标签
- `select_workshop_match()`
  - 选出当前命中的工坊规则

### 12.3 工坊怎么理解

工坊就是：

- 让卡片自带“故事开场”
- 让不同阶段能触发不同资源
- 让当前阶段的背景 / 音乐 / 图像按规则切换

---

## 13. `fantareal/memory_merge_logic.py`

负责记忆合并、记忆大纲、记忆归档相关逻辑。

### 13.1 主要 `def`

- `_now_text()`
  - 当前时间字符串
- `_build_api_url()`
  - 组请求地址
- `_compact_text()`
  - 压缩长文本
- `_sanitize_tags()`
  - 清理标签
- `_sanitize_memory_item()`
  - 清理原记忆
- `_sanitize_memory_list()`
  - 清理原记忆列表
- `_sanitize_string_list()`
  - 清理字符串列表
- `_sanitize_merged_memory_item()`
  - 清理合并记忆
- `_sanitize_merged_memory_list()`
  - 清理合并记忆列表
- `_sanitize_outline_item()`
  - 清理记忆大纲条目
- `_sanitize_outline_list()`
  - 清理记忆大纲列表
- `_base_data_dir()`
  - 推导槽位数据目录
- `merged_memories_path()`
  - 合并记忆路径
- `memory_outline_path()`
  - 记忆大纲路径
- `get_merged_memories()`
  - 读取合并记忆
- `save_merged_memories()`
  - 保存合并记忆
- `get_memory_outline()`
  - 读取记忆大纲
- `save_memory_outline()`
  - 保存记忆大纲
- `build_memory_merge_prompt()`
  - 生成记忆合并提示词
- `_fallback_merge_result()`
  - 合并失败时的兜底结果
- `_parse_merge_response_json()`
  - 解析模型返回的 JSON
- `request_memory_merge_with_model()`
  - 调模型做记忆合并
- `_build_final_merged_memory()`
  - 生成最终合并记忆
- `_build_final_outline_item()`
  - 生成最终大纲条目
- `merge_memories_to_outline()`
  - 核心合并入口

### 13.2 记忆合并怎么理解

它不是聊天时实时召回用的。

它是：

- 选中若干原记忆
- 用模型整理成更高层内容
- 生成合并记忆和大纲
- 保存回本地

---

## 14. `fantareal/slot_runtime.py`

负责把一个槽位的运行状态拼成快照。

### 14.1 主类

- `SlotRuntimeService`

### 14.2 你可以把它理解成

它在做的是：

- 把当前槽位的聊天、记忆、工坊、用户资料、卡片等整理成统一运行态
- 必要时保存 snapshot
- 给页面和导出用

### 14.3 重要方法

从名字就能看出来它负责：

- 读 snapshot
- 猜时间
- 标准化聊天历史
- 构建 summary buffer
- 构建 active preset
- 构建变量 store
- 构建 runtime media
- 构建完整 slot state

---

## 15. 插件模块总览

插件都在 `mods/` 下。

### 15.1 `mods/worldbook maker/app.py`

这是世界书生成工具。

#### 主要 `def`

- `get_resource_dir()`
- `ensure_data_files()`
- `read_json()`
- `write_json()`
- `default_worldbook_store()`
- `default_workspace()`
- `clamp_float()`
- `clamp_int()`
- `sanitize_color()`
- `sanitize_generation_settings()`
- `sanitize_appearance_settings()`
- `sanitize_settings()`
- `_normalize_entry_type()`
- `_normalize_group_operator()`
- `_normalize_insertion_position()`
- `_normalize_injection_role()`
- `_normalize_prompt_layer()`
- `sanitize_worldbook_settings()`
- `sanitize_worldbook_entry()`
- `sanitize_worldbook_store()`
- `dump_worldbook_store()`
- `build_entry_signature()`
- `ensure_unique_entry_id()`
- `merge_worldbook_stores()`
- `sanitize_workspace()`
- `get_settings()`
- `save_settings()`
- `get_workspace()`
- `save_workspace()`
- `build_api_url()`
- `build_headers()`
- `extract_json_text()`
- `parse_store_from_text()`
- `try_parse_store_from_text()`
- `summarize_store()`
- `probe_models_endpoint()`
- `request_chat_completion()`
- `build_generation_messages()`
- `startup_event()`
- `index()`
- `api_get_settings()`
- `api_save_settings()`
- `api_get_workspace()`
- `api_save_workspace()`
- `api_preview_workspace()`
- `api_detect_service()`
- `api_generate()`

### 15.2 `mods/soul weaver/app.py`

这是偏“故事生成 / 素材整理 / 多模块出稿”的工具。

#### 主要 `def`

- `get_resource_dir()`
- `ensure_data_files()`
- `read_json()`
- `write_json()`
- `clamp_float()`
- `clamp_int()`
- `parse_positive_int()`
- `sanitize_settings()`
- `normalize_speaker_name()`
- `normalize_target_character()`
- `sanitize_filename()`
- `unique_path()`
- `parse_script_line()`
- `entry_to_script_line()`
- `summarize_chunk()`
- `build_entry_chunks()`
- `build_speaker_chunks()`
- `summarize_speaker_chunks()`
- `build_text_chunks()`
- `parse_script_entries()`
- `extract_character_lines()`
- `extract_character_chunks()`
- `get_settings()`
- `save_settings()`
- `request_settings()`
- `get_drafts()`
- `save_draft()`
- `build_api_url()`
- `build_headers()`
- `get_wbmaker_module()`
- `build_wbmaker_settings()`
- `generate_worldbook_with_wbmaker()`
- `merge_worldbook_partials_with_wbmaker()`
- `extract_json_text()`
- `try_parse_json()`
- `split_text()`
- `request_chat_completion()`
- `generate_with_segments()`
- `normalize_role_card()`
- `normalize_single_preset()`
- `normalize_preset()`
- `normalize_memories()`
- `normalize_worldbook()`
- `startup_event()`
- `index()`
- `api_get_settings()`
- `api_save_settings()`
- `api_get_drafts()`
- `api_parse_script()`
- `api_probe_models()`
- `api_generate_role_card()`
- `api_generate_memory()`
- `api_generate_plot()`
- `api_generate_preset()`
- `api_generate_worldbook()`
- `task_system_prompt()`
- `task_draft_type()`
- `normalize_task_result()`
- `build_chunk_user()`
- `build_merge_user()`
- `api_generate_chunk()`
- `api_generate_merge()`
- `_proxy_import()`
- `api_import_card()`
- `api_import_preset()`
- `api_import_memories()`
- `api_import_worldbook()`
- `api_export_soul()`
- `api_export_soul_local()`

### 15.3 `mods/status panel/app.py`

这是状态栏 / 角色状态展示工具。

#### 主要 `def`

- `get_resource_dir()`
- `normalize_extra_key()`
- `clone_default()`
- `read_json()`
- `write_json()`
- `migrate_json_once()`
- `ensure_runtime_data_paths()`
- `now_string()`
- `compact_text()`
- `is_emptyish()`
- `normalize_list()`
- `normalize_aliases()`
- `normalize_mention_key()`
- `same_mention()`
- `normalize_extra()`
- `normalize_field_schema()`
- `get_field_schema()`
- `save_field_schema()`
- `split_pair()`
- `normalize_character()`
- `normalize_settings()`
- `get_state()`
- `save_state()`
- `build_status_summary()`
- `normalize_update()`
- `find_character()`
- `ensure_character()`
- `update_has_risky_fields()`
- `add_pending_update()`
- `mark_processed()`
- `normalize_effect_key()`
- `should_remove_effect()`
- `should_clear_effects()`
- `apply_update_fields()`
- `apply_update_to_state()`
- `resolve_pending_update()`
- `index()`
- `api_get_state()`
- `api_save_state()`
- `api_get_field_schema()`
- `api_save_field_schema()`
- `api_get_summary()`
- `api_apply_update()`
- `api_pending_updates()`
- `api_resolve_pending()`

### 15.4 `mods/card writer/app.py`

这是缃笺写卡器，偏“辅助写作 + 结构化改卡 + 调 LLM 生成”。

#### 主要 `def`

文件特别长，但大体可以分成：

- 项目存储
- 角色卡规范化
- worldbook / memory / preset 查找
- 候选建议生成
- prompt 构造
- LLM 调用
- 校验 / 导出 / 导入
- 页面接口

其中比较关键的是：

- `CardCompiler`
  - 编译项目成目标结构
- `build_copilot_prompt_text()`
  - 生成给模型的辅助写作 prompt
- `request_copilot_review()`
  - 让模型审阅当前卡片
- `build_copilot_candidate()`
  - 生成一个修改候选
- `build_copilot_fingerprint()`
  - 给项目做指纹
- `normalize_copilot_candidates()`
  - 清洗候选修改
- `build_copilot_review_summary()`
  - 生成审阅摘要
- `generate_copilot_fallback()`
  - 模型失败时给兜底结果
- `build_copilot_system_prompt()`
  - 生成系统提示词
- `build_copilot_user_payload()`
  - 生成用户输入负载
- `call_copilot_llm()`
  - 调模型
- `normalize_project()`
  - 清理项目数据
- `project_from_payload()`
  - 从请求体构造项目
- `make_access_style()` / `format_access_log()` / `resolve_access_label()`
  - 本模块自己的日志展示
- `chinese_access_log()`
  - 中文访问日志中间件

### 15.5 `mods/tavern-card-converter/app.py`

这是酒馆卡转换器。

#### 主要 `def`

- `read_upload_bytes()`
  - 限制上传大小地读取文件
- `strip_chara_metadata()`
  - 去掉酒馆卡元信息
- `extract_tavern_card()`
  - 解析 tavern card
- `convert_card_to_xuqi()`
  - 转换角色卡
- `convert_worldbook_to_xuqi()`
  - 转换世界书
- `convert_card()`
  - 卡片转换接口
- `convert_worldbook()`
  - 世界书转换接口
- `save_card()`
  - 保存转换后的卡
- `save_worldbook()`
  - 保存转换后的世界书

---

## 16. 配置默认值总表

这一段专门回答你说的“各个配置的 `=""` / `=False` / 数字默认值”。

### 16.1 `SettingsPayload` / `DEFAULT_SETTINGS`

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

### 16.2 `PersonaPayload` / `DEFAULT_PERSONA`

```json
{
  "name": "Xuxu",
  "system_prompt": "You are a gentle, patient, and attentive AI companion. Respond naturally, show care, and avoid overly templated phrasing.",
  "greeting": "What would you like to talk about today? I am here with you."
}
```

### 16.3 `MemoryItemPayload`

```json
{
  "id": "",
  "title": "",
  "content": "",
  "tags": [],
  "notes": ""
}
```

### 16.4 `MergedMemoryItemPayload`

```json
{
  "id": "",
  "title": "",
  "content": "",
  "tags": [],
  "notes": "",
  "source_memory_ids": [],
  "created_at": ""
}
```

### 16.5 `MemoryOutlineItemPayload`

```json
{
  "id": "",
  "title": "",
  "summary": "",
  "characters": "",
  "relationship_progress": "",
  "key_events": [],
  "conflicts": "",
  "next_hooks": "",
  "notes": "",
  "source_memory_ids": [],
  "merged_memory_id": "",
  "updated_at": ""
}
```

### 16.6 `WorldbookEntryPayload`

```json
{
  "id": "",
  "title": "",
  "trigger": "",
  "secondary_trigger": "",
  "content": "",
  "enabled": true,
  "priority": 100,
  "case_sensitive": false,
  "whole_word": false,
  "match_mode": "any",
  "secondary_mode": "all",
  "comment": "",
  "group": "",
  "entry_type": "keyword",
  "group_operator": "and",
  "chance": 100,
  "sticky_turns": 0,
  "cooldown_turns": 0,
  "order": 100,
  "insertion_position": "after_char_defs",
  "injection_depth": 0,
  "injection_role": "system",
  "injection_order": 100,
  "prompt_layer": "follow_position",
  "recursive_enabled": true,
  "prevent_further_recursion": false
}
```

### 16.7 `WorldbookSettingsPayload` / `DEFAULT_WORLDBOOK_SETTINGS`

见上文第 10 节。

### 16.8 `Preset` 默认值

预设相关默认值主要在 `preset_rules.py`：

- `DEFAULT_PRESET_MODULES`
  - 大多数模块是关 / 开混合配置
- `v4f_output_guard` 是特殊运行时模块
- `PRESET_MODULE_RULES` 里每个模块都有自己的 prompt

### 16.9 `Workshop` 默认值

创意工坊默认值主要在 `workshop_logic.py`：

- 开场默认不开启
- 氛围默认不开启
- 动态场景默认启用但内容为空
- 阶段默认用 `aMax=2, bMax=5`

---

## 17. 数据怎么分

如果只看数据文件夹，可以粗分成这样：

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

---

## 18. 页面检索速查

如果你想找某个功能，直接按这个顺序搜：

### 18.1 先找页面

- 聊天 → `/chat`
- 记忆 → `/config/memory`
- 世界书 → `/config/worldbook`
- 世界书词条 → `/config/worldbook/entries`
- 预设 → `/config/preset`
- 角色卡 → `/config/card`
- 用户资料 → `/config/user`
- 工坊 → `/config/workshop`
- 关于 → `/config/about`
- 插件 → `/mods/{slug}`

### 18.2 再找接口

- 聊天链路 → `chat_api_routes.py`
- 配置链路 → `config_api_routes.py`
- 页面壳 → `page_routes.py`
- 插件发现 → `mods_runtime.py`
- 插件专属 API → `mods/*/app.py`

### 18.3 再找核心函数

- prompt 打包 → `prompt_builder.py`
- 记忆合并 → `memory_merge_logic.py`
- 世界书匹配 → `worldbook_logic.py`
- 预设拼装 → `preset_rules.py`
- 工坊规则 → `workshop_logic.py`
- 槽位状态 → `slot_runtime.py`

---