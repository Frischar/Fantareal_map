# Fantareal 速查表

不想翻 5000 行说明书？从这里查起。

## 我想改...

| 我想改... | 去这里 | 关键函数 |
|-----------|--------|----------|
| 聊天接口 / 消息发送 | `fantareal/chat_api_routes.py` | `api_chat`, `api_reroll_assistant_message`, `api_edit_user_message` |
| AI 回复内容 / Prompt | `fantareal/prompt_builder.py` | `build_prompt`, `assemble_messages` |
| 角色卡配置 | `fantareal/config_api_routes.py` | `api_get_character_card`, `api_save_character_card` |
| 世界书词条 | `fantareal/worldbook_logic.py` | `match_worldbook_entries` |
| 记忆系统 | `fantareal/memory_merge_logic.py` | `merge_memory` |
| 设置 / API Key | `fantareal/config_api_routes.py` | `api_get_settings`, `api_save_settings` |
| 多角色 / 槽位 | `fantareal/slot_runtime.py` | slot 读写相关函数 |
| 页面显示 | `fantareal/page_routes.py` | 各种 page 路由 |
| 预设规则 | `fantareal/preset_rules.py` | `validate_output`, 预设模块加载 |
| 数据模型定义 | `fantareal/app_models.py` | 所有 Pydantic 模型 |
| Mod 注册 | `fantareal/mods_runtime.py` | `register_all_mods` |
| 添加新 Mod | `mods/<已有mod>/app.py` | 参考现有 mod 的 `register_mod_routes` |
| 持久化读写 | `fantareal/app.py` | `read_json`, `write_json` |
| 启动 / 端口 / 浏览器 | `fantareal/launcher.py` | `main`, `start_local_server` |

## Bug 现象 → 排查入口

| 现象 | 先看这里 |
|------|----------|
| 页面打不开 / 404 | `fantareal/page_routes.py` → 路由是否注册 |
| 按钮点不动 / API 报错 | `fantareal/chat_api_routes.py` 或 `config_api_routes.py` |
| AI 回复很奇怪 | `fantareal/prompt_builder.py` → prompt 拼装是否正确 |
| 世界书不触发 | `fantareal/worldbook_logic.py` → 匹配逻辑 |
| 记忆没保存 | `fantareal/memory_merge_logic.py` + `fantareal/app.py` 的 `write_json` |
| 切换角色后数据乱了 | `fantareal/slot_runtime.py` → slot_id 传递 |
| 设置保存后丢失 | `fantareal/app.py` 的 `persist_json` / `write_json` |
| 浏览器没打开 | `fantareal/launcher.py` → `find_browser_executable` |
| Mod 不生效 | `fantareal/mods_runtime.py` + mod 自己的 `app.py` |

## 数据流向

```
用户输入
  → chat_api_routes.py（接请求）
    → fantareal/app.py generate_reply()（汇总状态）
      → slot_runtime.py（读当前槽位数据）
      → worldbook_logic.py（匹配世界书词条）
      → memory_merge_logic.py（召回长期记忆）
      → prompt_builder.py（拼装 prompt）
      → 模型 API 调用
      → write_json（写回聊天历史）
  → 返回 AI 回复
```

## 项目核心约束

- **所有持久化**走 `read_json` / `write_json`（`fantareal/app.py`），不要自己 open 文件
- **数据按 slot_id 隔离**，改数据时确认 slot_id 正确
- **API 返回格式**统一 `{"ok": bool, ...}`
- **Mod 入口**统一 `register_mod_routes(app: FastAPI)`，在 `mods_runtime.py` 注册
- **JSON 写入无备份**，`write_json` 直接覆盖，谨慎操作
