# Fantareal 项目函数地图

> 本文档由 `scripts/scan_map.py` 自动生成。
> 行号由 AST 实时提取，始终与代码同步。
> 标记为 `[待补充]` 的字段需要在对应函数的 docstring 中补充。

## 目录

- **第 1 节** [fantareal/app.py](#fantareal-app-py)（233 个函数, 1 个类）
- **第 2 节** [fantareal/app_models.py](#fantareal-app_models-py)（50 个类）
- **第 3 节** [fantareal/chat_api_routes.py](#fantareal-chat_api_routes-py)（16 个函数）
- **第 4 节** [fantareal/config_api_routes.py](#fantareal-config_api_routes-py)（92 个函数）
- **第 5 节** [fantareal/launcher.py](#fantareal-launcher-py)（8 个函数）
- **第 6 节** [fantareal/macro_variables.py](#fantareal-macro_variables-py)（11 个函数）
- **第 7 节** [fantareal/memory_merge_logic.py](#fantareal-memory_merge_logic-py)（25 个函数）
- **第 8 节** [fantareal/mod_api_routes.py](#fantareal-mod_api_routes-py)（3 个函数）
- **第 9 节** [fantareal/mods_runtime.py](#fantareal-mods_runtime-py)（9 个函数, 1 个类）
- **第 10 节** [fantareal/page_routes.py](#fantareal-page_routes-py)（40 个函数）
- **第 11 节** [fantareal/preset_rules.py](#fantareal-preset_rules-py)（33 个函数）
- **第 12 节** [fantareal/prompt_builder.py](#fantareal-prompt_builder-py)（50 个函数）
- **第 13 节** [fantareal/route_forwarding.py](#fantareal-route_forwarding-py)（33 个函数, 1 个类）
- **第 14 节** [fantareal/slot_runtime.py](#fantareal-slot_runtime-py)（25 个函数, 1 个类）
- **第 15 节** [fantareal/workshop_logic.py](#fantareal-workshop_logic-py)（23 个函数）
- **第 16 节** [fantareal/worldbook_logic.py](#fantareal-worldbook_logic-py)（21 个函数）
- **第 17 节** [game/Tea Party/ai_instructions.py](#game-tea-party-ai_instructions-py)（2 个函数）
- **第 18 节** [game/Tea Party/ai_opponent.py](#game-tea-party-ai_opponent-py)（3 个函数）
- **第 19 节** [game/Tea Party/engine.py](#game-tea-party-engine-py)（36 个函数, 1 个类）
- **第 20 节** [game/Tea Party/models.py](#game-tea-party-models-py)（12 个函数, 11 个类）
- **第 21 节** [game/Tea Party/test_verify.py](#game-tea-party-test_verify-py)（4 个函数）
- **第 22 节** [mods/card writer/app.py](#mods-card-writer-app-py)（125 个函数, 7 个类）
- **第 23 节** [mods/mobile-chat/app.py](#mods-mobile-chat-app-py)（388 个函数, 32 个类）
- **第 24 节** [mods/soul weaver/app.py](#mods-soul-weaver-app-py)（75 个函数）
- **第 25 节** [mods/state_journal/app.py](#mods-state_journal-app-py)（265 个函数, 1 个类）
- **第 26 节** [mods/status panel/app.py](#mods-status-panel-app-py)（45 个函数, 4 个类）
- **第 27 节** [mods/tavern-card-converter/app.py](#mods-tavern-card-converter-app-py)（16 个函数, 2 个类）
- **第 28 节** [mods/worldbook maker/app.py](#mods-worldbook-maker-app-py)（47 个函数, 6 个类）

## 第 1 节 fantareal/app.py

### 一览

- **class StripAnsiFormatter** — 第 202 行

- `get_runtime_base_dir()` — 第 86 行
- `get_resource_dir()` — 第 103 行
- `flush_log_handlers()` — 第 223 行
- `make_access_style()` — 第 230 行
- `format_access_log()` — 第 240 行
- `format_access_route_tag()` — 第 248 行
- `resolve_access_label()` — 第 256 行
- `_copy_worldbook_debug_snapshot()` — 第 384 行
- `get_worldbook_debug_snapshot()` — 第 403 行
- `bootstrap_runtime_layout()` — 第 407 行
- `default_slot_registry()` — 第 467 行
- `default_sprite_base_path_for_slot()` — 第 474 行
- `sprite_dir_path()` — 第 478 行
- `sanitize_sprite_filename_tag()` — 第 482 行
- `list_sprite_assets()` — 第 488 行
- `default_state_journal_config()` — 第 509 行
- `_normalize_state_journal_key()` — 第 518 行
- `_state_journal_stage_letter()` — 第 529 行
- `_state_journal_default_stage_key()` — 第 537 行
- `_state_journal_default_stage_name()` — 第 541 行
- `_state_journal_int()` — 第 545 行
- `sanitize_state_journal_config()` — 第 555 行
- `default_role_card()` — 第 748 行
- `default_user_profile()` — 第 798 行
- `normalize_director_note_position()` — 第 811 行
- `sanitize_director_note()` — 第 816 行
- `sanitize_director_notes()` — 第 839 行
- `get_director_notes()` — 第 857 行
- `save_director_notes()` — 第 861 行
- `create_director_note()` — 第 871 行
- `delete_director_note()` — 第 890 行
- `consume_director_notes_turn()` — 第 896 行
- `default_creative_workshop()` — 第 914 行
- `get_workshop_state()` — 第 918 行
- `save_workshop_state()` — 第 922 行
- `reset_workshop_state()` — 第 932 行
- `workshop_signature()` — 第 936 行
- `evaluate_creative_workshop()` — 第 946 行
- `default_preset_store()` — 第 970 行
- `sanitize_preset_store()` — 第 974 行
- `preset_path()` — 第 978 行
- `get_preset_store()` — 第 982 行
- `save_preset_store()` — 第 986 行
- `get_active_preset()` — 第 996 行
- `build_preset_prompt()` — 第 1000 行
- `build_preset_observation_segments()` — 第 1004 行
- `build_active_preset_context()` — 第 1008 行
- `get_active_preset_module_labels()` — 第 1020 行
- `build_preset_debug_payload()` — 第 1030 行
- `load_env_file()` — 第 1044 行
- `read_json()` — 第 1057 行
- `write_json()` — 第 1068 行
- `persist_json()` — 第 1076 行
- `parse_bool()` — 第 1084 行
- `clamp_int()` — 第 1094 行
- `clamp_float()` — 第 1102 行
- `sanitize_background_image_url()` — 第 1110 行
- `sanitize_font_url()` — 第 1132 行
- `sanitize_font_color()` — 第 1149 行
- `sanitize_embedding_fields()` — 第 1158 行
- `sanitize_settings()` — 第 1168 行
- `sanitize_tags()` — 第 1220 行
- `sanitize_memories()` — 第 1236 行
- `sanitize_slot_id()` — 第 1257 行
- `sanitize_legacy_slot_id()` — 第 1261 行
- `sanitize_slot_registry()` — 第 1268 行
- `get_slot_registry()` — 第 1296 行
- `save_slot_registry()` — 第 1300 行
- `get_active_slot_id()` — 第 1311 行
- `get_slot_name()` — 第 1316 行
- `slot_summary()` — 第 1325 行
- `get_slot_dir()` — 第 1355 行
- `persona_path()` — 第 1360 行
- `legacy_slot_dir()` — 第 1365 行
- `legacy_persona_path()` — 第 1369 行
- `global_persona_path()` — 第 1373 行
- `conversation_path()` — 第 1377 行
- `settings_path()` — 第 1382 行
- `memories_path()` — 第 1387 行
- `card_runtime_dir()` — 第 1391 行
- `_normalize_card_runtime_key()` — 第 1396 行
- `current_memory_card_uid()` — 第 1404 行
- `worldbook_path()` — 第 1434 行
- `current_card_path()` — 第 1439 行
- `legacy_current_card_path()` — 第 1444 行
- `global_current_card_path()` — 第 1448 行
- `workshop_state_path()` — 第 1452 行
- `user_profile_path()` — 第 1457 行
- `director_notes_path()` — 第 1462 行
- `route_forwarding_path()` — 第 1467 行
- `avatar_upload_url()` — 第 1471 行
- `remove_upload_variants()` — 第 1476 行
- `save_image_upload_for_slot()` — 第 1483 行
- `workshop_asset_dir()` — 第 1514 行
- `workshop_asset_url()` — 第 1519 行
- `save_workshop_asset_upload()` — 第 1525 行
- `reset_slot_data()` — 第 1569 行
- `normalize_role_card()` — 第 1583 行
- `sanitize_role_alias_key()` — 第 1647 行
- `sanitize_role_aliases()` — 第 1654 行
- `extract_persona_name_from_fields()` — 第 1668 行
- `is_legacy_demo_reply()` — 第 1685 行
- `is_garbled_placeholder_message()` — 第 1701 行
- `normalize_legacy_message_content()` — 第 1708 行
- `sanitize_conversation()` — 第 1733 行
- `legacy_active_slot_id()` — 第 1783 行
- `legacy_slot_last_updated()` — 第 1792 行
- `legacy_slot_seed_order()` — 第 1803 行
- `legacy_slot_has_runtime_data()` — 第 1817 行
- `migrate_legacy_avatar_upload()` — 第 1844 行
- `migrate_legacy_sprite_assets()` — 第 1859 行
- `migrate_slot_runtime_to_global_files()` — 第 1878 行
- `slot_looks_uninitialized()` — 第 1930 行
- `has_legacy_root_data()` — 第 1939 行
- `migrate_legacy_root_to_primary_slot()` — 第 1951 行
- `slot_role_state_seed_order()` — 第 1987 行
- `seed_global_role_state()` — 第 2002 行
- `ensure_data_files()` — 第 2057 行
- `get_persona()` — 第 2123 行
- `get_conversation()` — 第 2129 行
- `get_settings()` — 第 2142 行
- `sanitize_user_profile()` — 第 2153 行
- `get_user_profile()` — 第 2177 行
- `save_user_profile()` — 第 2181 行
- `get_role_avatar_url()` — 第 2189 行
- `get_memories()` — 第 2193 行
- `get_worldbook()` — 第 2197 行
- `get_worldbook_store()` — 第 2201 行
- `get_worldbook_entries()` — 第 2205 行
- `get_worldbook_settings()` — 第 2209 行
- `save_memories()` — 第 2213 行
- `save_worldbook()` — 第 2223 行
- `save_worldbook_store()` — 第 2233 行
- `save_worldbook_entries()` — 第 2243 行
- `save_worldbook_settings()` — 第 2249 行
- `get_current_card()` — 第 2255 行
- `list_role_card_files()` — 第 2264 行
- `read_role_card_text()` — 第 2275 行
- `repair_deepseek_card_json()` — 第 2286 行
- `extract_role_card_payload()` — 第 2302 行
- `parse_role_card_json()` — 第 2326 行
- `build_persona_from_role_card()` — 第 2344 行
- `apply_role_card()` — 第 2410 行
- `save_workshop_card()` — 第 2449 行
- `sanitize_runtime_overrides()` — 第 2489 行
- `resolve_runtime_value()` — 第 2520 行
- `get_route_forwarding_chat_defaults()` — 第 2538 行
- `get_runtime_chat_config()` — 第 2564 行
- `get_runtime_embedding_config()` — 第 2586 行
- `get_runtime_rerank_config()` — 第 2599 行
- `append_messages()` — 第 2612 行
- `build_memory_text()` — 第 2631 行
- `normalize_base_url()` — 第 2644 行
- `build_api_url()` — 第 2648 行
- `build_headers()` — 第 2658 行
- `should_retry_status_code()` — 第 2665 行
- `safe_response_text()` — 第 2671 行
- `summarize_upstream_error()` — 第 2684 行
- `stream_compat_key()` — 第 2732 行
- `should_retry_without_stream()` — 第 2741 行
- `request_json()` — 第 2750 行
- `fetch_available_models()` — 第 2795 行
- `request_minimal_model_reply()` — 第 2836 行
- `fetch_embeddings()` — 第 2868 行
- `cosine_similarity()` — 第 2895 行
- `rerank_documents()` — 第 2907 行
- `default_worldbook_runtime_state()` — 第 2952 行
- `worldbook_runtime_state_path()` — 第 2956 行
- `sanitize_worldbook_runtime_state()` — 第 2960 行
- `get_worldbook_runtime_state()` — 第 2990 行
- `save_worldbook_runtime_state()` — 第 2994 行
- `get_route_forwarding_config()` — 第 3004 行
- `sync_route_forwarding_p1_to_chat_settings()` — 第 3010 行
- `save_route_forwarding_config()` — 第 3038 行
- `_normalize_worldbook_insertion_position()` — 第 3052 行
- `_normalize_worldbook_injection_role()` — 第 3057 行
- `_normalize_worldbook_injection_depth()` — 第 3064 行
- `_normalize_worldbook_injection_order()` — 第 3068 行
- `_normalize_worldbook_prompt_layer()` — 第 3072 行
- `_worldbook_position_priority()` — 第 3077 行
- `_worldbook_global_selection_sort_key()` — 第 3086 行
- `_worldbook_bucket_sort_key()` — 第 3094 行
- `bucket_worldbook_matches()` — 第 3104 行
- `_worldbook_entry_sort_key()` — 第 3135 行
- `_build_worldbook_runtime_debug_entries()` — 第 3142 行
- `_worldbook_alias_match_result()` — 第 3188 行
- `_evaluate_worldbook_keyword_entry()` — 第 3207 行
- `_worldbook_macro_context()` — 第 3257 行
- `_render_worldbook_item_macros()` — 第 3261 行
- `_worldbook_match_payload()` — 第 3283 行
- `_worldbook_recursive_seed_text()` — 第 3332 行
- `_worldbook_runtime_state_row()` — 第 3345 行
- `_worldbook_debug_display_sort_key()` — 第 3357 行
- `_normalize_state_journal_card_key()` — 第 3368 行
- `get_state_journal_current_card_uid()` — 第 3376 行
- `get_state_journal_active_stage_rows()` — 第 3393 行
- `get_state_journal_active_stage_tag_sources()` — 第 3429 行
- `get_state_journal_active_stage_tags()` — 第 3449 行
- `_normalize_active_tag_context()` — 第 3453 行
- `_merge_active_tag_contexts()` — 第 3491 行
- `build_active_tag_context()` — 第 3503 行
- `_active_tag_sources_by_tag()` — 第 3545 行
- `_source_labels_for_tags()` — 第 3557 行
- `match_worldbook_entries()` — 第 3567 行
- `enforce_worldbook_fact_in_reply()` — 第 3835 行
- `normalize_sprite_tag()` — 第 3843 行
- `extract_sprite_tag()` — 第 3861 行
- `_stringify_model_text()` — 第 3914 行
- `extract_reasoning_field()` — 第 3934 行
- `combine_think_parts()` — 第 3945 行
- `normalize_thought_markup()` — 第 3949 行
- `extract_reply_parts()` — 第 3999 行
- `compose_full_reply()` — 第 4055 行
- `extract_stream_visible_reply()` — 第 4065 行
- `retrieve_memories()` — 第 4070 行
- `request_model_reply()` — 第 4117 行
- `iter_non_stream_reply_events()` — 第 4169 行
- `build_worldbook_debug_payload()` — 第 4183 行
- `stream_model_reply()` — 第 4266 行
- `generate_reply()` — 第 4453 行
- `fallback_memory_from_conversation()` — 第 4490 行
- `request_conversation_summary_with_model()` — 第 4529 行
- `sanitize_memory_summary()` — 第 4748 行
- `summarize_conversation_to_memory()` — 第 4779 行
- `_get_archive_lock()` — 第 4793 行
- `archive_current_conversation()` — 第 4799 行
- `chinese_access_log()` — 第 4853 行

### 函数详情

#### [get_runtime_base_dir() -> Path](fantareal/app.py#L86)（第 86 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_resource_dir() -> Path](fantareal/app.py#L103)（第 103 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [format(record: logging.LogRecord) -> str（嵌套在 StripAnsiFormatter 内）](fantareal/app.py#L203)（第 203 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [flush_log_handlers() -> None](fantareal/app.py#L223)（第 223 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [make_access_style(label: str, method: str, status_code: int) -> str](fantareal/app.py#L230)（第 230 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [format_access_log(label: str, method: str, status_code: int, mood: str, route_tag: str) -> str](fantareal/app.py#L240)（第 240 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [format_access_route_tag(method: str, path: str) -> str](fantareal/app.py#L248)（第 248 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [resolve_access_label(method: str, path: str) -> str](fantareal/app.py#L256)（第 256 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_copy_worldbook_debug_snapshot(snapshot: dict[str, Any] | None = None) -> dict[str, Any]](fantareal/app.py#L384)（第 384 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_worldbook_debug_snapshot() -> dict[str, Any]](fantareal/app.py#L403)（第 403 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [bootstrap_runtime_layout() -> None](fantareal/app.py#L407)（第 407 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_slot_registry() -> dict[str, Any]](fantareal/app.py#L467)（第 467 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_sprite_base_path_for_slot(slot_id: str | None = None) -> str](fantareal/app.py#L474)（第 474 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sprite_dir_path(slot_id: str | None = None) -> Path](fantareal/app.py#L478)（第 478 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_sprite_filename_tag(value: str) -> str](fantareal/app.py#L482)（第 482 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [list_sprite_assets(slot_id: str | None = None) -> list[dict[str, Any]]](fantareal/app.py#L488)（第 488 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_state_journal_config() -> dict[str, Any]](fantareal/app.py#L509)（第 509 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_state_journal_key(value: Any, fallback: str) -> str](fantareal/app.py#L518)（第 518 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_state_journal_stage_letter(index: int) -> str](fantareal/app.py#L529)（第 529 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_state_journal_default_stage_key(index: int) -> str](fantareal/app.py#L537)（第 537 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_state_journal_default_stage_name(index: int) -> str](fantareal/app.py#L541)（第 541 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_state_journal_int(value: Any, default: int, minimum: int | None = None) -> int](fantareal/app.py#L545)（第 545 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_state_journal_config(raw: Any) -> dict[str, Any]](fantareal/app.py#L555)（第 555 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_role_card() -> dict[str, Any]](fantareal/app.py#L748)（第 748 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_user_profile() -> dict[str, Any]](fantareal/app.py#L798)（第 798 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_director_note_position(value: Any) -> str](fantareal/app.py#L811)（第 811 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_director_note(raw: Any) -> dict[str, Any] | None](fantareal/app.py#L816)（第 816 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_director_notes(raw: Any) -> list[dict[str, Any]]](fantareal/app.py#L839)（第 839 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_director_notes(slot_id: str | None = None) -> list[dict[str, Any]]](fantareal/app.py#L857)（第 857 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_director_notes(items: list[dict[str, Any]], slot_id: str | None = None) -> list[dict[str, Any]]](fantareal/app.py#L861)（第 861 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [create_director_note(payload: dict[str, Any], slot_id: str | None = None) -> list[dict[str, Any]]](fantareal/app.py#L871)（第 871 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [delete_director_note(note_id: str, slot_id: str | None = None) -> list[dict[str, Any]]](fantareal/app.py#L890)（第 890 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [consume_director_notes_turn(slot_id: str | None = None) -> list[dict[str, Any]]](fantareal/app.py#L896)（第 896 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_creative_workshop() -> dict[str, Any]](fantareal/app.py#L914)（第 914 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_workshop_state(slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L918)（第 918 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_workshop_state(payload: dict[str, Any], slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L922)（第 922 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [reset_workshop_state(slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L932)（第 932 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [workshop_signature(slot: dict[str, Any] | None, workshop: dict[str, Any], stage: str) -> str](fantareal/app.py#L936)（第 936 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [evaluate_creative_workshop() -> dict[str, Any]](fantareal/app.py#L946)（第 946 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_preset_store() -> dict[str, Any]](fantareal/app.py#L970)（第 970 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_preset_store(raw: Any) -> dict[str, Any]](fantareal/app.py#L974)（第 974 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [preset_path(slot_id: str | None = None) -> Path](fantareal/app.py#L978)（第 978 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_preset_store(slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L982)（第 982 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_preset_store(payload: dict[str, Any], slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L986)（第 986 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_active_preset(slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L996)（第 996 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_preset_prompt(slot_id: str | None = None) -> str](fantareal/app.py#L1000)（第 1000 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_preset_observation_segments(slot_id: str | None = None) -> list[dict[str, Any]]](fantareal/app.py#L1004)（第 1004 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_active_preset_context(slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L1008)（第 1008 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_active_preset_module_labels(slot_id: str | None = None) -> list[str]](fantareal/app.py#L1020)（第 1020 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_preset_debug_payload(slot_id: str | None = None, preset_context: dict[str, Any] | None = None) -> dict[str, Any]](fantareal/app.py#L1030)（第 1030 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [load_env_file() -> None](fantareal/app.py#L1044)（第 1044 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [read_json(path: Path, default: Any) -> Any](fantareal/app.py#L1057)（第 1057 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [write_json(path: Path, payload: Any) -> None](fantareal/app.py#L1068)（第 1068 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [persist_json(path: Path, payload: Any) -> None](fantareal/app.py#L1076)（第 1076 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_bool(value: Any, default: bool = False) -> bool](fantareal/app.py#L1084)（第 1084 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clamp_int(value: Any, minimum: int, maximum: int, default: int) -> int](fantareal/app.py#L1094)（第 1094 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clamp_float(value: Any, minimum: float, maximum: float, default: float) -> float](fantareal/app.py#L1102)（第 1102 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_background_image_url(value: Any) -> str](fantareal/app.py#L1110)（第 1110 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_font_url(value: Any) -> str](fantareal/app.py#L1132)（第 1132 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_font_color(value: Any) -> str](fantareal/app.py#L1149)（第 1149 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_embedding_fields(value: Any) -> list[str]](fantareal/app.py#L1158)（第 1158 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_settings(raw: dict[str, Any] | None) -> dict[str, Any]](fantareal/app.py#L1168)（第 1168 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_tags(value: Any) -> list[str]](fantareal/app.py#L1220)（第 1220 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_memories(raw: Any) -> list[dict[str, Any]]](fantareal/app.py#L1236)（第 1236 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_slot_id(value: Any, default: str | None = None) -> str](fantareal/app.py#L1257)（第 1257 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_legacy_slot_id(value: Any, default: str | None = None) -> str](fantareal/app.py#L1261)（第 1261 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_slot_registry(raw: Any) -> dict[str, Any]](fantareal/app.py#L1268)（第 1268 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_slot_registry() -> dict[str, Any]](fantareal/app.py#L1296)（第 1296 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_slot_registry(registry: dict[str, Any]) -> dict[str, Any]](fantareal/app.py#L1300)（第 1300 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_active_slot_id() -> str](fantareal/app.py#L1311)（第 1311 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_slot_name(slot_id: str | None = None) -> str](fantareal/app.py#L1316)（第 1316 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [slot_summary(slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L1325)（第 1325 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_slot_dir(slot_id: str | None = None) -> Path](fantareal/app.py#L1355)（第 1355 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [persona_path(slot_id: str | None = None) -> Path](fantareal/app.py#L1360)（第 1360 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [legacy_slot_dir(slot_id: str | None = None) -> Path](fantareal/app.py#L1365)（第 1365 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [legacy_persona_path(slot_id: str | None = None) -> Path](fantareal/app.py#L1369)（第 1369 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [global_persona_path() -> Path](fantareal/app.py#L1373)（第 1373 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [conversation_path(slot_id: str | None = None) -> Path](fantareal/app.py#L1377)（第 1377 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [settings_path(slot_id: str | None = None) -> Path](fantareal/app.py#L1382)（第 1382 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [memories_path(slot_id: str | None = None) -> Path](fantareal/app.py#L1387)（第 1387 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [card_runtime_dir(card_uid: str) -> Path](fantareal/app.py#L1391)（第 1391 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_card_runtime_key(value: Any, fallback: str = global) -> str](fantareal/app.py#L1396)（第 1396 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [current_memory_card_uid(slot_id: str | None = None) -> str](fantareal/app.py#L1404)（第 1404 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [worldbook_path(slot_id: str | None = None) -> Path](fantareal/app.py#L1434)（第 1434 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [current_card_path(slot_id: str | None = None) -> Path](fantareal/app.py#L1439)（第 1439 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [legacy_current_card_path(slot_id: str | None = None) -> Path](fantareal/app.py#L1444)（第 1444 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [global_current_card_path() -> Path](fantareal/app.py#L1448)（第 1448 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [workshop_state_path(slot_id: str | None = None) -> Path](fantareal/app.py#L1452)（第 1452 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [user_profile_path(slot_id: str | None = None) -> Path](fantareal/app.py#L1457)（第 1457 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [director_notes_path(slot_id: str | None = None) -> Path](fantareal/app.py#L1462)（第 1462 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [route_forwarding_path() -> Path](fantareal/app.py#L1467)（第 1467 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [avatar_upload_url(filename: str) -> str](fantareal/app.py#L1471)（第 1471 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [remove_upload_variants(prefix: str) -> None](fantareal/app.py#L1476)（第 1476 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_image_upload_for_slot() -> str](fantareal/app.py#L1483)（第 1483 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [workshop_asset_dir(kind: str) -> Path](fantareal/app.py#L1514)（第 1514 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [workshop_asset_url(kind: str, filename: str) -> str](fantareal/app.py#L1519)（第 1519 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_workshop_asset_upload() -> dict[str, Any]](fantareal/app.py#L1525)（第 1525 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [reset_slot_data(slot_id: str) -> dict[str, Any]](fantareal/app.py#L1569)（第 1569 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_role_card(raw: Any) -> dict[str, Any]](fantareal/app.py#L1583)（第 1583 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_role_alias_key(value: Any, fallback: str) -> str](fantareal/app.py#L1647)（第 1647 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_role_aliases(value: Any) -> list[str]](fantareal/app.py#L1654)（第 1654 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [extract_persona_name_from_fields() -> str](fantareal/app.py#L1668)（第 1668 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [is_legacy_demo_reply(content: str) -> bool](fantareal/app.py#L1685)（第 1685 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [is_garbled_placeholder_message(content: str) -> bool](fantareal/app.py#L1701)（第 1701 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_legacy_message_content(role: str, content: str) -> str](fantareal/app.py#L1708)（第 1708 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_conversation(raw: Any) -> list[dict[str, Any]]](fantareal/app.py#L1733)（第 1733 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [legacy_active_slot_id() -> str](fantareal/app.py#L1783)（第 1783 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [legacy_slot_last_updated(slot_id: str) -> float](fantareal/app.py#L1792)（第 1792 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [legacy_slot_seed_order() -> list[str]](fantareal/app.py#L1803)（第 1803 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [legacy_slot_has_runtime_data(slot_id: str) -> bool](fantareal/app.py#L1817)（第 1817 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [migrate_legacy_avatar_upload(prefix: str, legacy_slot_id: str) -> None](fantareal/app.py#L1844)（第 1844 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [migrate_legacy_sprite_assets(legacy_slot_id: str) -> None](fantareal/app.py#L1859)（第 1859 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [migrate_slot_runtime_to_global_files() -> None](fantareal/app.py#L1878)（第 1878 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [slot_looks_uninitialized(slot_id: str) -> bool](fantareal/app.py#L1930)（第 1930 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [has_legacy_root_data() -> bool](fantareal/app.py#L1939)（第 1939 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [migrate_legacy_root_to_primary_slot() -> None](fantareal/app.py#L1951)（第 1951 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [slot_role_state_seed_order() -> list[str]](fantareal/app.py#L1987)（第 1987 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [seed_global_role_state() -> None](fantareal/app.py#L2002)（第 2002 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [ensure_data_files() -> None](fantareal/app.py#L2057)（第 2057 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_persona(slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L2123)（第 2123 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_conversation(slot_id: str | None = None) -> list[dict[str, Any]]](fantareal/app.py#L2129)（第 2129 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_settings(slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L2142)（第 2142 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_user_profile(payload: Any) -> dict[str, Any]](fantareal/app.py#L2153)（第 2153 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_user_profile(slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L2177)（第 2177 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_user_profile(payload: dict[str, Any], slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L2181)（第 2181 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_role_avatar_url(slot_id: str | None = None) -> str](fantareal/app.py#L2189)（第 2189 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_memories(slot_id: str | None = None) -> list[dict[str, Any]]](fantareal/app.py#L2193)（第 2193 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_worldbook(slot_id: str | None = None) -> dict[str, str]](fantareal/app.py#L2197)（第 2197 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_worldbook_store(slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L2201)（第 2201 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_worldbook_entries(slot_id: str | None = None) -> list[dict[str, Any]]](fantareal/app.py#L2205)（第 2205 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_worldbook_settings(slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L2209)（第 2209 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_memories(items: list[dict[str, Any]], slot_id: str | None = None) -> list[dict[str, Any]]](fantareal/app.py#L2213)（第 2213 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_worldbook(entries: dict[str, str], slot_id: str | None = None) -> dict[str, str]](fantareal/app.py#L2223)（第 2223 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_worldbook_store(store: dict[str, Any], slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L2233)（第 2233 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_worldbook_entries(entries: list[dict[str, Any]], slot_id: str | None = None) -> list[dict[str, Any]]](fantareal/app.py#L2243)（第 2243 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_worldbook_settings(settings: dict[str, Any], slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L2249)（第 2249 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_current_card(slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L2255)（第 2255 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [list_role_card_files() -> list[dict[str, str]]](fantareal/app.py#L2264)（第 2264 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [read_role_card_text(path: Path) -> str](fantareal/app.py#L2275)（第 2275 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [repair_deepseek_card_json(text: str) -> str](fantareal/app.py#L2286)（第 2286 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [extract_role_card_payload(data: Any) -> dict[str, Any]](fantareal/app.py#L2302)（第 2302 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_role_card_json(text: str) -> dict[str, Any]](fantareal/app.py#L2326)（第 2326 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_persona_from_role_card(card: dict[str, Any]) -> dict[str, str]](fantareal/app.py#L2344)（第 2344 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [apply_role_card(card: dict[str, Any]) -> dict[str, Any]](fantareal/app.py#L2410)（第 2410 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_workshop_card(workshop: dict[str, Any]) -> dict[str, Any]](fantareal/app.py#L2449)（第 2449 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_runtime_overrides(raw: dict[str, Any] | None) -> dict[str, Any]](fantareal/app.py#L2489)（第 2489 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [resolve_runtime_value(override_value: Any, stored_value: Any, env_key: str | None = None) -> Any](fantareal/app.py#L2520)（第 2520 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_route_forwarding_chat_defaults() -> dict[str, str]](fantareal/app.py#L2538)（第 2538 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_runtime_chat_config(runtime_overrides: dict[str, Any] | None = None) -> dict[str, Any]](fantareal/app.py#L2564)（第 2564 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_runtime_embedding_config(runtime_overrides: dict[str, Any] | None = None) -> dict[str, Any]](fantareal/app.py#L2586)（第 2586 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_runtime_rerank_config(runtime_overrides: dict[str, Any] | None = None) -> dict[str, Any]](fantareal/app.py#L2599)（第 2599 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [append_messages(entries: list[tuple[str, str]]) -> None](fantareal/app.py#L2612)（第 2612 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_memory_text(memory: dict[str, Any], fields: list[str]) -> str](fantareal/app.py#L2631)（第 2631 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_base_url(base_url: str) -> str](fantareal/app.py#L2644)（第 2644 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_api_url(base_url: str, endpoint: str) -> str](fantareal/app.py#L2648)（第 2648 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_headers(api_key: str) -> dict[str, str]](fantareal/app.py#L2658)（第 2658 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [should_retry_status_code(status_code: int) -> bool](fantareal/app.py#L2665)（第 2665 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [safe_response_text(response: httpx.Response | None) -> str](fantareal/app.py#L2671)（第 2671 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [summarize_upstream_error(raw_text: str) -> str](fantareal/app.py#L2684)（第 2684 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：append_part

#### [append_part(label: str, value: Any) -> None（嵌套在 summarize_upstream_error 内）](fantareal/app.py#L2699)（第 2699 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [stream_compat_key(llm_config: dict[str, Any]) -> str](fantareal/app.py#L2732)（第 2732 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [should_retry_without_stream(status_code: int, error_detail: str) -> bool](fantareal/app.py#L2741)（第 2741 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [request_json() -> dict[str, Any]](fantareal/app.py#L2750)（第 2750 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [fetch_available_models() -> list[str]](fantareal/app.py#L2795)（第 2795 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [request_minimal_model_reply() -> dict[str, Any]](fantareal/app.py#L2836)（第 2836 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [fetch_embeddings(texts: list[str], runtime_overrides: dict[str, Any] | None = None) -> list[list[float]]](fantareal/app.py#L2868)（第 2868 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [cosine_similarity(left: list[float], right: list[float]) -> float](fantareal/app.py#L2895)（第 2895 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [rerank_documents(query: str, documents: list[dict[str, Any]], runtime_overrides: dict[str, Any] | None = None) -> list[dict[str, Any]]](fantareal/app.py#L2907)（第 2907 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_worldbook_runtime_state() -> dict[str, Any]](fantareal/app.py#L2952)（第 2952 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [worldbook_runtime_state_path(slot_id: str | None = None) -> Path](fantareal/app.py#L2956)（第 2956 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_worldbook_runtime_state(raw: Any) -> dict[str, Any]](fantareal/app.py#L2960)（第 2960 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_worldbook_runtime_state(slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L2990)（第 2990 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_worldbook_runtime_state(payload: dict[str, Any], slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L2994)（第 2994 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_route_forwarding_config() -> dict[str, Any]](fantareal/app.py#L3004)（第 3004 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sync_route_forwarding_p1_to_chat_settings(config: dict[str, Any]) -> None](fantareal/app.py#L3010)（第 3010 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_route_forwarding_config(payload: dict[str, Any]) -> dict[str, Any]](fantareal/app.py#L3038)（第 3038 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_worldbook_insertion_position(value: Any, default: str = after_char_defs) -> str](fantareal/app.py#L3052)（第 3052 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_worldbook_injection_role(value: Any, default: str = system) -> str](fantareal/app.py#L3057)（第 3057 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_worldbook_injection_depth(value: Any, default: int = 0) -> int](fantareal/app.py#L3064)（第 3064 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_worldbook_injection_order(value: Any, default: int = 100) -> int](fantareal/app.py#L3068)（第 3068 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_worldbook_prompt_layer(value: Any, default: str = follow_position) -> str](fantareal/app.py#L3072)（第 3072 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_worldbook_position_priority(item: dict[str, Any]) -> int](fantareal/app.py#L3077)（第 3077 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_worldbook_global_selection_sort_key(item: dict[str, Any]) -> tuple[int, int, str]](fantareal/app.py#L3086)（第 3086 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_worldbook_bucket_sort_key(item: dict[str, Any]) -> tuple[int, int, str]](fantareal/app.py#L3094)（第 3094 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [bucket_worldbook_matches(matches: list[dict[str, Any]] | None) -> dict[str, Any]](fantareal/app.py#L3104)（第 3104 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_worldbook_entry_sort_key(item: dict[str, Any]) -> tuple[int, int, int, str]](fantareal/app.py#L3135)（第 3135 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_build_worldbook_runtime_debug_entries(current_turn: int, entries: list[dict[str, Any]], runtime_entries: dict[str, dict[str, Any]]) -> list[dict[str, Any]]](fantareal/app.py#L3142)（第 3142 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_worldbook_alias_match_result(text: str, aliases: list[str]) -> tuple[bool, list[str]]](fantareal/app.py#L3188)（第 3188 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_evaluate_worldbook_keyword_entry(text: str, item: dict[str, Any], settings: dict[str, Any]) -> tuple[bool, list[str], list[str], str]](fantareal/app.py#L3207)（第 3207 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_worldbook_macro_context() -> dict[str, Any]](fantareal/app.py#L3257)（第 3257 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_render_worldbook_item_macros(item: dict[str, Any], macro_context: dict[str, Any]) -> dict[str, Any]](fantareal/app.py#L3261)（第 3261 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_worldbook_match_payload() -> dict[str, Any]](fantareal/app.py#L3283)（第 3283 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_worldbook_recursive_seed_text(item: dict[str, Any]) -> str](fantareal/app.py#L3332)（第 3332 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_worldbook_runtime_state_row(runtime: dict[str, Any]) -> dict[str, Any]](fantareal/app.py#L3345)（第 3345 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_worldbook_debug_display_sort_key(item: dict[str, Any]) -> tuple[int, int, int, int, str]](fantareal/app.py#L3357)（第 3357 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_state_journal_card_key(value: Any, fallback: str) -> str](fantareal/app.py#L3368)（第 3368 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_state_journal_current_card_uid() -> str](fantareal/app.py#L3376)（第 3376 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_state_journal_active_stage_rows() -> list[dict[str, Any]]](fantareal/app.py#L3393)（第 3393 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_state_journal_active_stage_tag_sources() -> list[dict[str, Any]]](fantareal/app.py#L3429)（第 3429 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_state_journal_active_stage_tags() -> list[dict[str, Any]]](fantareal/app.py#L3449)（第 3449 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_active_tag_context(value: Any, default_source: str = external) -> dict[str, Any]](fantareal/app.py#L3453)（第 3453 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：add_tag

#### [add_tag(tag_value: Any) -> None（嵌套在 _normalize_active_tag_context 内）](fantareal/app.py#L3457)（第 3457 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_merge_active_tag_contexts() -> dict[str, Any]](fantareal/app.py#L3491)（第 3491 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_active_tag_context(active_stage_tags: list[Any] | None = None, preset_context: dict[str, Any] | None = None) -> dict[str, Any]](fantareal/app.py#L3503)（第 3503 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_active_tag_sources_by_tag(active_tag_context: dict[str, Any]) -> dict[str, list[dict[str, Any]]]](fantareal/app.py#L3545)（第 3545 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_source_labels_for_tags(tags: list[str], sources_by_tag: dict[str, list[dict[str, Any]]]) -> list[str]](fantareal/app.py#L3557)（第 3557 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [match_worldbook_entries(query: str, external_active_tags: Any = None) -> list[dict[str, Any]]](fantareal/app.py#L3567)（第 3567 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [enforce_worldbook_fact_in_reply(user_message: str, reply_text: str, matches: list[dict[str, Any]]) -> str](fantareal/app.py#L3835)（第 3835 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_sprite_tag(tag: str) -> str](fantareal/app.py#L3843)（第 3843 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [extract_sprite_tag(reply_text: str) -> tuple[str, str]](fantareal/app.py#L3861)（第 3861 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_stringify_model_text(value: Any) -> str](fantareal/app.py#L3914)（第 3914 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [extract_reasoning_field(payload: Any) -> str](fantareal/app.py#L3934)（第 3934 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [combine_think_parts() -> str](fantareal/app.py#L3945)（第 3945 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_thought_markup(text: str) -> str](fantareal/app.py#L3949)（第 3949 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [extract_reply_parts(raw_text: str) -> dict[str, Any]](fantareal/app.py#L3999)（第 3999 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [compose_full_reply(think_text: str, visible_text: str) -> str](fantareal/app.py#L4055)（第 4055 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [extract_stream_visible_reply(raw_text: str) -> tuple[str, str]](fantareal/app.py#L4065)（第 4065 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [retrieve_memories(query: str, runtime_overrides: dict[str, Any] | None = None) -> list[dict[str, Any]]](fantareal/app.py#L4070)（第 4070 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [request_model_reply(user_message: str, retrieved_items: list[dict[str, Any]]) -> dict[str, Any]](fantareal/app.py#L4117)（第 4117 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [iter_non_stream_reply_events(reply_result: dict[str, Any])](fantareal/app.py#L4169)（第 4169 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_worldbook_debug_payload(user_message: str, worldbook_matches: list[dict[str, str]]) -> dict[str, Any]](fantareal/app.py#L4183)（第 4183 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [stream_model_reply(user_message: str, retrieved_items: list[dict[str, Any]])](fantareal/app.py#L4266)（第 4266 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [generate_reply(user_message: str, runtime_overrides: dict[str, Any] | None = None) -> tuple[dict[str, Any], list[dict[str, Any]], list[dict[str, str]], dict[str, Any], dict[str, Any]]](fantareal/app.py#L4453)（第 4453 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [fallback_memory_from_conversation(history: list[dict[str, Any]]) -> dict[str, Any]](fantareal/app.py#L4490)（第 4490 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：compact_text

#### [compact_text(value: Any, limit: int) -> str（嵌套在 fallback_memory_from_conversation 内）](fantareal/app.py#L4491)（第 4491 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [request_conversation_summary_with_model(history: list[dict[str, Any]]) -> dict[str, Any]](fantareal/app.py#L4529)（第 4529 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：parse_summary_json, is_mostly_english_summary

#### [parse_summary_json(candidate: str) -> dict[str, Any]（嵌套在 request_conversation_summary_with_model 内）](fantareal/app.py#L4562)（第 4562 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [is_mostly_english_summary(payload: dict[str, Any]) -> bool（嵌套在 request_conversation_summary_with_model 内）](fantareal/app.py#L4585)（第 4585 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_memory_summary(payload: dict[str, Any]) -> dict[str, Any]](fantareal/app.py#L4748)（第 4748 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [summarize_conversation_to_memory(history: list[dict[str, Any]]) -> dict[str, Any]](fantareal/app.py#L4779)（第 4779 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_get_archive_lock(slot_id: str) -> asyncio.Lock](fantareal/app.py#L4793)（第 4793 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [archive_current_conversation() -> dict[str, Any]](fantareal/app.py#L4799)（第 4799 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [chinese_access_log(request: Request, call_next)](fantareal/app.py#L4853)（第 4853 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 2 节 fantareal/app_models.py

### 一览

- **class ChatRequest** (Pydantic BaseModel) — 第 9 行
  - 字段: `message: str`, `runtime_config: dict[str, Any] | None`
- **class ChatHistoryEditRequest** (Pydantic BaseModel) — 第 14 行
  - 字段: `message_index: int`, `content: str`
- **class ChatHistoryRerollRequest** (Pydantic BaseModel) — 第 19 行
  - 字段: `message_index: int`
- **class DirectorNotePayload** (Pydantic BaseModel) — 第 23 行
  - 字段: `content: str`, `remaining_turns: int`, `position: str`
- **class DirectorNoteDeletePayload** (Pydantic BaseModel) — 第 29 行
  - 字段: `id: str`
- **class PersonaPayload** (Pydantic BaseModel) — 第 33 行
  - 字段: `name: str`, `system_prompt: str`, `greeting: str`
- **class SettingsPayload** (Pydantic BaseModel) — 第 39 行
  - 字段: `llm_base_url: str`, `llm_api_key: str`, `llm_model: str`, `theme: str`, `temperature: float`, `history_limit: int` ... 共 31 个字段
- **class MemoryItemPayload** (Pydantic BaseModel) — 第 73 行
  - 字段: `id: str`, `title: str`, `content: str`, `tags: list[str]`, `notes: str`
- **class MemoryListPayload** (Pydantic BaseModel) — 第 81 行
  - 字段: `items: list[MemoryItemPayload]`
- **class MergedMemoryItemPayload** (Pydantic BaseModel) — 第 85 行
  - 字段: `id: str`, `title: str`, `content: str`, `tags: list[str]`, `notes: str`, `source_memory_ids: list[str]` ... 共 7 个字段
- **class MergedMemoryListPayload** (Pydantic BaseModel) — 第 95 行
  - 字段: `items: list[MergedMemoryItemPayload]`
- **class MemoryOutlineItemPayload** (Pydantic BaseModel) — 第 99 行
  - 字段: `id: str`, `title: str`, `summary: str`, `characters: str`, `relationship_progress: str`, `key_events: list[str]` ... 共 12 个字段
- **class MemoryOutlineListPayload** (Pydantic BaseModel) — 第 114 行
  - 字段: `items: list[MemoryOutlineItemPayload]`
- **class MemoryMergePayload** (Pydantic BaseModel) — 第 118 行
  - 字段: `memory_ids: list[str]`, `merged_title: str`, `outline_title: str`, `delete_sources: bool`, `runtime_config: dict[str, Any] | None`
- **class UserProfilePayload** (Pydantic BaseModel) — 第 126 行
  - 字段: `display_name: str`, `nickname: str`, `profile_text: str`, `notes: str`
- **class WorldbookEntryPayload** (Pydantic BaseModel) — 第 133 行
  - 字段: `id: str`, `title: str`, `trigger: str`, `secondary_trigger: str`, `content: str`, `enabled: bool` ... 共 29 个字段
- **class WorldbookSettingsPayload** (Pydantic BaseModel) — 第 178 行
  - 字段: `enabled: bool`, `debug_enabled: bool`, `max_hits: int`, `default_case_sensitive: bool`, `default_whole_word: bool`, `default_match_mode: str` ... 共 19 个字段
- **class WorldbookPayload** (Pydantic BaseModel) — 第 208 行
  - 字段: `items: list[WorldbookEntryPayload]`, `settings: WorldbookSettingsPayload | None`
- **class PresetPromptPayload** (Pydantic BaseModel) — 第 213 行
  - 字段: `id: str`, `name: str`, `enabled: bool`, `content: str`, `order: int`, `placement: str | None` ... 共 11 个字段
- **class PresetPromptGroupItemPayload** (Pydantic BaseModel) — 第 227 行
  - 字段: `id: str`, `name: str`, `enabled: bool`, `content: str`, `placement: str | None`, `kind: str | None` ... 共 10 个字段
- **class PresetPromptGroupPayload** (Pydantic BaseModel) — 第 240 行
  - 字段: `id: str`, `name: str`, `enabled: bool`, `selection_mode: str`, `selected_ids: list[str]`, `items: list[PresetPromptGroupItemPayload]` ... 共 7 个字段
- **class PresetItemPayload** (Pydantic BaseModel) — 第 250 行
  - 字段: `id: str`, `name: str`, `enabled: bool`, `base_system_prompt: str`, `modules: dict[str, bool]`, `extra_prompts: list[PresetPromptPayload]` ... 共 7 个字段
- **class PresetStorePayload** (Pydantic BaseModel) — 第 260 行
  - 字段: `active_preset_id: str`, `presets: list[PresetItemPayload]`
- **class PresetCreatePayload** (Pydantic BaseModel) — 第 265 行
  - 字段: `name: str`
- **class PresetActionPayload** (Pydantic BaseModel) — 第 269 行
  - 字段: `preset_id: str`
- **class PresetImportPayload** (Pydantic BaseModel) — 第 273 行
  - 字段: `raw_json: str`, `activate_now: bool`
- **class SaveSlotSelectPayload** (Pydantic BaseModel) — 第 278 行
  - 字段: `slot_id: str`
- **class SaveSlotRenamePayload** (Pydantic BaseModel) — 第 282 行
  - 字段: `slot_id: str`, `name: str`
- **class SaveSlotResetPayload** (Pydantic BaseModel) — 第 287 行
  - 字段: `slot_id: str`
- **class SpriteDeletePayload** (Pydantic BaseModel) — 第 291 行
  - 字段: `filename: str`
- **class RoleCardPayload** (Pydantic BaseModel) — 第 295 行
  - 字段: `raw_json: str`, `filename: str`, `apply_now: bool`
- **class RoleCardLoadPayload** (Pydantic BaseModel) — 第 301 行
  - 字段: `filename: str`
- **class JsonImportPayload** (Pydantic BaseModel) — 第 305 行
  - 字段: `raw_json: str`, `apply_settings: bool`, `missing_injection_policy: str`, `force_in_chat_depth: int`, `force_injection_order: int | None`
- **class WorkshopEvaluatePayload** (Pydantic BaseModel) — 第 313 行
  - 字段: `reason: str`, `advance_temp: bool`
- **class WorkshopSavePayload** (Pydantic BaseModel) — 第 318 行
  - 字段: `creativeWorkshop: dict[str, Any]`
- **class SlotMetadata** (Pydantic BaseModel) — 第 322 行
  - 字段: `slot_id: str`, `slot_name: str`, `created_at: str`, `last_updated: str`, `card_id: str`
- **class SlotChatMessage** (Pydantic BaseModel) — 第 330 行
  - 字段: `role: str`, `content: str`, `timestamp: str`
- **class SlotSummaryBuffer** (Pydantic BaseModel) — 第 338 行
  - 字段: `content: str`, `updated_at: str`, `source_message_count: int`
- **class SlotActivePreset** (Pydantic BaseModel) — 第 344 行
  - 字段: `preset_id: str`, `name: str`, `enabled: bool`, `generation_params: dict[str, Any]`, `system_prompt_filter: str`, `prompt_fragments: list[str]` ... 共 7 个字段
- **class SlotVariableStore** (Pydantic BaseModel) — 第 354 行
  - 字段: `favorability: float`, `current_stage: str`, `virtual_time: str`
- **class SlotRuntimeMedia** (Pydantic BaseModel) — 第 362 行
  - 字段: `background_image_url: str`, `background_overlay: float`, `bgm_url: str`, `bgm_preset: str`, `media_note: str`
- **class SlotEnvironmentState** (Pydantic BaseModel) — 第 370 行
  - 字段: `active_preset: SlotActivePreset`, `variable_store: SlotVariableStore`, `runtime_media: SlotRuntimeMedia`
- **class SlotWorldbookContext** (Pydantic BaseModel) — 第 376 行
  - 字段: `unlocked_entry_ids: list[str]`, `active_entry_ids: list[str]`, `last_trigger_terms: list[str]`, `last_injected_at: str`
- **class SlotState** (Pydantic BaseModel) — 第 383 行
  - 字段: `metadata: SlotMetadata`, `chat_history: list[SlotChatMessage]`, `summary_buffer: SlotSummaryBuffer`, `environment_state: SlotEnvironmentState`, `worldbook_context: SlotWorldbookContext`
- **class SlotForkPayload** (Pydantic BaseModel) — 第 391 行
  - 字段: `source_slot_id: str`, `target_slot_id: str`, `target_name: str`, `chat_index: int | None`
- **class SlotSummaryBufferPayload** (Pydantic BaseModel) — 第 398 行
  - 字段: `slot_id: str`, `content: str`, `source_message_count: int | None`
- **class SlotVariablePatchPayload** (Pydantic BaseModel) — 第 404 行
  - 字段: `slot_id: str`, `variables: dict[str, Any]`
- **class DynamicWorldbookPreviewPayload** (Pydantic BaseModel) — 第 409 行
  - 字段: `slot_id: str`, `message: str`, `recent_window: int`
- **class ScenarioBundle** (Pydantic BaseModel) — 第 415 行
  - 字段: `version: int`, `bundle_type: str`, `exported_at: str`, `card_id: str`, `card_payload: dict[str, Any]`, `worldbook_asset: dict[str, Any]` ... 共 12 个字段
- **class ScenarioBundleImportPayload** (Pydantic BaseModel) — 第 430 行
  - 字段: `raw_json: str`, `target_slot_id: str`, `load_card: bool`


## 第 3 节 fantareal/chat_api_routes.py

### 一览

- `register_chat_api_routes()` — 第 18 行

### 函数详情

#### [register_chat_api_routes(app: FastAPI) -> None](fantareal/chat_api_routes.py#L18)（第 18 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：api_get_history, api_get_director_notes, api_create_director_note, api_delete_director_note, api_patch_message_metadata, api_edit_user_message, api_reroll_assistant_message, api_chat, api_chat_prompt_preview, api_chat_stream, api_end_conversation, api_reset, api_export_history

#### [api_get_history() -> list[dict[str, Any]]（嵌套在 register_chat_api_routes 内）](fantareal/chat_api_routes.py#L20)（第 20 行）
GET /api/history 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_director_notes() -> dict[str, Any]（嵌套在 register_chat_api_routes 内）](fantareal/chat_api_routes.py#L24)（第 24 行）
GET /api/chat/director-notes 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_create_director_note(payload: DirectorNotePayload) -> dict[str, Any]（嵌套在 register_chat_api_routes 内）](fantareal/chat_api_routes.py#L28)（第 28 行）
POST /api/chat/director-notes 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_delete_director_note(payload: DirectorNoteDeletePayload) -> dict[str, Any]（嵌套在 register_chat_api_routes 内）](fantareal/chat_api_routes.py#L33)（第 33 行）
POST /api/chat/director-notes/delete 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_patch_message_metadata(payload: dict[str, Any]) -> dict[str, Any]（嵌套在 register_chat_api_routes 内）](fantareal/chat_api_routes.py#L39)（第 39 行）
POST /api/chat/history/message-meta 端点。Persist client-side chat message identity for mod hooks
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：same_text

#### [same_text(left: str, right: str) -> bool（嵌套在 api_patch_message_metadata 内）](fantareal/chat_api_routes.py#L66)（第 66 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_edit_user_message(payload: ChatHistoryEditRequest) -> dict[str, Any]（嵌套在 register_chat_api_routes 内）](fantareal/chat_api_routes.py#L155)（第 155 行）
POST /api/chat/history/edit-user 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_reroll_assistant_message(payload: ChatHistoryRerollRequest) -> dict[str, Any]（嵌套在 register_chat_api_routes 内）](fantareal/chat_api_routes.py#L182)（第 182 行）
POST /api/chat/history/reroll 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_chat(payload: ChatRequest) -> dict[str, Any]（嵌套在 register_chat_api_routes 内）](fantareal/chat_api_routes.py#L221)（第 221 行）
POST /api/chat 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_chat_prompt_preview(payload: ChatRequest) -> dict[str, Any]（嵌套在 register_chat_api_routes 内）](fantareal/chat_api_routes.py#L262)（第 262 行）
POST /api/chat/prompt-preview 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_chat_stream(payload: ChatRequest) -> StreamingResponse（嵌套在 register_chat_api_routes 内）](fantareal/chat_api_routes.py#L295)（第 295 行）
POST /api/chat/stream 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：event_stream

#### [event_stream()（嵌套在 api_chat_stream 内）](fantareal/chat_api_routes.py#L347)（第 347 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_end_conversation() -> dict[str, Any]（嵌套在 register_chat_api_routes 内）](fantareal/chat_api_routes.py#L401)（第 401 行）
POST /api/conversation/end 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_reset() -> dict[str, Any]（嵌套在 register_chat_api_routes 内）](fantareal/chat_api_routes.py#L427)（第 427 行）
POST /api/reset 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export_history() -> FileResponse（嵌套在 register_chat_api_routes 内）](fantareal/chat_api_routes.py#L437)（第 437 行）
GET /api/export/history 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 4 节 fantareal/config_api_routes.py

### 一览

- `strip_json_comments()` — 第 66 行
- `parse_json_import_payload()` — 第 117 行
- `_worldbook_field_present()` — 第 130 行
- `_apply_worldbook_import_options()` — 第 141 行
- `register_config_api_routes()` — 第 183 行

### 函数详情

#### [strip_json_comments(raw_text: str) -> str](fantareal/config_api_routes.py#L66)（第 66 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_json_import_payload(raw_json: str) -> Any](fantareal/config_api_routes.py#L117)（第 117 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_worldbook_field_present(row: dict[str, Any], key: str) -> bool](fantareal/config_api_routes.py#L130)（第 130 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_apply_worldbook_import_options(entries: list[Any]) -> list[Any]](fantareal/config_api_routes.py#L141)（第 141 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [register_config_api_routes(app: FastAPI) -> None](fantareal/config_api_routes.py#L183)（第 183 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：build_bundle_label, parse_bundle_option, get_nested_value, set_nested_value, iter_workshop_media_fields, classify_workshop_media_url, workshop_media_zip_path, is_safe_workshop_media_zip_path, allowed_workshop_media_suffix, collect_workshop_media_for_export, make_import_media_filename, restore_workshop_media_from_bundle, api_get_user_profile, api_save_user_profile, api_upload_user_avatar, api_upload_role_avatar, api_get_preset, api_save_preset, api_create_preset, api_activate_preset, api_duplicate_preset, api_delete_preset, api_export_current_preset, api_import_preset, api_get_persona, api_save_persona, api_get_settings, api_save_settings, api_get_route_forwarding, api_save_route_forwarding, api_test_route_forwarding_provider, api_get_memories, api_export_memories, api_import_memories, api_save_memories, api_get_merged_memories, api_save_merged_memories, api_export_merged_memories, api_get_memory_outline, api_save_memory_outline, api_export_memory_outline, api_export_memory_bundle, api_import_memory_bundle, api_merge_memories, api_get_worldbook, api_export_worldbook, api_import_worldbook, api_save_worldbook, api_get_worldbook_settings, api_save_worldbook_settings, api_get_worldbook_entries, api_save_worldbook_entries, api_preview_dynamic_worldbook, api_get_sprites, api_upload_sprite, api_delete_sprite, api_get_cards, workshop_has_effective_binding, normalize_card_filename, read_existing_role_card_for_workshop, preserve_existing_workshop_when_importing, api_import_card, api_load_card, api_export_current_card, api_export_current_bundle, api_import_bundle, api_export_logs, workshop_card_binding_summary, workshop_status_payload, api_get_workshop_status, api_save_workshop, api_clear_workshop_card_binding, api_evaluate_workshop, api_upload_background, api_upload_font, api_upload_workshop_asset, api_export_workspace_bundle, api_import_workspace_bundle, api_get_models, api_test_connection, api_test_embedding

#### [build_bundle_label() -> tuple[str, dict[str, Any], dict[str, Any]]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L184)（第 184 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_bundle_option(value: Any, default: bool = True) -> bool（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L202)（第 202 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_nested_value(payload: Any, path: str) -> Any（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L207)（第 207 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [set_nested_value(payload: Any, path: str, value: Any) -> bool（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L223)（第 223 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [iter_workshop_media_fields(card: dict[str, Any]) -> list[tuple[str, str]]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L252)（第 252 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [classify_workshop_media_url(url: str) -> tuple[str, str] | None（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L285)（第 285 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [workshop_media_zip_path(kind: str, filename: str) -> str（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L294)（第 294 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [is_safe_workshop_media_zip_path(name: str, kind: str) -> bool（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L299)（第 299 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [allowed_workshop_media_suffix(kind: str, filename: str) -> bool（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L308)（第 308 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [collect_workshop_media_for_export(card: dict[str, Any]) -> tuple[list[dict[str, Any]], list[str]]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L313)（第 313 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [make_import_media_filename(original: str, existing_target: Path) -> str（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L359)（第 359 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [restore_workshop_media_from_bundle(archive: ZipFile, card: dict[str, Any]) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L367)（第 367 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_user_profile() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L456)（第 456 行）
GET /api/user-profile 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_user_profile(payload: UserProfilePayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L461)（第 461 行）
POST /api/user-profile 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_upload_user_avatar(file: UploadFile = File(...)) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L467)（第 467 行）
POST /api/user-avatar 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_upload_role_avatar(file: UploadFile = File(...)) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L481)（第 481 行）
POST /api/role-avatar 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_preset() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L499)（第 499 行）
GET /api/preset 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_preset(payload: PresetStorePayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L510)（第 510 行）
POST /api/preset 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_create_preset(payload: PresetCreatePayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L522)（第 522 行）
POST /api/preset/create 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_activate_preset(payload: PresetActionPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L537)（第 537 行）
POST /api/preset/activate 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_duplicate_preset(payload: PresetActionPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L550)（第 550 行）
POST /api/preset/duplicate 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_delete_preset(payload: PresetActionPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L565)（第 565 行）
POST /api/preset/delete 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export_current_preset() -> FileResponse（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L578)（第 578 行）
GET /api/preset/export/current 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_import_preset(payload: PresetImportPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L591)（第 591 行）
POST /api/preset/import 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_persona() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L629)（第 629 行）
GET /api/persona 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_persona(payload: PersonaPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L634)（第 634 行）
POST /api/persona 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_settings() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L647)（第 647 行）
GET /api/settings 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_settings(payload: SettingsPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L656)（第 656 行）
POST /api/settings 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_route_forwarding() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L678)（第 678 行）
GET /api/route-forwarding 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_route_forwarding(payload: dict[str, Any] = Body(default_factory=dict)) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L686)（第 686 行）
POST /api/route-forwarding 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_test_route_forwarding_provider(payload: dict[str, Any] = Body(default_factory=dict)) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L695)（第 695 行）
POST /api/route-forwarding/test-provider 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_memories() -> list[dict[str, Any]]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L707)（第 707 行）
GET /api/memories 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export_memories() -> FileResponse（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L712)（第 712 行）
GET /api/memories/export 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_import_memories(payload: JsonImportPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L725)（第 725 行）
POST /api/memories/import 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_memories(payload: MemoryListPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L740)（第 740 行）
POST /api/memories 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_merged_memories() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L747)（第 747 行）
GET /api/memories/merged 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_merged_memories(payload: MergedMemoryListPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L752)（第 752 行）
POST /api/memories/merged 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export_merged_memories() -> FileResponse（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L758)（第 758 行）
GET /api/memories/merged/export 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_memory_outline() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L771)（第 771 行）
GET /api/memories/outline 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_memory_outline(payload: MemoryOutlineListPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L776)（第 776 行）
POST /api/memories/outline 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export_memory_outline() -> FileResponse（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L782)（第 782 行）
GET /api/memories/outline/export 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export_memory_bundle() -> FileResponse（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L796)（第 796 行）
GET /api/memories/export-bundle 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_import_memory_bundle(file: UploadFile = File(...)) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L833)（第 833 行）
POST /api/memories/import-bundle 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：validate_bundle_archive, payload_items, read_bundle_json, clone_rows, ensure_unique_ids, remap_source_ids

#### [validate_bundle_archive(archive: ZipFile) -> None（嵌套在 api_import_memory_bundle 内）](fantareal/config_api_routes.py#L845)（第 845 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [payload_items(payload: Any) -> list[Any]（嵌套在 api_import_memory_bundle 内）](fantareal/config_api_routes.py#L870)（第 870 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [read_bundle_json(archive: ZipFile, entry_name: str) -> list[Any]（嵌套在 api_import_memory_bundle 内）](fantareal/config_api_routes.py#L884)（第 884 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clone_rows(rows: list[Any]) -> list[dict[str, Any]]（嵌套在 api_import_memory_bundle 内）](fantareal/config_api_routes.py#L898)（第 898 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [ensure_unique_ids(rows: list[dict[str, Any]], existing_ids: set[str]) -> tuple[list[dict[str, Any]], dict[str, str]]（嵌套在 api_import_memory_bundle 内）](fantareal/config_api_routes.py#L905)（第 905 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [remap_source_ids(rows: list[dict[str, Any]]) -> None（嵌套在 api_import_memory_bundle 内）](fantareal/config_api_routes.py#L960)（第 960 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_merge_memories(payload: MemoryMergePayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L987)（第 987 行）
POST /api/memories/merge 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_worldbook() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1000)（第 1000 行）
GET /api/worldbook 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export_worldbook() -> FileResponse（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1006)（第 1006 行）
GET /api/worldbook/export 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_import_worldbook(payload: JsonImportPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1019)（第 1019 行）
POST /api/worldbook/import 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_worldbook(payload: WorldbookPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1059)（第 1059 行）
POST /api/worldbook 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_worldbook_settings() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1132)（第 1132 行）
GET /api/worldbook/settings 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_worldbook_settings(payload: WorldbookSettingsPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1137)（第 1137 行）
POST /api/worldbook/settings 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_worldbook_entries() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1143)（第 1143 行）
GET /api/worldbook/entries 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_worldbook_entries(payload: WorldbookPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1151)（第 1151 行）
POST /api/worldbook/entries 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_preview_dynamic_worldbook(payload: DynamicWorldbookPreviewPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1157)（第 1157 行）
POST /api/worldbook/dynamic-preview 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_sprites() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1165)（第 1165 行）
GET /api/sprites 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_upload_sprite(tag: str = Form(''), file: UploadFile = File(...)) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1173)（第 1173 行）
POST /api/sprites 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_delete_sprite(payload: SpriteDeletePayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1224)（第 1224 行）
POST /api/sprites/delete 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_cards() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1250)（第 1250 行）
GET /api/cards 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [workshop_has_effective_binding(raw: Any) -> bool（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1258)（第 1258 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_card_filename(filename: str, fallback_name: str = role_card) -> str（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1283)（第 1283 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [read_existing_role_card_for_workshop(filename: str) -> dict[str, Any] | None（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1289)（第 1289 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [preserve_existing_workshop_when_importing(card: dict[str, Any], filename: str) -> tuple[dict[str, Any], bool]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1298)（第 1298 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_import_card(payload: RoleCardPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1324)（第 1324 行）
POST /api/cards/import 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_load_card(payload: RoleCardLoadPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1344)（第 1344 行）
POST /api/cards/load 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export_current_card() -> FileResponse（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1361)（第 1361 行）
GET /api/cards/export/current 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export_current_bundle(memories: str | None = 1, worldbook: str | None = 1, preset: str | None = 1, media: str | None = 1) -> FileResponse（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1386)（第 1386 行）
GET /api/export/current-bundle 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_import_bundle(file: UploadFile = File(...), overwrite: str | None = None) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1492)（第 1492 行）
POST /api/import/bundle 端点。导入四卡完整存档 ZIP 包
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export_logs() -> FileResponse（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1602)（第 1602 行）
GET /api/logs/export 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [workshop_card_binding_summary(workshop: dict[str, Any], current_card: dict[str, Any] | None = None) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1622)（第 1622 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [workshop_status_payload(active_slot: str | None = None) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1646)（第 1646 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_workshop_status() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1666)（第 1666 行）
GET /api/workshop/status 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_workshop(payload: WorkshopSavePayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1670)（第 1670 行）
POST /api/workshop/save 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_clear_workshop_card_binding() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1684)（第 1684 行）
POST /api/workshop/clear-card-binding 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_evaluate_workshop(payload: WorkshopEvaluatePayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1698)（第 1698 行）
POST /api/workshop/evaluate 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_upload_background(file: UploadFile = File(...)) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1714)（第 1714 行）
POST /api/background 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_upload_font(file: UploadFile = File(...)) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1742)（第 1742 行）
POST /api/font 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_upload_workshop_asset(kind: str = Form('image'), file: UploadFile = File(...)) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1769)（第 1769 行）
POST /api/workshop/upload 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export_workspace_bundle() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1776)（第 1776 行）
GET /api/workspace/export 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_import_workspace_bundle(payload: JsonImportPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1799)（第 1799 行）
POST /api/workspace/import 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_models() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1868)（第 1868 行）
POST /api/models 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_test_connection() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1885)（第 1885 行）
POST /api/test-connection 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_test_embedding() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1894)（第 1894 行）
POST /api/test-embedding 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 5 节 fantareal/launcher.py

