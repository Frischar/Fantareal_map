# Fantareal 速查表

> 不想翻 1600 行说明书？从这里查起。
> **当前源项目**：`Fantareal-beta`（不是 `Fantareal`，因为本地图仓库指向 beta 分支）。
> 同步命令：`python scripts/sync_map.py --source "../Fantareal-beta"`。
> 校验命令：`python scripts/verify_map.py --strict`（保证 `说明书.md` 行号 100% 准）。

## 我想改...

| 我想改... | 去这里 | 关键函数 |
|-----------|--------|----------|
| 聊天接口 / 消息发送 | `fantareal/chat_api_routes.py` | `api_chat` / `api_reroll_assistant_message` / `api_edit_user_message` |
| AI 回复内容 / Prompt | `fantareal/prompt_builder.py` | `build_prompt_package` / `build_messages` |
| Prompt 里的 `{{var}}` 宏变量 | `fantareal/macro_variables.py` ⭐ | `render_macro_variables` / `render_messages_with_macros` |
| 多 Provider 路由 / failover | `fantareal/route_forwarding.py` ⭐ | `class RouteForwardingRuntime` / `sanitize_provider` |
| 角色卡配置 | `fantareal/config_api_routes.py` | `api_get_character_card` / `api_save_character_card` |
| 世界书词条 | `fantareal/worldbook_logic.py` | `match_worldbook_entries` |
| 记忆系统 | `fantareal/memory_merge_logic.py` | `merge_memories_to_outline` |
| 设置 / API Key | `fantareal/config_api_routes.py` | `api_get_settings` / `api_save_settings` |
| 多角色 / 槽位 | `fantareal/slot_runtime.py` | `SlotRuntimeService` 相关方法 |
| 页面显示 | `fantareal/page_routes.py` | `register_page_routes` |
| 预设规则 | `fantareal/preset_rules.py` | `build_preset_prompt_from_preset` |
| 数据模型定义 | `fantareal/app_models.py` | 所有 Pydantic 模型 |
| Mod 注册 / 发现 | `fantareal/mods_runtime.py` | `mount_discovered_mods` / `discover_mods` |
| 添加新 Mod | `mods/<已有mod>/app.py` | 参考 `register_mod_routes` 模式 |
| 小手机（mobile-chat） | `mods/mobile-chat/app.py` | 387 个函数 / 32 个类，详见 `docs/mobile-chat-architecture.md` |
| 心笺（state_journal） | `mods/state_journal/app.py` | 265 个函数 / 1 个类 |
| 古法写卡器（card writer） | `mods/card writer/app.py` | `CardCompiler` / `request_copilot_review` |
| 余音（soul weaver） | `mods/soul weaver/app.py` | 75 个函数 |
| 状态栏（status panel） | `mods/status panel/app.py` | 45 个函数 / 4 个类 |
| 世界书生成器（worldbook maker） | `mods/worldbook maker/app.py` | 47 个函数 / 6 个类 |
| 酒馆卡转换器 | `mods/tavern-card-converter/app.py` | `convert_card` / `convert_worldbook` |
| 派对彩带大对决 | `game/Tea Party/engine.py` | `class PartyGame` |
| 持久化读写 | `fantareal/app.py` | `read_json` / `write_json` / `persist_json` |
| 启动 / 端口 / 浏览器 | `fantareal/launcher.py` | `is_port_open` / `wait_for_port` / `get_free_port` / `start_local_server` |

## Bug 现象 → 排查入口

| 现象 | 先看这里 |
|------|----------|
| 页面打不开 / 404 | `fantareal/page_routes.py` → 路由是否注册 |
| 按钮点不动 / API 报错 | `fantareal/chat_api_routes.py` 或 `fantareal/config_api_routes.py` |
| AI 回复很奇怪 | `fantareal/prompt_builder.py` → prompt 拼装是否正确 |
| 宏变量没替换 / 替换错 | `fantareal/macro_variables.py` → `build_macro_context` / `render_macro_variables` |
| 多 Provider 切换无效 / 一直用主 key | `fantareal/route_forwarding.py` → `sanitize_route_forwarding_config` |
| 世界书不触发 | `fantareal/worldbook_logic.py` → `match_worldbook_entries` |
| 记忆没保存 | `fantareal/memory_merge_logic.py` + `fantareal/app.py` 的 `write_json` |
| 切换角色后数据乱了 | `fantareal/slot_runtime.py` → `slot_id` 传递 |
| 设置保存后丢失 | `fantareal/app.py` 的 `persist_json` / `write_json` |
| 浏览器没打开 | `fantareal/launcher.py` → `find_browser_executable` |
| Mod 不生效 | `fantareal/mods_runtime.py` + mod 自己的 `app.py` |
| 小手机不显示 | `mods/mobile-chat/app.py` 入口 + `mod.json` hooks |
| 心笺不显示 | `mods/state_journal/app.py` 入口 + `mod.json` hooks |

## 数据流向

```
用户输入
  → chat_api_routes.py（接请求）
    → fantareal/app.py generate_reply()（汇总状态）
      → slot_runtime.py（读当前槽位数据）
      → worldbook_logic.py（匹配世界书词条）
      → memory_merge_logic.py（召回长期记忆）
      → prompt_builder.py（拼装 prompt）
        → macro_variables.py（替换 {{var}} / <var> 宏变量）⭐
        → route_forwarding.py（多 Provider 路由 / failover）⭐
      → 模型 API 调用
      → write_json（写回聊天历史）
  → 返回 AI 回复
```

## 项目核心约束

- **所有持久化**走 `read_json` / `write_json`（`fantareal/app.py`），不要自己 open 文件
- **数据按 slot_id 隔离**（小手机除外，它按 `card_uid` 隔离），改数据时确认 slot_id 正确
- **API 返回格式**统一 `{"ok": bool, ...}`
- **Mod 入口**：通过 `fantareal/mods_runtime.py` 自动扫描 `mods/*/mod.json`，自动加载 `mods/*/app.py`
- **Mod hooks 类型**：`chat_styles`（注入主 Chat 样式）/ `chat_scripts`（注入主 Chat 脚本）
- **JSON 写入无备份**，`write_json` 直接覆盖，谨慎操作
- **`说明书.md` 是注释版地图**，行号已通过 `verify_map.py --strict` 校验；以 `说明书_auto.md`（AST 提取）为行号权威源

## 地图同步

```bash
# 推荐：仅重新生成 AST 索引（说明书.md 是本仓库自维护的，不从 beta 复制）
python scripts/sync_map.py --source "../Fantareal-beta"

# 显式同步：把 beta 的手写说明书复制为 说明书_legacy.md
python scripts/sync_map.py --source "../Fantareal-beta" --with-legacy

# 仅复制手写说明书（不跑 AST 扫描）
python scripts/sync_map.py --source "../Fantareal-beta" --with-legacy --skip-scan

# 校验说明书.md 行号 100% 准
python scripts/verify_map.py --strict
```

> 默认 `--source` 是 `../Fantareal` 或 `../fantareal`，因为本地图默认指向 beta 分支，所以**必须显式指定** `--source "../Fantareal-beta"`。