### 一览

- `is_port_open()` — 第 20 行
- `wait_for_port()` — 第 26 行
- `get_free_port()` — 第 35 行
- `browser_profile_dir()` — 第 42 行
- `find_browser_executable()` — 第 48 行
- `start_local_server()` — 第 66 行
- `launch_app_window()` — 第 81 行
- `main()` — 第 101 行

### 函数详情

#### [is_port_open(host: str, port: int) -> bool](fantareal/launcher.py#L20)（第 20 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [wait_for_port(host: str, port: int, timeout_seconds: float = 20.0) -> bool](fantareal/launcher.py#L26)（第 26 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_free_port(host: str = HOST) -> int](fantareal/launcher.py#L35)（第 35 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [browser_profile_dir() -> Path](fantareal/launcher.py#L42)（第 42 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [find_browser_executable() -> str | None](fantareal/launcher.py#L48)（第 48 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [start_local_server(port: int) -> tuple[uvicorn.Server, threading.Thread]](fantareal/launcher.py#L66)（第 66 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [launch_app_window(url: str) -> subprocess.Popen[str] | None](fantareal/launcher.py#L81)（第 81 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [main() -> None](fantareal/launcher.py#L101)（第 101 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 6 节 fantareal/macro_variables.py

### 一览

- `_clean_text()` — 第 18 行
- `_normalize_role_id()` — 第 22 行
- `_split_aliases()` — 第 30 行
- `_role_from_persona()` — 第 45 行
- `_roles_from_card()` — 第 54 行
- `_format_cast()` — 第 86 行
- `build_macro_context()` — 第 100 行
- `render_macro_variables()` — 第 133 行
- `render_prompt_segments_with_macros()` — 第 202 行
- `render_messages_with_macros()` — 第 253 行

### 函数详情

#### [_clean_text(value: Any) -> str](fantareal/macro_variables.py#L18)（第 18 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_role_id(value: Any, fallback: str) -> str](fantareal/macro_variables.py#L22)（第 22 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_split_aliases(value: Any) -> list[str]](fantareal/macro_variables.py#L30)（第 30 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_role_from_persona(persona: dict[str, Any]) -> dict[str, Any] | None](fantareal/macro_variables.py#L45)（第 45 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_roles_from_card(role_card: dict[str, Any] | None) -> list[dict[str, Any]]](fantareal/macro_variables.py#L54)（第 54 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_format_cast(roles: list[dict[str, Any]]) -> str](fantareal/macro_variables.py#L86)（第 86 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_macro_context() -> dict[str, Any]](fantareal/macro_variables.py#L100)（第 100 行）
Build macro variable context from stable user, character, and cast data
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [render_macro_variables(text: Any, context: dict[str, Any] | None = None) -> tuple[str, dict[str, Any]]](fantareal/macro_variables.py#L133)（第 133 行）
Render macro variables in a single text block
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：replace

#### [replace(match: re.Match[str]) -> str（嵌套在 render_macro_variables 内）](fantareal/macro_variables.py#L144)（第 144 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [render_prompt_segments_with_macros(segments: list[dict[str, Any]], context: dict[str, Any] | None = None) -> tuple[list[dict[str, Any]], dict[str, Any]]](fantareal/macro_variables.py#L202)（第 202 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [render_messages_with_macros(messages: list[dict[str, Any]], context: dict[str, Any] | None = None) -> tuple[list[dict[str, Any]], dict[str, Any]]](fantareal/macro_variables.py#L253)（第 253 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 7 节 fantareal/memory_merge_logic.py

### 一览

- `_now_text()` — 第 15 行
- `_build_api_url()` — 第 19 行
- `_compact_text()` — 第 29 行
- `_sanitize_tags()` — 第 36 行
- `_sanitize_memory_item()` — 第 52 行
- `_sanitize_memory_list()` — 第 65 行
- `_sanitize_string_list()` — 第 75 行
- `_sanitize_merged_memory_item()` — 第 90 行
- `_sanitize_merged_memory_list()` — 第 108 行
- `_sanitize_outline_item()` — 第 118 行
- `_sanitize_outline_list()` — 第 138 行
- `_base_data_dir()` — 第 148 行
- `merged_memories_path()` — 第 152 行
- `memory_outline_path()` — 第 156 行
- `get_merged_memories()` — 第 160 行
- `save_merged_memories()` — 第 165 行
- `get_memory_outline()` — 第 175 行
- `save_memory_outline()` — 第 180 行
- `build_memory_merge_prompt()` — 第 190 行
- `_fallback_merge_result()` — 第 250 行
- `_parse_merge_response_json()` — 第 309 行
- `request_memory_merge_with_model()` — 第 339 行
- `_build_final_merged_memory()` — 第 427 行
- `_build_final_outline_item()` — 第 453 行
- `merge_memories_to_outline()` — 第 480 行

### 函数详情

#### [_now_text() -> str](fantareal/memory_merge_logic.py#L15)（第 15 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_build_api_url(base_url: str, endpoint: str) -> str](fantareal/memory_merge_logic.py#L19)（第 19 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_compact_text(value: Any, limit: int) -> str](fantareal/memory_merge_logic.py#L29)（第 29 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_sanitize_tags(value: Any) -> list[str]](fantareal/memory_merge_logic.py#L36)（第 36 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_sanitize_memory_item(item: Any) -> dict[str, Any]](fantareal/memory_merge_logic.py#L52)（第 52 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_sanitize_memory_list(items: Any) -> list[dict[str, Any]]](fantareal/memory_merge_logic.py#L65)（第 65 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_sanitize_string_list(value: Any) -> list[str]](fantareal/memory_merge_logic.py#L75)（第 75 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_sanitize_merged_memory_item(item: Any) -> dict[str, Any]](fantareal/memory_merge_logic.py#L90)（第 90 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_sanitize_merged_memory_list(items: Any) -> list[dict[str, Any]]](fantareal/memory_merge_logic.py#L108)（第 108 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_sanitize_outline_item(item: Any) -> dict[str, Any]](fantareal/memory_merge_logic.py#L118)（第 118 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_sanitize_outline_list(items: Any) -> list[dict[str, Any]]](fantareal/memory_merge_logic.py#L138)（第 138 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_base_data_dir(ctx: Any, slot_id: str | None = None) -> Path](fantareal/memory_merge_logic.py#L148)（第 148 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [merged_memories_path(ctx: Any, slot_id: str | None = None) -> Path](fantareal/memory_merge_logic.py#L152)（第 152 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [memory_outline_path(ctx: Any, slot_id: str | None = None) -> Path](fantareal/memory_merge_logic.py#L156)（第 156 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_merged_memories(ctx: Any, slot_id: str | None = None) -> list[dict[str, Any]]](fantareal/memory_merge_logic.py#L160)（第 160 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_merged_memories(ctx: Any, items: list[dict[str, Any]], slot_id: str | None = None) -> list[dict[str, Any]]](fantareal/memory_merge_logic.py#L165)（第 165 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_memory_outline(ctx: Any, slot_id: str | None = None) -> list[dict[str, Any]]](fantareal/memory_merge_logic.py#L175)（第 175 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_memory_outline(ctx: Any, items: list[dict[str, Any]], slot_id: str | None = None) -> list[dict[str, Any]]](fantareal/memory_merge_logic.py#L180)（第 180 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_memory_merge_prompt(selected_memories: list[dict[str, Any]]) -> str](fantareal/memory_merge_logic.py#L190)（第 190 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_fallback_merge_result(selected_memories: list[dict[str, Any]]) -> dict[str, Any]](fantareal/memory_merge_logic.py#L250)（第 250 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_parse_merge_response_json(text: str) -> dict[str, Any]](fantareal/memory_merge_logic.py#L309)（第 309 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [request_memory_merge_with_model(ctx: Any, selected_memories: list[dict[str, Any]]) -> dict[str, Any]](fantareal/memory_merge_logic.py#L339)（第 339 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_build_final_merged_memory(payload: dict[str, Any]) -> dict[str, Any]](fantareal/memory_merge_logic.py#L427)（第 427 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_build_final_outline_item(payload: dict[str, Any]) -> dict[str, Any]](fantareal/memory_merge_logic.py#L453)（第 453 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [merge_memories_to_outline(ctx: Any, memory_ids: list[str]) -> dict[str, Any]](fantareal/memory_merge_logic.py#L480)（第 480 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 8 节 fantareal/mod_api_routes.py

### 一览

- `register_mod_api_routes()` — 第 8 行

### 函数详情

#### [register_mod_api_routes(app: FastAPI) -> None](fantareal/mod_api_routes.py#L8)（第 8 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：list_mods, get_mod

#### [list_mods() -> dict[str, Any]（嵌套在 register_mod_api_routes 内）](fantareal/mod_api_routes.py#L10)（第 10 行）
GET /api/mods 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_mod(mod_slug: str) -> dict[str, Any]（嵌套在 register_mod_api_routes 内）](fantareal/mod_api_routes.py#L14)（第 14 行）
GET /api/mods/{mod_slug} 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 9 节 fantareal/mods_runtime.py

### 一览

- **class ModSpec** — 第 20 行

- `slugify_mod_name()` — 第 40 行
- `read_mod_manifest()` — 第 45 行
- `normalize_hook_url()` — 第 57 行
- `normalize_hooks()` — 第 68 行
- `discover_mods()` — 第 89 行
- `load_mod_app()` — 第 116 行
- `mount_discovered_mods()` — 第 132 行
- `find_mod()` — 第 144 行

### 函数详情

#### [to_dict() -> dict[str, Any]（嵌套在 ModSpec 内）](fantareal/mods_runtime.py#L29)（第 29 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [slugify_mod_name(name: str) -> str](fantareal/mods_runtime.py#L40)（第 40 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [read_mod_manifest(directory: Path) -> dict[str, Any]](fantareal/mods_runtime.py#L45)（第 45 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_hook_url(mount_path: str, value: Any) -> str](fantareal/mods_runtime.py#L57)（第 57 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_hooks(mount_path: str, raw: Any) -> dict[str, tuple[str, ...]]](fantareal/mods_runtime.py#L68)（第 68 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [discover_mods(mods_dir: Path) -> list[ModSpec]](fantareal/mods_runtime.py#L89)（第 89 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [load_mod_app(spec: ModSpec) -> FastAPI](fantareal/mods_runtime.py#L116)（第 116 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [mount_discovered_mods(app: FastAPI, mods_dir: Path) -> list[ModSpec]](fantareal/mods_runtime.py#L132)（第 132 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [find_mod(mods: list[ModSpec], slug: str) -> ModSpec | None](fantareal/mods_runtime.py#L144)（第 144 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 10 节 fantareal/page_routes.py

### 一览

- `register_page_routes()` — 第 15 行

### 函数详情

#### [register_page_routes(app: FastAPI) -> None](fantareal/page_routes.py#L15)（第 15 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：_read_challenge_card_json, _apply_challenge_four_cards, _opening_message_from_persona, _summary_buffer_content, _has_workshop_progress, _should_show_opening_message, _should_show_workshop_opening, _prompt_package_cache_scope, build_chat_template_context, root_redirect, index, mobile_index, config_page, preset_config_page, user_config_page, card_config_page, workshop_config_page, route_forwarding_config_page, memory_config_page, worldbook_config_page, worldbook_manager_page, sprite_config_page, about_config_page, challenge_mode_page, clear_challenge_mode_cards, _setup_tea_party, _get_game_or_404, game_page, game_state, game_new, game_shoot, game_skip_turn, game_use_item, game_discard_item, game_check_ready, game_reset, game_no_ai_turn, game_ai_turn, mod_host_page

#### [_read_challenge_card_json(filename: str) -> dict[str, Any]（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L18)（第 18 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_apply_challenge_four_cards() -> None（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L31)（第 31 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_opening_message_from_persona(persona: dict[str, Any]) -> str（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L55)（第 55 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_summary_buffer_content(slot_id: str | None = None) -> str（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L66)（第 66 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_has_workshop_progress(workshop_state: dict[str, Any]) -> bool（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L82)（第 82 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_should_show_opening_message() -> bool（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L92)（第 92 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_should_show_workshop_opening() -> bool（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L108)（第 108 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_prompt_package_cache_scope(active_slot: str | None, current_card: dict[str, Any], history: list[dict[str, Any]]) -> dict[str, str]（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L125)（第 125 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_chat_template_context() -> dict[str, Any]（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L170)（第 170 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [root_redirect() -> RedirectResponse（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L221)（第 221 行）
GET / 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [index(request: Request) -> HTMLResponse（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L225)（第 225 行）
GET /chat 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [mobile_index(request: Request) -> HTMLResponse（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L233)（第 233 行）
GET /mobile 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [config_page(request: Request) -> HTMLResponse（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L241)（第 241 行）
GET /config 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [preset_config_page(request: Request) -> HTMLResponse（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L254)（第 254 行）
GET /config/preset 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [user_config_page(request: Request) -> HTMLResponse（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L275)（第 275 行）
GET /config/user 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [card_config_page(request: Request) -> HTMLResponse（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L287)（第 287 行）
GET /config/card 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [workshop_config_page(request: Request) -> HTMLResponse（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L309)（第 309 行）
GET /config/workshop 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [route_forwarding_config_page(request: Request) -> HTMLResponse（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L329)（第 329 行）
GET /config/route-forwarding 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [memory_config_page(request: Request) -> HTMLResponse（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L342)（第 342 行）
GET /config/memory 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [worldbook_config_page(request: Request) -> HTMLResponse（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L355)（第 355 行）
GET /config/worldbook 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [worldbook_manager_page(request: Request) -> HTMLResponse（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L367)（第 367 行）
GET /config/worldbook/entries 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sprite_config_page(request: Request) -> HTMLResponse（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L381)（第 381 行）
GET /config/sprite 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [about_config_page(request: Request) -> HTMLResponse（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L396)（第 396 行）
GET /config/about 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [challenge_mode_page(request: Request) -> HTMLResponse（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L407)（第 407 行）
GET /mods/challenge-mode 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clear_challenge_mode_cards() -> dict[str, Any]（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L418)（第 418 行）
POST /api/challenge-mode/clear 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_setup_tea_party() -> types.ModuleType（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L434)（第 434 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_get_game_or_404(tp: types.ModuleType) -> Any（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L464)（第 464 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [game_page(request: Request) -> HTMLResponse（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L478)（第 478 行）
GET /game 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [game_state() -> dict[str, Any]（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L489)（第 489 行）
GET /api/game/state 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [game_new(request: Request) -> dict[str, Any]（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L497)（第 497 行）
POST /api/game/new 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [game_shoot(request: Request) -> dict[str, Any]（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L511)（第 511 行）
POST /api/game/shoot 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [game_skip_turn(request: Request) -> dict[str, Any]（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L522)（第 522 行）
POST /api/game/skip-turn 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [game_use_item(request: Request) -> dict[str, Any]（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L530)（第 530 行）
POST /api/game/use-item 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [game_discard_item(request: Request) -> dict[str, Any]（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L539)（第 539 行）
POST /api/game/discard-item 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [game_check_ready() -> dict[str, Any]（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L547)（第 547 行）
GET /api/game/check-ready 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [game_reset() -> dict[str, Any]（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L560)（第 560 行）
POST /api/game/reset 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [game_no_ai_turn(request: Request) -> dict[str, Any]（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L569)（第 569 行）
POST /api/game/no-ai-turn 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [game_ai_turn(request: Request) -> dict[str, Any]（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L610)（第 610 行）
POST /api/game/ai-turn 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [mod_host_page(request: Request, mod_slug: str) -> HTMLResponse（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L666)（第 666 行）
GET /mods/{mod_slug} 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 11 节 fantareal/preset_rules.py

### 一览

- `parse_bool()` — 第 213 行
- `parse_int()` — 第 223 行
- `normalize_preset_segment_placement()` — 第 272 行
- `normalize_preset_segment_kind()` — 第 279 行
- `normalize_preset_segment_strength()` — 第 284 行
- `sanitize_activation_tags()` — 第 289 行
- `apply_prompt_segment_fields()` — 第 300 行
- `generate_preset_id()` — 第 320 行
- `generate_prompt_group_id()` — 第 324 行
- `generate_prompt_group_item_id()` — 第 328 行
- `default_extra_prompts()` — 第 332 行
- `default_prompt_groups()` — 第 351 行
- `default_single_preset()` — 第 355 行
- `default_preset_store()` — 第 367 行
- `sanitize_prompt_item()` — 第 375 行
- `normalize_selection_mode()` — 第 392 行
- `sanitize_prompt_group_item()` — 第 399 行
- `sanitize_prompt_group()` — 第 415 行
- `apply_module_mutex()` — 第 464 行
- `sanitize_single_preset()` — 第 474 行
- `sanitize_preset_store()` — 第 511 行
- `get_active_preset_from_store()` — 第 538 行
- `build_base_kernel_metadata()` — 第 547 行
- `build_selected_prompt_group_blocks()` — 第 563 行
- `build_preset_observation_segments_from_preset()` — 第 593 行
- `build_preset_prompt_from_preset()` — 第 755 行
- `build_preset_output_guard_from_preset()` — 第 799 行
- `build_preset_output_guard_from_store()` — 第 810 行
- `create_preset_in_store()` — 第 813 行
- `activate_preset_in_store()` — 第 821 行
- `duplicate_preset_in_store()` — 第 829 行
- `delete_preset_from_store()` — 第 844 行

### 函数详情

#### [parse_bool(value: Any, default: bool = False) -> bool](fantareal/preset_rules.py#L213)（第 213 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_int(value: Any, default: int = 0) -> int](fantareal/preset_rules.py#L223)（第 223 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_preset_segment_placement(value: Any, default: str | None = None) -> str | None](fantareal/preset_rules.py#L272)（第 272 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_preset_segment_kind(value: Any, default: str = style) -> str](fantareal/preset_rules.py#L279)（第 279 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_preset_segment_strength(value: Any, default: str = soft) -> str](fantareal/preset_rules.py#L284)（第 284 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_activation_tags(value: Any) -> list[str]](fantareal/preset_rules.py#L289)（第 289 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [apply_prompt_segment_fields(target: dict[str, Any], raw: dict[str, Any]) -> None](fantareal/preset_rules.py#L300)（第 300 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [generate_preset_id() -> str](fantareal/preset_rules.py#L320)（第 320 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [generate_prompt_group_id() -> str](fantareal/preset_rules.py#L324)（第 324 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [generate_prompt_group_item_id() -> str](fantareal/preset_rules.py#L328)（第 328 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_extra_prompts() -> list[dict[str, Any]]](fantareal/preset_rules.py#L332)（第 332 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_prompt_groups() -> list[dict[str, Any]]](fantareal/preset_rules.py#L351)（第 351 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_single_preset(preset_id: str = preset_default, name: str = 默认预设) -> dict[str, Any]](fantareal/preset_rules.py#L355)（第 355 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_preset_store() -> dict[str, Any]](fantareal/preset_rules.py#L367)（第 367 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_prompt_item(raw: Any, index: int) -> dict[str, Any] | None](fantareal/preset_rules.py#L375)（第 375 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_selection_mode(value: Any) -> str](fantareal/preset_rules.py#L392)（第 392 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_prompt_group_item(raw: Any, index: int) -> dict[str, Any] | None](fantareal/preset_rules.py#L399)（第 399 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_prompt_group(raw: Any, index: int) -> dict[str, Any] | None](fantareal/preset_rules.py#L415)（第 415 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [apply_module_mutex(modules: dict[str, bool]) -> dict[str, bool]](fantareal/preset_rules.py#L464)（第 464 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_single_preset(raw: Any) -> dict[str, Any]](fantareal/preset_rules.py#L474)（第 474 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_preset_store(raw: Any) -> dict[str, Any]](fantareal/preset_rules.py#L511)（第 511 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_active_preset_from_store(store: dict[str, Any]) -> dict[str, Any]](fantareal/preset_rules.py#L538)（第 538 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_base_kernel_metadata(content: Any) -> dict[str, Any]](fantareal/preset_rules.py#L547)（第 547 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_selected_prompt_group_blocks(groups: list[dict[str, Any]]) -> list[tuple[int, str]]](fantareal/preset_rules.py#L563)（第 563 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_preset_observation_segments_from_preset(preset: dict[str, Any]) -> list[dict[str, Any]]](fantareal/preset_rules.py#L593)（第 593 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：append_segment

#### [append_segment(segment_id: str) -> None（嵌套在 build_preset_observation_segments_from_preset 内）](fantareal/preset_rules.py#L600)（第 600 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_preset_prompt_from_preset(preset: dict[str, Any]) -> str](fantareal/preset_rules.py#L755)（第 755 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_preset_output_guard_from_preset(preset: dict[str, Any]) -> str](fantareal/preset_rules.py#L799)（第 799 行）
Build a runtime-only guard that should be injected near the current user input
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_preset_output_guard_from_store(store: dict[str, Any]) -> str](fantareal/preset_rules.py#L810)（第 810 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [create_preset_in_store(store: dict[str, Any], name: str) -> dict[str, Any]](fantareal/preset_rules.py#L813)（第 813 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [activate_preset_in_store(store: dict[str, Any], preset_id: str) -> dict[str, Any]](fantareal/preset_rules.py#L821)（第 821 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [duplicate_preset_in_store(store: dict[str, Any], preset_id: str) -> dict[str, Any]](fantareal/preset_rules.py#L829)（第 829 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [delete_preset_from_store(store: dict[str, Any], preset_id: str) -> dict[str, Any]](fantareal/preset_rules.py#L844)（第 844 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 12 节 fantareal/prompt_builder.py

### 一览

- `build_base_kernel_metadata()` — 第 64 行
- `build_base_thinking_protocol_metadata()` — 第 80 行
- `_is_base_thinking_protocol_segment()` — 第 90 行
- `_empty_layered_injection_state()` — 第 96 行
- `_message()` — 第 113 行
- `_append_joined_message()` — 第 121 行
- `_segment_map()` — 第 128 行
- `_segment_contents_by()` — 第 136 行
- `_build_legacy_messages_from_segments()` — 第 159 行
- `_director_note_placement()` — 第 208 行
- `_format_director_note()` — 第 217 行
- `_bucket_director_notes()` — 第 231 行
- `_director_note_sections()` — 第 246 行
- `_is_layerable_preset_segment()` — 第 250 行
- `_set_layered_effect()` — 第 256 行
- `_build_layered_messages()` — 第 284 行
- `configure_prompt_builder()` — 第 440 行
- `_dep()` — 第 444 行
- `_optional_dep()` — 第 454 行
- `_extract_runtime_guard_from_preset()` — 第 459 行
- `_build_prompt_segment()` — 第 467 行
- `_sanitize_segment_activation_tags()` — 第 501 行
- `_preset_segment_title()` — 第 511 行
- `collect_preset_activation_tags()` — 第 524 行
- `_estimate_prompt_tokens()` — 第 552 行
- `_read_segment_token_budget()` — 第 562 行
- `_segment_budget_title()` — 第 571 行
- `_budget_bucket_totals()` — 第 582 行
- `_build_prompt_budget_dry_run()` — 第 593 行
- `_append_prompt_segment()` — 第 752 行
- `_worldbook_direct_question()` — 第 758 行
- `build_worldbook_prompt()` — 第 769 行
- `build_worldbook_answer_guard()` — 第 806 行
- `build_retrieval_prompt()` — 第 828 行
- `build_memory_recap_prompt()` — 第 842 行
- `build_user_profile_prompt()` — 第 867 行
- `build_sprite_prompt()` — 第 895 行
- `strip_thought_blocks()` — 第 907 行
- `_same_normalized_text()` — 第 930 行
- `_is_opening_only_message()` — 第 937 行
- `filter_prompt_history()` — 第 964 行
- `build_conversation_transcript()` — 第 969 行
- `build_prompt_package()` — 第 981 行
- `build_messages()` — 第 1724 行

### 函数详情

#### [build_base_kernel_metadata(content: Any) -> dict[str, Any]](fantareal/prompt_builder.py#L64)（第 64 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_base_thinking_protocol_metadata(content: Any) -> dict[str, Any]](fantareal/prompt_builder.py#L80)（第 80 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_is_base_thinking_protocol_segment(segment: dict[str, Any]) -> bool](fantareal/prompt_builder.py#L90)（第 90 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_empty_layered_injection_state(enabled: bool) -> dict[str, Any]](fantareal/prompt_builder.py#L96)（第 96 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_message(role: str, content: str) -> dict[str, str] | None](fantareal/prompt_builder.py#L113)（第 113 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_append_joined_message(messages: list[dict[str, str]], role: str, sections: list[str]) -> None](fantareal/prompt_builder.py#L121)（第 121 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_segment_map(prompt_segments: list[dict[str, Any]]) -> dict[str, str]](fantareal/prompt_builder.py#L128)（第 128 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_segment_contents_by(prompt_segments: list[dict[str, Any]]) -> list[str]](fantareal/prompt_builder.py#L136)（第 136 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_build_legacy_messages_from_segments(prompt_segments: list[dict[str, Any]]) -> list[dict[str, str]]](fantareal/prompt_builder.py#L159)（第 159 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_director_note_placement(position: Any) -> str](fantareal/prompt_builder.py#L208)（第 208 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_format_director_note(note: dict[str, Any], index: int) -> str](fantareal/prompt_builder.py#L217)（第 217 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_bucket_director_notes(notes: list[dict[str, Any]] | None) -> dict[str, list[dict[str, Any]]]](fantareal/prompt_builder.py#L231)（第 231 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_director_note_sections(buckets: dict[str, list[dict[str, Any]]], placement: str) -> list[str]](fantareal/prompt_builder.py#L246)（第 246 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_is_layerable_preset_segment(segment: dict[str, Any]) -> bool](fantareal/prompt_builder.py#L250)（第 250 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_set_layered_effect(state: dict[str, Any], segment: dict[str, Any]) -> None](fantareal/prompt_builder.py#L256)（第 256 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_build_layered_messages() -> tuple[list[dict[str, str]], dict[str, Any]]](fantareal/prompt_builder.py#L284)（第 284 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：preset_sections, append_in_chat_bucket

#### [preset_sections(placement: str) -> list[str]（嵌套在 _build_layered_messages 内）](fantareal/prompt_builder.py#L359)（第 359 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [append_in_chat_bucket(depth: int) -> None（嵌套在 _build_layered_messages 内）](fantareal/prompt_builder.py#L402)（第 402 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [configure_prompt_builder() -> None](fantareal/prompt_builder.py#L440)（第 440 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_dep(name: str) -> Callable[..., Any]](fantareal/prompt_builder.py#L444)（第 444 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_optional_dep(name: str) -> Callable[..., Any] | None](fantareal/prompt_builder.py#L454)（第 454 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_extract_runtime_guard_from_preset(preset_prompt: str) -> tuple[str, str]](fantareal/prompt_builder.py#L459)（第 459 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_build_prompt_segment(segment_id: str) -> dict[str, Any] | None](fantareal/prompt_builder.py#L467)（第 467 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_sanitize_segment_activation_tags(value: Any) -> list[str]](fantareal/prompt_builder.py#L501)（第 501 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_preset_segment_title(segment: dict[str, Any]) -> str](fantareal/prompt_builder.py#L511)（第 511 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [collect_preset_activation_tags(prompt_segments: list[dict[str, Any]]) -> dict[str, Any]](fantareal/prompt_builder.py#L524)（第 524 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_estimate_prompt_tokens(text: Any) -> int](fantareal/prompt_builder.py#L552)（第 552 行）
Very rough cross-model estimate for debug display, not tokenizer-accurate
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_read_segment_token_budget(segment: dict[str, Any]) -> int | None](fantareal/prompt_builder.py#L562)（第 562 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_segment_budget_title(segment: dict[str, Any]) -> str](fantareal/prompt_builder.py#L571)（第 571 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_budget_bucket_totals(items: list[dict[str, Any]], key: str) -> list[dict[str, Any]]](fantareal/prompt_builder.py#L582)（第 582 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_build_prompt_budget_dry_run() -> dict[str, Any]](fantareal/prompt_builder.py#L593)（第 593 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_append_prompt_segment(segments: list[dict[str, Any]]) -> None](fantareal/prompt_builder.py#L752)（第 752 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_worldbook_direct_question(user_message: str) -> bool](fantareal/prompt_builder.py#L758)（第 758 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_worldbook_prompt(matches: list[dict[str, Any]]) -> str](fantareal/prompt_builder.py#L769)（第 769 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_worldbook_answer_guard(user_message: str, matches: list[dict[str, Any]]) -> str](fantareal/prompt_builder.py#L806)（第 806 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_retrieval_prompt(retrieved_items: list[dict[str, Any]]) -> str](fantareal/prompt_builder.py#L828)（第 828 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_memory_recap_prompt(memories: list[dict[str, Any]]) -> str](fantareal/prompt_builder.py#L842)（第 842 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_user_profile_prompt(user_profile: dict[str, Any]) -> str](fantareal/prompt_builder.py#L867)（第 867 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_sprite_prompt(llm_config: dict[str, Any]) -> str](fantareal/prompt_builder.py#L895)（第 895 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [strip_thought_blocks(text: Any) -> str](fantareal/prompt_builder.py#L907)（第 907 行）
Keep stored chat intact, but remove <think>...</think> blocks before building prompts
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_same_normalized_text(left: Any, right: Any) -> bool](fantareal/prompt_builder.py#L930)（第 930 行）
Compare long opening text safely without being too sensitive to whitespace
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_is_opening_only_message(item: dict[str, Any], persona: dict[str, Any] | None = None) -> bool](fantareal/prompt_builder.py#L937)（第 937 行）
Opening/greeting is UI-only. It must not be sent back as chat history context
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [filter_prompt_history(history: list[dict[str, Any]], persona: dict[str, Any] | None = None) -> list[dict[str, Any]]](fantareal/prompt_builder.py#L964)（第 964 行）
Remove UI-only opening messages before building model prompts
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_conversation_transcript(history: list[dict[str, Any]], persona: dict[str, Any] | None = None) -> str](fantareal/prompt_builder.py#L969)（第 969 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_prompt_package(user_message: str, retrieved_items: list[dict[str, Any]] | None = None) -> dict[str, Any]](fantareal/prompt_builder.py#L981)（第 981 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：append_in_chat_bucket, append_segment, append_in_chat_segments, append_layer

#### [append_in_chat_bucket(depth: int) -> None（嵌套在 build_prompt_package 内）](fantareal/prompt_builder.py#L1092)（第 1092 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [append_segment(segment_id: str) -> None（嵌套在 build_prompt_package 内）](fantareal/prompt_builder.py#L1146)（第 1146 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [append_in_chat_segments(depth: int) -> None（嵌套在 build_prompt_package 内）](fantareal/prompt_builder.py#L1363)（第 1363 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [append_layer(layer_id: str, title: str, sections: list[str]) -> None（嵌套在 build_prompt_package 内）](fantareal/prompt_builder.py#L1551)（第 1551 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_messages(user_message: str, retrieved_items: list[dict[str, Any]] | None = None) -> list[dict[str, str]]](fantareal/prompt_builder.py#L1724)（第 1724 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 13 节 fantareal/route_forwarding.py

### 一览

- **class RouteForwardingRuntime** — 第 147 行

- `_clamp_int()` — 第 34 行
- `_clean_text()` — 第 42 行
- `sanitize_provider()` — 第 46 行
- `sanitize_route_forwarding_config()` — 第 79 行
- `should_retry_status_code()` — 第 104 行
- `endpoint_suffix_from_url()` — 第 108 行
- `build_forward_url()` — 第 122 行
- `is_external_http_url()` — 第 134 行
- `provider_keys()` — 第 142 行

### 函数详情

#### [_clamp_int(value: Any, min_value: int, max_value: int, default: int) -> int](fantareal/route_forwarding.py#L34)（第 34 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_clean_text(value: Any, limit: int = 500) -> str](fantareal/route_forwarding.py#L42)（第 42 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_provider(raw: Any, index: int) -> dict[str, Any] | None](fantareal/route_forwarding.py#L46)（第 46 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_route_forwarding_config(raw: Any) -> dict[str, Any]](fantareal/route_forwarding.py#L79)（第 79 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [should_retry_status_code(status_code: int) -> bool](fantareal/route_forwarding.py#L104)（第 104 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [endpoint_suffix_from_url(url: str) -> str](fantareal/route_forwarding.py#L108)（第 108 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_forward_url(provider_base_url: str, original_url: str) -> str](fantareal/route_forwarding.py#L122)（第 122 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [is_external_http_url(url: Any) -> bool](fantareal/route_forwarding.py#L134)（第 134 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [provider_keys(provider: dict[str, Any]) -> list[str]](fantareal/route_forwarding.py#L142)（第 142 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [__init__(get_config: Callable[[], dict[str, Any]]) -> None（嵌套在 RouteForwardingRuntime 内）](fantareal/route_forwarding.py#L148)（第 148 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [install() -> None（嵌套在 RouteForwardingRuntime 内）](fantareal/route_forwarding.py#L171)（第 171 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：patched_async_post, patched_async_request, patched_async_stream, patched_sync_post, patched_sync_request

#### [patched_async_post(client: httpx.AsyncClient, url: Any) -> httpx.Response（嵌套在 install 内）](fantareal/route_forwarding.py#L182)（第 182 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [patched_async_request(client: httpx.AsyncClient, method: str, url: Any) -> httpx.Response（嵌套在 install 内）](fantareal/route_forwarding.py#L185)（第 185 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [patched_async_stream(client: httpx.AsyncClient, method: str, url: Any) -> Any（嵌套在 install 内）](fantareal/route_forwarding.py#L194)（第 194 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [patched_sync_post(client: httpx.Client, url: Any) -> httpx.Response（嵌套在 install 内）](fantareal/route_forwarding.py#L197)（第 197 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [patched_sync_request(client: httpx.Client, method: str, url: Any) -> httpx.Response（嵌套在 install 内）](fantareal/route_forwarding.py#L200)（第 200 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [snapshot() -> dict[str, Any]（嵌套在 RouteForwardingRuntime 内）](fantareal/route_forwarding.py#L215)（第 215 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_provider_id(provider: dict[str, Any]) -> str（嵌套在 RouteForwardingRuntime 内）](fantareal/route_forwarding.py#L225)（第 225 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_provider_status(provider: dict[str, Any]) -> dict[str, Any]（嵌套在 RouteForwardingRuntime 内）](fantareal/route_forwarding.py#L228)（第 228 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_sync_provider_statuses(providers: list[Any]) -> None（嵌套在 RouteForwardingRuntime 内）](fantareal/route_forwarding.py#L253)（第 253 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_is_circuit_open(provider: dict[str, Any]) -> bool（嵌套在 RouteForwardingRuntime 内）](fantareal/route_forwarding.py#L268)（第 268 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_providers(config: dict[str, Any]) -> list[dict[str, Any]]（嵌套在 RouteForwardingRuntime 内）](fantareal/route_forwarding.py#L271)（第 271 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_candidate_requests(url: Any, kwargs: dict[str, Any]) -> list[tuple[dict[str, Any], str, dict[str, Any]]]（嵌套在 RouteForwardingRuntime 内）](fantareal/route_forwarding.py#L286)（第 286 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_rewrite_kwargs(kwargs: dict[str, Any], provider: dict[str, Any], api_key: str) -> dict[str, Any]（嵌套在 RouteForwardingRuntime 内）](fantareal/route_forwarding.py#L309)（第 309 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_record(provider: dict[str, Any], url: str) -> None（嵌套在 RouteForwardingRuntime 内）](fantareal/route_forwarding.py#L326)（第 326 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_open_circuit(provider: dict[str, Any], detail: str) -> None（嵌套在 RouteForwardingRuntime 内）](fantareal/route_forwarding.py#L365)（第 365 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_retry_attempts() -> int（嵌套在 RouteForwardingRuntime 内）](fantareal/route_forwarding.py#L373)（第 373 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [test_provider(provider_id: str) -> dict[str, Any]（嵌套在 RouteForwardingRuntime 内）](fantareal/route_forwarding.py#L381)（第 381 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [async_post(client: httpx.AsyncClient, url: Any) -> httpx.Response（嵌套在 RouteForwardingRuntime 内）](fantareal/route_forwarding.py#L451)（第 451 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [async_request(client: httpx.AsyncClient, method: str, url: Any) -> httpx.Response（嵌套在 RouteForwardingRuntime 内）](fantareal/route_forwarding.py#L494)（第 494 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [async_stream(client: httpx.AsyncClient, method: str, url: Any) -> Any（嵌套在 RouteForwardingRuntime 内）](fantareal/route_forwarding.py#L552)（第 552 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sync_post(client: httpx.Client, url: Any) -> httpx.Response（嵌套在 RouteForwardingRuntime 内）](fantareal/route_forwarding.py#L563)（第 563 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sync_request(client: httpx.Client, method: str, url: Any) -> httpx.Response（嵌套在 RouteForwardingRuntime 内）](fantareal/route_forwarding.py#L604)（第 604 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 14 节 fantareal/slot_runtime.py

### 一览

- **class SlotRuntimeService** — 第 27 行

### 函数详情

#### [__init__(ctx: Any)（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L30)（第 30 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_now_iso() -> str（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L33)（第 33 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_slot_id(slot_id: str | None = None) -> str（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L36)（第 36 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [slot_state_path(slot_id: str | None = None) -> Path（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L39)（第 39 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_read_snapshot(slot_id: str | None = None) -> SlotState | None（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L42)（第 42 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_guess_created_at(slot_id: str) -> str（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L53)（第 53 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_chat_history(history: list[dict[str, Any]]) -> list[SlotChatMessage]（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L65)（第 65 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_build_summary_buffer() -> SlotSummaryBuffer（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L79)（第 79 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_collect_preset_fragments(preset: dict[str, Any]) -> list[str]（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L112)（第 112 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_build_active_preset(slot_id: str, settings: dict[str, Any]) -> SlotActivePreset（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L129)（第 129 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_build_variable_store() -> SlotVariableStore（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L148)（第 148 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_build_runtime_media() -> SlotRuntimeMedia（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L167)（第 167 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_slot_state(slot_id: str | None = None) -> SlotState（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L188)（第 188 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [persist_slot_state(slot_state: SlotState) -> SlotState（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L239)（第 239 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [upsert_summary_buffer(payload: SlotSummaryBufferPayload) -> SlotState（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L247)（第 247 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [patch_variable_store(payload: SlotVariablePatchPayload) -> SlotState（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L257)（第 257 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_match_aliases(query_text: str, aliases: list[str]) -> tuple[bool, list[str]]（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L265)（第 265 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [resolve_dynamic_worldbook_context(payload: DynamicWorldbookPreviewPayload) -> dict[str, Any]（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L290)（第 290 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_slot_injection_payload(payload: DynamicWorldbookPreviewPayload) -> dict[str, Any]（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L400)（第 400 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_resolve_fork_target(source_slot_id: str, preferred_target: str) -> str（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L422)（第 422 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_rename_slot_if_needed(slot_id: str, target_name: str) -> None（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L432)（第 432 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [fork_slot(payload: SlotForkPayload) -> SlotState（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L443)（第 443 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [export_campaign_bundle(slot_id: str | None = None) -> ScenarioBundle（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L486)（第 486 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [import_campaign_bundle(bundle: ScenarioBundle) -> SlotState（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L505)（第 505 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [import_campaign_bundle_json(raw_json: str) -> SlotState（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L550)（第 550 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 15 节 fantareal/workshop_logic.py

### 一览

- `_parse_bool()` — 第 6 行
- `_clamp_int()` — 第 16 行
- `_clamp_float()` — 第 24 行
- `_safe_text()` — 第 32 行
- `normalize_workshop_opening_animation()` — 第 44 行
- `normalize_workshop_opening_after_mode()` — 第 49 行
- `default_workshop_opening()` — 第 54 行
- `default_workshop_ambience()` — 第 75 行
- `default_dynamic_scene()` — 第 102 行
- `default_creative_workshop()` — 第 137 行
- `normalize_workshop_stage()` — 第 147 行
- `normalize_dynamic_trigger_type()` — 第 152 行
- `normalize_dynamic_repeat_mode()` — 第 157 行
- `normalize_dynamic_content_type()` — 第 162 行
- `normalize_dynamic_presentation_mode()` — 第 167 行
- `sanitize_workshop_opening()` — 第 172 行
- `sanitize_workshop_ambience()` — 第 201 行
- `sanitize_dynamic_scene()` — 第 242 行
- `sanitize_creative_workshop()` — 第 288 行
- `default_workshop_state()` — 第 309 行
- `sanitize_workshop_state()` — 第 322 行
- `get_workshop_stage()` — 第 351 行
- `get_workshop_stage_label()` — 第 361 行

### 函数详情

#### [_parse_bool(value: Any, default: bool = False) -> bool](fantareal/workshop_logic.py#L6)（第 6 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_clamp_int(value: Any, minimum: int, maximum: int, default: int) -> int](fantareal/workshop_logic.py#L16)（第 16 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_clamp_float(value: Any, minimum: float, maximum: float, default: float) -> float](fantareal/workshop_logic.py#L24)（第 24 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_safe_text(value: Any, limit: int = 2000) -> str](fantareal/workshop_logic.py#L32)（第 32 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_workshop_opening_animation(value: Any) -> str](fantareal/workshop_logic.py#L44)（第 44 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_workshop_opening_after_mode(value: Any) -> str](fantareal/workshop_logic.py#L49)（第 49 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_workshop_opening() -> dict[str, Any]](fantareal/workshop_logic.py#L54)（第 54 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_workshop_ambience() -> dict[str, Any]](fantareal/workshop_logic.py#L75)（第 75 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_dynamic_scene() -> dict[str, Any]](fantareal/workshop_logic.py#L102)（第 102 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_creative_workshop() -> dict[str, Any]](fantareal/workshop_logic.py#L137)（第 137 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_workshop_stage(value: Any) -> str](fantareal/workshop_logic.py#L147)（第 147 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_dynamic_trigger_type(value: Any) -> str](fantareal/workshop_logic.py#L152)（第 152 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_dynamic_repeat_mode(value: Any) -> str](fantareal/workshop_logic.py#L157)（第 157 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_dynamic_content_type(value: Any) -> str](fantareal/workshop_logic.py#L162)（第 162 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_dynamic_presentation_mode(value: Any) -> str](fantareal/workshop_logic.py#L167)（第 167 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_workshop_opening(raw: Any) -> dict[str, Any]](fantareal/workshop_logic.py#L172)（第 172 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_workshop_ambience(raw: Any) -> dict[str, Any]](fantareal/workshop_logic.py#L201)（第 201 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_dynamic_scene(raw: Any) -> dict[str, Any] | None](fantareal/workshop_logic.py#L242)（第 242 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_creative_workshop(raw: Any) -> dict[str, Any]](fantareal/workshop_logic.py#L288)（第 288 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_workshop_state() -> dict[str, Any]](fantareal/workshop_logic.py#L309)（第 309 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_workshop_state(raw: Any) -> dict[str, Any]](fantareal/workshop_logic.py#L322)（第 322 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_workshop_stage(temp: Any, stage_limits: dict[str, int] | None = None) -> str](fantareal/workshop_logic.py#L351)（第 351 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_workshop_stage_label(stage: str) -> str](fantareal/workshop_logic.py#L361)（第 361 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 16 节 fantareal/worldbook_logic.py

### 一览

- `default_worldbook_store()` — 第 35 行
- `_clamp_int()` — 第 39 行
- `_normalize_yes_no_bool()` — 第 47 行
- `_normalize_match_mode()` — 第 61 行
- `_normalize_entry_type()` — 第 66 行
- `_normalize_activation_tags()` — 第 71 行
- `_sanitize_external_ref()` — 第 86 行
- `_normalize_group_operator()` — 第 98 行
- `_normalize_insertion_position()` — 第 107 行
- `_normalize_injection_role()` — 第 112 行
- `_normalize_injection_depth()` — 第 119 行
- `_normalize_injection_order()` — 第 123 行
- `_normalize_prompt_layer()` — 第 127 行
- `_normalize_recursion_depth()` — 第 132 行
- `sanitize_worldbook_settings()` — 第 136 行
- `sanitize_worldbook_entry()` — 第 220 行
- `sanitize_worldbook_store()` — 第 360 行
- `sanitize_worldbook()` — 第 383 行
- `normalize_match_text()` — 第 394 行
- `split_trigger_aliases()` — 第 400 行
- `keyword_matches_query()` — 第 406 行

### 函数详情

#### [default_worldbook_store() -> dict[str, Any]](fantareal/worldbook_logic.py#L35)（第 35 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_clamp_int(value: Any, minimum: int, maximum: int, default: int) -> int](fantareal/worldbook_logic.py#L39)（第 39 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_yes_no_bool(value: Any, default: bool) -> bool](fantareal/worldbook_logic.py#L47)（第 47 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_match_mode(value: Any, default: str) -> str](fantareal/worldbook_logic.py#L61)（第 61 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_entry_type(value: Any, default: str = keyword) -> str](fantareal/worldbook_logic.py#L66)（第 66 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_activation_tags(value: Any) -> list[str]](fantareal/worldbook_logic.py#L71)（第 71 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_sanitize_external_ref(value: Any) -> dict[str, str]](fantareal/worldbook_logic.py#L86)（第 86 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_group_operator(value: Any, default: str = and) -> str](fantareal/worldbook_logic.py#L98)（第 98 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_insertion_position(value: Any, default: str = after_char_defs) -> str](fantareal/worldbook_logic.py#L107)（第 107 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_injection_role(value: Any, default: str = system) -> str](fantareal/worldbook_logic.py#L112)（第 112 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_injection_depth(value: Any, default: int = 0) -> int](fantareal/worldbook_logic.py#L119)（第 119 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_injection_order(value: Any, default: int = 100) -> int](fantareal/worldbook_logic.py#L123)（第 123 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_prompt_layer(value: Any, default: str = follow_position) -> str](fantareal/worldbook_logic.py#L127)（第 127 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_recursion_depth(value: Any, default: int = 2) -> int](fantareal/worldbook_logic.py#L132)（第 132 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_worldbook_settings(raw: Any) -> dict[str, Any]](fantareal/worldbook_logic.py#L136)（第 136 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_worldbook_entry(raw: Any) -> dict[str, Any] | None](fantareal/worldbook_logic.py#L220)（第 220 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_worldbook_store(raw: Any) -> dict[str, Any]](fantareal/worldbook_logic.py#L360)（第 360 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_worldbook(raw: Any) -> dict[str, str]](fantareal/worldbook_logic.py#L383)（第 383 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_match_text(value: Any) -> str](fantareal/worldbook_logic.py#L394)（第 394 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [split_trigger_aliases(trigger: Any) -> list[str]](fantareal/worldbook_logic.py#L400)（第 400 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [keyword_matches_query(query_text: str, keyword: str) -> bool](fantareal/worldbook_logic.py#L406)（第 406 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 17 节 game/Tea Party/ai_instructions.py

### 一览

- `build_ai_system_prompt()` — 第 102 行
- `build_ai_user_message()` — 第 126 行

### 函数详情

#### [build_ai_system_prompt(persona: dict) -> str](game/Tea Party/ai_instructions.py#L102)（第 102 行）
构建 AI 对手的 system prompt：游戏规则 + 角色信息 + 响应格式
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_ai_user_message(sanitized_state: dict) -> str](game/Tea Party/ai_instructions.py#L126)（第 126 行）
构建给 AI 的 user message：当前游戏状态 + 要求做出决策
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 18 节 game/Tea Party/ai_opponent.py

### 一览

- `_parse_ai_response()` — 第 26 行
- `_fallback_decision()` — 第 89 行
- `request_ai_action()` — 第 102 行

### 函数详情

#### [_parse_ai_response(content: str) -> dict](game/Tea Party/ai_opponent.py#L26)（第 26 行）
从 LLM 响应文本中解析 DECISION 和 DIALOGUE
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_fallback_decision() -> dict](game/Tea Party/ai_opponent.py#L89)（第 89 行）
LLM 调用失败或解析失败时的随机 fallback
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [request_ai_action(sanitized_state: dict, persona: dict, llm_config: dict, request_json_func: Callable[..., Any]) -> dict](game/Tea Party/ai_opponent.py#L102)（第 102 行）
调用 LLM 获取 AI 对手的游戏决策
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 19 节 game/Tea Party/engine.py

### 一览

- **class PartyGame** — 第 58 行

- `_level_ammo()` — 第 38 行
- `_level_items_per_player()` — 第 47 行
- `no_ai_decision()` — 第 742 行
- `no_ai_reaction_dialogue()` — 第 810 行
- `get_session()` — 第 830 行
- `reset_session()` — 第 836 行

### 函数详情

#### [_level_ammo(level: int) -> tuple[int, int]](game/Tea Party/engine.py#L38)（第 38 行）
返回 (live_count, blank_count)
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_level_items_per_player(level: int) -> tuple[int, int]](game/Tea Party/engine.py#L47)（第 47 行）
返回每回合每个玩家获得的道具数 (min, max)
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [__init__(p1_name: str = 玩家1, p2_name: str = 玩家2, difficulty: str = normal, mode: GameMode = GameMode.CLASSIC, seed: Optional[int] = None)（嵌套在 PartyGame 内）](game/Tea Party/engine.py#L61)（第 61 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [current() -> PlayerState（嵌套在 PartyGame 内）](game/Tea Party/engine.py#L100)（第 100 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [opponent() -> PlayerState（嵌套在 PartyGame 内）](game/Tea Party/engine.py#L104)（第 104 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_other(player_index: int) -> PlayerState（嵌套在 PartyGame 内）](game/Tea Party/engine.py#L107)（第 107 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [start_new_level() -> ActionResult（嵌套在 PartyGame 内）](game/Tea Party/engine.py#L114)（第 114 行）
开始新一局：生成弹药、洗牌装填、分配道具
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_distribute_items() -> list[GameEvent]（嵌套在 PartyGame 内）](game/Tea Party/engine.py#L149)（第 149 行）
为双方随机分配道具。填入第一个 None 槽位
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_state() -> dict（嵌套在 PartyGame 内）](game/Tea Party/engine.py#L183)（第 183 行）
返回对前端可见的完整游戏状态（隐藏弹药顺序）
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_sanitized_state() -> dict（嵌套在 PartyGame 内）](game/Tea Party/engine.py#L203)（第 203 行）
返回对 AI 安全的状态（隐藏弹药顺序、hint 状态对对手隐藏）
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_battle_log() -> list[dict]（嵌套在 PartyGame 内）](game/Tea Party/engine.py#L243)（第 243 行）
返回对战日志
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_log_battle(description: str, round_type: str, player: int) -> None（嵌套在 PartyGame 内）](game/Tea Party/engine.py#L249)（第 249 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_should_hide_cannon() -> bool（嵌套在 PartyGame 内）](game/Tea Party/engine.py#L258)（第 258 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_map_to_original(cannon_idx: int) -> int（嵌套在 PartyGame 内）](game/Tea Party/engine.py#L261)（第 261 行）
将 cannon.rounds 索引映射到 _round_statuses 原始索引
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_compute_round_states() -> list[dict]（嵌套在 PartyGame 内）](game/Tea Party/engine.py#L271)（第 271 行）
计算子弹圆圈所需的每发弹药状态。只显示当前玩家自己的 hint
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_record_fired(orig_idx: int) -> None（嵌套在 PartyGame 内）](game/Tea Party/engine.py#L288)（第 288 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_record_ejected(orig_idx: int) -> None（嵌套在 PartyGame 内）](game/Tea Party/engine.py#L292)（第 292 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_record_hint(orig_idx: int, round_type: str, player_index: int) -> None（嵌套在 PartyGame 内）](game/Tea Party/engine.py#L296)（第 296 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [use_item(player_index: int, item_type_str: str, target_item: Optional[str] = None) -> ActionResult（嵌套在 PartyGame 内）](game/Tea Party/engine.py#L305)（第 305 行）
玩家使用道具。target_item：怪盗猫爪手套指定偷取的道具类型
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [discard_item(player_index: int, item_type_str: str) -> ActionResult（嵌套在 PartyGame 内）](game/Tea Party/engine.py#L351)（第 351 行）
丢弃道具（不触发效果）
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_apply_item_effect(player_index: int, item_type: ItemType, target_item: Optional[str] = None) -> list[GameEvent]（嵌套在 PartyGame 内）](game/Tea Party/engine.py#L384)（第 384 行）
执行道具效果，返回事件列表。target_item 仅 phantom_cat_gloves 使用
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_effect_candy_lens(player_index: int) -> list[GameEvent]（嵌套在 PartyGame 内）](game/Tea Party/engine.py#L423)（第 423 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_effect_bubble_soda() -> list[GameEvent]（嵌套在 PartyGame 内）](game/Tea Party/engine.py#L432)（第 432 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_effect_whisper_conch(player_index: int) -> list[GameEvent]（嵌套在 PartyGame 内）](game/Tea Party/engine.py#L449)（第 449 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_effect_miracle_wand() -> list[GameEvent]（嵌套在 PartyGame 内）](game/Tea Party/engine.py#L460)（第 460 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_effect_phantom_cat_gloves(player_index: int, target_item: Optional[str] = None) -> list[GameEvent]（嵌套在 PartyGame 内）](game/Tea Party/engine.py#L468)（第 468 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_effect_kiwi_juice(player_index: int) -> list[GameEvent]（嵌套在 PartyGame 内）](game/Tea Party/engine.py#L494)（第 494 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [shoot(player_index: int, target_str: str) -> ActionResult（嵌套在 PartyGame 内）](game/Tea Party/engine.py#L507)（第 507 行）
玩家开火
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [skip_turn(player_index: int) -> ActionResult（嵌套在 PartyGame 内）](game/Tea Party/engine.py#L578)（第 578 行）
超时跳过回合：不射击，直接切换回合
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_resolve_shot(player_index: int, target: Target, round_type: RoundType, events: list[GameEvent]) -> bool（嵌套在 PartyGame 内）](game/Tea Party/engine.py#L600)（第 600 行）
解析射击结果。返回 True 表示需要切换回合
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_advance_turn() -> list[GameEvent]（嵌套在 PartyGame 内）](game/Tea Party/engine.py#L647)（第 647 行）
推进回合到下一个玩家。处理跳过、空膛等逻辑
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_check_game_over() -> Optional[ActionResult]（嵌套在 PartyGame 内）](game/Tea Party/engine.py#L674)（第 674 行）
检查是否有人的气球归零。返回 ActionResult 或 None
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [no_ai_decision(sanitized_state: dict) -> dict](game/Tea Party/engine.py#L742)（第 742 行）
无AI模式的随机决策（不依赖 LLM）
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [no_ai_reaction_dialogue(event_type: str) -> str](game/Tea Party/engine.py#L810)（第 810 行）
根据事件类型返回预制反应对话
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_session() -> Optional[PartyGame]](game/Tea Party/engine.py#L830)（第 830 行）
获取当前游戏实例。无活跃游戏返回 None
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [reset_session(mode: str = classic, difficulty: str = normal, p1_name: str = 玩家, p2_name: str = 对手) -> PartyGame](game/Tea Party/engine.py#L836)（第 836 行）
创建新游戏并替换当前实例
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 20 节 game/Tea Party/models.py

### 一览

- **class RoundType** — 第 15 行
- **class Target** — 第 24 行
- **class ItemType** — 第 30 行
- **class GamePhase** — 第 71 行
- **class GameMode** — 第 76 行
- **class PlayerState** — 第 100 行
- **class CannonState** — 第 119 行
- **class GameEvent** — 第 155 行
- **class ActionResult** — 第 166 行
- **class ItemInfo** — 第 177 行
- **class BattleLogEntry** — 第 189 行

- `_action_result_to_dict()` — 第 199 行

### 函数详情

#### [label() -> str（嵌套在 RoundType 内）](game/Tea Party/models.py#L20)（第 20 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [label() -> str（嵌套在 ItemType 内）](game/Tea Party/models.py#L42)（第 42 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [description() -> str（嵌套在 ItemType 内）](game/Tea Party/models.py#L56)（第 56 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [to_dict() -> dict（嵌套在 PlayerState 内）](game/Tea Party/models.py#L108)（第 108 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [current_round() -> Optional[RoundType]（嵌套在 CannonState 内）](game/Tea Party/models.py#L125)（第 125 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [remaining_rounds() -> list[RoundType]（嵌套在 CannonState 内）](game/Tea Party/models.py#L131)（第 131 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [is_empty() -> bool（嵌套在 CannonState 内）](game/Tea Party/models.py#L135)（第 135 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [advance() -> None（嵌套在 CannonState 内）](game/Tea Party/models.py#L138)（第 138 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [to_dict() -> dict（嵌套在 CannonState 内）](game/Tea Party/models.py#L141)（第 141 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [of(event_type: str) -> GameEvent（嵌套在 GameEvent 内）](game/Tea Party/models.py#L161)（第 161 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [from_type(it: ItemType) -> ItemInfo（嵌套在 ItemInfo 内）](game/Tea Party/models.py#L184)（第 184 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_action_result_to_dict() -> dict](game/Tea Party/models.py#L199)（第 199 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 21 节 game/Tea Party/test_verify.py

### 一览

- `check()` — 第 11 行
- `pstate()` — 第 20 行
- `use()` — 第 27 行
- `shoot()` — 第 36 行

### 函数详情

#### [check(cond, msg)](game/Tea Party/test_verify.py#L11)（第 11 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [pstate(g)](game/Tea Party/test_verify.py#L20)（第 20 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [use(g, item_type, expect_ok = True)](game/Tea Party/test_verify.py#L27)（第 27 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [shoot(g, target, expect_ok = True)](game/Tea Party/test_verify.py#L36)（第 36 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 22 节 mods/card writer/app.py

### 一览

- **class CardWriterProject** (Pydantic BaseModel) — 第 281 行
  - 字段: `version: int`, `type: str`, `title: str`, `persona_card: dict[str, Any]`, `worldbook: dict[str, Any]`, `memory: dict[str, Any]` ... 共 8 个字段
- **class ExportPayload** (Pydantic BaseModel) — 第 292 行
  - 字段: `project: CardWriterProject`, `filename: str`, `target: str`
- **class CopilotSettingsPayload** (Pydantic BaseModel) — 第 298 行
  - 字段: `base_url: str`, `api_key: str`, `model: str`, `request_timeout: int`, `temperature: float`, `base_system_prompt: str` ... 共 10 个字段
- **class CopilotGeneratePayload** (Pydantic BaseModel) — 第 311 行
  - 字段: `project: CardWriterProject`, `module: str`, `prompt: str`, `follow_up: str`, `current_view: str`, `focus_hint: dict[str, Any]` ... 共 7 个字段
- **class CopilotGenerateResponse** (Pydantic BaseModel) — 第 321 行
  - 字段: `ok: bool`, `review_id: str`, `summary: str`, `prompt_used: str`, `current_view: str`, `base_revision: str` ... 共 8 个字段
- **class ProjectStore** — 第 339 行
- **class CardCompiler** — 第 431 行

- `get_resource_dir()` — 第 28 行
- `now_text()` — 第 511 行
- `read_json()` — 第 515 行
- `write_json()` — 第 524 行
- `clamp_float()` — 第 529 行
- `sanitize_copilot_settings()` — 第 537 行
- `get_copilot_settings()` — 第 555 行
- `save_copilot_settings()` — 第 559 行
- `sanitize_filename()` — 第 565 行
- `ensure_project_filename()` — 第 569 行
- `ensure_export_filename()` — 第 574 行
- `make_id()` — 第 579 行
- `create_empty_project()` — 第 583 行
- `split_tags()` — 第 587 行
- `as_bool()` — 第 593 行
- `as_int()` — 第 606 行
- `as_float()` — 第 613 行
- `normalize_text()` — 第 620 行
- `normalize_persona_single()` — 第 628 行
- `normalize_personas_map()` — 第 636 行
- `normalize_workshop_item()` — 第 652 行
- `normalize_creative_workshop()` — 第 675 行
- `normalize_persona_card()` — 第 684 行
- `normalize_copilot_view()` — 第 695 行
- `build_project_revision()` — 第 702 行
- `normalize_copilot_focus_hint()` — 第 707 行
- `build_copilot_prompt_text()` — 第 758 行
- `get_runtime_llm_config()` — 第 766 行
- `request_copilot_review()` — 第 785 行
- `build_copilot_candidate()` — 第 806 行
- `build_copilot_fingerprint()` — 第 832 行
- `normalize_copilot_target_ref()` — 第 843 行
- `get_persona_main_snapshot()` — 第 855 行
- `find_worldbook_entry()` — 第 860 行
- `find_memory_item()` — 第 868 行
- `find_preset_item()` — 第 876 行
- `build_default_candidate_target()` — 第 884 行
- `build_default_candidate_reason()` — 第 910 行
- `normalize_candidate_action()` — 第 916 行
- `normalize_copilot_candidates()` — 第 929 行
- `get_project_path_value()` — 第 942 行
- `is_allowed_json_patch_path()` — 第 961 行
- `should_keep_patch_value()` — 第 971 行
- `build_json_patch_candidate()` — 第 983 行
- `persona_replace_to_json_patch_candidates()` — 第 997 行
- `normalize_json_patch_candidate()` — 第 1021 行
- `normalize_single_copilot_candidate()` — 第 1044 行
- `build_copilot_review_summary()` — 第 1181 行
- `build_copilot_candidate_schema()` — 第 1195 行
- `build_card_writer_json_schema()` — 第 1215 行
- `truncate_preview_text()` — 第 1235 行
- `infer_persona_name()` — 第 1240 行
- `infer_persona_tags()` — 第 1262 行
- `build_fallback_persona_after()` — 第 1284 行
- `generate_copilot_fallback()` — 第 1311 行
- `build_copilot_module_prompt()` — 第 1352 行
- `build_copilot_system_prompt()` — 第 1362 行
- `build_copilot_user_payload()` — 第 1393 行
- `parse_llm_json_text()` — 第 1406 行
- `call_copilot_llm()` — 第 1420 行
- `build_copilot_api_url()` — 第 1454 行
- `build_copilot_headers()` — 第 1464 行
- `request_json_sync()` — 第 1476 行
- `normalize_worldbook_entry()` — 第 1502 行
- `normalize_worldbook()` — 第 1547 行
- `normalize_memory_item()` — 第 1565 行
- `normalize_memory()` — 第 1576 行
- `normalize_extra_prompt()` — 第 1582 行
- `normalize_modules()` — 第 1593 行
- `normalize_preset_item()` — 第 1603 行
- `normalize_preset()` — 第 1618 行
- `normalize_project()` — 第 1631 行
- `normalize_old_project()` — 第 1682 行
- `legacy_worldbook_to_entry()` — 第 1713 行
- `legacy_memory_to_item()` — 第 1745 行
- `legacy_preset_to_item()` — 第 1756 行
- `normalize_legacy_project()` — 第 1769 行
- `parse_basic()` — 第 1796 行
- `parse_personas()` — 第 1810 行
- `extract_section()` — 第 1836 行
- `looks_like_persona_card()` — 第 1846 行
- `looks_like_worldbook()` — 第 1850 行
- `looks_like_memory()` — 第 1854 行
- `looks_like_preset()` — 第 1858 行
- `project_from_payload()` — 第 1862 行
- `normalized_has_content()` — 第 1868 行
- `make_access_style()` — 第 1895 行
- `format_access_log()` — 第 1905 行
- `resolve_access_label()` — 第 1922 行
- `chinese_access_log()` — 第 1941 行
- `startup()` — 第 1963 行
- `index()` — 第 1968 行
- `list_projects()` — 第 1982 行
- `get_project()` — 第 1987 行
- `save_project()` — 第 1992 行
- `delete_project()` — 第 1997 行
- `get_autosave()` — 第 2003 行
- `save_autosave()` — 第 2008 行
- `get_workspace()` — 第 2013 行
- `save_workspace()` — 第 2018 行
- `clear_workspace()` — 第 2023 行
- `api_compile()` — 第 2028 行
- `api_validate()` — 第 2033 行
- `api_get_settings()` — 第 2041 行
- `api_save_settings()` — 第 2046 行
- `api_ai_generate()` — 第 2051 行
- `api_export()` — 第 2056 行
- `api_import_card()` — 第 2068 行

### 函数详情

#### [get_resource_dir() -> Path](mods/card writer/app.py#L28)（第 28 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [__init__(projects_dir: Path, autosaves_dir: Path, exports_dir: Path, workspace_path: Path) -> None（嵌套在 ProjectStore 内）](mods/card writer/app.py#L340)（第 340 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [ensure_dirs() -> None（嵌套在 ProjectStore 内）](mods/card writer/app.py#L346)（第 346 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [list_projects() -> list[dict[str, Any]]（嵌套在 ProjectStore 内）](mods/card writer/app.py#L352)（第 352 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [load_project(filename: str) -> dict[str, Any]（嵌套在 ProjectStore 内）](mods/card writer/app.py#L366)（第 366 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_project(filename: str, project: dict[str, Any]) -> dict[str, Any]（嵌套在 ProjectStore 内）](mods/card writer/app.py#L375)（第 375 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [delete_project(filename: str) -> None（嵌套在 ProjectStore 内）](mods/card writer/app.py#L382)（第 382 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [load_autosave() -> dict[str, Any]（嵌套在 ProjectStore 内）](mods/card writer/app.py#L387)（第 387 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_autosave(project: dict[str, Any]) -> dict[str, Any]（嵌套在 ProjectStore 内）](mods/card writer/app.py#L400)（第 400 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [load_workspace() -> dict[str, Any]（嵌套在 ProjectStore 内）](mods/card writer/app.py#L407)（第 407 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_workspace(project: dict[str, Any]) -> dict[str, Any]（嵌套在 ProjectStore 内）](mods/card writer/app.py#L413)（第 413 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clear_workspace() -> dict[str, Any]（嵌套在 ProjectStore 内）](mods/card writer/app.py#L419)（第 419 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [export_json(filename: str, payload: dict[str, Any]) -> dict[str, Any]（嵌套在 ProjectStore 内）](mods/card writer/app.py#L424)（第 424 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [compile(project: dict[str, Any]) -> dict[str, Any]（嵌套在 CardCompiler 内）](mods/card writer/app.py#L432)（第 432 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [generate_copilot_draft(payload: CopilotGeneratePayload) -> CopilotGenerateResponse（嵌套在 CardCompiler 内）](mods/card writer/app.py#L440)（第 440 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [export_payload(project: dict[str, Any], target: str) -> dict[str, Any]（嵌套在 CardCompiler 内）](mods/card writer/app.py#L468)（第 468 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [validate(project: dict[str, Any], card: dict[str, Any]) -> list[dict[str, Any]]（嵌套在 CardCompiler 内）](mods/card writer/app.py#L481)（第 481 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [import_payload(payload: dict[str, Any]) -> dict[str, Any]（嵌套在 CardCompiler 内）](mods/card writer/app.py#L507)（第 507 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [now_text() -> str](mods/card writer/app.py#L511)（第 511 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [read_json(path: Path, default: Any) -> Any](mods/card writer/app.py#L515)（第 515 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [write_json(path: Path, payload: Any) -> None](mods/card writer/app.py#L524)（第 524 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clamp_float(value: Any, minimum: float, maximum: float, default: float) -> float](mods/card writer/app.py#L529)（第 529 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_copilot_settings(raw: Any) -> dict[str, Any]](mods/card writer/app.py#L537)（第 537 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_copilot_settings() -> dict[str, Any]](mods/card writer/app.py#L555)（第 555 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_copilot_settings(payload: Any) -> dict[str, Any]](mods/card writer/app.py#L559)（第 559 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_filename(name: str) -> str](mods/card writer/app.py#L565)（第 565 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [ensure_project_filename(name: str) -> str](mods/card writer/app.py#L569)（第 569 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [ensure_export_filename(name: str) -> str](mods/card writer/app.py#L574)（第 574 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [make_id(prefix: str) -> str](mods/card writer/app.py#L579)（第 579 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [create_empty_project() -> dict[str, Any]](mods/card writer/app.py#L583)（第 583 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [split_tags(value: str | list[Any]) -> list[str]](mods/card writer/app.py#L587)（第 587 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [as_bool(value: Any, default: bool = False) -> bool](mods/card writer/app.py#L593)（第 593 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [as_int(value: Any, default: int = 0) -> int](mods/card writer/app.py#L606)（第 606 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [as_float(value: Any, default: float = 0.0) -> float](mods/card writer/app.py#L613)（第 613 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_text(value: Any) -> str](mods/card writer/app.py#L620)（第 620 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_persona_single(value: Any) -> dict[str, Any]](mods/card writer/app.py#L628)（第 628 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_personas_map(value: Any) -> dict[str, dict[str, Any]]](mods/card writer/app.py#L636)（第 636 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_workshop_item(item: Any, index: int) -> dict[str, Any]](mods/card writer/app.py#L652)（第 652 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_creative_workshop(value: Any) -> dict[str, Any]](mods/card writer/app.py#L675)（第 675 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_persona_card(value: Any) -> dict[str, Any]](mods/card writer/app.py#L684)（第 684 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_copilot_view(value: Any) -> str](mods/card writer/app.py#L695)（第 695 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_project_revision(project: dict[str, Any]) -> str](mods/card writer/app.py#L702)（第 702 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_copilot_focus_hint(raw: Any, project: dict[str, Any], current_view: str) -> dict[str, Any]](mods/card writer/app.py#L707)（第 707 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_copilot_prompt_text(prompt: Any, follow_up: Any) -> str](mods/card writer/app.py#L758)（第 758 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_runtime_llm_config() -> dict[str, Any]](mods/card writer/app.py#L766)（第 766 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [request_copilot_review() -> dict[str, Any]](mods/card writer/app.py#L785)（第 785 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_copilot_candidate() -> dict[str, Any]](mods/card writer/app.py#L806)（第 806 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_copilot_fingerprint(module: str, action: str, target: dict[str, Any], before: Any) -> str](mods/card writer/app.py#L832)（第 832 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_copilot_target_ref(module: str, action: str, raw: Any) -> dict[str, Any]](mods/card writer/app.py#L843)（第 843 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_persona_main_snapshot(project: dict[str, Any]) -> dict[str, Any]](mods/card writer/app.py#L855)（第 855 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [find_worldbook_entry(project: dict[str, Any], entry_id: str) -> tuple[int, dict[str, Any] | None]](mods/card writer/app.py#L860)（第 860 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [find_memory_item(project: dict[str, Any], item_id: str) -> tuple[int, dict[str, Any] | None]](mods/card writer/app.py#L868)（第 868 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [find_preset_item(project: dict[str, Any], item_id: str) -> tuple[int, dict[str, Any] | None]](mods/card writer/app.py#L876)（第 876 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_default_candidate_target(module_name: str, project: dict[str, Any], current_view: str, focus_hint: dict[str, Any]) -> dict[str, Any]](mods/card writer/app.py#L884)（第 884 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_default_candidate_reason(module_name: str, current_view: str) -> str](mods/card writer/app.py#L910)（第 910 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_candidate_action(module_name: str, action: Any) -> str](mods/card writer/app.py#L916)（第 916 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_copilot_candidates(raw_candidates: Any, project: dict[str, Any]) -> list[dict[str, Any]]](mods/card writer/app.py#L929)（第 929 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_project_path_value(project: dict[str, Any], path: str) -> Any](mods/card writer/app.py#L942)（第 942 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [is_allowed_json_patch_path(path: str) -> bool](mods/card writer/app.py#L961)（第 961 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [should_keep_patch_value(value: Any) -> bool](mods/card writer/app.py#L971)（第 971 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_json_patch_candidate(module_name: str, path: str, operation: str, before: Any, after: Any, label: str, reason: str) -> dict[str, Any] | None](mods/card writer/app.py#L983)（第 983 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [persona_replace_to_json_patch_candidates(raw: dict[str, Any], project: dict[str, Any], label: str, reason: str) -> list[dict[str, Any]]](mods/card writer/app.py#L997)（第 997 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_json_patch_candidate(raw: dict[str, Any], project: dict[str, Any], module_name: str, label: str, reason: str) -> dict[str, Any] | None](mods/card writer/app.py#L1021)（第 1021 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_single_copilot_candidate(raw: Any, project: dict[str, Any]) -> dict[str, Any] | list[dict[str, Any]] | None](mods/card writer/app.py#L1044)（第 1044 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_copilot_review_summary(candidates: list[dict[str, Any]], current_view: str) -> str](mods/card writer/app.py#L1181)（第 1181 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_copilot_candidate_schema() -> dict[str, Any]](mods/card writer/app.py#L1195)（第 1195 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_card_writer_json_schema() -> dict[str, Any]](mods/card writer/app.py#L1215)（第 1215 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [truncate_preview_text(value: Any, limit: int) -> str](mods/card writer/app.py#L1235)（第 1235 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [infer_persona_name(prompt_text: str) -> str](mods/card writer/app.py#L1240)（第 1240 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [infer_persona_tags(prompt_text: str, name: str) -> list[str]](mods/card writer/app.py#L1262)（第 1262 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_fallback_persona_after(prompt_text: str, project: dict[str, Any]) -> dict[str, Any]](mods/card writer/app.py#L1284)（第 1284 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [generate_copilot_fallback(prompt_text: str, current_view: str, focus_hint: dict[str, Any], project: dict[str, Any]) -> dict[str, Any]](mods/card writer/app.py#L1311)（第 1311 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_copilot_module_prompt(module_name: str, settings: dict[str, Any]) -> str](mods/card writer/app.py#L1352)（第 1352 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_copilot_system_prompt(current_view: str, focus_hint: dict[str, Any], settings: dict[str, Any]) -> str](mods/card writer/app.py#L1362)（第 1362 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_copilot_user_payload(prompt_text: str, focus_hint: dict[str, Any], project: dict[str, Any], project_revision: str, current_view: str) -> str](mods/card writer/app.py#L1393)（第 1393 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_llm_json_text(raw_text: str) -> dict[str, Any]](mods/card writer/app.py#L1406)（第 1406 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [call_copilot_llm() -> dict[str, Any]](mods/card writer/app.py#L1420)（第 1420 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_copilot_api_url(base_url: str, endpoint: str) -> str](mods/card writer/app.py#L1454)（第 1454 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_copilot_headers(api_key: str) -> dict[str, str]](mods/card writer/app.py#L1464)（第 1464 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [request_json_sync() -> dict[str, Any]](mods/card writer/app.py#L1476)（第 1476 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_worldbook_entry(value: Any, index: int) -> dict[str, Any]](mods/card writer/app.py#L1502)（第 1502 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_worldbook(value: Any) -> dict[str, Any]](mods/card writer/app.py#L1547)（第 1547 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_memory_item(value: Any, index: int) -> dict[str, Any]](mods/card writer/app.py#L1565)（第 1565 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_memory(value: Any) -> dict[str, Any]](mods/card writer/app.py#L1576)（第 1576 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_extra_prompt(value: Any, index: int) -> dict[str, Any]](mods/card writer/app.py#L1582)（第 1582 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_modules(value: Any) -> dict[str, bool]](mods/card writer/app.py#L1593)（第 1593 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_preset_item(value: Any, index: int) -> dict[str, Any]](mods/card writer/app.py#L1603)（第 1603 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_preset(value: Any) -> dict[str, Any]](mods/card writer/app.py#L1618)（第 1618 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_project(payload: Any) -> dict[str, Any]](mods/card writer/app.py#L1631)（第 1631 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_old_project(payload: dict[str, Any]) -> dict[str, Any]](mods/card writer/app.py#L1682)（第 1682 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [legacy_worldbook_to_entry(item: Any, index: int) -> dict[str, Any]](mods/card writer/app.py#L1713)（第 1713 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [legacy_memory_to_item(item: Any, index: int) -> dict[str, Any]](mods/card writer/app.py#L1745)（第 1745 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [legacy_preset_to_item(item: Any, index: int) -> dict[str, Any]](mods/card writer/app.py#L1756)（第 1756 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_legacy_project(payload: dict[str, Any]) -> dict[str, Any]](mods/card writer/app.py#L1769)（第 1769 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_basic(content: str) -> dict[str, Any]](mods/card writer/app.py#L1796)（第 1796 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_personas(content: str) -> list[dict[str, Any]]](mods/card writer/app.py#L1810)（第 1810 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [extract_section(body: str, label: str, next_labels: list[str]) -> str](mods/card writer/app.py#L1836)（第 1836 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [looks_like_persona_card(payload: dict[str, Any]) -> bool](mods/card writer/app.py#L1846)（第 1846 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [looks_like_worldbook(payload: dict[str, Any]) -> bool](mods/card writer/app.py#L1850)（第 1850 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [looks_like_memory(payload: dict[str, Any]) -> bool](mods/card writer/app.py#L1854)（第 1854 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [looks_like_preset(payload: dict[str, Any]) -> bool](mods/card writer/app.py#L1858)（第 1858 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [project_from_payload(payload: dict[str, Any]) -> dict[str, Any]](mods/card writer/app.py#L1862)（第 1862 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalized_has_content(project: dict[str, Any]) -> bool](mods/card writer/app.py#L1868)（第 1868 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [make_access_style(label: str, method: str, status_code: int) -> str](mods/card writer/app.py#L1895)（第 1895 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [format_access_log(label: str, method: str, status_code: int, mood: str) -> str](mods/card writer/app.py#L1905)（第 1905 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [resolve_access_label(method: str, path: str) -> str](mods/card writer/app.py#L1922)（第 1922 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [chinese_access_log(request: Request, call_next)](mods/card writer/app.py#L1941)（第 1941 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [startup() -> None](mods/card writer/app.py#L1963)（第 1963 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [index(request: Request)](mods/card writer/app.py#L1968)（第 1968 行）
GET / 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [list_projects() -> dict[str, Any]](mods/card writer/app.py#L1982)（第 1982 行）
GET /api/projects 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_project(filename: str) -> dict[str, Any]](mods/card writer/app.py#L1987)（第 1987 行）
GET /api/projects/{filename} 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_project(filename: str, payload: CardWriterProject) -> dict[str, Any]](mods/card writer/app.py#L1992)（第 1992 行）
POST /api/projects/{filename} 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [delete_project(filename: str) -> dict[str, Any]](mods/card writer/app.py#L1997)（第 1997 行）
DELETE /api/projects/{filename} 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_autosave() -> dict[str, Any]](mods/card writer/app.py#L2003)（第 2003 行）
GET /api/autosave 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_autosave(payload: CardWriterProject) -> dict[str, Any]](mods/card writer/app.py#L2008)（第 2008 行）
POST /api/autosave 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_workspace() -> dict[str, Any]](mods/card writer/app.py#L2013)（第 2013 行）
GET /api/workspace 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_workspace(payload: CardWriterProject) -> dict[str, Any]](mods/card writer/app.py#L2018)（第 2018 行）
POST /api/workspace 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clear_workspace() -> dict[str, Any]](mods/card writer/app.py#L2023)（第 2023 行）
DELETE /api/workspace 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_compile(payload: CardWriterProject) -> dict[str, Any]](mods/card writer/app.py#L2028)（第 2028 行）
POST /api/compile 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_validate(payload: CardWriterProject) -> dict[str, Any]](mods/card writer/app.py#L2033)（第 2033 行）
POST /api/validate 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_settings() -> dict[str, Any]](mods/card writer/app.py#L2041)（第 2041 行）
GET /api/settings 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_settings(payload: CopilotSettingsPayload) -> dict[str, Any]](mods/card writer/app.py#L2046)（第 2046 行）
POST /api/settings 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_ai_generate(payload: CopilotGeneratePayload) -> dict[str, Any]](mods/card writer/app.py#L2051)（第 2051 行）
POST /api/ai/generate 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export(payload: ExportPayload) -> Response](mods/card writer/app.py#L2056)（第 2056 行）
POST /api/export 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_import_card(payload: dict[str, Any]) -> dict[str, Any]](mods/card writer/app.py#L2068)（第 2068 行）
POST /api/import-card 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 23 节 mods/mobile-chat/app.py

### 一览

- **class SettingsPayload** (Pydantic BaseModel) — 第 379 行
  - 字段: `schema_version: int | None`, `enabled: bool | None`, `show_floating_button: bool | None`, `remember_position: bool | None`, `floating_position: dict[str, Any] | None`, `panel_position: dict[str, Any] | None` ... 共 30 个字段
- **class GroupCreatePayload** (Pydantic BaseModel) — 第 412 行
  - 字段: `name: str`, `description: str`, `members: list[dict[str, Any]]`, `allow_role_to_role_reply: bool | None`, `allow_auto_interject: bool | None`, `reply_count: str | None` ... 共 7 个字段
- **class GroupPatchPayload** (Pydantic BaseModel) — 第 422 行
  - 字段: `name: str | None`, `description: str | None`, `members: list[dict[str, Any]] | None`, `allow_role_to_role_reply: bool | None`, `allow_auto_interject: bool | None`, `reply_count: str | None` ... 共 7 个字段
- **class MessageCreatePayload** (Pydantic BaseModel) — 第 432 行
  - 字段: `content: str`, `type: str`
- **class GeneratePayload** (Pydantic BaseModel) — 第 437 行
  - 字段: `group_id: str`, `user_message: str`
- **class ContinuePayload** (Pydantic BaseModel) — 第 442 行
  - 字段: `group_id: str`
- **class RoleProfilePayload** (Pydantic BaseModel) — 第 446 行
  - 字段: `role_id: str | None`, `display_name: str`, `source: str | None`, `source_ref: str | None`, `aliases: list[Any] | None`, `avatar: str | None` ... 共 18 个字段
- **class RoleProfilePatchPayload** (Pydantic BaseModel) — 第 467 行
  - 字段: `display_name: str | None`, `source: str | None`, `source_ref: str | None`, `aliases: list[Any] | None`, `avatar: str | None`, `identity: str | None` ... 共 17 个字段
- **class RoleGeneratorPayload** (Pydantic BaseModel) — 第 487 行
  - 字段: `known_info: str | None`, `overall_request: str | None`, `real_name: str | None`, `nickname: str | None`, `identity: str | None`, `impression: str | None` ... 共 14 个字段
- **class RoleGeneratorSavePayload** (Pydantic BaseModel) — 第 504 行
  - 字段: `role: dict[str, Any] | None`, `roles: list[Any] | None`
- **class RoleEventExtractPayload** (Pydantic BaseModel) — 第 509 行
  - 字段: `channel_ids: list[Any] | None`, `limit: int | None`
- **class RoleChatExtractPayload** (Pydantic BaseModel) — 第 514 行
  - 字段: `limit: int | None`, `recent_messages: int | None`
- **class StickerManifestPayload** (Pydantic BaseModel) — 第 519 行
  - 字段: `stickers: Any`
- **class AutomationPayload** (Pydantic BaseModel) — 第 523 行
  - 字段: `enabled: bool | None`, `idle_seconds: int | None`, `interval_seconds: int | None`, `max_rounds_per_session: int | None`, `max_generations_per_hour: int | None`, `active_group_only: bool | None`
- **class AutomationTestPayload** (Pydantic BaseModel) — 第 532 行
  - 字段: `group_id: str`
- **class PromptBlocksPayload** (Pydantic BaseModel) — 第 536 行
  - 字段: `blocks: Any`
- **class AppRegistryPayload** (Pydantic BaseModel) — 第 540 行
  - 字段: `apps: Any`
- **class ChannelEventPayload** (Pydantic BaseModel) — 第 544 行
  - 字段: `title: str | None`, `content: str`, `event_type: str | None`, `author_id: str | None`, `author_name: str | None`, `tags: list[Any] | None` ... 共 7 个字段
- **class ChannelEventPatchPayload** (Pydantic BaseModel) — 第 554 行
  - 字段: `read: bool | None`
- **class ChannelSeedPayload** (Pydantic BaseModel) — 第 557 行
  - 字段: `channel_id: str`, `count: int | None`, `force: bool | None`
- **class ChannelInteractionPayload** (Pydantic BaseModel) — 第 563 行
  - 字段: `title: str | None`, `content: str`
- **class ChannelReplyPayload** (Pydantic BaseModel) — 第 568 行
  - 字段: `content: str`
- **class MailReplyPayload** (Pydantic BaseModel) — 第 572 行
  - 字段: `content: str`, `generate_reply: bool | None`
- **class MailOutgoingPayload** (Pydantic BaseModel) — 第 577 行
  - 字段: `recipient_id: str`, `title: str | None`, `content: str`, `generate_reply: bool | None`
- **class LiveMessagePayload** (Pydantic BaseModel) — 第 584 行
  - 字段: `content: str`
- **class WorkbenchRoleDraftPayload** (Pydantic BaseModel) — 第 588 行
  - 字段: `role_id: str | None`, `display_name: str | None`, `source: str | None`
- **class WorkbenchGeneratePayload** (Pydantic BaseModel) — 第 594 行
  - 字段: `scope: str`, `mode: str`, `channel_id: str | None`, `role_id: str | None`, `user_input: str | None`, `save: bool | None`
- **class PromptTestPayload** (Pydantic BaseModel) — 第 603 行
  - 字段: `scope: str`, `mode: str`, `channel_id: str | None`, `role_id: str | None`, `user_input: str | None`
- **class NotificationPatchPayload** (Pydantic BaseModel) — 第 611 行
  - 字段: `read: bool | None`
- **class PhoneCallPayload** (Pydantic BaseModel) — 第 615 行
  - 字段: `role_id: str`, `user_line: str | None`, `session_id: str | None`
- **class PhoneHangupPayload** (Pydantic BaseModel) — 第 621 行
  - 字段: `session_id: str`
- **class ModelListPayload** (Pydantic BaseModel) — 第 625 行
  - 字段: `base_url: str | None`, `api_key: str | None`, `request_timeout: int | None`

- `clone_default()` — 第 636 行
- `compact_text()` — 第 640 行
- `safe_url_host()` — 第 644 行
- `classify_mobile_error()` — 第 657 行
- `mobile_error_suggestions()` — 第 672 行
- `mobile_error_payload()` — 第 688 行
- `clean_multiline_text()` — 第 714 行
- `clamp_int()` — 第 720 行
- `clamp_float()` — 第 728 行
- `is_safe_sticker_filename()` — 第 736 行
- `is_safe_sticker_pack_id()` — 第 745 行
- `custom_sticker_packs()` — 第 752 行
- `custom_sticker_pack()` — 第 771 行
- `default_sticker_directory()` — 第 778 行
- `default_sticker_files()` — 第 782 行
- `custom_sticker_path()` — 第 794 行
- `custom_sticker_sort_key()` — 第 815 行
- `custom_sticker_files()` — 第 820 行
- `sticker_tags()` — 第 837 行
- `custom_sticker_manifest()` — 第 853 行
- `is_valid_sticker_id()` — 第 885 行
- `sticker_catalog()` — 第 895 行
- `sticker_pack_summaries()` — 第 942 行
- `sticker_manifest_rows()` — 第 970 行
- `sanitize_manifest_rows()` — 第 991 行
- `save_sticker_manifest()` — 第 1021 行
- `now_iso()` — 第 1038 行
- `local_today()` — 第 1042 行
- `local_today_iso()` — 第 1046 行
- `daily_weather_payload()` — 第 1050 行
- `daily_fortune_payload()` — 第 1074 行
- `weather_context_message()` — 第 1091 行
- `normalize_id()` — 第 1103 行
- `make_id()` — 第 1109 行
- `current_role_card_payload()` — 第 1113 行
- `current_mobile_card_uid()` — 第 1121 行
- `current_mobile_card_dir()` — 第 1138 行
- `card_groups_path()` — 第 1143 行
- `card_role_profiles_path()` — 第 1147 行
- `card_messages_dir()` — 第 1151 行
- `card_events_dir()` — 第 1155 行
- `card_notifications_path()` — 第 1159 行
- `card_phone_calls_path()` — 第 1163 行
- `card_generation_state_path()` — 第 1167 行
- `card_parser_diagnostics_path()` — 第 1171 行
- `_read_json_unlocked()` — 第 1175 行
- `read_json()` — 第 1184 行
- `_write_json_unlocked()` — 第 1189 行
- `write_json()` — 第 1203 行
- `ensure_runtime_data()` — 第 1208 行
- `sanitize_position()` — 第 1239 行
- `sanitize_background_filename()` — 第 1247 行
- `section_source()` — 第 1254 行
- `pick_section_value()` — 第 1259 行
- `sanitize_auto_behavior()` — 第 1267 行
- `sanitize_generation_control()` — 第 1280 行
- `generation_kind_scope()` — 第 1297 行
- `assert_generation_allowed()` — 第 1310 行
- `generation_control_payload()` — 第 1324 行
- `sanitize_channel_token_settings()` — 第 1332 行
- `sanitize_model_source()` — 第 1343 行
- `sanitize_api_config()` — 第 1347 行
- `redact_api_config()` — 第 1359 行
- `settings_public_payload()` — 第 1370 行
- `sanitize_custom_prompts()` — 第 1382 行
- `normalize_prompt_scope()` — 第 1387 行
- `normalize_prompt_mode()` — 第 1392 行
- `sanitize_world_theme()` — 第 1401 行
- `sanitize_prompt_settings()` — 第 1406 行
- `sanitize_settings()` — 第 1423 行
- `get_settings()` — 第 1531 行
- `sanitize_automation_state()` — 第 1539 行
- `get_automation_state()` — 第 1550 行
- `save_automation_state()` — 第 1558 行
- `update_auto_behavior()` — 第 1564 行
- `sanitize_prompt_block()` — 第 1575 行
- `sanitize_prompt_blocks()` — 第 1596 行
- `get_prompt_blocks()` — 第 1613 行
- `save_prompt_blocks()` — 第 1621 行
- `prompt_scope_catalog()` — 第 1627 行
- `prompt_blocks_for_scope()` — 第 1631 行
- `prompt_mode_for_settings()` — 第 1643 行
- `custom_prompt_for_scope()` — 第 1648 行
- `default_prompt_text()` — 第 1656 行
- `locked_prompt_contract_text()` — 第 1662 行
- `strip_locked_prompt_contract()` — 第 1667 行
- `editable_default_prompt_text()` — 第 1675 行
- `prompt_body_preview_text()` — 第 1680 行
- `world_theme_prompt_section()` — 第 1689 行
- `custom_prompt_user_section()` — 第 1694 行
- `apply_custom_prompt_to_user_text()` — 第 1709 行
- `assembled_prompt_text()` — 第 1716 行
- `channel_schema_catalog()` — 第 1736 行
- `prompt_preview_payload()` — 第 1805 行
- `sanitize_generation_state()` — 第 1858 行
- `get_generation_state()` — 第 1915 行
- `save_generation_state()` — 第 1923 行
- `active_job_age_seconds()` — 第 1929 行
- `prune_stale_generation_jobs()` — 第 1942 行
- `interrupted_generation_error()` — 第 1965 行
- `begin_generation_job()` — 第 1971 行
- `finish_generation_job()` — 第 1990 行
- `record_live_tick_diagnostic()` — 第 2008 行
- `merge_settings_update()` — 第 2030 行
- `safe_avatar()` — 第 2089 行
- `role_name_key()` — 第 2094 行
- `placeholder_role_name()` — 第 2099 行
- `sanitize_member()` — 第 2105 行
- `current_user_member()` — 第 2126 行
- `sanitize_aliases()` — 第 2140 行
- `split_compact_values()` — 第 2161 行
- `normalize_app_alias()` — 第 2181 行
- `sanitize_role_app_scope()` — 第 2200 行
- `sanitize_role_app_roles()` — 第 2214 行
- `role_app_allowed()` — 第 2231 行
- `role_app_usage()` — 第 2244 行
- `role_profiles_for_app()` — 第 2249 行
- `role_app_generation_policy()` — 第 2257 行
- `sanitize_sticker_preferences()` — 第 2282 行
- `sanitize_role_profile()` — 第 2294 行
- `get_role_profiles()` — 第 2332 行
- `save_role_profiles()` — 第 2344 行
- `role_generator_display_name()` — 第 2349 行
- `default_app_roles_for_profile()` — 第 2364 行
- `role_generator_notes()` — 第 2397 行
- `role_generator_profile()` — 第 2412 行
- `generate_role_profiles()` — 第 2474 行
- `unique_role_id()` — 第 2481 行
- `save_generated_role_profiles()` — 第 2492 行
- `decoded_metadata_value()` — 第 2514 行
- `clean_extracted_role_name()` — 第 2527 行
- `event_role_name_allowed()` — 第 2552 行
- `event_role_split_names()` — 第 2592 行
- `event_role_source_label()` — 第 2607 行
- `event_role_profile_from_candidate()` — 第 2620 行
- `extract_event_role_profiles()` — 第 2656 行
- `main_chat_existing_name_keys()` — 第 2734 行
- `iter_main_chat_messages()` — 第 2743 行
- `read_main_chat_conversation_payload()` — 第 2763 行
- `main_chat_message_text()` — 第 2774 行
- `main_chat_candidate_names()` — 第 2789 行
- `clean_main_story_text()` — 第 2810 行
- `summarize_main_story_messages()` — 第 2816 行
- `current_card_memory_items()` — 第 2830 行
- `main_story_context_payload()` — 第 2860 行
- `extract_main_chat_role_profiles()` — 第 2887 行
- `role_profile_to_member()` — 第 2936 行
- `merge_profile_update()` — 第 2946 行
- `available_role_members()` — 第 2978 行
- `profile_lookup()` — 第 2992 行
- `enriched_member_for_prompt()` — 第 2996 行
- `sanitize_members()` — 第 3020 行
- `summarize_persona()` — 第 3040 行
- `declared_persona_name()` — 第 3051 行
- `extract_current_card_roles()` — 第 3068 行
- `current_card_profiles()` — 第 3138 行
- `sync_current_card_profiles()` — 第 3159 行
- `import_group_members_to_profiles()` — 第 3174 行
- `validate_group_id()` — 第 3204 行
- `messages_path()` — 第 3211 行
- `sanitize_group()` — 第 3220 行
- `default_group()` — 第 3245 行
- `get_groups()` — 第 3288 行
- `save_groups()` — 第 3298 行
- `get_group_or_404()` — 第 3302 行
- `sanitize_message()` — 第 3310 行
- `get_messages()` — 第 3335 行
- `append_group_messages()` — 第 3343 行
- `group_with_last_message()` — 第 3357 行
- `sanitize_app_entry()` — 第 3365 行
- `sanitize_app_registry()` — 第 3385 行
- `get_app_registry()` — 第 3405 行
- `save_app_registry()` — 第 3414 行
- `sanitize_channel()` — 第 3420 行
- `sanitize_channels()` — 第 3441 行
- `get_channels()` — 第 3459 行
- `get_channel_or_404()` — 第 3468 行
- `channel_events_path()` — 第 3476 行
- `sanitize_event_tags()` — 第 3483 行
- `sanitize_event_metadata()` — 第 3502 行
- `date_only()` — 第 3521 行
- `calendar_date_only()` — 第 3533 行
- `normalize_author_type()` — 第 3545 行
- `sanitize_forum_replies()` — 第 3562 行
- `sanitize_mail_replies()` — 第 3590 行
- `sanitize_live_messages()` — 第 3620 行
- `sanitize_live_contributors()` — 第 3646 行
- `live_contributor_key()` — 第 3668 行
- `merge_live_contributors()` — 第 3672 行
- `live_metric_int()` — 第 3706 行
- `live_metric_text()` — 第 3728 行
- `next_live_metric()` — 第 3736 行
- `sanitize_channel_event()` — 第 3741 行
- `get_channel_events()` — 第 3797 行
- `append_channel_events()` — 第 3806 行
- `save_channel_events()` — 第 3817 行
- `update_channel_event()` — 第 3825 行
- `find_channel_event_or_404()` — 第 3845 行
- `summarize_mobile_context()` — 第 3853 行
- `summarize_mobile_seed_context()` — 第 3894 行
- `effective_channel_seed_count()` — 第 3931 行
- `build_channel_seed_messages()` — 第 3938 行
- `build_channel_seed_retry_messages()` — 第 3996 行
- `channel_seed_max_tokens()` — 第 4035 行
- `build_channel_interaction_messages()` — 第 4050 行
- `parse_channel_interaction_replies()` — 第 4090 行
- `generate_channel_replies()` — 第 4125 行
- `attach_generated_channel_replies()` — 第 4147 行
- `build_live_tick_messages()` — 第 4157 行
- `parse_live_tick()` — 第 4215 行
- `apply_live_tick()` — 第 4237 行
- `advance_live_event()` — 第 4264 行
- `build_mail_reply_messages()` — 第 4287 行
- `parse_mail_replies()` — 第 4324 行
- `generate_mail_reply()` — 第 4358 行
- `parse_channel_seed_events()` — 第 4377 行
- `is_reasoning_only_error()` — 第 4399 行
- `sanitize_notification()` — 第 4404 行
- `get_notifications()` — 第 4423 行
- `save_notifications()` — 第 4436 行
- `add_notification()` — 第 4442 行
- `notification_from_event()` — 第 4460 行
- `sanitize_phone_line()` — 第 4470 行
- `sanitize_phone_session()` — 第 4488 行
- `get_phone_sessions()` — 第 4509 行
- `save_phone_sessions()` — 第 4522 行
- `phone_role_candidates()` — 第 4528 行
- `get_phone_role_or_404()` — 第 4570 行
- `build_phone_call_messages()` — 第 4578 行
- `parse_phone_lines()` — 第 4609 行
- `user_message_for()` — 第 4641 行
- `read_route_forwarding_fallback()` — 第 4654 行
- `read_main_llm_config()` — 第 4675 行
- `read_mobile_llm_config()` — 第 4689 行
- `build_api_url()` — 第 4704 行
- `provider_strategy_for_config()` — 第 4714 行
- `should_request_low_reasoning()` — 第 4783 行
- `chat_model_extra_payload()` — 第 4788 行
- `should_bypass_route_forwarding()` — 第 4795 行
- `extract_model_ids()` — 第 4799 行
- `fetch_mobile_models()` — 第 4825 行
- `call_chat_model()` — 第 4860 行
- `system_prompt_text()` — 第 4925 行
- `sticker_prompt_catalog()` — 第 4942 行
- `build_mobile_model_messages()` — 第 4958 行
- `strip_thinking_sections()` — 第 5014 行
- `strip_json_fence()` — 第 5023 行
- `escape_json_string_newlines()` — 第 5029 行
- `json_text_candidates()` — 第 5053 行
- `loads_json_lenient_with_reason()` — 第 5071 行
- `loads_json_lenient()` — 第 5100 行
- `recover_json_array_items()` — 第 5105 行
- `parse_payload_shape()` — 第 5151 行
- `get_parser_diagnostics()` — 第 5161 行
- `record_parser_diagnostic()` — 第 5185 行
- `parse_model_json_output()` — 第 5202 行
- `first_ai_member()` — 第 5218 行
- `parse_model_mobile_messages()` — 第 5222 行
- `group_async_lock()` — 第 5283 行
- `index()` — 第 5290 行
- `chat_index()` — 第 5296 行
- `api_get_settings()` — 第 5302 行
- `api_get_background()` — 第 5315 行
- `api_upload_background()` — 第 5330 行
- `api_clear_background()` — 第 5354 行
- `api_get_stickers()` — 第 5366 行
- `api_get_sticker_image()` — 第 5371 行
- `api_admin_sticker_packs()` — 第 5379 行
- `api_admin_get_sticker_manifest()` — 第 5384 行
- `api_admin_save_sticker_manifest()` — 第 5389 行
- `api_admin_scan_sticker_pack()` — 第 5396 行
- `api_save_settings()` — 第 5402 行
- `api_admin_models()` — 第 5412 行
- `api_admin_automation()` — 第 5427 行
- `api_admin_patch_automation()` — 第 5439 行
- `api_admin_pause_automation()` — 第 5446 行
- `api_admin_test_automation()` — 第 5453 行
- `api_current_card_roles()` — 第 5463 行
- `api_get_available_roles()` — 第 5468 行
- `api_get_disabled_roles()` — 第 5473 行
- `api_restore_mobile_role()` — 第 5479 行
- `api_admin_roles()` — 第 5491 行
- `api_admin_role_app_pools()` — 第 5496 行
- `api_create_role()` — 第 5535 行
- `api_patch_role()` — 第 5549 行
- `api_disable_role()` — 第 5568 行
- `api_restore_role()` — 第 5580 行
- `api_delete_role()` — 第 5592 行
- `api_sync_current_card_roles()` — 第 5603 行
- `api_import_group_roles()` — 第 5608 行
- `api_role_generator_draft()` — 第 5613 行
- `api_admin_role_generator_draft()` — 第 5619 行
- `api_role_generator_extract_events()` — 第 5625 行
- `api_admin_role_generator_extract_events()` — 第 5631 行
- `api_role_generator_extract_chat()` — 第 5637 行
- `api_admin_role_generator_extract_chat()` — 第 5643 行
- `api_role_generator_save()` — 第 5649 行
- `api_admin_role_generator_save()` — 第 5656 行
- `api_get_groups()` — 第 5663 行
- `api_create_group()` — 第 5668 行
- `api_clear_groups()` — 第 5701 行
- `api_get_group()` — 第 5711 行
- `api_patch_group()` — 第 5716 行
- `api_delete_group()` — 第 5736 行
- `api_get_messages()` — 第 5749 行
- `api_post_message()` — 第 5754 行
- `api_delete_messages()` — 第 5770 行
- `api_generate()` — 第 5777 行
- `api_continue()` — 第 5844 行
- `model_status_deep()` — 第 5906 行
- `workbench_overview()` — 第 5922 行
- `role_draft_from_source()` — 第 5933 行
- `prompt_test_root_key()` — 第 5964 行
- `prompt_test_mock_raw()` — 第 5973 行
- `prompt_test_messages()` — 第 5979 行
- `redact_prompt_test_messages()` — 第 6020 行
- `run_prompt_test()` — 第 6028 行
- `build_workbench_mock_payload()` — 第 6083 行
- `workbench_channel_for_scope()` — 第 6105 行
- `run_workbench_generation()` — 第 6118 行
- `channel_event_admin_rows()` — 第 6193 行
- `notification_invalid_source_ids()` — 第 6222 行
- `admin_data_overview()` — 第 6237 行
- `clear_channel_test_events()` — 第 6269 行
- `clear_invalid_notifications()` — 第 6286 行
- `prune_empty_phone_sessions()` — 第 6294 行
- `prune_ended_phone_sessions()` — 第 6302 行
- `delete_phone_session()` — 第 6309 行
- `delete_channel_event()` — 第 6321 行
- `api_admin_workbench()` — 第 6335 行
- `api_admin_workbench_role_draft()` — 第 6340 行
- `api_admin_workbench_generate()` — 第 6345 行
- `api_admin_prompt_test()` — 第 6354 行
- `api_admin_provider_strategy()` — 第 6363 行
- `api_admin_prompt_blocks()` — 第 6369 行
- `api_admin_save_prompt_blocks()` — 第 6374 行
- `api_admin_reset_prompt_blocks()` — 第 6379 行
- `api_admin_prompt_preview()` — 第 6385 行
- `api_admin_channel_schemas()` — 第 6392 行
- `api_admin_generation_control()` — 第 6398 行
- `api_admin_save_generation_control()` — 第 6403 行
- `api_admin_generation_guard()` — 第 6412 行
- `api_admin_reset_generation_guard()` — 第 6417 行
- `api_admin_diagnostics()` — 第 6423 行
- `api_apps()` — 第 6428 行
- `api_admin_data_overview()` — 第 6434 行
- `api_admin_clear_channel_test_events()` — 第 6439 行
- `api_admin_notifications_read_all()` — 第 6444 行
- `api_admin_clear_invalid_notifications()` — 第 6453 行
- `api_admin_prune_empty_phone_sessions()` — 第 6458 行
- `api_admin_clear_all_channel_test_events()` — 第 6464 行
- `api_admin_delete_channel_event()` — 第 6470 行
- `api_admin_prune_ended_phone_sessions()` — 第 6475 行
- `api_admin_delete_phone_session()` — 第 6480 行
- `api_admin_apps()` — 第 6484 行
- `api_admin_save_apps()` — 第 6489 行
- `api_admin_reset_apps()` — 第 6494 行
- `api_channels()` — 第 6500 行
- `api_admin_channels()` — 第 6505 行
- `api_channel_events()` — 第 6510 行
- `api_create_channel_event()` — 第 6516 行
- `api_patch_channel_event()` — 第 6536 行
- `api_create_channel_interaction()` — 第 6556 行
- `api_reply_channel_event()` — 第 6591 行
- `api_reply_mail_event()` — 第 6628 行
- `api_create_outgoing_mail()` — 第 6675 行
- `api_add_live_message()` — 第 6739 行
- `api_advance_live_event()` — 第 6766 行
- `run_channel_seed()` — 第 6779 行
- `api_seed_channel()` — 第 6813 行
- `api_admin_seed_channel()` — 第 6823 行
- `api_notifications()` — 第 6836 行
- `api_patch_notification()` — 第 6842 行
- `api_notifications_read_all()` — 第 6858 行
- `api_phone_sessions()` — 第 6867 行
- `api_hangup_phone_session()` — 第 6872 行
- `api_phone_call()` — 第 6887 行
- `api_export()` — 第 6948 行
- `admin_model_status()` — 第 6972 行
- `admin_latest_error()` — 第 6987 行
- `admin_diagnostics()` — 第 7004 行
- `api_admin_summary()` — 第 7051 行

### 函数详情

#### [clone_default(value: Any) -> Any](mods/mobile-chat/app.py#L636)（第 636 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [compact_text(value: Any, limit: int = 500) -> str](mods/mobile-chat/app.py#L640)（第 640 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [safe_url_host(value: Any) -> str](mods/mobile-chat/app.py#L644)（第 644 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [classify_mobile_error(message: str, status_code: int = 0) -> str](mods/mobile-chat/app.py#L657)（第 657 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [mobile_error_suggestions(error_type: str) -> list[str]](mods/mobile-chat/app.py#L672)（第 672 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [mobile_error_payload(exc: HTTPException) -> dict[str, Any]](mods/mobile-chat/app.py#L688)（第 688 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clean_multiline_text(value: Any, limit: int = 12000) -> str](mods/mobile-chat/app.py#L714)（第 714 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clamp_int(value: Any, minimum: int, maximum: int, default: int) -> int](mods/mobile-chat/app.py#L720)（第 720 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clamp_float(value: Any, minimum: float, maximum: float, default: float) -> float](mods/mobile-chat/app.py#L728)（第 728 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [is_safe_sticker_filename(filename: Any) -> bool](mods/mobile-chat/app.py#L736)（第 736 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [is_safe_sticker_pack_id(pack_id: Any) -> bool](mods/mobile-chat/app.py#L745)（第 745 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [custom_sticker_packs() -> dict[str, dict[str, Any]]](mods/mobile-chat/app.py#L752)（第 752 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [custom_sticker_pack(pack_id: Any) -> dict[str, Any] | None](mods/mobile-chat/app.py#L771)（第 771 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_sticker_directory() -> Path](mods/mobile-chat/app.py#L778)（第 778 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_sticker_files() -> list[Path]](mods/mobile-chat/app.py#L782)（第 782 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [custom_sticker_path(pack_id: str, filename: str, require_exists: bool = True) -> Path | None](mods/mobile-chat/app.py#L794)（第 794 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [custom_sticker_sort_key(path: Path) -> tuple[int, int | str]](mods/mobile-chat/app.py#L815)（第 815 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [custom_sticker_files(pack_id: str) -> list[Path]](mods/mobile-chat/app.py#L820)（第 820 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sticker_tags(value: Any) -> list[str]](mods/mobile-chat/app.py#L837)（第 837 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [custom_sticker_manifest(pack_id: str) -> dict[str, dict[str, Any]]](mods/mobile-chat/app.py#L853)（第 853 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [is_valid_sticker_id(sticker_id: Any, require_exists: bool = False) -> bool](mods/mobile-chat/app.py#L885)（第 885 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sticker_catalog() -> list[dict[str, Any]]](mods/mobile-chat/app.py#L895)（第 895 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sticker_pack_summaries() -> list[dict[str, Any]]](mods/mobile-chat/app.py#L942)（第 942 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sticker_manifest_rows(pack_id: str) -> list[dict[str, Any]]](mods/mobile-chat/app.py#L970)（第 970 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_manifest_rows(value: Any) -> list[dict[str, Any]]](mods/mobile-chat/app.py#L991)（第 991 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_sticker_manifest(pack_id: str, rows: list[dict[str, Any]]) -> None](mods/mobile-chat/app.py#L1021)（第 1021 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [now_iso() -> str](mods/mobile-chat/app.py#L1038)（第 1038 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [local_today() -> date](mods/mobile-chat/app.py#L1042)（第 1042 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [local_today_iso() -> str](mods/mobile-chat/app.py#L1046)（第 1046 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [daily_weather_payload(target_date: date | None = None) -> dict[str, Any]](mods/mobile-chat/app.py#L1050)（第 1050 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [daily_fortune_payload(target_date: date | None = None) -> dict[str, Any]](mods/mobile-chat/app.py#L1074)（第 1074 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [weather_context_message() -> dict[str, str]](mods/mobile-chat/app.py#L1091)（第 1091 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_id(value: Any, fallback: str) -> str](mods/mobile-chat/app.py#L1103)（第 1103 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [make_id(prefix: str) -> str](mods/mobile-chat/app.py#L1109)（第 1109 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [current_role_card_payload() -> dict[str, Any]](mods/mobile-chat/app.py#L1113)（第 1113 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [current_mobile_card_uid() -> str](mods/mobile-chat/app.py#L1121)（第 1121 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [current_mobile_card_dir() -> Path](mods/mobile-chat/app.py#L1138)（第 1138 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [card_groups_path() -> Path](mods/mobile-chat/app.py#L1143)（第 1143 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [card_role_profiles_path() -> Path](mods/mobile-chat/app.py#L1147)（第 1147 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [card_messages_dir() -> Path](mods/mobile-chat/app.py#L1151)（第 1151 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [card_events_dir() -> Path](mods/mobile-chat/app.py#L1155)（第 1155 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [card_notifications_path() -> Path](mods/mobile-chat/app.py#L1159)（第 1159 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [card_phone_calls_path() -> Path](mods/mobile-chat/app.py#L1163)（第 1163 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [card_generation_state_path() -> Path](mods/mobile-chat/app.py#L1167)（第 1167 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [card_parser_diagnostics_path() -> Path](mods/mobile-chat/app.py#L1171)（第 1171 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_read_json_unlocked(path: Path, default: Any) -> Any](mods/mobile-chat/app.py#L1175)（第 1175 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [read_json(path: Path, default: Any) -> Any](mods/mobile-chat/app.py#L1184)（第 1184 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_write_json_unlocked(path: Path, payload: Any) -> None](mods/mobile-chat/app.py#L1189)（第 1189 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [write_json(path: Path, payload: Any) -> None](mods/mobile-chat/app.py#L1203)（第 1203 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [ensure_runtime_data() -> None](mods/mobile-chat/app.py#L1208)（第 1208 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_position(raw: Any, default: dict[str, int]) -> dict[str, int]](mods/mobile-chat/app.py#L1239)（第 1239 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_background_filename(value: Any) -> str](mods/mobile-chat/app.py#L1247)（第 1247 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [section_source(raw: dict[str, Any], key: str) -> dict[str, Any]](mods/mobile-chat/app.py#L1254)（第 1254 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [pick_section_value(source: dict[str, Any], section: dict[str, Any], key: str, default: Any) -> Any](mods/mobile-chat/app.py#L1259)（第 1259 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_auto_behavior(raw: Any, legacy_enabled: bool) -> dict[str, Any]](mods/mobile-chat/app.py#L1267)（第 1267 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_generation_control(raw: Any) -> dict[str, Any]](mods/mobile-chat/app.py#L1280)（第 1280 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [generation_kind_scope(kind: str) -> str](mods/mobile-chat/app.py#L1297)（第 1297 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [assert_generation_allowed(kind: str) -> None](mods/mobile-chat/app.py#L1310)（第 1310 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [generation_control_payload() -> dict[str, Any]](mods/mobile-chat/app.py#L1324)（第 1324 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_channel_token_settings(raw: Any) -> dict[str, dict[str, int]]](mods/mobile-chat/app.py#L1332)（第 1332 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_model_source(value: Any) -> str](mods/mobile-chat/app.py#L1343)（第 1343 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_api_config(raw: Any) -> dict[str, Any]](mods/mobile-chat/app.py#L1347)（第 1347 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [redact_api_config(config: dict[str, Any]) -> dict[str, Any]](mods/mobile-chat/app.py#L1359)（第 1359 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [settings_public_payload(settings: dict[str, Any]) -> dict[str, Any]](mods/mobile-chat/app.py#L1370)（第 1370 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_custom_prompts(raw: Any) -> dict[str, str]](mods/mobile-chat/app.py#L1382)（第 1382 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_prompt_scope(value: Any) -> str](mods/mobile-chat/app.py#L1387)（第 1387 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_prompt_mode(value: Any) -> str](mods/mobile-chat/app.py#L1392)（第 1392 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_world_theme(value: Any) -> str](mods/mobile-chat/app.py#L1401)（第 1401 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_prompt_settings(raw: Any) -> dict[str, Any]](mods/mobile-chat/app.py#L1406)（第 1406 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_settings(raw: Any) -> dict[str, Any]](mods/mobile-chat/app.py#L1423)（第 1423 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_settings() -> dict[str, Any]](mods/mobile-chat/app.py#L1531)（第 1531 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_automation_state(raw: Any) -> dict[str, Any]](mods/mobile-chat/app.py#L1539)（第 1539 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_automation_state() -> dict[str, Any]](mods/mobile-chat/app.py#L1550)（第 1550 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_automation_state(state: dict[str, Any]) -> dict[str, Any]](mods/mobile-chat/app.py#L1558)（第 1558 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [update_auto_behavior(updates: dict[str, Any]) -> dict[str, Any]](mods/mobile-chat/app.py#L1564)（第 1564 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_prompt_block(raw: Any, index: int = 0) -> dict[str, Any] | None](mods/mobile-chat/app.py#L1575)（第 1575 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_prompt_blocks(raw: Any) -> dict[str, Any]](mods/mobile-chat/app.py#L1596)（第 1596 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_prompt_blocks() -> dict[str, Any]](mods/mobile-chat/app.py#L1613)（第 1613 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_prompt_blocks(blocks: Any) -> dict[str, Any]](mods/mobile-chat/app.py#L1621)（第 1621 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [prompt_scope_catalog() -> list[dict[str, str]]](mods/mobile-chat/app.py#L1627)（第 1627 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [prompt_blocks_for_scope(scope: str) -> list[dict[str, Any]]](mods/mobile-chat/app.py#L1631)（第 1631 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [prompt_mode_for_settings(settings: dict[str, Any] | None = None) -> str](mods/mobile-chat/app.py#L1643)（第 1643 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [custom_prompt_for_scope(scope: str, settings: dict[str, Any] | None = None) -> str](mods/mobile-chat/app.py#L1648)（第 1648 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_prompt_text(scope: str) -> str](mods/mobile-chat/app.py#L1656)（第 1656 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [locked_prompt_contract_text(scope: str) -> str](mods/mobile-chat/app.py#L1662)（第 1662 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [strip_locked_prompt_contract(text: str, scope: str) -> str](mods/mobile-chat/app.py#L1667)（第 1667 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [editable_default_prompt_text(scope: str) -> str](mods/mobile-chat/app.py#L1675)（第 1675 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [prompt_body_preview_text(scope: str, settings: dict[str, Any] | None = None) -> str](mods/mobile-chat/app.py#L1680)（第 1680 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [world_theme_prompt_section(settings: dict[str, Any] | None = None) -> str](mods/mobile-chat/app.py#L1689)（第 1689 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [custom_prompt_user_section(scope: str, settings: dict[str, Any] | None = None) -> str](mods/mobile-chat/app.py#L1694)（第 1694 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [apply_custom_prompt_to_user_text(scope: str, user_text: str, settings: dict[str, Any] | None = None) -> str](mods/mobile-chat/app.py#L1709)（第 1709 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [assembled_prompt_text(scope: str) -> str](mods/mobile-chat/app.py#L1716)（第 1716 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [channel_schema_catalog() -> list[dict[str, Any]]](mods/mobile-chat/app.py#L1736)（第 1736 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [prompt_preview_payload(scope: str = group_chat, group_id: str) -> dict[str, Any]](mods/mobile-chat/app.py#L1805)（第 1805 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_generation_state(raw: Any) -> dict[str, Any]](mods/mobile-chat/app.py#L1858)（第 1858 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_generation_state() -> dict[str, Any]](mods/mobile-chat/app.py#L1915)（第 1915 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_generation_state(state: dict[str, Any]) -> dict[str, Any]](mods/mobile-chat/app.py#L1923)（第 1923 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [active_job_age_seconds(job: dict[str, Any]) -> float](mods/mobile-chat/app.py#L1929)（第 1929 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [prune_stale_generation_jobs(state: dict[str, Any]) -> dict[str, Any]](mods/mobile-chat/app.py#L1942)（第 1942 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [interrupted_generation_error(exc: BaseException | None = None) -> str](mods/mobile-chat/app.py#L1965)（第 1965 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [begin_generation_job(kind: str, target_id: str) -> dict[str, str]](mods/mobile-chat/app.py#L1971)（第 1971 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [finish_generation_job(job: dict[str, str], status: str, error: str) -> None](mods/mobile-chat/app.py#L1990)（第 1990 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [record_live_tick_diagnostic(channel: dict[str, Any], event: dict[str, Any]) -> None](mods/mobile-chat/app.py#L2008)（第 2008 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [merge_settings_update(current: dict[str, Any], updates: dict[str, Any]) -> dict[str, Any]](mods/mobile-chat/app.py#L2030)（第 2030 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [safe_avatar(value: Any) -> str](mods/mobile-chat/app.py#L2089)（第 2089 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [role_name_key(value: Any) -> str](mods/mobile-chat/app.py#L2094)（第 2094 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [placeholder_role_name(value: Any) -> bool](mods/mobile-chat/app.py#L2099)（第 2099 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_member(raw: Any, index: int = 0) -> dict[str, Any] | None](mods/mobile-chat/app.py#L2105)（第 2105 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [current_user_member() -> dict[str, str]](mods/mobile-chat/app.py#L2126)（第 2126 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_aliases(value: Any) -> list[str]](mods/mobile-chat/app.py#L2140)（第 2140 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [split_compact_values(value: Any) -> list[str]](mods/mobile-chat/app.py#L2161)（第 2161 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_app_alias(value: Any) -> str](mods/mobile-chat/app.py#L2181)（第 2181 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_role_app_scope(value: Any) -> list[str]](mods/mobile-chat/app.py#L2200)（第 2200 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_role_app_roles(value: Any) -> dict[str, list[str]]](mods/mobile-chat/app.py#L2214)（第 2214 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [role_app_allowed(profile: dict[str, Any], app_id: str) -> bool](mods/mobile-chat/app.py#L2231)（第 2231 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [role_app_usage(profile: dict[str, Any], app_id: str) -> list[str]](mods/mobile-chat/app.py#L2244)（第 2244 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [role_profiles_for_app(app_id: str) -> list[dict[str, Any]]](mods/mobile-chat/app.py#L2249)（第 2249 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [role_app_generation_policy(app_id: str) -> dict[str, Any]](mods/mobile-chat/app.py#L2257)（第 2257 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_sticker_preferences(value: Any) -> dict[str, Any]](mods/mobile-chat/app.py#L2282)（第 2282 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_role_profile(raw: Any, index: int = 0) -> dict[str, Any] | None](mods/mobile-chat/app.py#L2294)（第 2294 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_role_profiles() -> list[dict[str, Any]]](mods/mobile-chat/app.py#L2332)（第 2332 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_role_profiles(profiles: list[dict[str, Any]]) -> None](mods/mobile-chat/app.py#L2344)（第 2344 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [role_generator_display_name(raw: dict[str, Any], index: int, count: int) -> str](mods/mobile-chat/app.py#L2349)（第 2349 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_app_roles_for_profile(apps: list[str], raw: dict[str, Any] | None = None) -> dict[str, list[str]]](mods/mobile-chat/app.py#L2364)（第 2364 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [role_generator_notes(raw: dict[str, Any]) -> str](mods/mobile-chat/app.py#L2397)（第 2397 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [role_generator_profile(raw: dict[str, Any], index: int, count: int) -> dict[str, Any]](mods/mobile-chat/app.py#L2412)（第 2412 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [generate_role_profiles(payload: RoleGeneratorPayload) -> list[dict[str, Any]]](mods/mobile-chat/app.py#L2474)（第 2474 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [unique_role_id(base_role_id: str, existing_ids: set[str]) -> str](mods/mobile-chat/app.py#L2481)（第 2481 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_generated_role_profiles(raw_roles: list[Any]) -> list[dict[str, Any]]](mods/mobile-chat/app.py#L2492)（第 2492 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [decoded_metadata_value(value: Any) -> Any](mods/mobile-chat/app.py#L2514)（第 2514 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clean_extracted_role_name(value: Any) -> str](mods/mobile-chat/app.py#L2527)（第 2527 行）
Normalize role names extracted from loose JSON/list-looking text
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [event_role_name_allowed(name: str) -> bool](mods/mobile-chat/app.py#L2552)（第 2552 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [event_role_split_names(value: Any) -> list[str]](mods/mobile-chat/app.py#L2592)（第 2592 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [event_role_source_label(channel: dict[str, Any], kind: str) -> str](mods/mobile-chat/app.py#L2607)（第 2607 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [event_role_profile_from_candidate(candidate: dict[str, Any], index: int, source: str) -> dict[str, Any]](mods/mobile-chat/app.py#L2620)（第 2620 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [extract_event_role_profiles(payload: RoleEventExtractPayload | None = None) -> list[dict[str, Any]]](mods/mobile-chat/app.py#L2656)（第 2656 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：add_candidate

#### [add_candidate(channel: dict[str, Any], event: dict[str, Any], name: Any, kind: str, content: Any) -> None（嵌套在 extract_event_role_profiles 内）](mods/mobile-chat/app.py#L2667)（第 2667 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [main_chat_existing_name_keys() -> set[str]](mods/mobile-chat/app.py#L2734)（第 2734 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [iter_main_chat_messages(payload: Any) -> list[dict[str, Any]]](mods/mobile-chat/app.py#L2743)（第 2743 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：visit

#### [visit(value: Any) -> None（嵌套在 iter_main_chat_messages 内）](mods/mobile-chat/app.py#L2746)（第 2746 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [read_main_chat_conversation_payload() -> Any](mods/mobile-chat/app.py#L2763)（第 2763 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [main_chat_message_text(message: dict[str, Any]) -> str](mods/mobile-chat/app.py#L2774)（第 2774 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [main_chat_candidate_names(text: str) -> list[tuple[str, str]]](mods/mobile-chat/app.py#L2789)（第 2789 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：add

#### [add(name: Any, kind: str) -> None（嵌套在 main_chat_candidate_names 内）](mods/mobile-chat/app.py#L2793)（第 2793 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clean_main_story_text(value: Any, limit: int = 360) -> str](mods/mobile-chat/app.py#L2810)（第 2810 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [summarize_main_story_messages(messages: list[dict[str, Any]], limit: int = 620) -> str](mods/mobile-chat/app.py#L2816)（第 2816 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [current_card_memory_items(limit: int = 6) -> list[dict[str, str]]](mods/mobile-chat/app.py#L2830)（第 2830 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [main_story_context_payload(recent_limit: int = 8, memory_limit: int = 6) -> dict[str, Any]](mods/mobile-chat/app.py#L2860)（第 2860 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [extract_main_chat_role_profiles(payload: RoleChatExtractPayload | None = None) -> list[dict[str, Any]]](mods/mobile-chat/app.py#L2887)（第 2887 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：add_candidate

#### [add_candidate(message: dict[str, Any], name: str, kind: str, snippet_source: str) -> None（嵌套在 extract_main_chat_role_profiles 内）](mods/mobile-chat/app.py#L2896)（第 2896 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [role_profile_to_member(profile: dict[str, Any]) -> dict[str, str]](mods/mobile-chat/app.py#L2936)（第 2936 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [merge_profile_update(existing: dict[str, Any] | None, updates: dict[str, Any]) -> dict[str, Any]](mods/mobile-chat/app.py#L2946)（第 2946 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [available_role_members() -> dict[str, Any]](mods/mobile-chat/app.py#L2978)（第 2978 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [profile_lookup() -> dict[str, dict[str, Any]]](mods/mobile-chat/app.py#L2992)（第 2992 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [enriched_member_for_prompt(member: dict[str, Any], profiles: dict[str, dict[str, Any]]) -> dict[str, Any]](mods/mobile-chat/app.py#L2996)（第 2996 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_members(raw: Any) -> list[dict[str, str]]](mods/mobile-chat/app.py#L3020)（第 3020 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [summarize_persona(raw: dict[str, Any]) -> str](mods/mobile-chat/app.py#L3040)（第 3040 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [declared_persona_name(raw: dict[str, Any], fallback: Any) -> str](mods/mobile-chat/app.py#L3051)（第 3051 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [extract_current_card_roles() -> dict[str, Any]](mods/mobile-chat/app.py#L3068)（第 3068 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：upsert

#### [upsert(candidate: dict[str, Any], index: int) -> None（嵌套在 extract_current_card_roles 内）](mods/mobile-chat/app.py#L3077)（第 3077 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [current_card_profiles() -> list[dict[str, Any]]](mods/mobile-chat/app.py#L3138)（第 3138 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sync_current_card_profiles() -> list[dict[str, Any]]](mods/mobile-chat/app.py#L3159)（第 3159 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [import_group_members_to_profiles() -> list[dict[str, Any]]](mods/mobile-chat/app.py#L3174)（第 3174 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [validate_group_id(value: Any) -> str](mods/mobile-chat/app.py#L3204)（第 3204 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [messages_path(group_id: str) -> Path](mods/mobile-chat/app.py#L3211)（第 3211 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_group(raw: Any) -> dict[str, Any] | None](mods/mobile-chat/app.py#L3220)（第 3220 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_group() -> dict[str, Any]](mods/mobile-chat/app.py#L3245)（第 3245 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_groups() -> list[dict[str, Any]]](mods/mobile-chat/app.py#L3288)（第 3288 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_groups(groups: list[dict[str, Any]]) -> None](mods/mobile-chat/app.py#L3298)（第 3298 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_group_or_404(group_id: str) -> dict[str, Any]](mods/mobile-chat/app.py#L3302)（第 3302 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_message(raw: Any) -> dict[str, str] | None](mods/mobile-chat/app.py#L3310)（第 3310 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_messages(group_id: str) -> list[dict[str, str]]](mods/mobile-chat/app.py#L3335)（第 3335 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [append_group_messages(group_id: str, entries: list[dict[str, Any]]) -> list[dict[str, str]]](mods/mobile-chat/app.py#L3343)（第 3343 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [group_with_last_message(group: dict[str, Any]) -> dict[str, Any]](mods/mobile-chat/app.py#L3357)（第 3357 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_app_entry(raw: Any, index: int = 0) -> dict[str, Any] | None](mods/mobile-chat/app.py#L3365)（第 3365 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_app_registry(raw: Any) -> dict[str, Any]](mods/mobile-chat/app.py#L3385)（第 3385 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_app_registry() -> dict[str, Any]](mods/mobile-chat/app.py#L3405)（第 3405 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_app_registry(apps: Any) -> dict[str, Any]](mods/mobile-chat/app.py#L3414)（第 3414 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_channel(raw: Any, index: int = 0) -> dict[str, Any] | None](mods/mobile-chat/app.py#L3420)（第 3420 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_channels(raw: Any) -> dict[str, Any]](mods/mobile-chat/app.py#L3441)（第 3441 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_channels() -> list[dict[str, Any]]](mods/mobile-chat/app.py#L3459)（第 3459 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_channel_or_404(channel_id: str) -> dict[str, Any]](mods/mobile-chat/app.py#L3468)（第 3468 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [channel_events_path(channel_id: str) -> Path](mods/mobile-chat/app.py#L3476)（第 3476 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_event_tags(value: Any) -> list[str]](mods/mobile-chat/app.py#L3483)（第 3483 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_event_metadata(value: Any) -> dict[str, Any]](mods/mobile-chat/app.py#L3502)（第 3502 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [date_only(value: Any, fallback: str | None = None) -> str](mods/mobile-chat/app.py#L3521)（第 3521 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [calendar_date_only(value: Any, index: int = 0) -> str](mods/mobile-chat/app.py#L3533)（第 3533 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_author_type(value: Any, fallback: str = role) -> str](mods/mobile-chat/app.py#L3545)（第 3545 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_forum_replies(value: Any) -> list[dict[str, Any]]](mods/mobile-chat/app.py#L3562)（第 3562 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_mail_replies(value: Any) -> list[dict[str, Any]]](mods/mobile-chat/app.py#L3590)（第 3590 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_live_messages(value: Any) -> list[dict[str, Any]]](mods/mobile-chat/app.py#L3620)（第 3620 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_live_contributors(value: Any) -> list[dict[str, Any]]](mods/mobile-chat/app.py#L3646)（第 3646 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [live_contributor_key(value: Any) -> str](mods/mobile-chat/app.py#L3668)（第 3668 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [merge_live_contributors(existing: Any, incoming: Any) -> list[dict[str, Any]]](mods/mobile-chat/app.py#L3672)（第 3672 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [live_metric_int(value: Any, fallback: int = 0) -> int](mods/mobile-chat/app.py#L3706)（第 3706 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [live_metric_text(value: Any, fallback: int = 0) -> str](mods/mobile-chat/app.py#L3728)（第 3728 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [next_live_metric(value: Any, fallback: int, step: int) -> str](mods/mobile-chat/app.py#L3736)（第 3736 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_channel_event(raw: Any, channel: dict[str, Any], index: int = 0) -> dict[str, Any] | None](mods/mobile-chat/app.py#L3741)（第 3741 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_channel_events(channel_id: str) -> list[dict[str, Any]]](mods/mobile-chat/app.py#L3797)（第 3797 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [append_channel_events(channel_id: str, entries: list[dict[str, Any]]) -> list[dict[str, Any]]](mods/mobile-chat/app.py#L3806)（第 3806 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_channel_events(channel_id: str, events: list[dict[str, Any]]) -> list[dict[str, Any]]](mods/mobile-chat/app.py#L3817)（第 3817 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [update_channel_event(channel_id: str, event: dict[str, Any]) -> dict[str, Any]](mods/mobile-chat/app.py#L3825)（第 3825 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [find_channel_event_or_404(channel_id: str, event_id: str) -> dict[str, Any]](mods/mobile-chat/app.py#L3845)（第 3845 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [summarize_mobile_context(app_id: str) -> dict[str, Any]](mods/mobile-chat/app.py#L3853)（第 3853 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [summarize_mobile_seed_context(channel: dict[str, Any]) -> dict[str, Any]](mods/mobile-chat/app.py#L3894)（第 3894 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [effective_channel_seed_count(channel: dict[str, Any], count: Any = None) -> int](mods/mobile-chat/app.py#L3931)（第 3931 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_channel_seed_messages(channel: dict[str, Any], count: int) -> list[dict[str, str]]](mods/mobile-chat/app.py#L3938)（第 3938 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_channel_seed_retry_messages(channel: dict[str, Any], count: int) -> list[dict[str, str]]](mods/mobile-chat/app.py#L3996)（第 3996 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [channel_seed_max_tokens(channel: dict[str, Any], count: int) -> int](mods/mobile-chat/app.py#L4035)（第 4035 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_channel_interaction_messages(channel: dict[str, Any], event: dict[str, Any], user_content: str) -> list[dict[str, str]]](mods/mobile-chat/app.py#L4050)（第 4050 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_channel_interaction_replies(raw: str, channel: dict[str, Any], start_floor: int, count: int) -> list[dict[str, Any]]](mods/mobile-chat/app.py#L4090)（第 4090 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [generate_channel_replies(channel: dict[str, Any], event: dict[str, Any], user_content: str) -> list[dict[str, Any]]](mods/mobile-chat/app.py#L4125)（第 4125 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [attach_generated_channel_replies(channel: dict[str, Any], event: dict[str, Any], user_content: str) -> dict[str, Any]](mods/mobile-chat/app.py#L4147)（第 4147 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_live_tick_messages(channel: dict[str, Any], event: dict[str, Any]) -> list[dict[str, str]]](mods/mobile-chat/app.py#L4157)（第 4157 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_live_tick(raw: str, event: dict[str, Any]) -> dict[str, Any]](mods/mobile-chat/app.py#L4215)（第 4215 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [apply_live_tick(event: dict[str, Any], tick: dict[str, Any]) -> dict[str, Any]](mods/mobile-chat/app.py#L4237)（第 4237 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [advance_live_event(channel: dict[str, Any], event: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any] | None]](mods/mobile-chat/app.py#L4264)（第 4264 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_mail_reply_messages(event: dict[str, Any], user_content: str) -> list[dict[str, str]]](mods/mobile-chat/app.py#L4287)（第 4287 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_mail_replies(raw: str, event: dict[str, Any]) -> list[dict[str, Any]]](mods/mobile-chat/app.py#L4324)（第 4324 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [generate_mail_reply(event: dict[str, Any], user_content: str) -> list[dict[str, Any]]](mods/mobile-chat/app.py#L4358)（第 4358 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_channel_seed_events(raw: str, channel: dict[str, Any], count: int) -> list[dict[str, Any]]](mods/mobile-chat/app.py#L4377)（第 4377 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [is_reasoning_only_error(exc: HTTPException) -> bool](mods/mobile-chat/app.py#L4399)（第 4399 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_notification(raw: Any, index: int = 0) -> dict[str, Any] | None](mods/mobile-chat/app.py#L4404)（第 4404 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_notifications() -> list[dict[str, Any]]](mods/mobile-chat/app.py#L4423)（第 4423 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_notifications(items: list[dict[str, Any]]) -> list[dict[str, Any]]](mods/mobile-chat/app.py#L4436)（第 4436 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [add_notification(title: str, content: str) -> dict[str, Any] | None](mods/mobile-chat/app.py#L4442)（第 4442 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [notification_from_event(event: dict[str, Any]) -> dict[str, Any] | None](mods/mobile-chat/app.py#L4460)（第 4460 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_phone_line(raw: Any, index: int = 0) -> dict[str, Any] | None](mods/mobile-chat/app.py#L4470)（第 4470 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_phone_session(raw: Any, index: int = 0) -> dict[str, Any] | None](mods/mobile-chat/app.py#L4488)（第 4488 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_phone_sessions() -> list[dict[str, Any]]](mods/mobile-chat/app.py#L4509)（第 4509 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_phone_sessions(sessions: list[dict[str, Any]]) -> list[dict[str, Any]]](mods/mobile-chat/app.py#L4522)（第 4522 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [phone_role_candidates() -> list[dict[str, Any]]](mods/mobile-chat/app.py#L4528)（第 4528 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：add_role

#### [add_role(role_id: Any, name: Any, summary: Any, avatar: Any, chat_style: Any, status: Any) -> None（嵌套在 phone_role_candidates 内）](mods/mobile-chat/app.py#L4532)（第 4532 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_phone_role_or_404(role_id: str) -> dict[str, Any]](mods/mobile-chat/app.py#L4570)（第 4570 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_phone_call_messages(role: dict[str, Any], session: dict[str, Any], user_line: str) -> list[dict[str, str]]](mods/mobile-chat/app.py#L4578)（第 4578 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_phone_lines(raw: str, role: dict[str, Any]) -> tuple[list[dict[str, Any]], str]](mods/mobile-chat/app.py#L4609)（第 4609 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [user_message_for(group: dict[str, Any], content: str, message_type: str = text) -> dict[str, Any]](mods/mobile-chat/app.py#L4641)（第 4641 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [read_route_forwarding_fallback() -> dict[str, str]](mods/mobile-chat/app.py#L4654)（第 4654 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [read_main_llm_config() -> dict[str, Any]](mods/mobile-chat/app.py#L4675)（第 4675 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [read_mobile_llm_config() -> dict[str, Any]](mods/mobile-chat/app.py#L4689)（第 4689 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_api_url(base_url: str, endpoint: str) -> str](mods/mobile-chat/app.py#L4704)（第 4704 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [provider_strategy_for_config(config: dict[str, Any] | None = None) -> dict[str, Any]](mods/mobile-chat/app.py#L4714)（第 4714 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [should_request_low_reasoning(model: str) -> bool](mods/mobile-chat/app.py#L4783)（第 4783 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [chat_model_extra_payload(config: dict[str, Any]) -> dict[str, Any]](mods/mobile-chat/app.py#L4788)（第 4788 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [should_bypass_route_forwarding(config: dict[str, Any]) -> bool](mods/mobile-chat/app.py#L4795)（第 4795 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [extract_model_ids(payload: Any) -> list[str]](mods/mobile-chat/app.py#L4799)（第 4799 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [fetch_mobile_models(base_url: str, api_key: str, request_timeout: int) -> list[str]](mods/mobile-chat/app.py#L4825)（第 4825 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [call_chat_model(messages: list[dict[str, str]]) -> str](mods/mobile-chat/app.py#L4860)（第 4860 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [system_prompt_text() -> str](mods/mobile-chat/app.py#L4925)（第 4925 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sticker_prompt_catalog() -> list[dict[str, Any]]](mods/mobile-chat/app.py#L4942)（第 4942 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_mobile_model_messages(group: dict[str, Any], recent_messages: list[dict[str, str]], user_message: str) -> list[dict[str, str]]](mods/mobile-chat/app.py#L4958)（第 4958 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [strip_thinking_sections(text: str) -> str](mods/mobile-chat/app.py#L5014)（第 5014 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [strip_json_fence(text: str) -> str](mods/mobile-chat/app.py#L5023)（第 5023 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [escape_json_string_newlines(text: str) -> str](mods/mobile-chat/app.py#L5029)（第 5029 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [json_text_candidates(text: str) -> list[str]](mods/mobile-chat/app.py#L5053)（第 5053 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [loads_json_lenient_with_reason(text: str) -> tuple[Any, str]](mods/mobile-chat/app.py#L5071)（第 5071 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [loads_json_lenient(text: str) -> Any](mods/mobile-chat/app.py#L5100)（第 5100 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [recover_json_array_items(text: str, root_key: str) -> list[dict[str, Any]]](mods/mobile-chat/app.py#L5105)（第 5105 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_payload_shape(payload: Any, root_key: str) -> Any](mods/mobile-chat/app.py#L5151)（第 5151 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_parser_diagnostics() -> list[dict[str, Any]]](mods/mobile-chat/app.py#L5161)（第 5161 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [record_parser_diagnostic(scope: str, schema: str, target_id: str, reason: str, raw: str) -> None](mods/mobile-chat/app.py#L5185)（第 5185 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_model_json_output(raw: str) -> tuple[Any, str]](mods/mobile-chat/app.py#L5202)（第 5202 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [first_ai_member(group: dict[str, Any]) -> dict[str, str] | None](mods/mobile-chat/app.py#L5218)（第 5218 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_model_mobile_messages(raw: str, group: dict[str, Any]) -> list[dict[str, Any]]](mods/mobile-chat/app.py#L5222)（第 5222 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [group_async_lock(group_id: str) -> asyncio.Lock](mods/mobile-chat/app.py#L5283)（第 5283 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [index(request: Request) -> HTMLResponse](mods/mobile-chat/app.py#L5290)（第 5290 行）
GET / 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [chat_index(request: Request) -> HTMLResponse](mods/mobile-chat/app.py#L5296)（第 5296 行）
GET /chat 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_settings() -> dict[str, Any]](mods/mobile-chat/app.py#L5302)（第 5302 行）
GET /api/settings 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_background() -> FileResponse](mods/mobile-chat/app.py#L5315)（第 5315 行）
GET /api/background 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_upload_background(file: UploadFile = File(...)) -> dict[str, Any]](mods/mobile-chat/app.py#L5330)（第 5330 行）
POST /api/background 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_clear_background() -> dict[str, Any]](mods/mobile-chat/app.py#L5354)（第 5354 行）
DELETE /api/background 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_stickers() -> dict[str, Any]](mods/mobile-chat/app.py#L5366)（第 5366 行）
GET /api/stickers 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_sticker_image(pack_id: str, filename: str) -> FileResponse](mods/mobile-chat/app.py#L5371)（第 5371 行）
GET /api/stickers/{pack_id}/{filename} 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_sticker_packs() -> dict[str, Any]](mods/mobile-chat/app.py#L5379)（第 5379 行）
GET /api/admin/sticker-packs 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_get_sticker_manifest(pack_id: str) -> dict[str, Any]](mods/mobile-chat/app.py#L5384)（第 5384 行）
GET /api/admin/sticker-packs/{pack_id}/manifest 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_save_sticker_manifest(pack_id: str, payload: StickerManifestPayload) -> dict[str, Any]](mods/mobile-chat/app.py#L5389)（第 5389 行）
PUT /api/admin/sticker-packs/{pack_id}/manifest 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_scan_sticker_pack(pack_id: str) -> dict[str, Any]](mods/mobile-chat/app.py#L5396)（第 5396 行）
POST /api/admin/sticker-packs/{pack_id}/scan 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_settings(payload: SettingsPayload) -> dict[str, Any]](mods/mobile-chat/app.py#L5402)（第 5402 行）
POST /api/settings 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_models(payload: ModelListPayload | None = None) -> dict[str, Any]](mods/mobile-chat/app.py#L5412)（第 5412 行）
POST /api/admin/models 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_automation() -> dict[str, Any]](mods/mobile-chat/app.py#L5427)（第 5427 行）
GET /api/admin/automation 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_patch_automation(payload: AutomationPayload) -> dict[str, Any]](mods/mobile-chat/app.py#L5439)（第 5439 行）
PATCH /api/admin/automation 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_pause_automation() -> dict[str, Any]](mods/mobile-chat/app.py#L5446)（第 5446 行）
POST /api/admin/automation/pause-all 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_test_automation(payload: AutomationTestPayload) -> JSONResponse | dict[str, Any]](mods/mobile-chat/app.py#L5453)（第 5453 行）
POST /api/admin/automation/test-once 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_current_card_roles() -> dict[str, Any]](mods/mobile-chat/app.py#L5463)（第 5463 行）
GET /api/current-card-roles 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_available_roles() -> dict[str, Any]](mods/mobile-chat/app.py#L5468)（第 5468 行）
GET /api/roles 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_disabled_roles() -> dict[str, Any]](mods/mobile-chat/app.py#L5473)（第 5473 行）
GET /api/roles/disabled 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_restore_mobile_role(role_id: str) -> dict[str, Any]](mods/mobile-chat/app.py#L5479)（第 5479 行）
POST /api/roles/{role_id}/restore 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_roles() -> dict[str, Any]](mods/mobile-chat/app.py#L5491)（第 5491 行）
GET /api/admin/roles 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_role_app_pools() -> dict[str, Any]](mods/mobile-chat/app.py#L5496)（第 5496 行）
GET /api/admin/role-app-pools 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_create_role(payload: RoleProfilePayload) -> dict[str, Any]](mods/mobile-chat/app.py#L5535)（第 5535 行）
POST /api/admin/roles 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_patch_role(role_id: str, payload: RoleProfilePatchPayload) -> dict[str, Any]](mods/mobile-chat/app.py#L5549)（第 5549 行）
PATCH /api/admin/roles/{role_id} 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_disable_role(role_id: str) -> dict[str, Any]](mods/mobile-chat/app.py#L5568)（第 5568 行）
DELETE /api/admin/roles/{role_id} 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_restore_role(role_id: str) -> dict[str, Any]](mods/mobile-chat/app.py#L5580)（第 5580 行）
POST /api/admin/roles/{role_id}/restore 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_delete_role(role_id: str) -> dict[str, Any]](mods/mobile-chat/app.py#L5592)（第 5592 行）
DELETE /api/admin/roles/{role_id}/purge 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_sync_current_card_roles() -> dict[str, Any]](mods/mobile-chat/app.py#L5603)（第 5603 行）
POST /api/admin/roles/sync-current-card 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_import_group_roles() -> dict[str, Any]](mods/mobile-chat/app.py#L5608)（第 5608 行）
POST /api/admin/roles/import-from-groups 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_role_generator_draft(payload: RoleGeneratorPayload) -> dict[str, Any]](mods/mobile-chat/app.py#L5613)（第 5613 行）
POST /api/role-generator/draft 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_role_generator_draft(payload: RoleGeneratorPayload) -> dict[str, Any]](mods/mobile-chat/app.py#L5619)（第 5619 行）
POST /api/admin/role-generator/draft 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_role_generator_extract_events(payload: RoleEventExtractPayload | None = None) -> dict[str, Any]](mods/mobile-chat/app.py#L5625)（第 5625 行）
POST /api/role-generator/extract-events 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_role_generator_extract_events(payload: RoleEventExtractPayload | None = None) -> dict[str, Any]](mods/mobile-chat/app.py#L5631)（第 5631 行）
POST /api/admin/role-generator/extract-events 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_role_generator_extract_chat(payload: RoleChatExtractPayload | None = None) -> dict[str, Any]](mods/mobile-chat/app.py#L5637)（第 5637 行）
POST /api/role-generator/extract-chat 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_role_generator_extract_chat(payload: RoleChatExtractPayload | None = None) -> dict[str, Any]](mods/mobile-chat/app.py#L5643)（第 5643 行）
POST /api/admin/role-generator/extract-chat 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_role_generator_save(payload: RoleGeneratorSavePayload) -> dict[str, Any]](mods/mobile-chat/app.py#L5649)（第 5649 行）
POST /api/role-generator/save 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_role_generator_save(payload: RoleGeneratorSavePayload) -> dict[str, Any]](mods/mobile-chat/app.py#L5656)（第 5656 行）
POST /api/admin/role-generator/save 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_groups() -> dict[str, Any]](mods/mobile-chat/app.py#L5663)（第 5663 行）
GET /api/groups 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_create_group(payload: GroupCreatePayload) -> dict[str, Any]](mods/mobile-chat/app.py#L5668)（第 5668 行）
POST /api/groups 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_clear_groups() -> dict[str, Any]](mods/mobile-chat/app.py#L5701)（第 5701 行）
DELETE /api/groups 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_group(group_id: str) -> dict[str, Any]](mods/mobile-chat/app.py#L5711)（第 5711 行）
GET /api/groups/{group_id} 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_patch_group(group_id: str, payload: GroupPatchPayload) -> dict[str, Any]](mods/mobile-chat/app.py#L5716)（第 5716 行）
PATCH /api/groups/{group_id} 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_delete_group(group_id: str) -> dict[str, Any]](mods/mobile-chat/app.py#L5736)（第 5736 行）
DELETE /api/groups/{group_id} 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_messages(group_id: str) -> dict[str, Any]](mods/mobile-chat/app.py#L5749)（第 5749 行）
GET /api/groups/{group_id}/messages 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_post_message(group_id: str, payload: MessageCreatePayload) -> dict[str, Any]](mods/mobile-chat/app.py#L5754)（第 5754 行）
POST /api/groups/{group_id}/messages 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_delete_messages(group_id: str) -> dict[str, Any]](mods/mobile-chat/app.py#L5770)（第 5770 行）
DELETE /api/groups/{group_id}/messages 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_generate(payload: GeneratePayload) -> JSONResponse | dict[str, Any]](mods/mobile-chat/app.py#L5777)（第 5777 行）
POST /api/generate 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_continue(payload: ContinuePayload) -> JSONResponse | dict[str, Any]](mods/mobile-chat/app.py#L5844)（第 5844 行）
POST /api/continue 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [model_status_deep() -> dict[str, Any]](mods/mobile-chat/app.py#L5906)（第 5906 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [workbench_overview() -> dict[str, Any]](mods/mobile-chat/app.py#L5922)（第 5922 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [role_draft_from_source(payload: WorkbenchRoleDraftPayload) -> dict[str, Any]](mods/mobile-chat/app.py#L5933)（第 5933 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [prompt_test_root_key(scope: str) -> str](mods/mobile-chat/app.py#L5964)（第 5964 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [prompt_test_mock_raw(scope: str, user_input: str) -> str](mods/mobile-chat/app.py#L5973)（第 5973 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [prompt_test_messages(scope: str, user_input: str, channel_id: str, role_id: str) -> tuple[list[dict[str, str]], dict[str, Any]]](mods/mobile-chat/app.py#L5979)（第 5979 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [redact_prompt_test_messages(messages: list[dict[str, str]]) -> list[dict[str, str]]](mods/mobile-chat/app.py#L6020)（第 6020 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [run_prompt_test(payload: PromptTestPayload) -> dict[str, Any]](mods/mobile-chat/app.py#L6028)（第 6028 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_workbench_mock_payload(scope: str, user_input: str) -> dict[str, Any]](mods/mobile-chat/app.py#L6083)（第 6083 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [workbench_channel_for_scope(scope: str, channel_id: str) -> dict[str, Any]](mods/mobile-chat/app.py#L6105)（第 6105 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [run_workbench_generation(payload: WorkbenchGeneratePayload) -> dict[str, Any]](mods/mobile-chat/app.py#L6118)（第 6118 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [channel_event_admin_rows(limit: int = 8) -> dict[str, Any]](mods/mobile-chat/app.py#L6193)（第 6193 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [notification_invalid_source_ids() -> set[str]](mods/mobile-chat/app.py#L6222)（第 6222 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [admin_data_overview() -> dict[str, Any]](mods/mobile-chat/app.py#L6237)（第 6237 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clear_channel_test_events(channel_id: str) -> dict[str, Any]](mods/mobile-chat/app.py#L6269)（第 6269 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clear_invalid_notifications() -> dict[str, Any]](mods/mobile-chat/app.py#L6286)（第 6286 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [prune_empty_phone_sessions() -> dict[str, Any]](mods/mobile-chat/app.py#L6294)（第 6294 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [prune_ended_phone_sessions() -> dict[str, Any]](mods/mobile-chat/app.py#L6302)（第 6302 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [delete_phone_session(session_id: str) -> dict[str, Any]](mods/mobile-chat/app.py#L6309)（第 6309 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [delete_channel_event(channel_id: str, event_id: str) -> dict[str, Any]](mods/mobile-chat/app.py#L6321)（第 6321 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_workbench() -> dict[str, Any]](mods/mobile-chat/app.py#L6335)（第 6335 行）
GET /api/admin/workbench 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_workbench_role_draft(payload: WorkbenchRoleDraftPayload) -> dict[str, Any]](mods/mobile-chat/app.py#L6340)（第 6340 行）
POST /api/admin/workbench/role-draft 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_workbench_generate(payload: WorkbenchGeneratePayload) -> JSONResponse | dict[str, Any]](mods/mobile-chat/app.py#L6345)（第 6345 行）
POST /api/admin/workbench/generate 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_prompt_test(payload: PromptTestPayload) -> JSONResponse | dict[str, Any]](mods/mobile-chat/app.py#L6354)（第 6354 行）
POST /api/admin/prompt-test 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_provider_strategy() -> dict[str, Any]](mods/mobile-chat/app.py#L6363)（第 6363 行）
GET /api/admin/provider-strategy 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_prompt_blocks() -> dict[str, Any]](mods/mobile-chat/app.py#L6369)（第 6369 行）
GET /api/admin/prompt-blocks 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_save_prompt_blocks(payload: PromptBlocksPayload) -> dict[str, Any]](mods/mobile-chat/app.py#L6374)（第 6374 行）
PUT /api/admin/prompt-blocks 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_reset_prompt_blocks() -> dict[str, Any]](mods/mobile-chat/app.py#L6379)（第 6379 行）
POST /api/admin/prompt-blocks/reset 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_prompt_preview(scope: str = group_chat, group_id: str) -> dict[str, Any]](mods/mobile-chat/app.py#L6385)（第 6385 行）
GET /api/admin/prompt-preview 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_channel_schemas() -> dict[str, Any]](mods/mobile-chat/app.py#L6392)（第 6392 行）
GET /api/admin/channel-schemas 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_generation_control() -> dict[str, Any]](mods/mobile-chat/app.py#L6398)（第 6398 行）
GET /api/admin/generation-control 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_save_generation_control(payload: dict[str, Any]) -> dict[str, Any]](mods/mobile-chat/app.py#L6403)（第 6403 行）
PUT /api/admin/generation-control 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_generation_guard() -> dict[str, Any]](mods/mobile-chat/app.py#L6412)（第 6412 行）
GET /api/admin/generation-guard 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_reset_generation_guard() -> dict[str, Any]](mods/mobile-chat/app.py#L6417)（第 6417 行）
POST /api/admin/generation-guard/reset 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_diagnostics() -> dict[str, Any]](mods/mobile-chat/app.py#L6423)（第 6423 行）
GET /api/admin/diagnostics 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_apps() -> dict[str, Any]](mods/mobile-chat/app.py#L6428)（第 6428 行）
GET /api/apps 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_data_overview() -> dict[str, Any]](mods/mobile-chat/app.py#L6434)（第 6434 行）
GET /api/admin/data-overview 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_clear_channel_test_events(channel_id: str) -> dict[str, Any]](mods/mobile-chat/app.py#L6439)（第 6439 行）
POST /api/admin/data/channels/{channel_id}/clear-test-events 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_notifications_read_all() -> dict[str, Any]](mods/mobile-chat/app.py#L6444)（第 6444 行）
POST /api/admin/data/notifications/read-all 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_clear_invalid_notifications() -> dict[str, Any]](mods/mobile-chat/app.py#L6453)（第 6453 行）
POST /api/admin/data/notifications/clear-invalid 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_prune_empty_phone_sessions() -> dict[str, Any]](mods/mobile-chat/app.py#L6458)（第 6458 行）
POST /api/admin/data/phone/prune-empty 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_clear_all_channel_test_events() -> dict[str, Any]](mods/mobile-chat/app.py#L6464)（第 6464 行）
POST /api/admin/data/channels/clear-test-events 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_delete_channel_event(channel_id: str, event_id: str) -> dict[str, Any]](mods/mobile-chat/app.py#L6470)（第 6470 行）
DELETE /api/admin/data/channels/{channel_id}/events/{event_id} 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_prune_ended_phone_sessions() -> dict[str, Any]](mods/mobile-chat/app.py#L6475)（第 6475 行）
POST /api/admin/data/phone/prune-ended 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_delete_phone_session(session_id: str) -> dict[str, Any]](mods/mobile-chat/app.py#L6480)（第 6480 行）
DELETE /api/admin/data/phone/sessions/{session_id} 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_apps() -> dict[str, Any]](mods/mobile-chat/app.py#L6484)（第 6484 行）
GET /api/admin/apps 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_save_apps(payload: AppRegistryPayload) -> dict[str, Any]](mods/mobile-chat/app.py#L6489)（第 6489 行）
PUT /api/admin/apps 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_reset_apps() -> dict[str, Any]](mods/mobile-chat/app.py#L6494)（第 6494 行）
POST /api/admin/apps/reset 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_channels() -> dict[str, Any]](mods/mobile-chat/app.py#L6500)（第 6500 行）
GET /api/channels 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_channels() -> dict[str, Any]](mods/mobile-chat/app.py#L6505)（第 6505 行）
GET /api/admin/channels 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_channel_events(channel_id: str) -> dict[str, Any]](mods/mobile-chat/app.py#L6510)（第 6510 行）
GET /api/channels/{channel_id}/events 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_create_channel_event(channel_id: str, payload: ChannelEventPayload) -> dict[str, Any]](mods/mobile-chat/app.py#L6516)（第 6516 行）
POST /api/channels/{channel_id}/events 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_patch_channel_event(channel_id: str, event_id: str, payload: ChannelEventPatchPayload) -> dict[str, Any]](mods/mobile-chat/app.py#L6536)（第 6536 行）
PATCH /api/channels/{channel_id}/events/{event_id} 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_create_channel_interaction(channel_id: str, payload: ChannelInteractionPayload) -> JSONResponse | dict[str, Any]](mods/mobile-chat/app.py#L6556)（第 6556 行）
POST /api/channels/{channel_id}/interactions 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_reply_channel_event(channel_id: str, event_id: str, payload: ChannelReplyPayload) -> JSONResponse | dict[str, Any]](mods/mobile-chat/app.py#L6591)（第 6591 行）
POST /api/channels/{channel_id}/events/{event_id}/replies 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_reply_mail_event(channel_id: str, event_id: str, payload: MailReplyPayload) -> JSONResponse | dict[str, Any]](mods/mobile-chat/app.py#L6628)（第 6628 行）
POST /api/channels/{channel_id}/events/{event_id}/mail-replies 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_create_outgoing_mail(channel_id: str, payload: MailOutgoingPayload) -> JSONResponse | dict[str, Any]](mods/mobile-chat/app.py#L6675)（第 6675 行）
POST /api/channels/{channel_id}/outgoing-mails 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_add_live_message(channel_id: str, event_id: str, payload: LiveMessagePayload) -> dict[str, Any]](mods/mobile-chat/app.py#L6739)（第 6739 行）
POST /api/channels/{channel_id}/events/{event_id}/live-messages 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_advance_live_event(channel_id: str, event_id: str) -> JSONResponse | dict[str, Any]](mods/mobile-chat/app.py#L6766)（第 6766 行）
POST /api/channels/{channel_id}/events/{event_id}/live-tick 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [run_channel_seed(channel: dict[str, Any], count: int) -> dict[str, Any]](mods/mobile-chat/app.py#L6779)（第 6779 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_seed_channel(channel_id: str, payload: ChannelSeedPayload | None = None) -> JSONResponse | dict[str, Any]](mods/mobile-chat/app.py#L6813)（第 6813 行）
POST /api/channels/{channel_id}/seed 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_seed_channel(payload: ChannelSeedPayload) -> JSONResponse | dict[str, Any]](mods/mobile-chat/app.py#L6823)（第 6823 行）
POST /api/admin/seed-channel 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_notifications() -> dict[str, Any]](mods/mobile-chat/app.py#L6836)（第 6836 行）
GET /api/notifications 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_patch_notification(notification_id: str, payload: NotificationPatchPayload) -> dict[str, Any]](mods/mobile-chat/app.py#L6842)（第 6842 行）
PATCH /api/notifications/{notification_id} 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_notifications_read_all() -> dict[str, Any]](mods/mobile-chat/app.py#L6858)（第 6858 行）
POST /api/notifications/read-all 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_phone_sessions() -> dict[str, Any]](mods/mobile-chat/app.py#L6867)（第 6867 行）
GET /api/phone/sessions 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_hangup_phone_session(session_id: str) -> dict[str, Any]](mods/mobile-chat/app.py#L6872)（第 6872 行）
POST /api/phone/sessions/{session_id}/hangup 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_phone_call(payload: PhoneCallPayload) -> JSONResponse | dict[str, Any]](mods/mobile-chat/app.py#L6887)（第 6887 行）
POST /api/phone/call 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export() -> JSONResponse](mods/mobile-chat/app.py#L6948)（第 6948 行）
GET /api/export 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [admin_model_status() -> dict[str, Any]](mods/mobile-chat/app.py#L6972)（第 6972 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [admin_latest_error(groups: list[dict[str, Any]]) -> dict[str, str] | None](mods/mobile-chat/app.py#L6987)（第 6987 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [admin_diagnostics() -> dict[str, Any]](mods/mobile-chat/app.py#L7004)（第 7004 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_admin_summary() -> dict[str, Any]](mods/mobile-chat/app.py#L7051)（第 7051 行）
GET /api/admin/summary 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 24 节 mods/soul weaver/app.py

### 一览

- `get_resource_dir()` — 第 22 行
- `ensure_data_files()` — 第 447 行
- `read_json()` — 第 455 行
- `write_json()` — 第 464 行
- `clamp_float()` — 第 469 行
- `clamp_int()` — 第 477 行
- `parse_positive_int()` — 第 485 行
- `sanitize_settings()` — 第 503 行
- `normalize_speaker_name()` — 第 516 行
- `normalize_target_character()` — 第 529 行
- `sanitize_filename()` — 第 537 行
- `unique_path()` — 第 544 行
- `parse_script_line()` — 第 556 行
- `entry_to_script_line()` — 第 564 行
- `summarize_chunk()` — 第 570 行
- `build_entry_chunks()` — 第 579 行
- `build_speaker_chunks()` — 第 634 行
- `summarize_speaker_chunks()` — 第 659 行
- `build_text_chunks()` — 第 666 行
- `parse_script_entries()` — 第 686 行
- `extract_character_lines()` — 第 751 行
- `extract_character_chunks()` — 第 766 行
- `get_settings()` — 第 778 行
- `save_settings()` — 第 782 行
- `request_settings()` — 第 796 行
- `get_drafts()` — 第 805 行
- `save_draft()` — 第 810 行
- `build_api_url()` — 第 817 行
- `build_headers()` — 第 826 行
- `get_wbmaker_module()` — 第 833 行
- `build_wbmaker_settings()` — 第 848 行
- `generate_worldbook_with_wbmaker()` — 第 868 行
- `merge_worldbook_partials_with_wbmaker()` — 第 885 行
- `extract_json_text()` — 第 903 行
- `try_parse_json()` — 第 922 行
- `split_text()` — 第 933 行
- `request_chat_completion()` — 第 954 行
- `generate_with_segments()` — 第 992 行
- `normalize_role_card()` — 第 1070 行
- `normalize_single_preset()` — 第 1155 行
- `normalize_preset()` — 第 1249 行
- `normalize_memories()` — 第 1278 行
- `normalize_worldbook()` — 第 1292 行
- `startup_event()` — 第 1344 行
- `index()` — 第 1349 行
- `api_get_settings()` — 第 1366 行
- `api_save_settings()` — 第 1372 行
- `api_get_drafts()` — 第 1378 行
- `api_parse_script()` — 第 1383 行
- `api_probe_models()` — 第 1437 行
- `api_generate_role_card()` — 第 1476 行
- `api_generate_memory()` — 第 1514 行
- `api_generate_plot()` — 第 1552 行
- `api_generate_preset()` — 第 1588 行
- `api_generate_worldbook()` — 第 1626 行
- `task_system_prompt()` — 第 1659 行
- `task_draft_type()` — 第 1672 行
- `normalize_task_result()` — 第 1682 行
- `build_chunk_user()` — 第 1694 行
- `build_merge_user()` — 第 1718 行
- `api_generate_chunk()` — 第 1733 行
- `api_generate_merge()` — 第 1777 行
- `_proxy_import()` — 第 1848 行
- `api_import_card()` — 第 1860 行
- `api_import_preset()` — 第 1873 行
- `api_import_memories()` — 第 1885 行
- `api_import_worldbook()` — 第 1896 行
- `api_export_soul()` — 第 1909 行
- `api_export_soul_local()` — 第 1964 行

### 函数详情

#### [get_resource_dir() -> Path](mods/soul weaver/app.py#L22)（第 22 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [ensure_data_files() -> None](mods/soul weaver/app.py#L447)（第 447 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [read_json(path: Path, default: Any) -> Any](mods/soul weaver/app.py#L455)（第 455 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [write_json(path: Path, payload: Any) -> None](mods/soul weaver/app.py#L464)（第 464 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clamp_float(value: Any, minimum: float, maximum: float, default: float) -> float](mods/soul weaver/app.py#L469)（第 469 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clamp_int(value: Any, minimum: int, maximum: int, default: int) -> int](mods/soul weaver/app.py#L477)（第 477 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_positive_int(value: Any, default: int = 0) -> int](mods/soul weaver/app.py#L485)（第 485 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_settings(raw: Any) -> dict[str, Any]](mods/soul weaver/app.py#L503)（第 503 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_speaker_name(value: Any) -> str](mods/soul weaver/app.py#L516)（第 516 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_target_character(value: Any) -> str](mods/soul weaver/app.py#L529)（第 529 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_filename(value: Any, fallback: str = yusheng) -> str](mods/soul weaver/app.py#L537)（第 537 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [unique_path(path: Path) -> Path](mods/soul weaver/app.py#L544)（第 544 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_script_line(line: str) -> tuple[str, str] | None](mods/soul weaver/app.py#L556)（第 556 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [entry_to_script_line(entry: dict[str, Any]) -> str](mods/soul weaver/app.py#L564)（第 564 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [summarize_chunk(chunk: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L570)（第 570 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_entry_chunks(entries: list[dict[str, Any]], target_lines: int = CHUNK_TARGET_LINES) -> list[dict[str, Any]]](mods/soul weaver/app.py#L579)（第 579 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：flush

#### [flush() -> None（嵌套在 build_entry_chunks 内）](mods/soul weaver/app.py#L594)（第 594 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_speaker_chunks(entries: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]](mods/soul weaver/app.py#L634)（第 634 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [summarize_speaker_chunks(speaker_chunks: dict[str, list[dict[str, Any]]]) -> dict[str, list[dict[str, Any]]]](mods/soul weaver/app.py#L659)（第 659 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_text_chunks(text: str, prefix: str = chunk, target_lines: int = TEXT_CHUNK_TARGET_LINES) -> list[dict[str, Any]]](mods/soul weaver/app.py#L666)（第 666 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_script_entries(source_text: str) -> dict[str, Any]](mods/soul weaver/app.py#L686)（第 686 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [extract_character_lines(parsed: dict[str, Any], character_name: str) -> str](mods/soul weaver/app.py#L751)（第 751 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [extract_character_chunks(parsed: dict[str, Any], character_name: str) -> list[dict[str, Any]]](mods/soul weaver/app.py#L766)（第 766 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_settings() -> dict[str, Any]](mods/soul weaver/app.py#L778)（第 778 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_settings(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L782)（第 782 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [request_settings(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L796)（第 796 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_drafts() -> list[dict[str, Any]]](mods/soul weaver/app.py#L805)（第 805 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_draft(draft: dict[str, Any]) -> None](mods/soul weaver/app.py#L810)（第 810 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_api_url(base_url: str, endpoint: str) -> str](mods/soul weaver/app.py#L817)（第 817 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_headers(api_key: str) -> dict[str, str]](mods/soul weaver/app.py#L826)（第 826 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_wbmaker_module() -> Any](mods/soul weaver/app.py#L833)（第 833 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_wbmaker_settings(payload_settings: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L848)（第 848 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [generate_worldbook_with_wbmaker(settings: dict[str, Any], source_text: str, current_store: Any | None = None) -> dict[str, Any]](mods/soul weaver/app.py#L868)（第 868 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [merge_worldbook_partials_with_wbmaker(partials: list[Any]) -> dict[str, Any]](mods/soul weaver/app.py#L885)（第 885 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [extract_json_text(raw_text: str) -> str](mods/soul weaver/app.py#L903)（第 903 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [try_parse_json(raw_text: str) -> tuple[dict[str, Any] | None, str]](mods/soul weaver/app.py#L922)（第 922 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [split_text(text: str, segment_length: int = SEGMENT_LENGTH) -> list[str]](mods/soul weaver/app.py#L933)（第 933 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [request_chat_completion(settings: dict[str, Any], messages: list[dict[str, str]]) -> str](mods/soul weaver/app.py#L954)（第 954 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [generate_with_segments(settings: dict[str, Any], source_text: str, system_prompt: str, build_user_msg) -> tuple[str, list[str]]](mods/soul weaver/app.py#L992)（第 992 行）
Handle long text with segmentation. Returns (final_output, warnings)
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_role_card(raw: dict[str, Any], character_name: str) -> dict[str, Any]](mods/soul weaver/app.py#L1070)（第 1070 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_single_preset(raw: dict[str, Any], character_name: str) -> dict[str, Any]](mods/soul weaver/app.py#L1155)（第 1155 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_preset(raw: dict[str, Any], character_name: str) -> dict[str, Any]](mods/soul weaver/app.py#L1249)（第 1249 行）
Return the same preset-store shape used by Fantareal preset exports
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_memories(raw: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1278)（第 1278 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_worldbook(raw: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1292)（第 1292 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [startup_event() -> None](mods/soul weaver/app.py#L1344)（第 1344 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [index(request: Request) -> HTMLResponse](mods/soul weaver/app.py#L1349)（第 1349 行）
GET / 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_settings() -> dict[str, Any]](mods/soul weaver/app.py#L1366)（第 1366 行）
GET /api/settings 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_settings(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1372)（第 1372 行）
POST /api/settings 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_drafts() -> dict[str, Any]](mods/soul weaver/app.py#L1378)（第 1378 行）
GET /api/drafts 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_parse_script(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1383)（第 1383 行）
POST /api/parse-script 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_probe_models(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1437)（第 1437 行）
POST /api/probe-models 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_generate_role_card(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1476)（第 1476 行）
POST /api/generate/role-card 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：build_user

#### [build_user(text: str) -> str（嵌套在 api_generate_role_card 内）](mods/soul weaver/app.py#L1484)（第 1484 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_generate_memory(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1514)（第 1514 行）
POST /api/generate/memory 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：build_user

#### [build_user(text: str) -> str（嵌套在 api_generate_memory 内）](mods/soul weaver/app.py#L1522)（第 1522 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_generate_plot(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1552)（第 1552 行）
POST /api/generate/plot 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：build_user

#### [build_user(text: str) -> str（嵌套在 api_generate_plot 内）](mods/soul weaver/app.py#L1560)（第 1560 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_generate_preset(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1588)（第 1588 行）
POST /api/generate/preset 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：build_user

#### [build_user(text: str) -> str（嵌套在 api_generate_preset 内）](mods/soul weaver/app.py#L1596)（第 1596 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_generate_worldbook(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1626)（第 1626 行）
POST /api/generate/worldbook 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：build_user

#### [build_user(text: str) -> str（嵌套在 api_generate_worldbook 内）](mods/soul weaver/app.py#L1633)（第 1633 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [task_system_prompt(task: str) -> str](mods/soul weaver/app.py#L1659)（第 1659 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [task_draft_type(task: str) -> str](mods/soul weaver/app.py#L1672)（第 1672 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_task_result(task: str, parsed: dict[str, Any], character_name: str) -> dict[str, Any]](mods/soul weaver/app.py#L1682)（第 1682 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_chunk_user(task: str, source_text: str, character_name: str, chunk_meta: dict[str, Any], context: Any) -> str](mods/soul weaver/app.py#L1694)（第 1694 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_merge_user(task: str, partials: list[Any], character_name: str, context: Any) -> str](mods/soul weaver/app.py#L1718)（第 1718 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_generate_chunk(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1733)（第 1733 行）
POST /api/generate/chunk 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_generate_merge(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1777)（第 1777 行）
POST /api/generate/merge 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_proxy_import(main_base_url: str, endpoint: str, payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1848)（第 1848 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_import_card(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1860)（第 1860 行）
POST /api/import/card 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_import_preset(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1873)（第 1873 行）
POST /api/import/preset 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_import_memories(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1885)（第 1885 行）
POST /api/import/memories 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_import_worldbook(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1896)（第 1896 行）
POST /api/import/worldbook 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export_soul(payload: dict[str, Any]) -> FileResponse](mods/soul weaver/app.py#L1909)（第 1909 行）
POST /api/export/soul 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export_soul_local(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1964)（第 1964 行）
POST /api/export/soul-local 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 25 节 mods/state_journal/app.py

### 一览

- **class WorkerProviderError** — 第 5412 行

- `get_resource_dir()` — 第 22 行
- `now_string()` — 第 290 行
- `clone_json()` — 第 294 行
- `hash_text()` — 第 298 行
- `normalize_turn_id()` — 第 303 行
- `read_json()` — 第 309 行
- `write_json()` — 第 319 行
- `safe_id()` — 第 324 行
- `qident()` — 第 331 行
- `data_table_name()` — 第 338 行
- `sqlite_type()` — 第 342 行
- `connect_db()` — 第 350 行
- `normalize_field()` — 第 361 行
- `normalize_schema()` — 第 388 行
- `normalize_template_field()` — 第 429 行
- `default_output_line_for_template_field()` — 第 442 行
- `ensure_template_output_fields()` — 第 448 行
- `build_template_character_schema()` — 第 467 行
- `normalize_turn_note_template()` — 第 482 行
- `refresh_builtin_turn_note_template()` — 第 511 行
- `refresh_builtin_turn_note_theme_pack()` — 第 536 行
- `refresh_builtin_assets()` — 第 547 行
- `normalize_turn_note_templates()` — 第 554 行
- `active_turn_note_template()` — 第 572 行
- `normalize_turn_note_theme_pack()` — 第 590 行
- `normalize_turn_note_theme_packs()` — 第 665 行
- `active_turn_note_theme_pack()` — 第 685 行
- `normalize_config()` — 第 693 行
- `init_meta_tables()` — 第 740 行
- `table_exists()` — 第 1096 行
- `field_map()` — 第 1101 行
- `build_create_table_sql()` — 第 1105 行
- `sync_physical_table()` — 第 1125 行
- `save_schema_to_db()` — 第 1164 行
- `load_schema_from_row()` — 第 1208 行
- `list_schemas_from_db()` — 第 1247 行
- `get_schema_from_db()` — 第 1252 行
- `serialize_db_value()` — 第 1262 行
- `get_table_rows_from_db()` — 第 1280 行
- `coerce_value()` — 第 1296 行
- `clean_rows()` — 第 1331 行
- `replace_table_rows()` — 第 1357 行
- `delete_table_from_db()` — 第 1372 行
- `build_table_snapshot()` — 第 1381 行
- `save_snapshot()` — 第 1392 行
- `ensure_runtime_data()` — 第 1405 行
- `get_config()` — 第 1420 行
- `save_config()` — 第 1433 行
- `get_config_value()` — 第 1445 行
- `set_config_value()` — 第 1458 行
- `build_openai_url()` — 第 1469 行
- `auth_headers()` — 第 1479 行
- `read_route_forwarding_p1_config()` — 第 1487 行
- `read_main_llm_config()` — 第 1521 行
- `merge_config_with_main_llm()` — 第 1556 行
- `fetch_model_list()` — 第 1571 行
- `test_chat_completion()` — 第 1601 行
- `strip_json_fence()` — 第 1627 行
- `extract_json_candidates()` — 第 1635 行
- `repair_common_json_issues()` — 第 1655 行
- `extract_json_from_text()` — 第 1683 行
- `normalize_updates()` — 第 1702 行
- `select_row_by_pk()` — 第 1712 行
- `reverse_pair_id()` — 第 1728 行
- `resolve_relationship_pk()` — 第 1738 行
- `apply_updates()` — 第 1755 行
- `upsert_full_row()` — 第 1854 行
- `rollback_turn_effects()` — 第 1870 行
- `save_turn_record()` — 第 1919 行
- `mark_turns_stale()` — 第 1979 行
- `save_turn_effects()` — 第 2000 行
- `record_hook_event()` — 第 2015 行
- `save_worker_turn_state()` — 第 2025 行
- `strip_title_sequence()` — 第 2044 行
- `clean_display_text()` — 第 2050 行
- `normalize_role_source_mode()` — 第 2081 行
- `role_source_mode_label()` — 第 2100 行
- `normalize_role_state_mode()` — 第 2108 行
- `role_state_mode()` — 第 2136 行
- `role_state_mode_uses_snapshot()` — 第 2148 行
- `role_state_mode_uses_variables()` — 第 2152 行
- `role_state_mode_uses_stages()` — 第 2156 行
- `role_state_current_card_path()` — 第 2160 行
- `current_role_card_payload()` — 第 2164 行
- `current_card_uid()` — 第 2176 行
- `current_card_summary()` — 第 2194 行
- `normalize_role_state_key()` — 第 2202 行
- `stage_letter()` — 第 2212 行
- `default_stage_key()` — 第 2220 行
- `default_stage_name()` — 第 2224 行
- `role_state_number()` — 第 2228 行
- `role_state_int()` — 第 2236 行
- `normalize_role_state_variable()` — 第 2246 行
- `normalize_snapshot_field()` — 第 2275 行
- `normalize_role_state_stage()` — 第 2289 行
- `normalize_role_state_role()` — 第 2333 行
- `role_state_role_tokens()` — 第 2433 行
- `role_state_role_score()` — 第 2446 行
- `is_placeholder_role_label()` — 第 2466 行
- `is_placeholder_role_state_role()` — 第 2471 行
- `is_placeholder_persona()` — 第 2484 行
- `persona_has_state_journal_payload()` — 第 2496 行
- `is_empty_persona_slot()` — 第 2505 行
- `merge_role_state_role()` — 第 2533 行
- `normalize_role_state_config()` — 第 2562 行
- `default_variable_configs()` — 第 2597 行
- `role_state_main_card_role()` — 第 2617 行
- `role_state_persona_roles()` — 第 2647 行
- `current_card_role_identity_roles()` — 第 2682 行
- `current_card_allowed_role_tokens()` — 第 2696 行
- `overlay_role_state_config()` — 第 2703 行
- `filter_roles_to_current_card()` — 第 2727 行
- `role_source_summary()` — 第 2752 行
- `role_state_config_from_current_card()` — 第 2777 行
- `sync_role_state_config_to_current_card()` — 第 2829 行
- `role_config_names()` — 第 2852 行
- `find_role_config()` — 第 2859 行
- `clamp_number()` — 第 2870 行
- `format_metric_number()` — 第 2878 行
- `format_metric_delta()` — 第 2886 行
- `format_metric_value()` — 第 2892 行
- `metric_keys_by_scope()` — 第 2896 行
- `parse_metric_value()` — 第 2900 行
- `row_to_dict()` — 第 2921 行
- `derive_season()` — 第 2927 行
- `derive_time_slot()` — 第 2937 行
- `parse_story_time()` — 第 2955 行
- `story_time_from_parts()` — 第 2971 行
- `normalize_story_time_mode()` — 第 2993 行
- `normalize_story_time_display_mode()` — 第 2998 行
- `normalize_story_time_custom_advance_type()` — 第 3003 行
- `normalize_story_time_custom_seconds()` — 第 3008 行
- `story_time_label()` — 第 3016 行
- `story_time_state_defaults()` — 第 3021 行
- `serialize_story_time_state()` — 第 3052 行
- `story_time_context_from_state()` — 第 3101 行
- `format_story_time_display()` — 第 3117 行
- `load_story_time_state()` — 第 3131 行
- `upsert_story_time_state()` — 第 3138 行
- `story_time_config_from_payload()` — 第 3209 行
- `record_story_time_history()` — 第 3245 行
- `apply_story_time_delta_to_state()` — 第 3284 行
- `normalize_story_time_delta()` — 第 3302 行
- `format_duration_zh()` — 第 3331 行
- `story_time_custom_delta()` — 第 3348 行
- `apply_story_time_update()` — 第 3382 行
- `rollback_story_time_effects()` — 第 3427 行
- `inject_story_time_display()` — 第 3470 行
- `manual_set_story_time()` — 第 3491 行
- `load_role_state_config()` — 第 3535 行
- `save_role_state_config()` — 第 3597 行
- `role_snapshot_fields_for_character()` — 第 3632 行
- `role_variables_for_character()` — 第 3647 行
- `ensure_display_metrics_for_full_roles()` — 第 3661 行
- `ensure_relationship_fallback()` — 第 3699 行
- `get_metric_snapshot()` — 第 3750 行
- `normalize_metric_display_value()` — 第 3780 行
- `metric_entry_matches()` — 第 3784 行
- `parse_explicit_metric_entry()` — 第 3798 行
- `character_metric_payload()` — 第 3812 行
- `apply_role_metric_state()` — 第 3837 行
- `apply_display_metrics()` — 第 3922 行
- `parse_metric_summary_items()` — 第 3952 行
- `apply_update_metric_summaries()` — 第 3968 行
- `compare_stage_condition()` — 第 4012 行
- `stage_by_key()` — 第 4041 行
- `stage_label_by_key()` — 第 4048 行
- `role_metric_values()` — 第 4053 行
- `evaluate_stage_conditions()` — 第 4062 行
- `choose_stage_for_role()` — 第 4094 行
- `build_stage_active_tag()` — 第 4107 行
- `append_stage_relationships()` — 第 4113 行
- `evaluate_stage_rules()` — 第 4133 行
- `get_active_stage_tags_from_db()` — 第 4238 行
- `stage_activation_tag()` — 第 4287 行
- `role_state_stage_catalog()` — 第 4297 行
- `worldbook_store_path()` — 第 4339 行
- `read_worldbook_store_for_stage_tags()` — 第 4343 行
- `write_worldbook_store_for_stage_tags()` — 第 4362 行
- `find_stage_catalog_item()` — 第 4372 行
- `default_stage_worldbook_content()` — 第 4384 行
- `build_stage_worldbook_entry()` — 第 4395 行
- `rollback_metric_effects()` — 第 4440 行
- `metric_state_display()` — 第 4487 行
- `ensure_schema_extra_field()` — 第 4494 行
- `ensure_metric_history_schema()` — 第 4508 行
- `delta_display()` — 第 4549 行
- `sync_metric_history_table()` — 第 4553 行
- `sync_metric_summary_tables()` — 第 4583 行
- `sync_visible_metric_tables()` — 第 4643 行
- `normalize_metric_display_records()` — 第 4649 行
- `attach_metrics_to_display()` — 第 4693 行
- `collect_role_specific_display_characters()` — 第 4713 行
- `normalize_display_payload()` — 第 4781 行
- `build_fallback_display()` — 第 4915 行
- `allocate_turn_sequence()` — 第 4967 行
- `get_turn_sequence()` — 第 4979 行
- `save_turn_display()` — 第 4983 行
- `latest_turn_display()` — 第 5054 行
- `build_update_summary()` — 第 5068 行
- `format_history()` — 第 5104 行
- `split_prompt_names()` — 第 5134 行
- `build_protagonist_prompt_rule()` — 第 5137 行
- `build_worker_custom_prompt_rule()` — 第 5151 行
- `build_worker_prompt()` — 第 5165 行
- `normalize_chat_completion_url()` — 第 5403 行
- `classify_provider_status()` — 第 5421 行
- `provider_error_message()` — 第 5433 行
- `call_worker_model()` — 第 5454 行
- `repair_worker_json()` — 第 5515 行
- `save_worker_log()` — 第 5536 行
- `latest_worker_log()` — 第 5555 行
- `index()` — 第 5572 行
- `api_get_config()` — 第 5578 行
- `api_save_config()` — 第 5585 行
- `api_main_config()` — 第 5592 行
- `api_story_time()` — 第 5608 行
- `api_story_time_config()` — 第 5616 行
- `api_story_time_initialize()` — 第 5631 行
- `api_story_time_reset()` — 第 5650 行
- `api_story_time_calibrate()` — 第 5669 行
- `api_story_time_history()` — 第 5682 行
- `api_role_state_config()` — 第 5698 行
- `api_save_role_state_config()` — 第 5707 行
- `api_role_state_from_card()` — 第 5719 行
- `api_role_state_sync_to_card()` — 第 5729 行
- `api_role_state_init_current()` — 第 5744 行
- `api_role_state_active_tags()` — 第 5818 行
- `api_stage_tags_active()` — 第 5826 行
- `api_stage_tags_catalog()` — 第 5832 行
- `api_stage_tags_create_worldbook_entry()` — 第 5840 行
- `api_role_state_debug_advance_stage()` — 第 5869 行
- `api_models()` — 第 5940 行
- `api_test_connection()` — 第 5953 行
- `api_hook_ping()` — 第 5978 行
- `api_hook_status()` — 第 6002 行
- `api_turn_start()` — 第 6010 行
- `api_turn_complete()` — 第 6026 行
- `api_turn_invalidate()` — 第 6043 行
- `api_recent_turns()` — 第 6065 行
- `api_state()` — 第 6078 行
- `api_metrics()` — 第 6092 行
- `api_create_table()` — 第 6100 行
- `api_get_table()` — 第 6112 行
- `api_save_table()` — 第 6122 行
- `get_table_rows_for_response()` — 第 6136 行
- `api_delete_table()` — 第 6143 行
- `api_import()` — 第 6152 行
- `api_export()` — 第 6173 行
- `recent_turn_displays()` — 第 6185 行
- `api_latest_display()` — 第 6222 行
- `api_recent_display()` — 第 6227 行
- `api_latest_log()` — 第 6234 行
- `redact_secret()` — 第 6238 行
- `load_json_row()` — 第 6247 行
- `api_export_debug_log()` — 第 6255 行
- `api_worker_update()` — 第 6311 行

### 函数详情

#### [get_resource_dir() -> Path](mods/state_journal/app.py#L22)（第 22 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [now_string() -> str](mods/state_journal/app.py#L290)（第 290 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clone_json(value: Any) -> Any](mods/state_journal/app.py#L294)（第 294 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [hash_text(value: Any) -> str](mods/state_journal/app.py#L298)（第 298 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_turn_id(value: Any) -> str](mods/state_journal/app.py#L303)（第 303 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [read_json(path: Path, default: Any) -> Any](mods/state_journal/app.py#L309)（第 309 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [write_json(path: Path, payload: Any) -> None](mods/state_journal/app.py#L319)（第 319 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [safe_id(value: Any, fallback: str = table) -> str](mods/state_journal/app.py#L324)（第 324 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [qident(identifier: str) -> str](mods/state_journal/app.py#L331)（第 331 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [data_table_name(table_id: str) -> str](mods/state_journal/app.py#L338)（第 338 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sqlite_type(field_type: str) -> str](mods/state_journal/app.py#L342)（第 342 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [connect_db() -> sqlite3.Connection](mods/state_journal/app.py#L350)（第 350 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_field(field: Any) -> dict[str, Any] | None](mods/state_journal/app.py#L361)（第 361 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_schema(schema: Any) -> dict[str, Any]](mods/state_journal/app.py#L388)（第 388 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_template_field(field: Any) -> dict[str, Any] | None](mods/state_journal/app.py#L429)（第 429 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_output_line_for_template_field(field: dict[str, Any]) -> str](mods/state_journal/app.py#L442)（第 442 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [ensure_template_output_fields(output_template: Any, fields: list[dict[str, Any]]) -> str](mods/state_journal/app.py#L448)（第 448 行）
Keep field definitions and output placeholders in sync
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_template_character_schema(fields: list[dict[str, Any]]) -> dict[str, str]](mods/state_journal/app.py#L467)（第 467 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_turn_note_template(template: Any, fallback_id: str = custom) -> dict[str, Any] | None](mods/state_journal/app.py#L482)（第 482 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [refresh_builtin_turn_note_template(template: dict[str, Any]) -> dict[str, Any]](mods/state_journal/app.py#L511)（第 511 行）
让旧配置中的内置标准模板跟随新版说明更新，同时不影响用户自定义模板
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [refresh_builtin_turn_note_theme_pack(pack: dict[str, Any]) -> dict[str, Any]](mods/state_journal/app.py#L536)（第 536 行）
刷新内置外观包定义，保留用户导入包与自定义包
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [refresh_builtin_assets(config: dict[str, Any]) -> dict[str, Any]](mods/state_journal/app.py#L547)（第 547 行）
正式版配置收口：刷新内置模板/美化包，不覆盖用户自定义项目
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_turn_note_templates(value: Any) -> list[dict[str, Any]]](mods/state_journal/app.py#L554)（第 554 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [active_turn_note_template(config: dict[str, Any]) -> dict[str, Any]](mods/state_journal/app.py#L572)（第 572 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_turn_note_theme_pack(pack: Any, fallback_id: str = theme) -> dict[str, Any] | None](mods/state_journal/app.py#L590)（第 590 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：json_dict, json_copy

#### [json_dict(value: Any) -> dict[str, Any]（嵌套在 normalize_turn_note_theme_pack 内）](mods/state_journal/app.py#L610)（第 610 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [json_copy(value: Any) -> Any（嵌套在 normalize_turn_note_theme_pack 内）](mods/state_journal/app.py#L618)（第 618 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_turn_note_theme_packs(value: Any) -> list[dict[str, Any]]](mods/state_journal/app.py#L665)（第 665 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [active_turn_note_theme_pack(config: dict[str, Any]) -> dict[str, Any]](mods/state_journal/app.py#L685)（第 685 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_config(config: Any) -> dict[str, Any]](mods/state_journal/app.py#L693)（第 693 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [init_meta_tables(conn: sqlite3.Connection) -> None](mods/state_journal/app.py#L740)（第 740 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：rebuild_card_scoped_table

#### [rebuild_card_scoped_table(table: str, create_sql: str, copy_columns: list[str]) -> None（嵌套在 init_meta_tables 内）](mods/state_journal/app.py#L987)（第 987 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [table_exists(conn: sqlite3.Connection, name: str) -> bool](mods/state_journal/app.py#L1096)（第 1096 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [field_map(schema: dict[str, Any]) -> dict[str, dict[str, Any]]](mods/state_journal/app.py#L1101)（第 1101 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_create_table_sql(schema: dict[str, Any], physical_name: str | None = None) -> str](mods/state_journal/app.py#L1105)（第 1105 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sync_physical_table(conn: sqlite3.Connection, schema: dict[str, Any]) -> None](mods/state_journal/app.py#L1125)（第 1125 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_schema_to_db(conn: sqlite3.Connection, schema: dict[str, Any]) -> dict[str, Any]](mods/state_journal/app.py#L1164)（第 1164 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [load_schema_from_row(conn: sqlite3.Connection, table_row: sqlite3.Row) -> dict[str, Any]](mods/state_journal/app.py#L1208)（第 1208 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [list_schemas_from_db(conn: sqlite3.Connection) -> list[dict[str, Any]]](mods/state_journal/app.py#L1247)（第 1247 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_schema_from_db(conn: sqlite3.Connection, table_id: str) -> dict[str, Any]](mods/state_journal/app.py#L1252)（第 1252 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [serialize_db_value(value: Any, field: dict[str, Any]) -> Any](mods/state_journal/app.py#L1262)（第 1262 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_table_rows_from_db(conn: sqlite3.Connection, schema: dict[str, Any]) -> list[dict[str, Any]]](mods/state_journal/app.py#L1280)（第 1280 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [coerce_value(value: Any, field: dict[str, Any]) -> Any](mods/state_journal/app.py#L1296)（第 1296 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clean_rows(schema: dict[str, Any], rows: Any) -> list[dict[str, Any]]](mods/state_journal/app.py#L1331)（第 1331 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [replace_table_rows(conn: sqlite3.Connection, schema: dict[str, Any], rows: list[dict[str, Any]]) -> None](mods/state_journal/app.py#L1357)（第 1357 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [delete_table_from_db(conn: sqlite3.Connection, table_id: str) -> None](mods/state_journal/app.py#L1372)（第 1372 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_table_snapshot(conn: sqlite3.Connection, table_ids: list[str] | None = None) -> list[dict[str, Any]]](mods/state_journal/app.py#L1381)（第 1381 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_snapshot(conn: sqlite3.Connection, table_id: str, reason: str = update) -> None](mods/state_journal/app.py#L1392)（第 1392 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [ensure_runtime_data() -> None](mods/state_journal/app.py#L1405)（第 1405 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_config() -> dict[str, Any]](mods/state_journal/app.py#L1420)（第 1420 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_config(config: dict[str, Any]) -> dict[str, Any]](mods/state_journal/app.py#L1433)（第 1433 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_config_value(key: str, default: Any = None) -> Any](mods/state_journal/app.py#L1445)（第 1445 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [set_config_value(key: str, value: Any) -> Any](mods/state_journal/app.py#L1458)（第 1458 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_openai_url(base_url: str, endpoint: str) -> str](mods/state_journal/app.py#L1469)（第 1469 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [auth_headers(api_key: str) -> dict[str, str]](mods/state_journal/app.py#L1479)（第 1479 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [read_route_forwarding_p1_config() -> dict[str, Any]](mods/state_journal/app.py#L1487)（第 1487 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [read_main_llm_config() -> dict[str, Any]](mods/state_journal/app.py#L1521)（第 1521 行）
Best-effort read of Fantareal's main model config
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [merge_config_with_main_llm(config: dict[str, Any]) -> dict[str, Any]](mods/state_journal/app.py#L1556)（第 1556 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [fetch_model_list(base_url: str, api_key: str, timeout: int | float = 30) -> list[str]](mods/state_journal/app.py#L1571)（第 1571 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [test_chat_completion(base_url: str, api_key: str, model: str, timeout: int | float = 30) -> None](mods/state_journal/app.py#L1601)（第 1601 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [strip_json_fence(text: str) -> str](mods/state_journal/app.py#L1627)（第 1627 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [extract_json_candidates(text: str) -> list[str]](mods/state_journal/app.py#L1635)（第 1635 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [repair_common_json_issues(text: str) -> str](mods/state_journal/app.py#L1655)（第 1655 行）
Fix small model-formatting mistakes without changing semantics
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [extract_json_from_text(text: str) -> Any](mods/state_journal/app.py#L1683)（第 1683 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_updates(payload: Any) -> list[dict[str, Any]]](mods/state_journal/app.py#L1702)（第 1702 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [select_row_by_pk(conn: sqlite3.Connection, schema: dict[str, Any], pk_value: str) -> dict[str, Any] | None](mods/state_journal/app.py#L1712)（第 1712 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [reverse_pair_id(value: str) -> str](mods/state_journal/app.py#L1728)（第 1728 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [resolve_relationship_pk(conn: sqlite3.Connection, schema: dict[str, Any], pk_value: str) -> tuple[str, dict[str, Any] | None, str]](mods/state_journal/app.py#L1738)（第 1738 行）
relationship 表 A-B / B-A 自动反查，避免正反主键不同导致整轮失败
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [apply_updates(updates: list[dict[str, Any]]) -> dict[str, Any]](mods/state_journal/app.py#L1755)（第 1755 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [upsert_full_row(conn: sqlite3.Connection, schema: dict[str, Any], row: dict[str, Any]) -> None](mods/state_journal/app.py#L1854)（第 1854 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [rollback_turn_effects(conn: sqlite3.Connection, turn_id: str, reason: str = reroll) -> int](mods/state_journal/app.py#L1870)（第 1870 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_turn_record(conn: sqlite3.Connection) -> dict[str, Any]](mods/state_journal/app.py#L1919)（第 1919 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [mark_turns_stale(conn: sqlite3.Connection, from_turn_id: str | None = None, reason: str = history_changed) -> dict[str, Any]](mods/state_journal/app.py#L1979)（第 1979 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_turn_effects(conn: sqlite3.Connection, turn_id: str, result: dict[str, Any]) -> None](mods/state_journal/app.py#L2000)（第 2000 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [record_hook_event(conn: sqlite3.Connection) -> None](mods/state_journal/app.py#L2015)（第 2015 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_worker_turn_state() -> None](mods/state_journal/app.py#L2025)（第 2025 行）
Persist worker lifecycle status so reroll / timeout states never remain invisible pending rows
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [strip_title_sequence(value: Any) -> str](mods/state_journal/app.py#L2044)（第 2044 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clean_display_text(value: Any, limit: int = 360) -> str](mods/state_journal/app.py#L2050)（第 2050 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_role_source_mode(value: Any) -> str](mods/state_journal/app.py#L2081)（第 2081 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [role_source_mode_label(mode: str) -> str](mods/state_journal/app.py#L2100)（第 2100 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_role_state_mode(value: Any) -> str](mods/state_journal/app.py#L2108)（第 2108 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [role_state_mode(role: dict[str, Any] | None) -> str](mods/state_journal/app.py#L2136)（第 2136 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [role_state_mode_uses_snapshot(role: dict[str, Any] | None) -> bool](mods/state_journal/app.py#L2148)（第 2148 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [role_state_mode_uses_variables(role: dict[str, Any] | None) -> bool](mods/state_journal/app.py#L2152)（第 2152 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [role_state_mode_uses_stages(role: dict[str, Any] | None) -> bool](mods/state_journal/app.py#L2156)（第 2156 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [role_state_current_card_path() -> Path](mods/state_journal/app.py#L2160)（第 2160 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [current_role_card_payload() -> dict[str, Any]](mods/state_journal/app.py#L2164)（第 2164 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [current_card_uid() -> str](mods/state_journal/app.py#L2176)（第 2176 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [current_card_summary() -> dict[str, Any]](mods/state_journal/app.py#L2194)（第 2194 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_role_state_key(value: Any, fallback: str) -> str](mods/state_journal/app.py#L2202)（第 2202 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [stage_letter(index: int) -> str](mods/state_journal/app.py#L2212)（第 2212 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_stage_key(index: int) -> str](mods/state_journal/app.py#L2220)（第 2220 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_stage_name(index: int) -> str](mods/state_journal/app.py#L2224)（第 2224 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [role_state_number(value: Any, default: float = 0) -> float](mods/state_journal/app.py#L2228)（第 2228 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [role_state_int(value: Any, default: int = 0, minimum: int | None = None) -> int](mods/state_journal/app.py#L2236)（第 2236 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_role_state_variable(raw: Any, index: int = 1) -> dict[str, Any] | None](mods/state_journal/app.py#L2246)（第 2246 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_snapshot_field(raw: Any, index: int = 1) -> dict[str, Any] | None](mods/state_journal/app.py#L2275)（第 2275 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_role_state_stage(raw: Any, role_id: str, index: int = 1) -> dict[str, Any] | None](mods/state_journal/app.py#L2289)（第 2289 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_role_state_role(raw: Any, index: int = 1) -> dict[str, Any] | None](mods/state_journal/app.py#L2333)（第 2333 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [role_state_role_tokens(role: dict[str, Any]) -> set[str]](mods/state_journal/app.py#L2433)（第 2433 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [role_state_role_score(role: dict[str, Any]) -> int](mods/state_journal/app.py#L2446)（第 2446 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [is_placeholder_role_label(value: Any) -> bool](mods/state_journal/app.py#L2466)（第 2466 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [is_placeholder_role_state_role(role: dict[str, Any]) -> bool](mods/state_journal/app.py#L2471)（第 2471 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [is_placeholder_persona(persona_key: str, persona: dict[str, Any]) -> bool](mods/state_journal/app.py#L2484)（第 2484 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [persona_has_state_journal_payload(persona: dict[str, Any]) -> bool](mods/state_journal/app.py#L2496)（第 2496 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [is_empty_persona_slot(persona_key: str, persona: dict[str, Any]) -> bool](mods/state_journal/app.py#L2505)（第 2505 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [merge_role_state_role(base: dict[str, Any], incoming: dict[str, Any]) -> dict[str, Any]](mods/state_journal/app.py#L2533)（第 2533 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_role_state_config(raw: Any) -> dict[str, Any]](mods/state_journal/app.py#L2562)（第 2562 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_variable_configs() -> list[dict[str, Any]]](mods/state_journal/app.py#L2597)（第 2597 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [role_state_main_card_role(raw_card: dict[str, Any]) -> dict[str, Any] | None](mods/state_journal/app.py#L2617)（第 2617 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [role_state_persona_roles(raw_card: dict[str, Any]) -> list[dict[str, Any]]](mods/state_journal/app.py#L2647)（第 2647 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [current_card_role_identity_roles(raw_card: dict[str, Any], source_mode: str = auto) -> list[dict[str, Any]]](mods/state_journal/app.py#L2682)（第 2682 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [current_card_allowed_role_tokens(raw_card: dict[str, Any], source_mode: str = auto) -> set[str]](mods/state_journal/app.py#L2696)（第 2696 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [overlay_role_state_config(identity: dict[str, Any], configured: dict[str, Any]) -> dict[str, Any]](mods/state_journal/app.py#L2703)（第 2703 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [filter_roles_to_current_card(roles: list[dict[str, Any]], raw_card: dict[str, Any], source_mode: str = auto) -> list[dict[str, Any]]](mods/state_journal/app.py#L2727)（第 2727 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [role_source_summary(mode: str, detected: str, roles: list[dict[str, Any]], has_personas: bool, main_role_name: str) -> dict[str, Any]](mods/state_journal/app.py#L2752)（第 2752 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [role_state_config_from_current_card() -> dict[str, Any]](mods/state_journal/app.py#L2777)（第 2777 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sync_role_state_config_to_current_card(config: dict[str, Any]) -> bool](mods/state_journal/app.py#L2829)（第 2829 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [role_config_names(role: dict[str, Any]) -> set[str]](mods/state_journal/app.py#L2852)（第 2852 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [find_role_config(config: dict[str, Any], character_name: str) -> dict[str, Any] | None](mods/state_journal/app.py#L2859)（第 2859 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clamp_number(value: Any, minimum: float = 0, maximum: float = 100) -> float](mods/state_journal/app.py#L2870)（第 2870 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [format_metric_number(value: Any) -> int | float](mods/state_journal/app.py#L2878)（第 2878 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [format_metric_delta(delta: Any) -> str](mods/state_journal/app.py#L2886)（第 2886 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [format_metric_value(value: Any, max_value: Any = 100, delta: Any = 0) -> str](mods/state_journal/app.py#L2892)（第 2892 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [metric_keys_by_scope(scope: str) -> set[str]](mods/state_journal/app.py#L2896)（第 2896 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_metric_value(raw_value: Any, default_max: float = 100) -> dict[str, Any] | None](mods/state_journal/app.py#L2900)（第 2900 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [row_to_dict(row: sqlite3.Row | None) -> dict[str, Any] | None](mods/state_journal/app.py#L2921)（第 2921 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [derive_season(month: int) -> str](mods/state_journal/app.py#L2927)（第 2927 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [derive_time_slot(hour: int) -> str](mods/state_journal/app.py#L2937)（第 2937 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_story_time(value: Any, fallback: datetime | None = None) -> datetime](mods/state_journal/app.py#L2955)（第 2955 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [story_time_from_parts(payload: dict[str, Any], prefix: str) -> datetime](mods/state_journal/app.py#L2971)（第 2971 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_story_time_mode(value: Any) -> str](mods/state_journal/app.py#L2993)（第 2993 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_story_time_display_mode(value: Any) -> str](mods/state_journal/app.py#L2998)（第 2998 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_story_time_custom_advance_type(value: Any) -> str](mods/state_journal/app.py#L3003)（第 3003 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_story_time_custom_seconds(value: Any, fallback: int = 0) -> int](mods/state_journal/app.py#L3008)（第 3008 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [story_time_label(value: Any, mapping: dict[str, str]) -> str](mods/state_journal/app.py#L3016)（第 3016 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [story_time_state_defaults(card_uid: str | None = None) -> dict[str, Any]](mods/state_journal/app.py#L3021)（第 3021 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [serialize_story_time_state(row: dict[str, Any] | sqlite3.Row | None, card_uid: str | None = None) -> dict[str, Any]](mods/state_journal/app.py#L3052)（第 3052 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [story_time_context_from_state(state: dict[str, Any] | None) -> dict[str, Any]](mods/state_journal/app.py#L3101)（第 3101 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [format_story_time_display(state: dict[str, Any] | None) -> str](mods/state_journal/app.py#L3117)（第 3117 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [load_story_time_state(conn: sqlite3.Connection, card_uid: str | None = None) -> dict[str, Any]](mods/state_journal/app.py#L3131)（第 3131 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [upsert_story_time_state(conn: sqlite3.Connection, state: dict[str, Any]) -> dict[str, Any]](mods/state_journal/app.py#L3138)（第 3138 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [story_time_config_from_payload(payload: dict[str, Any], existing: dict[str, Any]) -> dict[str, Any]](mods/state_journal/app.py#L3209)（第 3209 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [record_story_time_history(conn: sqlite3.Connection) -> None](mods/state_journal/app.py#L3245)（第 3245 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [apply_story_time_delta_to_state(state: dict[str, Any], delta_seconds: int) -> dict[str, Any]](mods/state_journal/app.py#L3284)（第 3284 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_story_time_delta(raw: Any, advance_mode: str = smart) -> dict[str, Any]](mods/state_journal/app.py#L3302)（第 3302 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [format_duration_zh(seconds: int) -> str](mods/state_journal/app.py#L3331)（第 3331 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [story_time_custom_delta(state: dict[str, Any]) -> dict[str, Any]](mods/state_journal/app.py#L3348)（第 3348 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [apply_story_time_update(conn: sqlite3.Connection, raw_delta: Any) -> dict[str, Any] | None](mods/state_journal/app.py#L3382)（第 3382 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [rollback_story_time_effects(conn: sqlite3.Connection, turn_id: str, message_id: str) -> int](mods/state_journal/app.py#L3427)（第 3427 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [inject_story_time_display(display_payload: dict[str, Any], story_time_result: dict[str, Any] | None = None) -> dict[str, Any]](mods/state_journal/app.py#L3470)（第 3470 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [manual_set_story_time(conn: sqlite3.Connection) -> dict[str, Any]](mods/state_journal/app.py#L3491)（第 3491 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [load_role_state_config(conn: sqlite3.Connection, card_uid: str | None = None) -> dict[str, Any]](mods/state_journal/app.py#L3535)（第 3535 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_role_state_config(conn: sqlite3.Connection, config: dict[str, Any], card_uid: str | None = None) -> dict[str, Any]](mods/state_journal/app.py#L3597)（第 3597 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [role_snapshot_fields_for_character(config: dict[str, Any], character_name: str) -> list[dict[str, Any]]](mods/state_journal/app.py#L3632)（第 3632 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [role_variables_for_character(conn: sqlite3.Connection, character_name: str) -> tuple[dict[str, Any] | None, list[dict[str, Any]]]](mods/state_journal/app.py#L3647)（第 3647 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [ensure_display_metrics_for_full_roles(conn: sqlite3.Connection, display_payload: dict[str, Any]) -> int](mods/state_journal/app.py#L3661)（第 3661 行）
Ensure full-mode role cards always have a metrics array for display and state updates
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [ensure_relationship_fallback(display_payload: dict[str, Any]) -> int](mods/state_journal/app.py#L3699)（第 3699 行）
Backfill relationship changes when the model omits display.relationships
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_metric_snapshot(conn: sqlite3.Connection) -> dict[str, Any]](mods/state_journal/app.py#L3750)（第 3750 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_metric_display_value(parsed: dict[str, Any]) -> str](mods/state_journal/app.py#L3780)（第 3780 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [metric_entry_matches(entry: dict[str, Any], key: str, label: str) -> bool](mods/state_journal/app.py#L3784)（第 3784 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_explicit_metric_entry(entry: dict[str, Any]) -> dict[str, Any] | None](mods/state_journal/app.py#L3798)（第 3798 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [character_metric_payload(character: dict[str, Any], key: str, label: str, default_max: float) -> dict[str, Any] | None](mods/state_journal/app.py#L3812)（第 3812 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [apply_role_metric_state(conn: sqlite3.Connection) -> dict[str, Any] | None](mods/state_journal/app.py#L3837)（第 3837 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [apply_display_metrics(conn: sqlite3.Connection, turn_id: str, display_payload: dict[str, Any]) -> list[dict[str, Any]]](mods/state_journal/app.py#L3922)（第 3922 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_metric_summary_items(summary: Any) -> list[dict[str, Any]]](mods/state_journal/app.py#L3952)（第 3952 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [apply_update_metric_summaries(conn: sqlite3.Connection, turn_id: str, updates: list[dict[str, Any]]) -> list[dict[str, Any]]](mods/state_journal/app.py#L3968)（第 3968 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [compare_stage_condition(current_value: Any, op: str, target_value: Any) -> bool](mods/state_journal/app.py#L4012)（第 4012 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [stage_by_key(role: dict[str, Any], key: str) -> dict[str, Any] | None](mods/state_journal/app.py#L4041)（第 4041 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [stage_label_by_key(role: dict[str, Any], key: str) -> str](mods/state_journal/app.py#L4048)（第 4048 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [role_metric_values(conn: sqlite3.Connection, role: dict[str, Any]) -> tuple[str, dict[str, float]]](mods/state_journal/app.py#L4053)（第 4053 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [evaluate_stage_conditions(stage: dict[str, Any], values: dict[str, float], story_time_context: dict[str, Any] | None = None) -> tuple[bool, dict[str, Any]]](mods/state_journal/app.py#L4062)（第 4062 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [choose_stage_for_role(role: dict[str, Any], values: dict[str, float], story_time_context: dict[str, Any] | None = None) -> tuple[dict[str, Any] | None, dict[str, Any]]](mods/state_journal/app.py#L4094)（第 4094 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_stage_active_tag(role_id: str, stage_key: str) -> str](mods/state_journal/app.py#L4107)（第 4107 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [append_stage_relationships(display_payload: dict[str, Any], stage_rows: list[dict[str, Any]]) -> None](mods/state_journal/app.py#L4113)（第 4113 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [evaluate_stage_rules(conn: sqlite3.Connection, turn_id: str, display_payload: dict[str, Any] | None = None, turn_index: int = 0) -> list[dict[str, Any]]](mods/state_journal/app.py#L4133)（第 4133 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_active_stage_tags_from_db() -> dict[str, Any]](mods/state_journal/app.py#L4238)（第 4238 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [stage_activation_tag(role_id: Any, stage_key: Any, explicit: Any) -> str](mods/state_journal/app.py#L4287)（第 4287 行）
Return the canonical active tag used by worldbook external_tag entries
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [role_state_stage_catalog(config: dict[str, Any] | None = None) -> dict[str, Any]](mods/state_journal/app.py#L4297)（第 4297 行）
Expose configured role stages in a UI-friendly shape for worldbook binding
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [worldbook_store_path() -> Path](mods/state_journal/app.py#L4339)（第 4339 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [read_worldbook_store_for_stage_tags() -> dict[str, Any]](mods/state_journal/app.py#L4343)（第 4343 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [write_worldbook_store_for_stage_tags(store: dict[str, Any]) -> None](mods/state_journal/app.py#L4362)（第 4362 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [find_stage_catalog_item(role_id: str, stage_key: str) -> dict[str, Any] | None](mods/state_journal/app.py#L4372)（第 4372 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_stage_worldbook_content(item: dict[str, Any]) -> str](mods/state_journal/app.py#L4384)（第 4384 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_stage_worldbook_entry(item: dict[str, Any]) -> dict[str, Any]](mods/state_journal/app.py#L4395)（第 4395 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [rollback_metric_effects(conn: sqlite3.Connection, turn_id: str, metrics: list[dict[str, Any]]) -> int](mods/state_journal/app.py#L4440)（第 4440 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [metric_state_display(row: sqlite3.Row | dict[str, Any]) -> str](mods/state_journal/app.py#L4487)（第 4487 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [ensure_schema_extra_field(conn: sqlite3.Connection, table_id: str, field_def: dict[str, Any]) -> None](mods/state_journal/app.py#L4494)（第 4494 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [ensure_metric_history_schema(conn: sqlite3.Connection) -> None](mods/state_journal/app.py#L4508)（第 4508 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [delta_display(delta: Any) -> str](mods/state_journal/app.py#L4549)（第 4549 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sync_metric_history_table(conn: sqlite3.Connection) -> None](mods/state_journal/app.py#L4553)（第 4553 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sync_metric_summary_tables(conn: sqlite3.Connection) -> None](mods/state_journal/app.py#L4583)（第 4583 行）
把真实数值表镜像到用户可见表册：角色状态表、关系表、数值变化记录
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：summary_for

#### [summary_for(items: list[sqlite3.Row], allowed: set[str]) -> str（嵌套在 sync_metric_summary_tables 内）](mods/state_journal/app.py#L4606)（第 4606 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sync_visible_metric_tables(conn: sqlite3.Connection) -> None](mods/state_journal/app.py#L4643)（第 4643 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_metric_display_records(metrics: Any) -> list[dict[str, Any]]](mods/state_journal/app.py#L4649)（第 4649 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [attach_metrics_to_display(display: dict[str, Any], metrics: Any) -> dict[str, Any]](mods/state_journal/app.py#L4693)（第 4693 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [collect_role_specific_display_characters(display: Any) -> list[dict[str, Any]]](mods/state_journal/app.py#L4713)（第 4713 行）
Collect role-specific character cards from worker output or nested raw display
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：append_items, walk

#### [append_items(source: Any) -> None（嵌套在 collect_role_specific_display_characters 内）](mods/state_journal/app.py#L4724)（第 4724 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [walk(node: Any, depth: int = 0) -> None（嵌套在 collect_role_specific_display_characters 内）](mods/state_journal/app.py#L4769)（第 4769 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_display_payload(payload: Any) -> dict[str, Any]](mods/state_journal/app.py#L4781)（第 4781 行）
Normalize the assistant-generated front-end display payload
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_fallback_display() -> dict[str, Any]](mods/state_journal/app.py#L4915)（第 4915 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [allocate_turn_sequence(conn: sqlite3.Connection, turn_id: str) -> int](mods/state_journal/app.py#L4967)（第 4967 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_turn_sequence(conn: sqlite3.Connection, turn_id: str) -> int](mods/state_journal/app.py#L4979)（第 4979 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_turn_display(display: dict[str, Any]) -> dict[str, Any]](mods/state_journal/app.py#L4983)（第 4983 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [latest_turn_display() -> dict[str, Any]](mods/state_journal/app.py#L5054)（第 5054 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_update_summary(result: dict[str, Any], tables: list[dict[str, Any]] | None = None) -> dict[str, Any]](mods/state_journal/app.py#L5068)（第 5068 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [format_history(history: Any, limit_turns: int) -> list[dict[str, str]]](mods/state_journal/app.py#L5104)（第 5104 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [split_prompt_names(value: object) -> list[str]](mods/state_journal/app.py#L5134)（第 5134 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_protagonist_prompt_rule(config: dict[str, Any]) -> str](mods/state_journal/app.py#L5137)（第 5137 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_worker_custom_prompt_rule(config: dict[str, Any]) -> str](mods/state_journal/app.py#L5151)（第 5151 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_worker_prompt() -> tuple[str, str]](mods/state_journal/app.py#L5165)（第 5165 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_chat_completion_url(base_url: str) -> str](mods/state_journal/app.py#L5403)（第 5403 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [__init__(error_type: str, message: str) -> None（嵌套在 WorkerProviderError 内）](mods/state_journal/app.py#L5413)（第 5413 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [classify_provider_status(status_code: int) -> str](mods/state_journal/app.py#L5421)（第 5421 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [provider_error_message(error_type: str, detail: str) -> str](mods/state_journal/app.py#L5433)（第 5433 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [call_worker_model() -> str](mods/state_journal/app.py#L5454)（第 5454 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：_post

#### [_post(current_payload: dict[str, Any]) -> dict[str, Any]（嵌套在 call_worker_model 内）](mods/state_journal/app.py#L5475)（第 5475 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [repair_worker_json() -> str](mods/state_journal/app.py#L5515)（第 5515 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_worker_log(payload: dict[str, Any]) -> None](mods/state_journal/app.py#L5536)（第 5536 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [latest_worker_log() -> dict[str, Any]](mods/state_journal/app.py#L5555)（第 5555 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [index(request: Request) -> HTMLResponse](mods/state_journal/app.py#L5572)（第 5572 行）
GET / 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_config() -> dict[str, Any]](mods/state_journal/app.py#L5578)（第 5578 行）
GET /api/config 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_config(request: Request) -> dict[str, Any]](mods/state_journal/app.py#L5585)（第 5585 行）
POST /api/config 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_main_config() -> dict[str, Any]](mods/state_journal/app.py#L5592)（第 5592 行）
GET /api/main-config 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_story_time() -> dict[str, Any]](mods/state_journal/app.py#L5608)（第 5608 行）
GET /api/story-time 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_story_time_config(request: Request) -> dict[str, Any]](mods/state_journal/app.py#L5616)（第 5616 行）
POST /api/story-time/config 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_story_time_initialize(request: Request) -> dict[str, Any]](mods/state_journal/app.py#L5631)（第 5631 行）
POST /api/story-time/initialize 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_story_time_reset(request: Request) -> dict[str, Any]](mods/state_journal/app.py#L5650)（第 5650 行）
POST /api/story-time/reset 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_story_time_calibrate(request: Request) -> dict[str, Any]](mods/state_journal/app.py#L5669)（第 5669 行）
POST /api/story-time/calibrate 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_story_time_history(limit: int = 50) -> dict[str, Any]](mods/state_journal/app.py#L5682)（第 5682 行）
GET /api/story-time/history 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_role_state_config() -> dict[str, Any]](mods/state_journal/app.py#L5698)（第 5698 行）
GET /api/role-state/config 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_role_state_config(request: Request) -> dict[str, Any]](mods/state_journal/app.py#L5707)（第 5707 行）
POST /api/role-state/config 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_role_state_from_card() -> dict[str, Any]](mods/state_journal/app.py#L5719)（第 5719 行）
POST /api/role-state/from-card 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_role_state_sync_to_card(request: Request) -> dict[str, Any]](mods/state_journal/app.py#L5729)（第 5729 行）
POST /api/role-state/sync-to-card 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_role_state_init_current(request: Request) -> dict[str, Any]](mods/state_journal/app.py#L5744)（第 5744 行）
POST /api/role-state/init-current 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_role_state_active_tags() -> dict[str, Any]](mods/state_journal/app.py#L5818)（第 5818 行）
GET /api/role-state/active-tags 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_stage_tags_active() -> dict[str, Any]](mods/state_journal/app.py#L5826)（第 5826 行）
GET /api/stage-tags/active 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_stage_tags_catalog() -> dict[str, Any]](mods/state_journal/app.py#L5832)（第 5832 行）
GET /api/stage-tags/catalog 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_stage_tags_create_worldbook_entry(request: Request) -> dict[str, Any]](mods/state_journal/app.py#L5840)（第 5840 行）
POST /api/stage-tags/create-worldbook-entry 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_role_state_debug_advance_stage(request: Request) -> dict[str, Any]](mods/state_journal/app.py#L5869)（第 5869 行）
POST /api/role-state/debug-advance-stage 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_models(request: Request) -> dict[str, Any]](mods/state_journal/app.py#L5940)（第 5940 行）
POST /api/models 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_test_connection(request: Request) -> dict[str, Any]](mods/state_journal/app.py#L5953)（第 5953 行）
POST /api/test-connection 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_hook_ping(request: Request) -> dict[str, Any]](mods/state_journal/app.py#L5978)（第 5978 行）
POST /api/hook/ping 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_hook_status() -> dict[str, Any]](mods/state_journal/app.py#L6002)（第 6002 行）
GET /api/hook/status 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_turn_start(request: Request) -> dict[str, Any]](mods/state_journal/app.py#L6010)（第 6010 行）
POST /api/turn/start 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_turn_complete(request: Request) -> dict[str, Any]](mods/state_journal/app.py#L6026)（第 6026 行）
POST /api/turn/complete 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_turn_invalidate(request: Request) -> dict[str, Any]](mods/state_journal/app.py#L6043)（第 6043 行）
POST /api/turn/invalidate 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_recent_turns(limit: int = 30) -> dict[str, Any]](mods/state_journal/app.py#L6065)（第 6065 行）
GET /api/turns/recent 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_state() -> dict[str, Any]](mods/state_journal/app.py#L6078)（第 6078 行）
GET /api/state 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_metrics() -> dict[str, Any]](mods/state_journal/app.py#L6092)（第 6092 行）
GET /api/metrics 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_create_table(request: Request) -> dict[str, Any]](mods/state_journal/app.py#L6100)（第 6100 行）
POST /api/table 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_table(table_id: str) -> dict[str, Any]](mods/state_journal/app.py#L6112)（第 6112 行）
GET /api/table/{table_id} 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_table(table_id: str, request: Request) -> dict[str, Any]](mods/state_journal/app.py#L6122)（第 6122 行）
POST /api/table/{table_id} 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_table_rows_for_response(schema: dict[str, Any]) -> list[dict[str, Any]]](mods/state_journal/app.py#L6136)（第 6136 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_delete_table(table_id: str) -> dict[str, Any]](mods/state_journal/app.py#L6143)（第 6143 行）
DELETE /api/table/{table_id} 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_import(request: Request) -> dict[str, Any]](mods/state_journal/app.py#L6152)（第 6152 行）
POST /api/import 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export() -> JSONResponse](mods/state_journal/app.py#L6173)（第 6173 行）
GET /api/export 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [recent_turn_displays(limit: int = 20) -> list[dict[str, Any]]](mods/state_journal/app.py#L6185)（第 6185 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_latest_display() -> dict[str, Any]](mods/state_journal/app.py#L6222)（第 6222 行）
GET /api/display/latest 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_recent_display(limit: int = 20) -> dict[str, Any]](mods/state_journal/app.py#L6227)（第 6227 行）
GET /api/display/recent 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_latest_log() -> dict[str, Any]](mods/state_journal/app.py#L6234)（第 6234 行）
GET /api/logs/latest 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [redact_secret(value: Any) -> str](mods/state_journal/app.py#L6238)（第 6238 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [load_json_row(value: Any, fallback: Any) -> Any](mods/state_journal/app.py#L6247)（第 6247 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export_debug_log(limit: int = 80) -> JSONResponse](mods/state_journal/app.py#L6255)（第 6255 行）
GET /api/logs/export 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_worker_update(request: Request) -> dict[str, Any]](mods/state_journal/app.py#L6311)（第 6311 行）
POST /api/worker/update 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 26 节 mods/status panel/app.py

### 一览

- **class StatusPanelPayload** (Pydantic BaseModel) — 第 107 行
  - 字段: `settings: dict[str, Any]`, `characters: list[dict[str, Any]]`, `pending_updates: list[dict[str, Any]]`, `processed_update_ids: list[str]`
- **class ApplyUpdatePayload** (Pydantic BaseModel) — 第 114 行
  - 字段: `update: dict[str, Any]`, `mode: str | None`
- **class ResolvePendingPayload** (Pydantic BaseModel) — 第 119 行
  - 字段: `update_id: str`, `action: str`
- **class FieldSchemaPayload** (Pydantic BaseModel) — 第 124 行
  - 字段: `table_columns: list[dict[str, Any]]`, `detail_fields: list[dict[str, Any]]`

- `get_resource_dir()` — 第 18 行
- `normalize_extra_key()` — 第 76 行
- `clone_default()` — 第 137 行
- `read_json()` — 第 141 行
- `write_json()` — 第 151 行
- `migrate_json_once()` — 第 156 行
- `ensure_runtime_data_paths()` — 第 173 行
- `now_string()` — 第 178 行
- `compact_text()` — 第 182 行
- `is_emptyish()` — 第 186 行
- `normalize_list()` — 第 195 行
- `normalize_aliases()` — 第 212 行
- `normalize_mention_key()` — 第 218 行
- `same_mention()` — 第 227 行
- `normalize_extra()` — 第 233 行
- `normalize_field_schema()` — 第 252 行
- `get_field_schema()` — 第 289 行
- `save_field_schema()` — 第 295 行
- `split_pair()` — 第 307 行
- `normalize_character()` — 第 319 行
- `normalize_settings()` — 第 354 行
- `get_state()` — 第 367 行
- `save_state()` — 第 388 行
- `build_status_summary()` — 第 418 行
- `normalize_update()` — 第 455 行
- `find_character()` — 第 497 行
- `ensure_character()` — 第 513 行
- `update_has_risky_fields()` — 第 541 行
- `add_pending_update()` — 第 553 行
- `mark_processed()` — 第 570 行
- `normalize_effect_key()` — 第 592 行
- `should_remove_effect()` — 第 596 行
- `should_clear_effects()` — 第 612 行
- `apply_update_fields()` — 第 620 行
- `apply_update_to_state()` — 第 688 行
- `resolve_pending_update()` — 第 742 行
- `index()` — 第 768 行
- `api_get_state()` — 第 773 行
- `api_save_state()` — 第 778 行
- `api_get_field_schema()` — 第 787 行
- `api_save_field_schema()` — 第 792 行
- `api_get_summary()` — 第 801 行
- `api_apply_update()` — 第 807 行
- `api_pending_updates()` — 第 819 行
- `api_resolve_pending()` — 第 825 行

### 函数详情

#### [get_resource_dir() -> Path](mods/status panel/app.py#L18)（第 18 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_extra_key(key: Any) -> str](mods/status panel/app.py#L76)（第 76 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clone_default(value: Any) -> Any](mods/status panel/app.py#L137)（第 137 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [read_json(path: Path, default: Any) -> Any](mods/status panel/app.py#L141)（第 141 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [write_json(path: Path, payload: Any) -> None](mods/status panel/app.py#L151)（第 151 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [migrate_json_once(primary_path: Path, legacy_path: Path, default: Any) -> None](mods/status panel/app.py#L156)（第 156 行）
Copy legacy mod-local JSON into the project data dir only when needed
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [ensure_runtime_data_paths() -> None](mods/status panel/app.py#L173)（第 173 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [now_string() -> str](mods/status panel/app.py#L178)（第 178 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [compact_text(value: Any) -> str](mods/status panel/app.py#L182)（第 182 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [is_emptyish(value: Any) -> bool](mods/status panel/app.py#L186)（第 186 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_list(value: Any) -> list[str]](mods/status panel/app.py#L195)（第 195 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_aliases(value: Any) -> list[str]](mods/status panel/app.py#L212)（第 212 行）
User configured character aliases. Used for binding, not normal display
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_mention_key(value: Any) -> str](mods/status panel/app.py#L218)（第 218 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [same_mention(left: Any, right: Any) -> bool](mods/status panel/app.py#L227)（第 227 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_extra(value: Any) -> dict[str, str]](mods/status panel/app.py#L233)（第 233 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_field_schema(raw: dict[str, Any] | None) -> dict[str, Any]](mods/status panel/app.py#L252)（第 252 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_field_schema() -> dict[str, Any]](mods/status panel/app.py#L289)（第 289 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_field_schema(payload: dict[str, Any]) -> dict[str, Any]](mods/status panel/app.py#L295)（第 295 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [split_pair(value: Any) -> tuple[str, str]](mods/status panel/app.py#L307)（第 307 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_character(raw: dict[str, Any], index: int) -> dict[str, Any]](mods/status panel/app.py#L319)（第 319 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_settings(raw: dict[str, Any] | None) -> dict[str, Any]](mods/status panel/app.py#L354)（第 354 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_state() -> dict[str, Any]](mods/status panel/app.py#L367)（第 367 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_state(payload: dict[str, Any]) -> dict[str, Any]](mods/status panel/app.py#L388)（第 388 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_status_summary(state: dict[str, Any]) -> str](mods/status panel/app.py#L418)（第 418 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_update(raw: dict[str, Any]) -> dict[str, Any]](mods/status panel/app.py#L455)（第 455 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [find_character(characters: list[dict[str, Any]], update: dict[str, Any]) -> dict[str, Any] | None](mods/status panel/app.py#L497)（第 497 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [ensure_character(characters: list[dict[str, Any]], update: dict[str, Any]) -> dict[str, Any]](mods/status panel/app.py#L513)（第 513 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [update_has_risky_fields(update: dict[str, Any]) -> bool](mods/status panel/app.py#L541)（第 541 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [add_pending_update(state: dict[str, Any], update: dict[str, Any], pending_fields: list[str]) -> None](mods/status panel/app.py#L553)（第 553 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [mark_processed(state: dict[str, Any], update_id: str) -> None](mods/status panel/app.py#L570)（第 570 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_effect_key(value: str) -> str](mods/status panel/app.py#L592)（第 592 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [should_remove_effect(effect: str, remove_item: str) -> bool](mods/status panel/app.py#L596)（第 596 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [should_clear_effects(update: dict[str, Any]) -> bool](mods/status panel/app.py#L612)（第 612 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [apply_update_fields(target: dict[str, Any], update: dict[str, Any]) -> list[str]](mods/status panel/app.py#L620)（第 620 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [apply_update_to_state(state: dict[str, Any], raw_update: dict[str, Any], mode: str) -> dict[str, Any]](mods/status panel/app.py#L688)（第 688 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [resolve_pending_update(state: dict[str, Any], update_id: str, action: str) -> dict[str, Any]](mods/status panel/app.py#L742)（第 742 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [index(request: Request) -> HTMLResponse](mods/status panel/app.py#L768)（第 768 行）
GET / 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_state() -> dict[str, Any]](mods/status panel/app.py#L773)（第 773 行）
GET /api/state 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_state(payload: StatusPanelPayload) -> dict[str, Any]](mods/status panel/app.py#L778)（第 778 行）
POST /api/state 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_field_schema() -> dict[str, Any]](mods/status panel/app.py#L787)（第 787 行）
GET /api/field-schema 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_field_schema(payload: FieldSchemaPayload) -> dict[str, Any]](mods/status panel/app.py#L792)（第 792 行）
POST /api/field-schema 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_summary() -> dict[str, Any]](mods/status panel/app.py#L801)（第 801 行）
GET /api/summary 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_apply_update(payload: ApplyUpdatePayload) -> dict[str, Any]](mods/status panel/app.py#L807)（第 807 行）
POST /api/apply-update 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_pending_updates() -> dict[str, Any]](mods/status panel/app.py#L819)（第 819 行）
GET /api/pending-updates 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_resolve_pending(payload: ResolvePendingPayload) -> dict[str, Any]](mods/status panel/app.py#L825)（第 825 行）
POST /api/pending-updates/resolve 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 27 节 mods/tavern-card-converter/app.py

### 一览

- **class SaveCardPayload** (Pydantic BaseModel) — 第 84 行
  - 字段: `card_json: str`, `filename: str`
- **class SaveWorldbookPayload** (Pydantic BaseModel) — 第 88 行
  - 字段: `worldbook_json: str`, `filename: str`

- `read_upload_bytes()` — 第 67 行
- `strip_chara_metadata()` — 第 97 行
- `_extract_chara_raw()` — 第 109 行
- `extract_tavern_card()` — 第 126 行
- `convert_card_to_xuqi()` — 第 197 行
- `_has_meaningful_card()` — 第 297 行
- `_is_non_empty_tavern_value()` — 第 308 行
- `detect_non_character_content()` — 第 319 行
- `convert_card_general()` — 第 374 行
- `convert_worldbook_to_xuqi()` — 第 482 行
- `page()` — 第 620 行
- `convert_card()` — 第 625 行
- `convert_card_general_endpoint()` — 第 695 行
- `convert_worldbook()` — 第 739 行
- `save_card()` — 第 783 行
- `save_worldbook()` — 第 808 行

### 函数详情

#### [read_upload_bytes(file: UploadFile) -> bytes](mods/tavern-card-converter/app.py#L67)（第 67 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [strip_chara_metadata(file_bytes: bytes) -> bytes](mods/tavern-card-converter/app.py#L97)（第 97 行）
Remove 'chara' iTXt chunk from PNG, returning clean image bytes
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_extract_chara_raw(file_bytes: bytes) -> str | None](mods/tavern-card-converter/app.py#L109)（第 109 行）
Parse PNG chunks directly to find chara data (handles both tEXt and iTXt)
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [extract_tavern_card(file_bytes: bytes) -> tuple[dict, dict]](mods/tavern-card-converter/app.py#L126)（第 126 行）
Extract V2-spec JSON from a tavern PNG via iTXt/tEXt 'chara' chunk
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [convert_card_to_xuqi(tavern_data: dict) -> tuple[dict, list[str]]](mods/tavern-card-converter/app.py#L197)（第 197 行）
Map a V2-spec tavern card dict to Xuqi_LLM role card format
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_has_meaningful_card(src: dict) -> bool](mods/tavern-card-converter/app.py#L297)（第 297 行）
Check if the card has enough character content to be worth converting
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_is_non_empty_tavern_value(value) -> bool](mods/tavern-card-converter/app.py#L308)（第 308 行）
Return True when a SillyTavern extension/top-level value actually carries content
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [detect_non_character_content(src: dict) -> list[dict]](mods/tavern-card-converter/app.py#L319)（第 319 行）
Detect content that pure character conversion will not split out
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [convert_card_general(tavern_data: dict) -> dict](mods/tavern-card-converter/app.py#L374)（第 374 行）
General converter: auto-detects content types and returns named sections
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [convert_worldbook_to_xuqi(tavern_wb: dict) -> tuple[dict, dict]](mods/tavern-card-converter/app.py#L482)（第 482 行）
Convert a SillyTavern worldbook dict to Xuqi_LLM worldbook format
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [page(request: Request)](mods/tavern-card-converter/app.py#L620)（第 620 行）
GET / 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [convert_card(file: UploadFile = File(...))](mods/tavern-card-converter/app.py#L625)（第 625 行）
POST /api/convert/card 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [convert_card_general_endpoint(file: UploadFile = File(...))](mods/tavern-card-converter/app.py#L695)（第 695 行）
POST /api/convert/card/general 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [convert_worldbook(file: UploadFile = File(...))](mods/tavern-card-converter/app.py#L739)（第 739 行）
POST /api/convert/worldbook 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_card(payload: SaveCardPayload)](mods/tavern-card-converter/app.py#L783)（第 783 行）
POST /api/save/card 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_worldbook(payload: SaveWorldbookPayload)](mods/tavern-card-converter/app.py#L808)（第 808 行）
POST /api/save/worldbook 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 28 节 mods/worldbook maker/app.py

### 一览

- **class GenerationSettingsPayload** (Pydantic BaseModel) — 第 232 行
  - 字段: `source_mode: str`, `focus_mode: str`, `target_entry_count: int`, `extra_requirements: str`
- **class AppearanceSettingsPayload** (Pydantic BaseModel) — 第 239 行
  - 字段: `background_image: str`, `background_overlay: float`, `panel_opacity: float`, `blur_strength: int`, `accent_color: str`
- **class SettingsPayload** (Pydantic BaseModel) — 第 247 行
  - 字段: `base_url: str`, `api_key: str`, `model: str`, `temperature: float`, `request_timeout: int`, `system_prompt: str` ... 共 8 个字段
- **class WorkspacePayload** (Pydantic BaseModel) — 第 258 行
  - 字段: `project_name: str`, `source_text: str`, `raw_output: str`
- **class GeneratePayload** — 第 264 行
- **class PreviewPayload** (Pydantic BaseModel) — 第 271 行
  - 字段: `raw_output: str`

- `get_resource_dir()` — 第 18 行
- `ensure_data_files()` — 第 275 行
- `read_json()` — 第 283 行
- `write_json()` — 第 292 行
- `default_worldbook_store()` — 第 297 行
- `default_workspace()` — 第 301 行
- `clamp_float()` — 第 311 行
- `clamp_int()` — 第 319 行
- `sanitize_color()` — 第 327 行
- `sanitize_generation_settings()` — 第 332 行
- `sanitize_appearance_settings()` — 第 351 行
- `sanitize_settings()` — 第 380 行
- `_normalize_entry_type()` — 第 415 行
- `_normalize_group_operator()` — 第 420 行
- `_normalize_insertion_position()` — 第 429 行
- `_normalize_injection_role()` — 第 434 行
- `_normalize_prompt_layer()` — 第 441 行
- `sanitize_worldbook_settings()` — 第 446 行
- `sanitize_worldbook_entry()` — 第 505 行
- `sanitize_worldbook_store()` — 第 596 行
- `dump_worldbook_store()` — 第 621 行
- `build_entry_signature()` — 第 630 行
- `ensure_unique_entry_id()` — 第 639 行
- `merge_worldbook_stores()` — 第 650 行
- `sanitize_workspace()` — 第 688 行
- `get_settings()` — 第 704 行
- `save_settings()` — 第 708 行
- `get_workspace()` — 第 714 行
- `save_workspace()` — 第 718 行
- `build_api_url()` — 第 724 行
- `build_headers()` — 第 733 行
- `extract_json_text()` — 第 740 行
- `parse_store_from_text()` — 第 759 行
- `try_parse_store_from_text()` — 第 768 行
- `summarize_store()` — 第 775 行
- `probe_models_endpoint()` — 第 785 行
- `request_chat_completion()` — 第 822 行
- `build_generation_messages()` — 第 852 行
- `startup_event()` — 第 978 行
- `index()` — 第 983 行
- `api_get_settings()` — 第 1007 行
- `api_save_settings()` — 第 1013 行
- `api_get_workspace()` — 第 1019 行
- `api_save_workspace()` — 第 1026 行
- `api_preview_workspace()` — 第 1059 行
- `api_detect_service()` — 第 1065 行
- `api_generate()` — 第 1111 行

### 函数详情

#### [get_resource_dir() -> Path](mods/worldbook maker/app.py#L18)（第 18 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [ensure_data_files() -> None](mods/worldbook maker/app.py#L275)（第 275 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [read_json(path: Path, default: Any) -> Any](mods/worldbook maker/app.py#L283)（第 283 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [write_json(path: Path, payload: Any) -> None](mods/worldbook maker/app.py#L292)（第 292 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_worldbook_store() -> dict[str, Any]](mods/worldbook maker/app.py#L297)（第 297 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_workspace() -> dict[str, Any]](mods/worldbook maker/app.py#L301)（第 301 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clamp_float(value: Any, minimum: float, maximum: float, default: float) -> float](mods/worldbook maker/app.py#L311)（第 311 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clamp_int(value: Any, minimum: int, maximum: int, default: int) -> int](mods/worldbook maker/app.py#L319)（第 319 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_color(value: Any, default: str) -> str](mods/worldbook maker/app.py#L327)（第 327 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_generation_settings(raw: Any) -> dict[str, Any]](mods/worldbook maker/app.py#L332)（第 332 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_appearance_settings(raw: Any) -> dict[str, Any]](mods/worldbook maker/app.py#L351)（第 351 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_settings(raw: Any) -> dict[str, Any]](mods/worldbook maker/app.py#L380)（第 380 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_entry_type(value: Any, default: str = keyword) -> str](mods/worldbook maker/app.py#L415)（第 415 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_group_operator(value: Any, default: str = and) -> str](mods/worldbook maker/app.py#L420)（第 420 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_insertion_position(value: Any, default: str = after_char_defs) -> str](mods/worldbook maker/app.py#L429)（第 429 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_injection_role(value: Any, default: str = system) -> str](mods/worldbook maker/app.py#L434)（第 434 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_prompt_layer(value: Any, default: str = follow_position) -> str](mods/worldbook maker/app.py#L441)（第 441 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_worldbook_settings(raw: Any) -> dict[str, Any]](mods/worldbook maker/app.py#L446)（第 446 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_worldbook_entry(raw: Any) -> dict[str, Any] | None](mods/worldbook maker/app.py#L505)（第 505 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_worldbook_store(raw: Any) -> dict[str, Any]](mods/worldbook maker/app.py#L596)（第 596 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [dump_worldbook_store(store: Any) -> str](mods/worldbook maker/app.py#L621)（第 621 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_entry_signature(entry: dict[str, Any]) -> tuple[str, str, str, str]](mods/worldbook maker/app.py#L630)（第 630 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [ensure_unique_entry_id(entry_id: Any, used_ids: set[str]) -> str](mods/worldbook maker/app.py#L639)（第 639 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [merge_worldbook_stores(current_store: Any, generated_store: Any) -> tuple[dict[str, Any], dict[str, int]]](mods/worldbook maker/app.py#L650)（第 650 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_workspace(raw: Any) -> dict[str, Any]](mods/worldbook maker/app.py#L688)（第 688 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_settings() -> dict[str, Any]](mods/worldbook maker/app.py#L704)（第 704 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_settings(payload: dict[str, Any]) -> dict[str, Any]](mods/worldbook maker/app.py#L708)（第 708 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_workspace() -> dict[str, Any]](mods/worldbook maker/app.py#L714)（第 714 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_workspace(payload: dict[str, Any]) -> dict[str, Any]](mods/worldbook maker/app.py#L718)（第 718 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_api_url(base_url: str, endpoint: str) -> str](mods/worldbook maker/app.py#L724)（第 724 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_headers(api_key: str) -> dict[str, str]](mods/worldbook maker/app.py#L733)（第 733 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [extract_json_text(raw_text: str) -> str](mods/worldbook maker/app.py#L740)（第 740 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_store_from_text(raw_text: str) -> dict[str, Any]](mods/worldbook maker/app.py#L759)（第 759 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [try_parse_store_from_text(raw_text: str) -> tuple[dict[str, Any] | None, str]](mods/worldbook maker/app.py#L768)（第 768 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [summarize_store(store: dict[str, Any]) -> dict[str, int]](mods/worldbook maker/app.py#L775)（第 775 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [probe_models_endpoint(settings: dict[str, Any]) -> dict[str, Any]](mods/worldbook maker/app.py#L785)（第 785 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [request_chat_completion(settings: dict[str, Any], messages: list[dict[str, str]]) -> str](mods/worldbook maker/app.py#L822)（第 822 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_generation_messages(source_text: str, settings: dict[str, Any]) -> list[dict[str, str]]](mods/worldbook maker/app.py#L852)（第 852 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [startup_event() -> None](mods/worldbook maker/app.py#L978)（第 978 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [index(request: Request) -> HTMLResponse](mods/worldbook maker/app.py#L983)（第 983 行）
GET / 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_settings() -> dict[str, Any]](mods/worldbook maker/app.py#L1007)（第 1007 行）
GET /api/settings 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_settings(payload: SettingsPayload) -> dict[str, Any]](mods/worldbook maker/app.py#L1013)（第 1013 行）
POST /api/settings 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_workspace() -> dict[str, Any]](mods/worldbook maker/app.py#L1019)（第 1019 行）
GET /api/workspace 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_workspace(payload: WorkspacePayload) -> dict[str, Any]](mods/worldbook maker/app.py#L1026)（第 1026 行）
POST /api/workspace/save 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_preview_workspace(payload: PreviewPayload) -> dict[str, Any]](mods/worldbook maker/app.py#L1059)（第 1059 行）
POST /api/workspace/preview 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_detect_service(payload: SettingsPayload) -> dict[str, Any]](mods/worldbook maker/app.py#L1065)（第 1065 行）
POST /api/detect-service 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_generate(payload: GeneratePayload) -> dict[str, Any]](mods/worldbook maker/app.py#L1111)（第 1111 行）
POST /api/generate 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]


