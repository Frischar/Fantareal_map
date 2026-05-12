# Fantareal 项目函数地图

> 本文档由 `scripts/scan_map.py` 自动生成。
> 行号由 AST 实时提取，始终与代码同步。
> 标记为 `[待补充]` 的字段需要在对应函数的 docstring 中补充。

## 目录

- **第 1 节** [fantareal/app.py](#fantareal-app-py)（188 个函数, 1 个类）
- **第 2 节** [fantareal/app_models.py](#fantareal-app_models-py)（48 个类）
- **第 3 节** [fantareal/chat_api_routes.py](#fantareal-chat_api_routes-py)（11 个函数）
- **第 4 节** [fantareal/config_api_routes.py](#fantareal-config_api_routes-py)（71 个函数）
- **第 5 节** [fantareal/launcher.py](#fantareal-launcher-py)（8 个函数）
- **第 6 节** [fantareal/memory_merge_logic.py](#fantareal-memory_merge_logic-py)（25 个函数）
- **第 7 节** [fantareal/mod_api_routes.py](#fantareal-mod_api_routes-py)（3 个函数）
- **第 8 节** [fantareal/mods_runtime.py](#fantareal-mods_runtime-py)（9 个函数, 1 个类）
- **第 9 节** [fantareal/page_routes.py](#fantareal-page_routes-py)（20 个函数）
- **第 10 节** [fantareal/preset_rules.py](#fantareal-preset_rules-py)（25 个函数）
- **第 11 节** [fantareal/prompt_builder.py](#fantareal-prompt_builder-py)（20 个函数）
- **第 12 节** [fantareal/slot_runtime.py](#fantareal-slot_runtime-py)（25 个函数, 1 个类）
- **第 13 节** [fantareal/workshop_logic.py](#fantareal-workshop_logic-py)（32 个函数）
- **第 14 节** [fantareal/worldbook_logic.py](#fantareal-worldbook_logic-py)（19 个函数）
- **第 15 节** [mods/card writer/app.py](#mods-card-writer-app-py)（128 个函数, 7 个类）
- **第 16 节** [mods/soul weaver/app.py](#mods-soul-weaver-app-py)（75 个函数）
- **第 17 节** [mods/status panel/app.py](#mods-status-panel-app-py)（45 个函数, 4 个类）
- **第 18 节** [mods/tavern-card-converter/app.py](#mods-tavern-card-converter-app-py)（14 个函数, 2 个类）
- **第 19 节** [mods/worldbook maker/app.py](#mods-worldbook-maker-app-py)（47 个函数, 6 个类）
- **第 20 节** [mods/xinjian/app.py](#mods-xinjian-app-py)（135 个函数）

## 第 1 节 fantareal/app.py

### 一览

- **class StripAnsiFormatter** — 第 170 行

- `get_runtime_base_dir()` — 第 84 行
- `get_resource_dir()` — 第 101 行
- `flush_log_handlers()` — 第 191 行
- `make_access_style()` — 第 198 行
- `format_access_log()` — 第 208 行
- `resolve_access_label()` — 第 215 行
- `_copy_worldbook_debug_snapshot()` — 第 343 行
- `get_worldbook_debug_snapshot()` — 第 356 行
- `bootstrap_runtime_layout()` — 第 360 行
- `default_slot_registry()` — 第 414 行
- `default_sprite_base_path_for_slot()` — 第 421 行
- `sprite_dir_path()` — 第 425 行
- `sanitize_sprite_filename_tag()` — 第 429 行
- `list_sprite_assets()` — 第 435 行
- `default_role_card()` — 第 456 行
- `default_user_profile()` — 第 531 行
- `default_creative_workshop()` — 第 541 行
- `get_workshop_state()` — 第 545 行
- `save_workshop_state()` — 第 549 行
- `reset_workshop_state()` — 第 559 行
- `workshop_signature()` — 第 563 行
- `resolve_workshop_music_url()` — 第 580 行
- `resolve_workshop_image_url()` — 第 584 行
- `evaluate_creative_workshop()` — 第 588 行
- `default_preset_store()` — 第 678 行
- `sanitize_preset_store()` — 第 682 行
- `preset_path()` — 第 686 行
- `get_preset_store()` — 第 690 行
- `save_preset_store()` — 第 694 行
- `get_active_preset()` — 第 704 行
- `build_preset_prompt()` — 第 708 行
- `get_active_preset_module_labels()` — 第 712 行
- `build_preset_debug_payload()` — 第 722 行
- `load_env_file()` — 第 734 行
- `read_json()` — 第 747 行
- `write_json()` — 第 758 行
- `persist_json()` — 第 766 行
- `parse_bool()` — 第 774 行
- `clamp_int()` — 第 784 行
- `clamp_float()` — 第 792 行
- `sanitize_background_image_url()` — 第 800 行
- `sanitize_font_url()` — 第 820 行
- `sanitize_font_color()` — 第 837 行
- `sanitize_embedding_fields()` — 第 846 行
- `sanitize_settings()` — 第 856 行
- `sanitize_tags()` — 第 906 行
- `sanitize_memories()` — 第 922 行
- `sanitize_slot_id()` — 第 943 行
- `sanitize_legacy_slot_id()` — 第 947 行
- `sanitize_slot_registry()` — 第 954 行
- `get_slot_registry()` — 第 982 行
- `save_slot_registry()` — 第 986 行
- `get_active_slot_id()` — 第 997 行
- `get_slot_name()` — 第 1002 行
- `slot_summary()` — 第 1011 行
- `get_slot_dir()` — 第 1041 行
- `persona_path()` — 第 1046 行
- `legacy_slot_dir()` — 第 1051 行
- `legacy_persona_path()` — 第 1055 行
- `global_persona_path()` — 第 1059 行
- `conversation_path()` — 第 1063 行
- `settings_path()` — 第 1068 行
- `memories_path()` — 第 1073 行
- `worldbook_path()` — 第 1078 行
- `current_card_path()` — 第 1083 行
- `legacy_current_card_path()` — 第 1088 行
- `global_current_card_path()` — 第 1092 行
- `workshop_state_path()` — 第 1096 行
- `user_profile_path()` — 第 1101 行
- `avatar_upload_url()` — 第 1106 行
- `remove_upload_variants()` — 第 1111 行
- `save_image_upload_for_slot()` — 第 1118 行
- `workshop_asset_dir()` — 第 1149 行
- `workshop_asset_url()` — 第 1154 行
- `save_workshop_asset_upload()` — 第 1160 行
- `reset_slot_data()` — 第 1204 行
- `normalize_role_card()` — 第 1218 行
- `extract_persona_name_from_fields()` — 第 1294 行
- `is_legacy_demo_reply()` — 第 1311 行
- `is_garbled_placeholder_message()` — 第 1327 行
- `normalize_legacy_message_content()` — 第 1334 行
- `sanitize_conversation()` — 第 1346 行
- `legacy_active_slot_id()` — 第 1383 行
- `legacy_slot_last_updated()` — 第 1392 行
- `legacy_slot_seed_order()` — 第 1403 行
- `legacy_slot_has_runtime_data()` — 第 1417 行
- `migrate_legacy_avatar_upload()` — 第 1444 行
- `migrate_legacy_sprite_assets()` — 第 1459 行
- `migrate_slot_runtime_to_global_files()` — 第 1478 行
- `slot_looks_uninitialized()` — 第 1530 行
- `has_legacy_root_data()` — 第 1539 行
- `migrate_legacy_root_to_primary_slot()` — 第 1551 行
- `slot_role_state_seed_order()` — 第 1587 行
- `seed_global_role_state()` — 第 1602 行
- `ensure_data_files()` — 第 1657 行
- `get_persona()` — 第 1721 行
- `get_conversation()` — 第 1727 行
- `get_settings()` — 第 1740 行
- `sanitize_user_profile()` — 第 1745 行
- `get_user_profile()` — 第 1769 行
- `save_user_profile()` — 第 1773 行
- `get_role_avatar_url()` — 第 1781 行
- `get_memories()` — 第 1785 行
- `get_worldbook()` — 第 1789 行
- `get_worldbook_store()` — 第 1793 行
- `get_worldbook_entries()` — 第 1797 行
- `get_worldbook_settings()` — 第 1801 行
- `save_memories()` — 第 1805 行
- `save_worldbook()` — 第 1815 行
- `save_worldbook_store()` — 第 1825 行
- `save_worldbook_entries()` — 第 1835 行
- `save_worldbook_settings()` — 第 1841 行
- `get_current_card()` — 第 1847 行
- `list_role_card_files()` — 第 1856 行
- `read_role_card_text()` — 第 1867 行
- `repair_deepseek_card_json()` — 第 1878 行
- `extract_role_card_payload()` — 第 1903 行
- `parse_role_card_json()` — 第 1927 行
- `build_persona_from_role_card()` — 第 1945 行
- `build_memories_from_role_card()` — 第 2029 行
- `apply_role_card()` — 第 2105 行
- `save_workshop_card()` — 第 2144 行
- `sanitize_runtime_overrides()` — 第 2181 行
- `resolve_runtime_value()` — 第 2210 行
- `get_runtime_chat_config()` — 第 2228 行
- `get_runtime_embedding_config()` — 第 2244 行
- `get_runtime_rerank_config()` — 第 2257 行
- `append_messages()` — 第 2270 行
- `build_memory_text()` — 第 2289 行
- `normalize_base_url()` — 第 2302 行
- `build_api_url()` — 第 2306 行
- `build_headers()` — 第 2316 行
- `should_retry_status_code()` — 第 2323 行
- `request_json()` — 第 2329 行
- `fetch_available_models()` — 第 2375 行
- `request_minimal_model_reply()` — 第 2416 行
- `fetch_embeddings()` — 第 2448 行
- `cosine_similarity()` — 第 2475 行
- `rerank_documents()` — 第 2487 行
- `default_worldbook_runtime_state()` — 第 2532 行
- `worldbook_runtime_state_path()` — 第 2536 行
- `sanitize_worldbook_runtime_state()` — 第 2540 行
- `get_worldbook_runtime_state()` — 第 2570 行
- `save_worldbook_runtime_state()` — 第 2574 行
- `_normalize_worldbook_insertion_position()` — 第 2587 行
- `_normalize_worldbook_injection_role()` — 第 2592 行
- `_normalize_worldbook_injection_depth()` — 第 2599 行
- `_normalize_worldbook_injection_order()` — 第 2603 行
- `_normalize_worldbook_prompt_layer()` — 第 2607 行
- `_worldbook_position_priority()` — 第 2612 行
- `_worldbook_global_selection_sort_key()` — 第 2621 行
- `_worldbook_bucket_sort_key()` — 第 2629 行
- `bucket_worldbook_matches()` — 第 2639 行
- `_worldbook_entry_sort_key()` — 第 2670 行
- `_build_worldbook_runtime_debug_entries()` — 第 2677 行
- `_worldbook_alias_match_result()` — 第 2723 行
- `_evaluate_worldbook_keyword_entry()` — 第 2742 行
- `_worldbook_match_payload()` — 第 2792 行
- `_worldbook_recursive_seed_text()` — 第 2837 行
- `_worldbook_runtime_state_row()` — 第 2850 行
- `_worldbook_debug_display_sort_key()` — 第 2862 行
- `match_worldbook_entries()` — 第 2872 行
- `enforce_worldbook_fact_in_reply()` — 第 3080 行
- `normalize_sprite_tag()` — 第 3088 行
- `extract_sprite_tag()` — 第 3106 行
- `_stringify_model_text()` — 第 3159 行
- `extract_reasoning_field()` — 第 3179 行
- `combine_think_parts()` — 第 3190 行
- `normalize_thought_markup()` — 第 3194 行
- `extract_reply_parts()` — 第 3244 行
- `compose_full_reply()` — 第 3300 行
- `extract_stream_visible_reply()` — 第 3310 行
- `retrieve_memories()` — 第 3315 行
- `request_model_reply()` — 第 3362 行
- `build_worldbook_debug_payload()` — 第 3414 行
- `stream_model_reply()` — 第 3477 行
- `generate_reply()` — 第 3632 行
- `fallback_memory_from_conversation()` — 第 3665 行
- `request_conversation_summary_with_model()` — 第 3704 行
- `sanitize_memory_summary()` — 第 3923 行
- `summarize_conversation_to_memory()` — 第 3954 行
- `_get_archive_lock()` — 第 3968 行
- `archive_current_conversation()` — 第 3974 行
- `chinese_access_log()` — 第 4025 行

### 函数详情

#### [get_runtime_base_dir() -> Path](fantareal/app.py#L84)（第 84 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_resource_dir() -> Path](fantareal/app.py#L101)（第 101 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [format(record: logging.LogRecord) -> str（嵌套在 StripAnsiFormatter 内）](fantareal/app.py#L171)（第 171 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [flush_log_handlers() -> None](fantareal/app.py#L191)（第 191 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [make_access_style(label: str, method: str, status_code: int) -> str](fantareal/app.py#L198)（第 198 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [format_access_log(label: str, method: str, status_code: int, mood: str) -> str](fantareal/app.py#L208)（第 208 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [resolve_access_label(method: str, path: str) -> str](fantareal/app.py#L215)（第 215 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_copy_worldbook_debug_snapshot(snapshot: dict[str, Any] | None = None) -> dict[str, Any]](fantareal/app.py#L343)（第 343 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_worldbook_debug_snapshot() -> dict[str, Any]](fantareal/app.py#L356)（第 356 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [bootstrap_runtime_layout() -> None](fantareal/app.py#L360)（第 360 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_slot_registry() -> dict[str, Any]](fantareal/app.py#L414)（第 414 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_sprite_base_path_for_slot(slot_id: str | None = None) -> str](fantareal/app.py#L421)（第 421 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sprite_dir_path(slot_id: str | None = None) -> Path](fantareal/app.py#L425)（第 425 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_sprite_filename_tag(value: str) -> str](fantareal/app.py#L429)（第 429 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [list_sprite_assets(slot_id: str | None = None) -> list[dict[str, Any]]](fantareal/app.py#L435)（第 435 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_role_card() -> dict[str, Any]](fantareal/app.py#L456)（第 456 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_user_profile() -> dict[str, Any]](fantareal/app.py#L531)（第 531 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_creative_workshop() -> dict[str, Any]](fantareal/app.py#L541)（第 541 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_workshop_state(slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L545)（第 545 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_workshop_state(payload: dict[str, Any], slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L549)（第 549 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [reset_workshop_state(slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L559)（第 559 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [workshop_signature(slot: dict[str, Any] | None, workshop: dict[str, Any], stage: str) -> str](fantareal/app.py#L563)（第 563 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [resolve_workshop_music_url(item: dict[str, Any]) -> str](fantareal/app.py#L580)（第 580 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [resolve_workshop_image_url(item: dict[str, Any]) -> str](fantareal/app.py#L584)（第 584 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [evaluate_creative_workshop() -> dict[str, Any]](fantareal/app.py#L588)（第 588 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_preset_store() -> dict[str, Any]](fantareal/app.py#L678)（第 678 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_preset_store(raw: Any) -> dict[str, Any]](fantareal/app.py#L682)（第 682 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [preset_path(slot_id: str | None = None) -> Path](fantareal/app.py#L686)（第 686 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_preset_store(slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L690)（第 690 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_preset_store(payload: dict[str, Any], slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L694)（第 694 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_active_preset(slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L704)（第 704 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_preset_prompt(slot_id: str | None = None) -> str](fantareal/app.py#L708)（第 708 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_active_preset_module_labels(slot_id: str | None = None) -> list[str]](fantareal/app.py#L712)（第 712 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_preset_debug_payload(slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L722)（第 722 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [load_env_file() -> None](fantareal/app.py#L734)（第 734 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [read_json(path: Path, default: Any) -> Any](fantareal/app.py#L747)（第 747 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [write_json(path: Path, payload: Any) -> None](fantareal/app.py#L758)（第 758 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [persist_json(path: Path, payload: Any) -> None](fantareal/app.py#L766)（第 766 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_bool(value: Any, default: bool = False) -> bool](fantareal/app.py#L774)（第 774 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clamp_int(value: Any, minimum: int, maximum: int, default: int) -> int](fantareal/app.py#L784)（第 784 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clamp_float(value: Any, minimum: float, maximum: float, default: float) -> float](fantareal/app.py#L792)（第 792 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_background_image_url(value: Any) -> str](fantareal/app.py#L800)（第 800 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_font_url(value: Any) -> str](fantareal/app.py#L820)（第 820 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_font_color(value: Any) -> str](fantareal/app.py#L837)（第 837 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_embedding_fields(value: Any) -> list[str]](fantareal/app.py#L846)（第 846 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_settings(raw: dict[str, Any] | None) -> dict[str, Any]](fantareal/app.py#L856)（第 856 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_tags(value: Any) -> list[str]](fantareal/app.py#L906)（第 906 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_memories(raw: Any) -> list[dict[str, Any]]](fantareal/app.py#L922)（第 922 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_slot_id(value: Any, default: str | None = None) -> str](fantareal/app.py#L943)（第 943 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_legacy_slot_id(value: Any, default: str | None = None) -> str](fantareal/app.py#L947)（第 947 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_slot_registry(raw: Any) -> dict[str, Any]](fantareal/app.py#L954)（第 954 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_slot_registry() -> dict[str, Any]](fantareal/app.py#L982)（第 982 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_slot_registry(registry: dict[str, Any]) -> dict[str, Any]](fantareal/app.py#L986)（第 986 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_active_slot_id() -> str](fantareal/app.py#L997)（第 997 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_slot_name(slot_id: str | None = None) -> str](fantareal/app.py#L1002)（第 1002 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [slot_summary(slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L1011)（第 1011 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_slot_dir(slot_id: str | None = None) -> Path](fantareal/app.py#L1041)（第 1041 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [persona_path(slot_id: str | None = None) -> Path](fantareal/app.py#L1046)（第 1046 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [legacy_slot_dir(slot_id: str | None = None) -> Path](fantareal/app.py#L1051)（第 1051 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [legacy_persona_path(slot_id: str | None = None) -> Path](fantareal/app.py#L1055)（第 1055 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [global_persona_path() -> Path](fantareal/app.py#L1059)（第 1059 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [conversation_path(slot_id: str | None = None) -> Path](fantareal/app.py#L1063)（第 1063 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [settings_path(slot_id: str | None = None) -> Path](fantareal/app.py#L1068)（第 1068 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [memories_path(slot_id: str | None = None) -> Path](fantareal/app.py#L1073)（第 1073 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [worldbook_path(slot_id: str | None = None) -> Path](fantareal/app.py#L1078)（第 1078 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [current_card_path(slot_id: str | None = None) -> Path](fantareal/app.py#L1083)（第 1083 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [legacy_current_card_path(slot_id: str | None = None) -> Path](fantareal/app.py#L1088)（第 1088 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [global_current_card_path() -> Path](fantareal/app.py#L1092)（第 1092 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [workshop_state_path(slot_id: str | None = None) -> Path](fantareal/app.py#L1096)（第 1096 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [user_profile_path(slot_id: str | None = None) -> Path](fantareal/app.py#L1101)（第 1101 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [avatar_upload_url(filename: str) -> str](fantareal/app.py#L1106)（第 1106 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [remove_upload_variants(prefix: str) -> None](fantareal/app.py#L1111)（第 1111 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_image_upload_for_slot() -> str](fantareal/app.py#L1118)（第 1118 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [workshop_asset_dir(kind: str) -> Path](fantareal/app.py#L1149)（第 1149 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [workshop_asset_url(kind: str, filename: str) -> str](fantareal/app.py#L1154)（第 1154 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_workshop_asset_upload() -> dict[str, Any]](fantareal/app.py#L1160)（第 1160 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [reset_slot_data(slot_id: str) -> dict[str, Any]](fantareal/app.py#L1204)（第 1204 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_role_card(raw: Any) -> dict[str, Any]](fantareal/app.py#L1218)（第 1218 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [extract_persona_name_from_fields() -> str](fantareal/app.py#L1294)（第 1294 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [is_legacy_demo_reply(content: str) -> bool](fantareal/app.py#L1311)（第 1311 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [is_garbled_placeholder_message(content: str) -> bool](fantareal/app.py#L1327)（第 1327 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_legacy_message_content(role: str, content: str) -> str](fantareal/app.py#L1334)（第 1334 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_conversation(raw: Any) -> list[dict[str, Any]]](fantareal/app.py#L1346)（第 1346 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [legacy_active_slot_id() -> str](fantareal/app.py#L1383)（第 1383 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [legacy_slot_last_updated(slot_id: str) -> float](fantareal/app.py#L1392)（第 1392 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [legacy_slot_seed_order() -> list[str]](fantareal/app.py#L1403)（第 1403 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [legacy_slot_has_runtime_data(slot_id: str) -> bool](fantareal/app.py#L1417)（第 1417 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [migrate_legacy_avatar_upload(prefix: str, legacy_slot_id: str) -> None](fantareal/app.py#L1444)（第 1444 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [migrate_legacy_sprite_assets(legacy_slot_id: str) -> None](fantareal/app.py#L1459)（第 1459 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [migrate_slot_runtime_to_global_files() -> None](fantareal/app.py#L1478)（第 1478 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [slot_looks_uninitialized(slot_id: str) -> bool](fantareal/app.py#L1530)（第 1530 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [has_legacy_root_data() -> bool](fantareal/app.py#L1539)（第 1539 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [migrate_legacy_root_to_primary_slot() -> None](fantareal/app.py#L1551)（第 1551 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [slot_role_state_seed_order() -> list[str]](fantareal/app.py#L1587)（第 1587 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [seed_global_role_state() -> None](fantareal/app.py#L1602)（第 1602 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [ensure_data_files() -> None](fantareal/app.py#L1657)（第 1657 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_persona(slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L1721)（第 1721 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_conversation(slot_id: str | None = None) -> list[dict[str, Any]]](fantareal/app.py#L1727)（第 1727 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_settings(slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L1740)（第 1740 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_user_profile(payload: Any) -> dict[str, Any]](fantareal/app.py#L1745)（第 1745 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_user_profile(slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L1769)（第 1769 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_user_profile(payload: dict[str, Any], slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L1773)（第 1773 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_role_avatar_url(slot_id: str | None = None) -> str](fantareal/app.py#L1781)（第 1781 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_memories(slot_id: str | None = None) -> list[dict[str, Any]]](fantareal/app.py#L1785)（第 1785 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_worldbook(slot_id: str | None = None) -> dict[str, str]](fantareal/app.py#L1789)（第 1789 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_worldbook_store(slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L1793)（第 1793 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_worldbook_entries(slot_id: str | None = None) -> list[dict[str, Any]]](fantareal/app.py#L1797)（第 1797 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_worldbook_settings(slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L1801)（第 1801 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_memories(items: list[dict[str, Any]], slot_id: str | None = None) -> list[dict[str, Any]]](fantareal/app.py#L1805)（第 1805 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_worldbook(entries: dict[str, str], slot_id: str | None = None) -> dict[str, str]](fantareal/app.py#L1815)（第 1815 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_worldbook_store(store: dict[str, Any], slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L1825)（第 1825 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_worldbook_entries(entries: list[dict[str, Any]], slot_id: str | None = None) -> list[dict[str, Any]]](fantareal/app.py#L1835)（第 1835 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_worldbook_settings(settings: dict[str, Any], slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L1841)（第 1841 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_current_card(slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L1847)（第 1847 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [list_role_card_files() -> list[dict[str, str]]](fantareal/app.py#L1856)（第 1856 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [read_role_card_text(path: Path) -> str](fantareal/app.py#L1867)（第 1867 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [repair_deepseek_card_json(text: str) -> str](fantareal/app.py#L1878)（第 1878 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [extract_role_card_payload(data: Any) -> dict[str, Any]](fantareal/app.py#L1903)（第 1903 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_role_card_json(text: str) -> dict[str, Any]](fantareal/app.py#L1927)（第 1927 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_persona_from_role_card(card: dict[str, Any]) -> dict[str, str]](fantareal/app.py#L1945)（第 1945 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_memories_from_role_card(card: dict[str, Any]) -> list[dict[str, Any]]](fantareal/app.py#L2029)（第 2029 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [apply_role_card(card: dict[str, Any]) -> dict[str, Any]](fantareal/app.py#L2105)（第 2105 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_workshop_card(workshop: dict[str, Any]) -> dict[str, Any]](fantareal/app.py#L2144)（第 2144 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_runtime_overrides(raw: dict[str, Any] | None) -> dict[str, Any]](fantareal/app.py#L2181)（第 2181 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [resolve_runtime_value(override_value: Any, stored_value: Any, env_key: str | None = None) -> Any](fantareal/app.py#L2210)（第 2210 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_runtime_chat_config(runtime_overrides: dict[str, Any] | None = None) -> dict[str, Any]](fantareal/app.py#L2228)（第 2228 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_runtime_embedding_config(runtime_overrides: dict[str, Any] | None = None) -> dict[str, Any]](fantareal/app.py#L2244)（第 2244 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_runtime_rerank_config(runtime_overrides: dict[str, Any] | None = None) -> dict[str, Any]](fantareal/app.py#L2257)（第 2257 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [append_messages(entries: list[tuple[str, str]]) -> None](fantareal/app.py#L2270)（第 2270 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_memory_text(memory: dict[str, Any], fields: list[str]) -> str](fantareal/app.py#L2289)（第 2289 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_base_url(base_url: str) -> str](fantareal/app.py#L2302)（第 2302 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_api_url(base_url: str, endpoint: str) -> str](fantareal/app.py#L2306)（第 2306 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_headers(api_key: str) -> dict[str, str]](fantareal/app.py#L2316)（第 2316 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [should_retry_status_code(status_code: int) -> bool](fantareal/app.py#L2323)（第 2323 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [request_json() -> dict[str, Any]](fantareal/app.py#L2329)（第 2329 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [fetch_available_models() -> list[str]](fantareal/app.py#L2375)（第 2375 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [request_minimal_model_reply() -> dict[str, Any]](fantareal/app.py#L2416)（第 2416 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [fetch_embeddings(texts: list[str], runtime_overrides: dict[str, Any] | None = None) -> list[list[float]]](fantareal/app.py#L2448)（第 2448 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [cosine_similarity(left: list[float], right: list[float]) -> float](fantareal/app.py#L2475)（第 2475 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [rerank_documents(query: str, documents: list[dict[str, Any]], runtime_overrides: dict[str, Any] | None = None) -> list[dict[str, Any]]](fantareal/app.py#L2487)（第 2487 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_worldbook_runtime_state() -> dict[str, Any]](fantareal/app.py#L2532)（第 2532 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [worldbook_runtime_state_path(slot_id: str | None = None) -> Path](fantareal/app.py#L2536)（第 2536 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_worldbook_runtime_state(raw: Any) -> dict[str, Any]](fantareal/app.py#L2540)（第 2540 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_worldbook_runtime_state(slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L2570)（第 2570 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_worldbook_runtime_state(payload: dict[str, Any], slot_id: str | None = None) -> dict[str, Any]](fantareal/app.py#L2574)（第 2574 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_worldbook_insertion_position(value: Any, default: str = after_char_defs) -> str](fantareal/app.py#L2587)（第 2587 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_worldbook_injection_role(value: Any, default: str = system) -> str](fantareal/app.py#L2592)（第 2592 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_worldbook_injection_depth(value: Any, default: int = 0) -> int](fantareal/app.py#L2599)（第 2599 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_worldbook_injection_order(value: Any, default: int = 100) -> int](fantareal/app.py#L2603)（第 2603 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_worldbook_prompt_layer(value: Any, default: str = follow_position) -> str](fantareal/app.py#L2607)（第 2607 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_worldbook_position_priority(item: dict[str, Any]) -> int](fantareal/app.py#L2612)（第 2612 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_worldbook_global_selection_sort_key(item: dict[str, Any]) -> tuple[int, int, str]](fantareal/app.py#L2621)（第 2621 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_worldbook_bucket_sort_key(item: dict[str, Any]) -> tuple[int, int, str]](fantareal/app.py#L2629)（第 2629 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [bucket_worldbook_matches(matches: list[dict[str, Any]] | None) -> dict[str, Any]](fantareal/app.py#L2639)（第 2639 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_worldbook_entry_sort_key(item: dict[str, Any]) -> tuple[int, int, int, str]](fantareal/app.py#L2670)（第 2670 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_build_worldbook_runtime_debug_entries(current_turn: int, entries: list[dict[str, Any]], runtime_entries: dict[str, dict[str, Any]]) -> list[dict[str, Any]]](fantareal/app.py#L2677)（第 2677 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_worldbook_alias_match_result(text: str, aliases: list[str]) -> tuple[bool, list[str]]](fantareal/app.py#L2723)（第 2723 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_evaluate_worldbook_keyword_entry(text: str, item: dict[str, Any], settings: dict[str, Any]) -> tuple[bool, list[str], list[str], str]](fantareal/app.py#L2742)（第 2742 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_worldbook_match_payload() -> dict[str, Any]](fantareal/app.py#L2792)（第 2792 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_worldbook_recursive_seed_text(item: dict[str, Any]) -> str](fantareal/app.py#L2837)（第 2837 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_worldbook_runtime_state_row(runtime: dict[str, Any]) -> dict[str, Any]](fantareal/app.py#L2850)（第 2850 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_worldbook_debug_display_sort_key(item: dict[str, Any]) -> tuple[int, int, int, int, str]](fantareal/app.py#L2862)（第 2862 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [match_worldbook_entries(query: str) -> list[dict[str, Any]]](fantareal/app.py#L2872)（第 2872 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [enforce_worldbook_fact_in_reply(user_message: str, reply_text: str, matches: list[dict[str, Any]]) -> str](fantareal/app.py#L3080)（第 3080 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_sprite_tag(tag: str) -> str](fantareal/app.py#L3088)（第 3088 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [extract_sprite_tag(reply_text: str) -> tuple[str, str]](fantareal/app.py#L3106)（第 3106 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_stringify_model_text(value: Any) -> str](fantareal/app.py#L3159)（第 3159 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [extract_reasoning_field(payload: Any) -> str](fantareal/app.py#L3179)（第 3179 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [combine_think_parts() -> str](fantareal/app.py#L3190)（第 3190 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_thought_markup(text: str) -> str](fantareal/app.py#L3194)（第 3194 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [extract_reply_parts(raw_text: str) -> dict[str, Any]](fantareal/app.py#L3244)（第 3244 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [compose_full_reply(think_text: str, visible_text: str) -> str](fantareal/app.py#L3300)（第 3300 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [extract_stream_visible_reply(raw_text: str) -> tuple[str, str]](fantareal/app.py#L3310)（第 3310 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [retrieve_memories(query: str, runtime_overrides: dict[str, Any] | None = None) -> list[dict[str, Any]]](fantareal/app.py#L3315)（第 3315 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [request_model_reply(user_message: str, retrieved_items: list[dict[str, Any]]) -> dict[str, Any]](fantareal/app.py#L3362)（第 3362 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_worldbook_debug_payload(user_message: str, worldbook_matches: list[dict[str, str]]) -> dict[str, Any]](fantareal/app.py#L3414)（第 3414 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [stream_model_reply(user_message: str, retrieved_items: list[dict[str, Any]])](fantareal/app.py#L3477)（第 3477 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [generate_reply(user_message: str, runtime_overrides: dict[str, Any] | None = None) -> tuple[dict[str, Any], list[dict[str, Any]], list[dict[str, str]], dict[str, Any], dict[str, Any]]](fantareal/app.py#L3632)（第 3632 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [fallback_memory_from_conversation(history: list[dict[str, Any]]) -> dict[str, Any]](fantareal/app.py#L3665)（第 3665 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：compact_text

#### [compact_text(value: Any, limit: int) -> str（嵌套在 fallback_memory_from_conversation 内）](fantareal/app.py#L3666)（第 3666 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [request_conversation_summary_with_model(history: list[dict[str, Any]]) -> dict[str, Any]](fantareal/app.py#L3704)（第 3704 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：parse_summary_json, is_mostly_english_summary

#### [parse_summary_json(candidate: str) -> dict[str, Any]（嵌套在 request_conversation_summary_with_model 内）](fantareal/app.py#L3737)（第 3737 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [is_mostly_english_summary(payload: dict[str, Any]) -> bool（嵌套在 request_conversation_summary_with_model 内）](fantareal/app.py#L3760)（第 3760 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_memory_summary(payload: dict[str, Any]) -> dict[str, Any]](fantareal/app.py#L3923)（第 3923 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [summarize_conversation_to_memory(history: list[dict[str, Any]]) -> dict[str, Any]](fantareal/app.py#L3954)（第 3954 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_get_archive_lock(slot_id: str) -> asyncio.Lock](fantareal/app.py#L3968)（第 3968 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [archive_current_conversation() -> dict[str, Any]](fantareal/app.py#L3974)（第 3974 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [chinese_access_log(request: Request, call_next)](fantareal/app.py#L4025)（第 4025 行）
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
- **class PersonaPayload** (Pydantic BaseModel) — 第 23 行
  - 字段: `name: str`, `system_prompt: str`, `greeting: str`
- **class SettingsPayload** (Pydantic BaseModel) — 第 29 行
  - 字段: `llm_base_url: str`, `llm_api_key: str`, `llm_model: str`, `theme: str`, `temperature: float`, `history_limit: int` ... 共 30 个字段
- **class MemoryItemPayload** (Pydantic BaseModel) — 第 62 行
  - 字段: `id: str`, `title: str`, `content: str`, `tags: list[str]`, `notes: str`
- **class MemoryListPayload** (Pydantic BaseModel) — 第 70 行
  - 字段: `items: list[MemoryItemPayload]`
- **class MergedMemoryItemPayload** (Pydantic BaseModel) — 第 74 行
  - 字段: `id: str`, `title: str`, `content: str`, `tags: list[str]`, `notes: str`, `source_memory_ids: list[str]` ... 共 7 个字段
- **class MergedMemoryListPayload** (Pydantic BaseModel) — 第 84 行
  - 字段: `items: list[MergedMemoryItemPayload]`
- **class MemoryOutlineItemPayload** (Pydantic BaseModel) — 第 88 行
  - 字段: `id: str`, `title: str`, `summary: str`, `characters: str`, `relationship_progress: str`, `key_events: list[str]` ... 共 12 个字段
- **class MemoryOutlineListPayload** (Pydantic BaseModel) — 第 103 行
  - 字段: `items: list[MemoryOutlineItemPayload]`
- **class MemoryMergePayload** (Pydantic BaseModel) — 第 107 行
  - 字段: `memory_ids: list[str]`, `merged_title: str`, `outline_title: str`, `delete_sources: bool`, `runtime_config: dict[str, Any] | None`
- **class UserProfilePayload** (Pydantic BaseModel) — 第 115 行
  - 字段: `display_name: str`, `nickname: str`, `profile_text: str`, `notes: str`
- **class WorldbookEntryPayload** (Pydantic BaseModel) — 第 122 行
  - 字段: `id: str`, `title: str`, `trigger: str`, `secondary_trigger: str`, `content: str`, `enabled: bool` ... 共 26 个字段
- **class WorldbookSettingsPayload** (Pydantic BaseModel) — 第 162 行
  - 字段: `enabled: bool`, `debug_enabled: bool`, `max_hits: int`, `default_case_sensitive: bool`, `default_whole_word: bool`, `default_match_mode: str` ... 共 19 个字段
- **class WorldbookPayload** (Pydantic BaseModel) — 第 192 行
  - 字段: `items: list[WorldbookEntryPayload]`, `settings: WorldbookSettingsPayload | None`
- **class PresetPromptPayload** (Pydantic BaseModel) — 第 197 行
  - 字段: `id: str`, `name: str`, `enabled: bool`, `content: str`, `order: int`
- **class PresetPromptGroupItemPayload** (Pydantic BaseModel) — 第 205 行
  - 字段: `id: str`, `name: str`, `enabled: bool`, `content: str`
- **class PresetPromptGroupPayload** (Pydantic BaseModel) — 第 212 行
  - 字段: `id: str`, `name: str`, `enabled: bool`, `selection_mode: str`, `selected_ids: list[str]`, `items: list[PresetPromptGroupItemPayload]` ... 共 7 个字段
- **class PresetItemPayload** (Pydantic BaseModel) — 第 222 行
  - 字段: `id: str`, `name: str`, `enabled: bool`, `base_system_prompt: str`, `modules: dict[str, bool]`, `extra_prompts: list[PresetPromptPayload]` ... 共 7 个字段
- **class PresetStorePayload** (Pydantic BaseModel) — 第 232 行
  - 字段: `active_preset_id: str`, `presets: list[PresetItemPayload]`
- **class PresetCreatePayload** (Pydantic BaseModel) — 第 237 行
  - 字段: `name: str`
- **class PresetActionPayload** (Pydantic BaseModel) — 第 241 行
  - 字段: `preset_id: str`
- **class PresetImportPayload** (Pydantic BaseModel) — 第 245 行
  - 字段: `raw_json: str`, `activate_now: bool`
- **class SaveSlotSelectPayload** (Pydantic BaseModel) — 第 250 行
  - 字段: `slot_id: str`
- **class SaveSlotRenamePayload** (Pydantic BaseModel) — 第 254 行
  - 字段: `slot_id: str`, `name: str`
- **class SaveSlotResetPayload** (Pydantic BaseModel) — 第 259 行
  - 字段: `slot_id: str`
- **class SpriteDeletePayload** (Pydantic BaseModel) — 第 263 行
  - 字段: `filename: str`
- **class RoleCardPayload** (Pydantic BaseModel) — 第 267 行
  - 字段: `raw_json: str`, `filename: str`, `apply_now: bool`
- **class RoleCardLoadPayload** (Pydantic BaseModel) — 第 273 行
  - 字段: `filename: str`
- **class JsonImportPayload** (Pydantic BaseModel) — 第 277 行
  - 字段: `raw_json: str`, `apply_settings: bool`, `missing_injection_policy: str`, `force_in_chat_depth: int`, `force_injection_order: int | None`
- **class WorkshopEvaluatePayload** (Pydantic BaseModel) — 第 285 行
  - 字段: `reason: str`, `advance_temp: bool`
- **class WorkshopSavePayload** (Pydantic BaseModel) — 第 290 行
  - 字段: `creativeWorkshop: dict[str, Any]`
- **class SlotMetadata** (Pydantic BaseModel) — 第 294 行
  - 字段: `slot_id: str`, `slot_name: str`, `created_at: str`, `last_updated: str`, `card_id: str`
- **class SlotChatMessage** (Pydantic BaseModel) — 第 302 行
  - 字段: `role: str`, `content: str`, `timestamp: str`
- **class SlotSummaryBuffer** (Pydantic BaseModel) — 第 310 行
  - 字段: `content: str`, `updated_at: str`, `source_message_count: int`
- **class SlotActivePreset** (Pydantic BaseModel) — 第 316 行
  - 字段: `preset_id: str`, `name: str`, `enabled: bool`, `generation_params: dict[str, Any]`, `system_prompt_filter: str`, `prompt_fragments: list[str]` ... 共 7 个字段
- **class SlotVariableStore** (Pydantic BaseModel) — 第 326 行
  - 字段: `favorability: float`, `current_stage: str`, `virtual_time: str`
- **class SlotRuntimeMedia** (Pydantic BaseModel) — 第 334 行
  - 字段: `background_image_url: str`, `background_overlay: float`, `bgm_url: str`, `bgm_preset: str`, `media_note: str`
- **class SlotEnvironmentState** (Pydantic BaseModel) — 第 342 行
  - 字段: `active_preset: SlotActivePreset`, `variable_store: SlotVariableStore`, `runtime_media: SlotRuntimeMedia`
- **class SlotWorldbookContext** (Pydantic BaseModel) — 第 348 行
  - 字段: `unlocked_entry_ids: list[str]`, `active_entry_ids: list[str]`, `last_trigger_terms: list[str]`, `last_injected_at: str`
- **class SlotState** (Pydantic BaseModel) — 第 355 行
  - 字段: `metadata: SlotMetadata`, `chat_history: list[SlotChatMessage]`, `summary_buffer: SlotSummaryBuffer`, `environment_state: SlotEnvironmentState`, `worldbook_context: SlotWorldbookContext`
- **class SlotForkPayload** (Pydantic BaseModel) — 第 363 行
  - 字段: `source_slot_id: str`, `target_slot_id: str`, `target_name: str`, `chat_index: int | None`
- **class SlotSummaryBufferPayload** (Pydantic BaseModel) — 第 370 行
  - 字段: `slot_id: str`, `content: str`, `source_message_count: int | None`
- **class SlotVariablePatchPayload** (Pydantic BaseModel) — 第 376 行
  - 字段: `slot_id: str`, `variables: dict[str, Any]`
- **class DynamicWorldbookPreviewPayload** (Pydantic BaseModel) — 第 381 行
  - 字段: `slot_id: str`, `message: str`, `recent_window: int`
- **class ScenarioBundle** (Pydantic BaseModel) — 第 387 行
  - 字段: `version: int`, `bundle_type: str`, `exported_at: str`, `card_id: str`, `card_payload: dict[str, Any]`, `worldbook_asset: dict[str, Any]` ... 共 12 个字段
- **class ScenarioBundleImportPayload** (Pydantic BaseModel) — 第 402 行
  - 字段: `raw_json: str`, `target_slot_id: str`, `load_card: bool`


## 第 3 节 fantareal/chat_api_routes.py

### 一览

- `register_chat_api_routes()` — 第 11 行

### 函数详情

#### [register_chat_api_routes(app: FastAPI) -> None](fantareal/chat_api_routes.py#L11)（第 11 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：api_get_history, api_edit_user_message, api_reroll_assistant_message, api_chat, api_chat_prompt_preview, api_chat_stream, api_end_conversation, api_reset, api_export_history

#### [api_get_history() -> list[dict[str, Any]]（嵌套在 register_chat_api_routes 内）](fantareal/chat_api_routes.py#L13)（第 13 行）
GET /api/history 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_edit_user_message(payload: ChatHistoryEditRequest) -> dict[str, Any]（嵌套在 register_chat_api_routes 内）](fantareal/chat_api_routes.py#L18)（第 18 行）
POST /api/chat/history/edit-user 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_reroll_assistant_message(payload: ChatHistoryRerollRequest) -> dict[str, Any]（嵌套在 register_chat_api_routes 内）](fantareal/chat_api_routes.py#L45)（第 45 行）
POST /api/chat/history/reroll 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_chat(payload: ChatRequest) -> dict[str, Any]（嵌套在 register_chat_api_routes 内）](fantareal/chat_api_routes.py#L84)（第 84 行）
POST /api/chat 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_chat_prompt_preview(payload: ChatRequest) -> dict[str, Any]（嵌套在 register_chat_api_routes 内）](fantareal/chat_api_routes.py#L123)（第 123 行）
POST /api/chat/prompt-preview 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_chat_stream(payload: ChatRequest) -> StreamingResponse（嵌套在 register_chat_api_routes 内）](fantareal/chat_api_routes.py#L151)（第 151 行）
POST /api/chat/stream 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：event_stream

#### [event_stream()（嵌套在 api_chat_stream 内）](fantareal/chat_api_routes.py#L197)（第 197 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_end_conversation() -> dict[str, Any]（嵌套在 register_chat_api_routes 内）](fantareal/chat_api_routes.py#L244)（第 244 行）
POST /api/conversation/end 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_reset() -> dict[str, Any]（嵌套在 register_chat_api_routes 内）](fantareal/chat_api_routes.py#L270)（第 270 行）
POST /api/reset 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export_history() -> FileResponse（嵌套在 register_chat_api_routes 内）](fantareal/chat_api_routes.py#L280)（第 280 行）
GET /api/export/history 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 4 节 fantareal/config_api_routes.py

### 一览

- `strip_json_comments()` — 第 59 行
- `parse_json_import_payload()` — 第 110 行
- `_worldbook_field_present()` — 第 123 行
- `_apply_worldbook_import_options()` — 第 134 行
- `register_config_api_routes()` — 第 176 行

### 函数详情

#### [strip_json_comments(raw_text: str) -> str](fantareal/config_api_routes.py#L59)（第 59 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_json_import_payload(raw_json: str) -> Any](fantareal/config_api_routes.py#L110)（第 110 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_worldbook_field_present(row: dict[str, Any], key: str) -> bool](fantareal/config_api_routes.py#L123)（第 123 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_apply_worldbook_import_options(entries: list[Any]) -> list[Any]](fantareal/config_api_routes.py#L134)（第 134 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [register_config_api_routes(app: FastAPI) -> None](fantareal/config_api_routes.py#L176)（第 176 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：build_bundle_label, api_get_user_profile, api_save_user_profile, api_upload_user_avatar, api_upload_role_avatar, api_get_preset, api_save_preset, api_create_preset, api_activate_preset, api_duplicate_preset, api_delete_preset, api_export_current_preset, api_import_preset, api_get_persona, api_save_persona, api_get_settings, api_save_settings, api_get_memories, api_export_memories, api_import_memories, api_save_memories, api_get_merged_memories, api_save_merged_memories, api_export_merged_memories, api_get_memory_outline, api_save_memory_outline, api_export_memory_outline, api_export_memory_bundle, api_import_memory_bundle, api_merge_memories, api_get_worldbook, api_export_worldbook, api_import_worldbook, api_save_worldbook, api_get_worldbook_settings, api_save_worldbook_settings, api_get_worldbook_entries, api_save_worldbook_entries, api_preview_dynamic_worldbook, api_get_sprites, api_upload_sprite, api_delete_sprite, api_get_cards, api_import_card, api_load_card, api_export_current_card, api_export_current_bundle, api_import_bundle, api_export_logs, api_get_workshop_status, api_save_workshop, api_evaluate_workshop, api_upload_background, api_upload_font, api_upload_workshop_asset, api_export_workspace_bundle, api_import_workspace_bundle, api_get_models, api_test_connection, api_test_embedding

#### [build_bundle_label() -> tuple[str, dict[str, Any], dict[str, Any]]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L177)（第 177 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_user_profile() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L196)（第 196 行）
GET /api/user-profile 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_user_profile(payload: UserProfilePayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L201)（第 201 行）
POST /api/user-profile 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_upload_user_avatar(file: UploadFile = File(...)) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L207)（第 207 行）
POST /api/user-avatar 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_upload_role_avatar(file: UploadFile = File(...)) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L221)（第 221 行）
POST /api/role-avatar 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_preset() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L239)（第 239 行）
GET /api/preset 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_preset(payload: PresetStorePayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L250)（第 250 行）
POST /api/preset 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_create_preset(payload: PresetCreatePayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L262)（第 262 行）
POST /api/preset/create 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_activate_preset(payload: PresetActionPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L277)（第 277 行）
POST /api/preset/activate 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_duplicate_preset(payload: PresetActionPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L290)（第 290 行）
POST /api/preset/duplicate 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_delete_preset(payload: PresetActionPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L305)（第 305 行）
POST /api/preset/delete 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export_current_preset() -> FileResponse（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L318)（第 318 行）
GET /api/preset/export/current 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_import_preset(payload: PresetImportPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L331)（第 331 行）
POST /api/preset/import 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_persona() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L369)（第 369 行）
GET /api/persona 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_persona(payload: PersonaPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L374)（第 374 行）
POST /api/persona 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_settings() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L387)（第 387 行）
GET /api/settings 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_settings(payload: SettingsPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L396)（第 396 行）
POST /api/settings 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_memories() -> list[dict[str, Any]]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L407)（第 407 行）
GET /api/memories 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export_memories() -> FileResponse（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L412)（第 412 行）
GET /api/memories/export 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_import_memories(payload: JsonImportPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L425)（第 425 行）
POST /api/memories/import 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_memories(payload: MemoryListPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L440)（第 440 行）
POST /api/memories 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_merged_memories() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L447)（第 447 行）
GET /api/memories/merged 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_merged_memories(payload: MergedMemoryListPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L452)（第 452 行）
POST /api/memories/merged 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export_merged_memories() -> FileResponse（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L458)（第 458 行）
GET /api/memories/merged/export 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_memory_outline() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L471)（第 471 行）
GET /api/memories/outline 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_memory_outline(payload: MemoryOutlineListPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L476)（第 476 行）
POST /api/memories/outline 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export_memory_outline() -> FileResponse（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L482)（第 482 行）
GET /api/memories/outline/export 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export_memory_bundle() -> FileResponse（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L496)（第 496 行）
GET /api/memories/export-bundle 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_import_memory_bundle(file: UploadFile = File(...)) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L533)（第 533 行）
POST /api/memories/import-bundle 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：validate_bundle_archive, payload_items, read_bundle_json, clone_rows, ensure_unique_ids, remap_source_ids

#### [validate_bundle_archive(archive: ZipFile) -> None（嵌套在 api_import_memory_bundle 内）](fantareal/config_api_routes.py#L545)（第 545 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [payload_items(payload: Any) -> list[Any]（嵌套在 api_import_memory_bundle 内）](fantareal/config_api_routes.py#L570)（第 570 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [read_bundle_json(archive: ZipFile, entry_name: str) -> list[Any]（嵌套在 api_import_memory_bundle 内）](fantareal/config_api_routes.py#L584)（第 584 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clone_rows(rows: list[Any]) -> list[dict[str, Any]]（嵌套在 api_import_memory_bundle 内）](fantareal/config_api_routes.py#L598)（第 598 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [ensure_unique_ids(rows: list[dict[str, Any]], existing_ids: set[str]) -> tuple[list[dict[str, Any]], dict[str, str]]（嵌套在 api_import_memory_bundle 内）](fantareal/config_api_routes.py#L605)（第 605 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [remap_source_ids(rows: list[dict[str, Any]]) -> None（嵌套在 api_import_memory_bundle 内）](fantareal/config_api_routes.py#L660)（第 660 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_merge_memories(payload: MemoryMergePayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L687)（第 687 行）
POST /api/memories/merge 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_worldbook() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L700)（第 700 行）
GET /api/worldbook 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export_worldbook() -> FileResponse（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L706)（第 706 行）
GET /api/worldbook/export 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_import_worldbook(payload: JsonImportPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L719)（第 719 行）
POST /api/worldbook/import 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_worldbook(payload: WorldbookPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L759)（第 759 行）
POST /api/worldbook 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_worldbook_settings() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L819)（第 819 行）
GET /api/worldbook/settings 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_worldbook_settings(payload: WorldbookSettingsPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L824)（第 824 行）
POST /api/worldbook/settings 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_worldbook_entries() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L830)（第 830 行）
GET /api/worldbook/entries 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_worldbook_entries(payload: WorldbookPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L838)（第 838 行）
POST /api/worldbook/entries 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_preview_dynamic_worldbook(payload: DynamicWorldbookPreviewPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L844)（第 844 行）
POST /api/worldbook/dynamic-preview 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_sprites() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L852)（第 852 行）
GET /api/sprites 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_upload_sprite(tag: str = Form(''), file: UploadFile = File(...)) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L860)（第 860 行）
POST /api/sprites 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_delete_sprite(payload: SpriteDeletePayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L911)（第 911 行）
POST /api/sprites/delete 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_cards() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L937)（第 937 行）
GET /api/cards 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_import_card(payload: RoleCardPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L946)（第 946 行）
POST /api/cards/import 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_load_card(payload: RoleCardLoadPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L967)（第 967 行）
POST /api/cards/load 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export_current_card() -> FileResponse（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L984)（第 984 行）
GET /api/cards/export/current 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export_current_bundle() -> FileResponse（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1009)（第 1009 行）
GET /api/export/current-bundle 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_import_bundle(file: UploadFile = File(...)) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1065)（第 1065 行）
POST /api/import/bundle 端点。导入四卡完整存档 ZIP 包
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export_logs() -> FileResponse（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1141)（第 1141 行）
GET /api/logs/export 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_workshop_status() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1162)（第 1162 行）
GET /api/workshop/status 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_workshop(payload: WorkshopSavePayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1180)（第 1180 行）
POST /api/workshop/save 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_evaluate_workshop(payload: WorkshopEvaluatePayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1193)（第 1193 行）
POST /api/workshop/evaluate 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_upload_background(file: UploadFile = File(...)) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1209)（第 1209 行）
POST /api/background 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_upload_font(file: UploadFile = File(...)) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1237)（第 1237 行）
POST /api/font 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_upload_workshop_asset(kind: str = Form('image'), file: UploadFile = File(...)) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1264)（第 1264 行）
POST /api/workshop/upload 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export_workspace_bundle() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1271)（第 1271 行）
GET /api/workspace/export 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_import_workspace_bundle(payload: JsonImportPayload) -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1294)（第 1294 行）
POST /api/workspace/import 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_models() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1363)（第 1363 行）
POST /api/models 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_test_connection() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1380)（第 1380 行）
POST /api/test-connection 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_test_embedding() -> dict[str, Any]（嵌套在 register_config_api_routes 内）](fantareal/config_api_routes.py#L1389)（第 1389 行）
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



## 第 6 节 fantareal/memory_merge_logic.py

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



## 第 7 节 fantareal/mod_api_routes.py

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



## 第 8 节 fantareal/mods_runtime.py

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



## 第 9 节 fantareal/page_routes.py

### 一览

- `register_page_routes()` — 第 8 行

### 函数详情

#### [register_page_routes(app: FastAPI) -> None](fantareal/page_routes.py#L8)（第 8 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：_opening_message_from_persona, _summary_buffer_content, _has_workshop_progress, _should_show_opening_message, _should_show_workshop_opening, build_chat_template_context, root_redirect, index, config_page, preset_config_page, user_config_page, card_config_page, workshop_config_page, memory_config_page, worldbook_config_page, worldbook_manager_page, sprite_config_page, about_config_page, mod_host_page

#### [_opening_message_from_persona(persona: dict[str, Any]) -> str（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L9)（第 9 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_summary_buffer_content(slot_id: str | None = None) -> str（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L20)（第 20 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_has_workshop_progress(workshop_state: dict[str, Any]) -> bool（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L36)（第 36 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_should_show_opening_message() -> bool（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L46)（第 46 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_should_show_workshop_opening() -> bool（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L62)（第 62 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_chat_template_context() -> dict[str, Any]（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L79)（第 79 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [root_redirect() -> RedirectResponse（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L129)（第 129 行）
GET / 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [index(request: Request) -> HTMLResponse（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L133)（第 133 行）
GET /chat 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [config_page(request: Request) -> HTMLResponse（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L141)（第 141 行）
GET /config 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [preset_config_page(request: Request) -> HTMLResponse（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L153)（第 153 行）
GET /config/preset 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [user_config_page(request: Request) -> HTMLResponse（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L173)（第 173 行）
GET /config/user 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [card_config_page(request: Request) -> HTMLResponse（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L184)（第 184 行）
GET /config/card 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [workshop_config_page(request: Request) -> HTMLResponse（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L206)（第 206 行）
GET /config/workshop 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [memory_config_page(request: Request) -> HTMLResponse（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L225)（第 225 行）
GET /config/memory 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [worldbook_config_page(request: Request) -> HTMLResponse（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L237)（第 237 行）
GET /config/worldbook 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [worldbook_manager_page(request: Request) -> HTMLResponse（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L248)（第 248 行）
GET /config/worldbook/entries 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sprite_config_page(request: Request) -> HTMLResponse（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L261)（第 261 行）
GET /config/sprite 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [about_config_page(request: Request) -> HTMLResponse（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L275)（第 275 行）
GET /config/about 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [mod_host_page(request: Request, mod_slug: str) -> HTMLResponse（嵌套在 register_page_routes 内）](fantareal/page_routes.py#L285)（第 285 行）
GET /mods/{mod_slug} 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 10 节 fantareal/preset_rules.py

### 一览

- `parse_bool()` — 第 198 行
- `parse_int()` — 第 208 行
- `generate_preset_id()` — 第 220 行
- `generate_prompt_group_id()` — 第 224 行
- `generate_prompt_group_item_id()` — 第 228 行
- `default_extra_prompts()` — 第 232 行
- `default_prompt_groups()` — 第 251 行
- `default_single_preset()` — 第 255 行
- `default_preset_store()` — 第 267 行
- `sanitize_prompt_item()` — 第 275 行
- `normalize_selection_mode()` — 第 290 行
- `sanitize_prompt_group_item()` — 第 297 行
- `sanitize_prompt_group()` — 第 311 行
- `apply_module_mutex()` — 第 360 行
- `sanitize_single_preset()` — 第 370 行
- `sanitize_preset_store()` — 第 407 行
- `get_active_preset_from_store()` — 第 434 行
- `build_selected_prompt_group_blocks()` — 第 443 行
- `build_preset_prompt_from_preset()` — 第 473 行
- `build_preset_output_guard_from_preset()` — 第 517 行
- `build_preset_output_guard_from_store()` — 第 528 行
- `create_preset_in_store()` — 第 531 行
- `activate_preset_in_store()` — 第 539 行
- `duplicate_preset_in_store()` — 第 547 行
- `delete_preset_from_store()` — 第 562 行

### 函数详情

#### [parse_bool(value: Any, default: bool = False) -> bool](fantareal/preset_rules.py#L198)（第 198 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_int(value: Any, default: int = 0) -> int](fantareal/preset_rules.py#L208)（第 208 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [generate_preset_id() -> str](fantareal/preset_rules.py#L220)（第 220 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [generate_prompt_group_id() -> str](fantareal/preset_rules.py#L224)（第 224 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [generate_prompt_group_item_id() -> str](fantareal/preset_rules.py#L228)（第 228 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_extra_prompts() -> list[dict[str, Any]]](fantareal/preset_rules.py#L232)（第 232 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_prompt_groups() -> list[dict[str, Any]]](fantareal/preset_rules.py#L251)（第 251 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_single_preset(preset_id: str = preset_default, name: str = 默认预设) -> dict[str, Any]](fantareal/preset_rules.py#L255)（第 255 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_preset_store() -> dict[str, Any]](fantareal/preset_rules.py#L267)（第 267 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_prompt_item(raw: Any, index: int) -> dict[str, Any] | None](fantareal/preset_rules.py#L275)（第 275 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_selection_mode(value: Any) -> str](fantareal/preset_rules.py#L290)（第 290 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_prompt_group_item(raw: Any, index: int) -> dict[str, Any] | None](fantareal/preset_rules.py#L297)（第 297 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_prompt_group(raw: Any, index: int) -> dict[str, Any] | None](fantareal/preset_rules.py#L311)（第 311 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [apply_module_mutex(modules: dict[str, bool]) -> dict[str, bool]](fantareal/preset_rules.py#L360)（第 360 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_single_preset(raw: Any) -> dict[str, Any]](fantareal/preset_rules.py#L370)（第 370 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_preset_store(raw: Any) -> dict[str, Any]](fantareal/preset_rules.py#L407)（第 407 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_active_preset_from_store(store: dict[str, Any]) -> dict[str, Any]](fantareal/preset_rules.py#L434)（第 434 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_selected_prompt_group_blocks(groups: list[dict[str, Any]]) -> list[tuple[int, str]]](fantareal/preset_rules.py#L443)（第 443 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_preset_prompt_from_preset(preset: dict[str, Any]) -> str](fantareal/preset_rules.py#L473)（第 473 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_preset_output_guard_from_preset(preset: dict[str, Any]) -> str](fantareal/preset_rules.py#L517)（第 517 行）
Build a runtime-only guard that should be injected near the current user input
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_preset_output_guard_from_store(store: dict[str, Any]) -> str](fantareal/preset_rules.py#L528)（第 528 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [create_preset_in_store(store: dict[str, Any], name: str) -> dict[str, Any]](fantareal/preset_rules.py#L531)（第 531 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [activate_preset_in_store(store: dict[str, Any], preset_id: str) -> dict[str, Any]](fantareal/preset_rules.py#L539)（第 539 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [duplicate_preset_in_store(store: dict[str, Any], preset_id: str) -> dict[str, Any]](fantareal/preset_rules.py#L547)（第 547 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [delete_preset_from_store(store: dict[str, Any], preset_id: str) -> dict[str, Any]](fantareal/preset_rules.py#L562)（第 562 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 11 节 fantareal/prompt_builder.py

### 一览

- `configure_prompt_builder()` — 第 37 行
- `_dep()` — 第 41 行
- `_optional_dep()` — 第 51 行
- `_extract_runtime_guard_from_preset()` — 第 56 行
- `_worldbook_direct_question()` — 第 64 行
- `build_worldbook_prompt()` — 第 75 行
- `build_worldbook_answer_guard()` — 第 112 行
- `build_retrieval_prompt()` — 第 134 行
- `build_memory_recap_prompt()` — 第 148 行
- `build_user_profile_prompt()` — 第 173 行
- `build_sprite_prompt()` — 第 201 行
- `strip_thought_blocks()` — 第 213 行
- `_same_normalized_text()` — 第 236 行
- `_is_opening_only_message()` — 第 243 行
- `filter_prompt_history()` — 第 270 行
- `build_conversation_transcript()` — 第 275 行
- `build_prompt_package()` — 第 287 行
- `build_messages()` — 第 545 行

### 函数详情

#### [configure_prompt_builder() -> None](fantareal/prompt_builder.py#L37)（第 37 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_dep(name: str) -> Callable[..., Any]](fantareal/prompt_builder.py#L41)（第 41 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_optional_dep(name: str) -> Callable[..., Any] | None](fantareal/prompt_builder.py#L51)（第 51 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_extract_runtime_guard_from_preset(preset_prompt: str) -> tuple[str, str]](fantareal/prompt_builder.py#L56)（第 56 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_worldbook_direct_question(user_message: str) -> bool](fantareal/prompt_builder.py#L64)（第 64 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_worldbook_prompt(matches: list[dict[str, Any]]) -> str](fantareal/prompt_builder.py#L75)（第 75 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_worldbook_answer_guard(user_message: str, matches: list[dict[str, Any]]) -> str](fantareal/prompt_builder.py#L112)（第 112 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_retrieval_prompt(retrieved_items: list[dict[str, Any]]) -> str](fantareal/prompt_builder.py#L134)（第 134 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_memory_recap_prompt(memories: list[dict[str, Any]]) -> str](fantareal/prompt_builder.py#L148)（第 148 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_user_profile_prompt(user_profile: dict[str, Any]) -> str](fantareal/prompt_builder.py#L173)（第 173 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_sprite_prompt(llm_config: dict[str, Any]) -> str](fantareal/prompt_builder.py#L201)（第 201 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [strip_thought_blocks(text: Any) -> str](fantareal/prompt_builder.py#L213)（第 213 行）
Keep stored chat intact, but remove <think>...</think> blocks before building prompts
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_same_normalized_text(left: Any, right: Any) -> bool](fantareal/prompt_builder.py#L236)（第 236 行）
Compare long opening text safely without being too sensitive to whitespace
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_is_opening_only_message(item: dict[str, Any], persona: dict[str, Any] | None = None) -> bool](fantareal/prompt_builder.py#L243)（第 243 行）
Opening/greeting is UI-only. It must not be sent back as chat history context
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [filter_prompt_history(history: list[dict[str, Any]], persona: dict[str, Any] | None = None) -> list[dict[str, Any]]](fantareal/prompt_builder.py#L270)（第 270 行）
Remove UI-only opening messages before building model prompts
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_conversation_transcript(history: list[dict[str, Any]], persona: dict[str, Any] | None = None) -> str](fantareal/prompt_builder.py#L275)（第 275 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_prompt_package(user_message: str, retrieved_items: list[dict[str, Any]] | None = None) -> dict[str, Any]](fantareal/prompt_builder.py#L287)（第 287 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：append_in_chat_bucket, append_layer

#### [append_in_chat_bucket(depth: int) -> None（嵌套在 build_prompt_package 内）](fantareal/prompt_builder.py#L379)（第 379 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [append_layer(layer_id: str, title: str, sections: list[str]) -> None（嵌套在 build_prompt_package 内）](fantareal/prompt_builder.py#L428)（第 428 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_messages(user_message: str, retrieved_items: list[dict[str, Any]] | None = None) -> list[dict[str, str]]](fantareal/prompt_builder.py#L545)（第 545 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 12 节 fantareal/slot_runtime.py

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

#### [build_slot_state(slot_id: str | None = None) -> SlotState（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L203)（第 203 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [persist_slot_state(slot_state: SlotState) -> SlotState（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L254)（第 254 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [upsert_summary_buffer(payload: SlotSummaryBufferPayload) -> SlotState（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L262)（第 262 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [patch_variable_store(payload: SlotVariablePatchPayload) -> SlotState（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L272)（第 272 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_match_aliases(query_text: str, aliases: list[str]) -> tuple[bool, list[str]]（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L280)（第 280 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [resolve_dynamic_worldbook_context(payload: DynamicWorldbookPreviewPayload) -> dict[str, Any]（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L305)（第 305 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_slot_injection_payload(payload: DynamicWorldbookPreviewPayload) -> dict[str, Any]（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L415)（第 415 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_resolve_fork_target(source_slot_id: str, preferred_target: str) -> str（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L437)（第 437 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_rename_slot_if_needed(slot_id: str, target_name: str) -> None（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L447)（第 447 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [fork_slot(payload: SlotForkPayload) -> SlotState（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L458)（第 458 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [export_campaign_bundle(slot_id: str | None = None) -> ScenarioBundle（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L501)（第 501 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [import_campaign_bundle(bundle: ScenarioBundle) -> SlotState（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L520)（第 520 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [import_campaign_bundle_json(raw_json: str) -> SlotState（嵌套在 SlotRuntimeService 内）](fantareal/slot_runtime.py#L565)（第 565 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 13 节 fantareal/workshop_logic.py

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
- `normalize_workshop_stage()` — 第 168 行
- `normalize_workshop_trigger_mode()` — 第 173 行
- `normalize_workshop_action_type()` — 第 178 行
- `normalize_dynamic_trigger_type()` — 第 183 行
- `normalize_dynamic_repeat_mode()` — 第 188 行
- `normalize_dynamic_content_type()` — 第 193 行
- `normalize_dynamic_presentation_mode()` — 第 198 行
- `sanitize_workshop_opening()` — 第 203 行
- `sanitize_workshop_ambience()` — 第 232 行
- `sanitize_dynamic_scene()` — 第 273 行
- `sanitize_creative_workshop_item()` — 第 319 行
- `sanitize_creative_workshop()` — 第 343 行
- `workshop_effective_fields()` — 第 409 行
- `default_workshop_state()` — 第 442 行
- `sanitize_workshop_state()` — 第 455 行
- `get_workshop_stage()` — 第 484 行
- `get_workshop_stage_label()` — 第 494 行
- `workshop_rule_matches_trigger()` — 第 499 行
- `build_workshop_trigger_token()` — 第 510 行
- `get_workshop_trigger_label()` — 第 524 行
- `select_workshop_match()` — 第 537 行

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

#### [normalize_workshop_stage(value: Any) -> str](fantareal/workshop_logic.py#L168)（第 168 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_workshop_trigger_mode(value: Any) -> str](fantareal/workshop_logic.py#L173)（第 173 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_workshop_action_type(value: Any) -> str](fantareal/workshop_logic.py#L178)（第 178 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_dynamic_trigger_type(value: Any) -> str](fantareal/workshop_logic.py#L183)（第 183 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_dynamic_repeat_mode(value: Any) -> str](fantareal/workshop_logic.py#L188)（第 188 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_dynamic_content_type(value: Any) -> str](fantareal/workshop_logic.py#L193)（第 193 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_dynamic_presentation_mode(value: Any) -> str](fantareal/workshop_logic.py#L198)（第 198 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_workshop_opening(raw: Any) -> dict[str, Any]](fantareal/workshop_logic.py#L203)（第 203 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_workshop_ambience(raw: Any) -> dict[str, Any]](fantareal/workshop_logic.py#L232)（第 232 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_dynamic_scene(raw: Any) -> dict[str, Any] | None](fantareal/workshop_logic.py#L273)（第 273 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_creative_workshop_item(raw: Any) -> dict[str, Any] | None](fantareal/workshop_logic.py#L319)（第 319 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_creative_workshop(raw: Any) -> dict[str, Any]](fantareal/workshop_logic.py#L343)（第 343 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [workshop_effective_fields(item: dict[str, Any]) -> dict[str, Any]](fantareal/workshop_logic.py#L409)（第 409 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_workshop_state() -> dict[str, Any]](fantareal/workshop_logic.py#L442)（第 442 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_workshop_state(raw: Any) -> dict[str, Any]](fantareal/workshop_logic.py#L455)（第 455 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_workshop_stage(temp: Any, stage_limits: dict[str, int] | None = None) -> str](fantareal/workshop_logic.py#L484)（第 484 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_workshop_stage_label(stage: str) -> str](fantareal/workshop_logic.py#L494)（第 494 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [workshop_rule_matches_trigger(item: dict[str, Any]) -> bool](fantareal/workshop_logic.py#L499)（第 499 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_workshop_trigger_token(item: dict[str, Any]) -> str](fantareal/workshop_logic.py#L510)（第 510 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_workshop_trigger_label(item: dict[str, Any]) -> str](fantareal/workshop_logic.py#L524)（第 524 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [select_workshop_match(workshop: dict[str, Any]) -> dict[str, Any] | None](fantareal/workshop_logic.py#L537)（第 537 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：sort_key

#### [sort_key(item: dict[str, Any]) -> tuple[int, int]（嵌套在 select_workshop_match 内）](fantareal/workshop_logic.py#L548)（第 548 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 14 节 fantareal/worldbook_logic.py

### 一览

- `default_worldbook_store()` — 第 35 行
- `_clamp_int()` — 第 39 行
- `_normalize_yes_no_bool()` — 第 47 行
- `_normalize_match_mode()` — 第 61 行
- `_normalize_entry_type()` — 第 66 行
- `_normalize_group_operator()` — 第 71 行
- `_normalize_insertion_position()` — 第 80 行
- `_normalize_injection_role()` — 第 85 行
- `_normalize_injection_depth()` — 第 92 行
- `_normalize_injection_order()` — 第 96 行
- `_normalize_prompt_layer()` — 第 100 行
- `_normalize_recursion_depth()` — 第 105 行
- `sanitize_worldbook_settings()` — 第 109 行
- `sanitize_worldbook_entry()` — 第 193 行
- `sanitize_worldbook_store()` — 第 318 行
- `sanitize_worldbook()` — 第 341 行
- `normalize_match_text()` — 第 352 行
- `split_trigger_aliases()` — 第 358 行
- `keyword_matches_query()` — 第 364 行

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

#### [_normalize_group_operator(value: Any, default: str = and) -> str](fantareal/worldbook_logic.py#L71)（第 71 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_insertion_position(value: Any, default: str = after_char_defs) -> str](fantareal/worldbook_logic.py#L80)（第 80 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_injection_role(value: Any, default: str = system) -> str](fantareal/worldbook_logic.py#L85)（第 85 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_injection_depth(value: Any, default: int = 0) -> int](fantareal/worldbook_logic.py#L92)（第 92 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_injection_order(value: Any, default: int = 100) -> int](fantareal/worldbook_logic.py#L96)（第 96 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_prompt_layer(value: Any, default: str = follow_position) -> str](fantareal/worldbook_logic.py#L100)（第 100 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_normalize_recursion_depth(value: Any, default: int = 2) -> int](fantareal/worldbook_logic.py#L105)（第 105 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_worldbook_settings(raw: Any) -> dict[str, Any]](fantareal/worldbook_logic.py#L109)（第 109 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_worldbook_entry(raw: Any) -> dict[str, Any] | None](fantareal/worldbook_logic.py#L193)（第 193 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_worldbook_store(raw: Any) -> dict[str, Any]](fantareal/worldbook_logic.py#L318)（第 318 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_worldbook(raw: Any) -> dict[str, str]](fantareal/worldbook_logic.py#L341)（第 341 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_match_text(value: Any) -> str](fantareal/worldbook_logic.py#L352)（第 352 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [split_trigger_aliases(trigger: Any) -> list[str]](fantareal/worldbook_logic.py#L358)（第 358 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [keyword_matches_query(query_text: str, keyword: str) -> bool](fantareal/worldbook_logic.py#L364)（第 364 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 15 节 mods/card writer/app.py

### 一览

- **class CardWriterProject** (Pydantic BaseModel) — 第 286 行
  - 字段: `version: int`, `type: str`, `title: str`, `persona_card: dict[str, Any]`, `worldbook: dict[str, Any]`, `memory: dict[str, Any]` ... 共 8 个字段
- **class ExportPayload** (Pydantic BaseModel) — 第 297 行
  - 字段: `project: CardWriterProject`, `filename: str`, `target: str`
- **class CopilotSettingsPayload** (Pydantic BaseModel) — 第 303 行
  - 字段: `base_url: str`, `api_key: str`, `model: str`, `request_timeout: int`, `temperature: float`, `base_system_prompt: str` ... 共 10 个字段
- **class CopilotGeneratePayload** (Pydantic BaseModel) — 第 316 行
  - 字段: `project: CardWriterProject`, `module: str`, `prompt: str`, `follow_up: str`, `current_view: str`, `focus_hint: dict[str, Any]` ... 共 7 个字段
- **class CopilotGenerateResponse** (Pydantic BaseModel) — 第 326 行
  - 字段: `ok: bool`, `review_id: str`, `summary: str`, `prompt_used: str`, `current_view: str`, `base_revision: str` ... 共 8 个字段
- **class ProjectStore** — 第 344 行
- **class CardCompiler** — 第 436 行

- `get_resource_dir()` — 第 28 行
- `now_text()` — 第 517 行
- `read_json()` — 第 521 行
- `write_json()` — 第 530 行
- `clamp_float()` — 第 535 行
- `sanitize_copilot_settings()` — 第 543 行
- `get_copilot_settings()` — 第 561 行
- `save_copilot_settings()` — 第 565 行
- `sanitize_filename()` — 第 571 行
- `ensure_project_filename()` — 第 575 行
- `ensure_export_filename()` — 第 580 行
- `make_id()` — 第 585 行
- `create_empty_project()` — 第 589 行
- `split_tags()` — 第 593 行
- `as_bool()` — 第 599 行
- `as_int()` — 第 612 行
- `as_float()` — 第 619 行
- `normalize_text()` — 第 626 行
- `normalize_stage_item()` — 第 630 行
- `normalize_plot_stage_map()` — 第 640 行
- `normalize_persona_single()` — 第 654 行
- `normalize_personas_map()` — 第 662 行
- `normalize_workshop_item()` — 第 678 行
- `normalize_creative_workshop()` — 第 701 行
- `normalize_persona_card()` — 第 710 行
- `normalize_copilot_view()` — 第 722 行
- `build_project_revision()` — 第 729 行
- `normalize_copilot_focus_hint()` — 第 734 行
- `build_copilot_prompt_text()` — 第 785 行
- `get_runtime_llm_config()` — 第 793 行
- `request_copilot_review()` — 第 812 行
- `build_copilot_candidate()` — 第 833 行
- `build_copilot_fingerprint()` — 第 859 行
- `normalize_copilot_target_ref()` — 第 870 行
- `get_persona_main_snapshot()` — 第 882 行
- `find_worldbook_entry()` — 第 887 行
- `find_memory_item()` — 第 895 行
- `find_preset_item()` — 第 903 行
- `build_default_candidate_target()` — 第 911 行
- `build_default_candidate_reason()` — 第 937 行
- `normalize_candidate_action()` — 第 943 行
- `normalize_copilot_candidates()` — 第 956 行
- `get_project_path_value()` — 第 969 行
- `is_allowed_json_patch_path()` — 第 988 行
- `should_keep_patch_value()` — 第 998 行
- `build_json_patch_candidate()` — 第 1010 行
- `persona_replace_to_json_patch_candidates()` — 第 1024 行
- `normalize_json_patch_candidate()` — 第 1048 行
- `normalize_single_copilot_candidate()` — 第 1071 行
- `build_copilot_review_summary()` — 第 1208 行
- `build_copilot_candidate_schema()` — 第 1222 行
- `build_card_writer_json_schema()` — 第 1242 行
- `truncate_preview_text()` — 第 1263 行
- `infer_persona_name()` — 第 1268 行
- `infer_persona_tags()` — 第 1290 行
- `build_fallback_persona_after()` — 第 1312 行
- `generate_copilot_fallback()` — 第 1339 行
- `build_copilot_module_prompt()` — 第 1380 行
- `build_copilot_system_prompt()` — 第 1390 行
- `build_copilot_user_payload()` — 第 1421 行
- `parse_llm_json_text()` — 第 1434 行
- `call_copilot_llm()` — 第 1448 行
- `build_copilot_api_url()` — 第 1482 行
- `build_copilot_headers()` — 第 1492 行
- `request_json_sync()` — 第 1504 行
- `normalize_worldbook_entry()` — 第 1530 行
- `normalize_worldbook()` — 第 1575 行
- `normalize_memory_item()` — 第 1593 行
- `normalize_memory()` — 第 1604 行
- `normalize_extra_prompt()` — 第 1610 行
- `normalize_modules()` — 第 1621 行
- `normalize_preset_item()` — 第 1631 行
- `normalize_preset()` — 第 1646 行
- `normalize_project()` — 第 1659 行
- `normalize_old_project()` — 第 1710 行
- `legacy_worldbook_to_entry()` — 第 1744 行
- `legacy_memory_to_item()` — 第 1776 行
- `legacy_preset_to_item()` — 第 1787 行
- `normalize_legacy_project()` — 第 1800 行
- `parse_basic()` — 第 1829 行
- `parse_plot_stages()` — 第 1845 行
- `parse_personas()` — 第 1870 行
- `extract_section()` — 第 1896 行
- `looks_like_persona_card()` — 第 1906 行
- `looks_like_worldbook()` — 第 1910 行
- `looks_like_memory()` — 第 1914 行
- `looks_like_preset()` — 第 1918 行
- `project_from_payload()` — 第 1922 行
- `normalized_has_content()` — 第 1928 行
- `make_access_style()` — 第 1955 行
- `format_access_log()` — 第 1965 行
- `resolve_access_label()` — 第 1982 行
- `chinese_access_log()` — 第 2001 行
- `startup()` — 第 2023 行
- `index()` — 第 2028 行
- `list_projects()` — 第 2042 行
- `get_project()` — 第 2047 行
- `save_project()` — 第 2052 行
- `delete_project()` — 第 2057 行
- `get_autosave()` — 第 2063 行
- `save_autosave()` — 第 2068 行
- `get_workspace()` — 第 2073 行
- `save_workspace()` — 第 2078 行
- `clear_workspace()` — 第 2083 行
- `api_compile()` — 第 2088 行
- `api_validate()` — 第 2093 行
- `api_get_settings()` — 第 2101 行
- `api_save_settings()` — 第 2106 行
- `api_ai_generate()` — 第 2111 行
- `api_export()` — 第 2116 行
- `api_import_card()` — 第 2128 行

### 函数详情

#### [get_resource_dir() -> Path](mods/card writer/app.py#L28)（第 28 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [__init__(projects_dir: Path, autosaves_dir: Path, exports_dir: Path, workspace_path: Path) -> None（嵌套在 ProjectStore 内）](mods/card writer/app.py#L345)（第 345 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [ensure_dirs() -> None（嵌套在 ProjectStore 内）](mods/card writer/app.py#L351)（第 351 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [list_projects() -> list[dict[str, Any]]（嵌套在 ProjectStore 内）](mods/card writer/app.py#L357)（第 357 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [load_project(filename: str) -> dict[str, Any]（嵌套在 ProjectStore 内）](mods/card writer/app.py#L371)（第 371 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_project(filename: str, project: dict[str, Any]) -> dict[str, Any]（嵌套在 ProjectStore 内）](mods/card writer/app.py#L380)（第 380 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [delete_project(filename: str) -> None（嵌套在 ProjectStore 内）](mods/card writer/app.py#L387)（第 387 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [load_autosave() -> dict[str, Any]（嵌套在 ProjectStore 内）](mods/card writer/app.py#L392)（第 392 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_autosave(project: dict[str, Any]) -> dict[str, Any]（嵌套在 ProjectStore 内）](mods/card writer/app.py#L405)（第 405 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [load_workspace() -> dict[str, Any]（嵌套在 ProjectStore 内）](mods/card writer/app.py#L412)（第 412 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_workspace(project: dict[str, Any]) -> dict[str, Any]（嵌套在 ProjectStore 内）](mods/card writer/app.py#L418)（第 418 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clear_workspace() -> dict[str, Any]（嵌套在 ProjectStore 内）](mods/card writer/app.py#L424)（第 424 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [export_json(filename: str, payload: dict[str, Any]) -> dict[str, Any]（嵌套在 ProjectStore 内）](mods/card writer/app.py#L429)（第 429 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [compile(project: dict[str, Any]) -> dict[str, Any]（嵌套在 CardCompiler 内）](mods/card writer/app.py#L437)（第 437 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [generate_copilot_draft(payload: CopilotGeneratePayload) -> CopilotGenerateResponse（嵌套在 CardCompiler 内）](mods/card writer/app.py#L446)（第 446 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [export_payload(project: dict[str, Any], target: str) -> dict[str, Any]（嵌套在 CardCompiler 内）](mods/card writer/app.py#L474)（第 474 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [validate(project: dict[str, Any], card: dict[str, Any]) -> list[dict[str, Any]]（嵌套在 CardCompiler 内）](mods/card writer/app.py#L487)（第 487 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [import_payload(payload: dict[str, Any]) -> dict[str, Any]（嵌套在 CardCompiler 内）](mods/card writer/app.py#L513)（第 513 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [now_text() -> str](mods/card writer/app.py#L517)（第 517 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [read_json(path: Path, default: Any) -> Any](mods/card writer/app.py#L521)（第 521 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [write_json(path: Path, payload: Any) -> None](mods/card writer/app.py#L530)（第 530 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clamp_float(value: Any, minimum: float, maximum: float, default: float) -> float](mods/card writer/app.py#L535)（第 535 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_copilot_settings(raw: Any) -> dict[str, Any]](mods/card writer/app.py#L543)（第 543 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_copilot_settings() -> dict[str, Any]](mods/card writer/app.py#L561)（第 561 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_copilot_settings(payload: Any) -> dict[str, Any]](mods/card writer/app.py#L565)（第 565 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_filename(name: str) -> str](mods/card writer/app.py#L571)（第 571 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [ensure_project_filename(name: str) -> str](mods/card writer/app.py#L575)（第 575 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [ensure_export_filename(name: str) -> str](mods/card writer/app.py#L580)（第 580 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [make_id(prefix: str) -> str](mods/card writer/app.py#L585)（第 585 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [create_empty_project() -> dict[str, Any]](mods/card writer/app.py#L589)（第 589 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [split_tags(value: str | list[Any]) -> list[str]](mods/card writer/app.py#L593)（第 593 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [as_bool(value: Any, default: bool = False) -> bool](mods/card writer/app.py#L599)（第 599 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [as_int(value: Any, default: int = 0) -> int](mods/card writer/app.py#L612)（第 612 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [as_float(value: Any, default: float = 0.0) -> float](mods/card writer/app.py#L619)（第 619 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_text(value: Any) -> str](mods/card writer/app.py#L626)（第 626 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_stage_item(key: str, stage: Any) -> dict[str, Any]](mods/card writer/app.py#L630)（第 630 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_plot_stage_map(value: Any) -> dict[str, dict[str, Any]]](mods/card writer/app.py#L640)（第 640 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_persona_single(value: Any) -> dict[str, Any]](mods/card writer/app.py#L654)（第 654 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_personas_map(value: Any) -> dict[str, dict[str, Any]]](mods/card writer/app.py#L662)（第 662 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_workshop_item(item: Any, index: int) -> dict[str, Any]](mods/card writer/app.py#L678)（第 678 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_creative_workshop(value: Any) -> dict[str, Any]](mods/card writer/app.py#L701)（第 701 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_persona_card(value: Any) -> dict[str, Any]](mods/card writer/app.py#L710)（第 710 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_copilot_view(value: Any) -> str](mods/card writer/app.py#L722)（第 722 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_project_revision(project: dict[str, Any]) -> str](mods/card writer/app.py#L729)（第 729 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_copilot_focus_hint(raw: Any, project: dict[str, Any], current_view: str) -> dict[str, Any]](mods/card writer/app.py#L734)（第 734 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_copilot_prompt_text(prompt: Any, follow_up: Any) -> str](mods/card writer/app.py#L785)（第 785 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_runtime_llm_config() -> dict[str, Any]](mods/card writer/app.py#L793)（第 793 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [request_copilot_review() -> dict[str, Any]](mods/card writer/app.py#L812)（第 812 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_copilot_candidate() -> dict[str, Any]](mods/card writer/app.py#L833)（第 833 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_copilot_fingerprint(module: str, action: str, target: dict[str, Any], before: Any) -> str](mods/card writer/app.py#L859)（第 859 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_copilot_target_ref(module: str, action: str, raw: Any) -> dict[str, Any]](mods/card writer/app.py#L870)（第 870 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_persona_main_snapshot(project: dict[str, Any]) -> dict[str, Any]](mods/card writer/app.py#L882)（第 882 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [find_worldbook_entry(project: dict[str, Any], entry_id: str) -> tuple[int, dict[str, Any] | None]](mods/card writer/app.py#L887)（第 887 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [find_memory_item(project: dict[str, Any], item_id: str) -> tuple[int, dict[str, Any] | None]](mods/card writer/app.py#L895)（第 895 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [find_preset_item(project: dict[str, Any], item_id: str) -> tuple[int, dict[str, Any] | None]](mods/card writer/app.py#L903)（第 903 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_default_candidate_target(module_name: str, project: dict[str, Any], current_view: str, focus_hint: dict[str, Any]) -> dict[str, Any]](mods/card writer/app.py#L911)（第 911 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_default_candidate_reason(module_name: str, current_view: str) -> str](mods/card writer/app.py#L937)（第 937 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_candidate_action(module_name: str, action: Any) -> str](mods/card writer/app.py#L943)（第 943 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_copilot_candidates(raw_candidates: Any, project: dict[str, Any]) -> list[dict[str, Any]]](mods/card writer/app.py#L956)（第 956 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_project_path_value(project: dict[str, Any], path: str) -> Any](mods/card writer/app.py#L969)（第 969 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [is_allowed_json_patch_path(path: str) -> bool](mods/card writer/app.py#L988)（第 988 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [should_keep_patch_value(value: Any) -> bool](mods/card writer/app.py#L998)（第 998 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_json_patch_candidate(module_name: str, path: str, operation: str, before: Any, after: Any, label: str, reason: str) -> dict[str, Any] | None](mods/card writer/app.py#L1010)（第 1010 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [persona_replace_to_json_patch_candidates(raw: dict[str, Any], project: dict[str, Any], label: str, reason: str) -> list[dict[str, Any]]](mods/card writer/app.py#L1024)（第 1024 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_json_patch_candidate(raw: dict[str, Any], project: dict[str, Any], module_name: str, label: str, reason: str) -> dict[str, Any] | None](mods/card writer/app.py#L1048)（第 1048 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_single_copilot_candidate(raw: Any, project: dict[str, Any]) -> dict[str, Any] | list[dict[str, Any]] | None](mods/card writer/app.py#L1071)（第 1071 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_copilot_review_summary(candidates: list[dict[str, Any]], current_view: str) -> str](mods/card writer/app.py#L1208)（第 1208 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_copilot_candidate_schema() -> dict[str, Any]](mods/card writer/app.py#L1222)（第 1222 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_card_writer_json_schema() -> dict[str, Any]](mods/card writer/app.py#L1242)（第 1242 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [truncate_preview_text(value: Any, limit: int) -> str](mods/card writer/app.py#L1263)（第 1263 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [infer_persona_name(prompt_text: str) -> str](mods/card writer/app.py#L1268)（第 1268 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [infer_persona_tags(prompt_text: str, name: str) -> list[str]](mods/card writer/app.py#L1290)（第 1290 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_fallback_persona_after(prompt_text: str, project: dict[str, Any]) -> dict[str, Any]](mods/card writer/app.py#L1312)（第 1312 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [generate_copilot_fallback(prompt_text: str, current_view: str, focus_hint: dict[str, Any], project: dict[str, Any]) -> dict[str, Any]](mods/card writer/app.py#L1339)（第 1339 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_copilot_module_prompt(module_name: str, settings: dict[str, Any]) -> str](mods/card writer/app.py#L1380)（第 1380 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_copilot_system_prompt(current_view: str, focus_hint: dict[str, Any], settings: dict[str, Any]) -> str](mods/card writer/app.py#L1390)（第 1390 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_copilot_user_payload(prompt_text: str, focus_hint: dict[str, Any], project: dict[str, Any], project_revision: str, current_view: str) -> str](mods/card writer/app.py#L1421)（第 1421 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_llm_json_text(raw_text: str) -> dict[str, Any]](mods/card writer/app.py#L1434)（第 1434 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [call_copilot_llm() -> dict[str, Any]](mods/card writer/app.py#L1448)（第 1448 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_copilot_api_url(base_url: str, endpoint: str) -> str](mods/card writer/app.py#L1482)（第 1482 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_copilot_headers(api_key: str) -> dict[str, str]](mods/card writer/app.py#L1492)（第 1492 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [request_json_sync() -> dict[str, Any]](mods/card writer/app.py#L1504)（第 1504 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_worldbook_entry(value: Any, index: int) -> dict[str, Any]](mods/card writer/app.py#L1530)（第 1530 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_worldbook(value: Any) -> dict[str, Any]](mods/card writer/app.py#L1575)（第 1575 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_memory_item(value: Any, index: int) -> dict[str, Any]](mods/card writer/app.py#L1593)（第 1593 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_memory(value: Any) -> dict[str, Any]](mods/card writer/app.py#L1604)（第 1604 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_extra_prompt(value: Any, index: int) -> dict[str, Any]](mods/card writer/app.py#L1610)（第 1610 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_modules(value: Any) -> dict[str, bool]](mods/card writer/app.py#L1621)（第 1621 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_preset_item(value: Any, index: int) -> dict[str, Any]](mods/card writer/app.py#L1631)（第 1631 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_preset(value: Any) -> dict[str, Any]](mods/card writer/app.py#L1646)（第 1646 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_project(payload: Any) -> dict[str, Any]](mods/card writer/app.py#L1659)（第 1659 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_old_project(payload: dict[str, Any]) -> dict[str, Any]](mods/card writer/app.py#L1710)（第 1710 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [legacy_worldbook_to_entry(item: Any, index: int) -> dict[str, Any]](mods/card writer/app.py#L1744)（第 1744 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [legacy_memory_to_item(item: Any, index: int) -> dict[str, Any]](mods/card writer/app.py#L1776)（第 1776 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [legacy_preset_to_item(item: Any, index: int) -> dict[str, Any]](mods/card writer/app.py#L1787)（第 1787 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_legacy_project(payload: dict[str, Any]) -> dict[str, Any]](mods/card writer/app.py#L1800)（第 1800 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_basic(content: str) -> dict[str, Any]](mods/card writer/app.py#L1829)（第 1829 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_plot_stages(content: str) -> list[dict[str, Any]]](mods/card writer/app.py#L1845)（第 1845 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_personas(content: str) -> list[dict[str, Any]]](mods/card writer/app.py#L1870)（第 1870 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [extract_section(body: str, label: str, next_labels: list[str]) -> str](mods/card writer/app.py#L1896)（第 1896 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [looks_like_persona_card(payload: dict[str, Any]) -> bool](mods/card writer/app.py#L1906)（第 1906 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [looks_like_worldbook(payload: dict[str, Any]) -> bool](mods/card writer/app.py#L1910)（第 1910 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [looks_like_memory(payload: dict[str, Any]) -> bool](mods/card writer/app.py#L1914)（第 1914 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [looks_like_preset(payload: dict[str, Any]) -> bool](mods/card writer/app.py#L1918)（第 1918 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [project_from_payload(payload: dict[str, Any]) -> dict[str, Any]](mods/card writer/app.py#L1922)（第 1922 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalized_has_content(project: dict[str, Any]) -> bool](mods/card writer/app.py#L1928)（第 1928 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [make_access_style(label: str, method: str, status_code: int) -> str](mods/card writer/app.py#L1955)（第 1955 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [format_access_log(label: str, method: str, status_code: int, mood: str) -> str](mods/card writer/app.py#L1965)（第 1965 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [resolve_access_label(method: str, path: str) -> str](mods/card writer/app.py#L1982)（第 1982 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [chinese_access_log(request: Request, call_next)](mods/card writer/app.py#L2001)（第 2001 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [startup() -> None](mods/card writer/app.py#L2023)（第 2023 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [index(request: Request)](mods/card writer/app.py#L2028)（第 2028 行）
GET / 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [list_projects() -> dict[str, Any]](mods/card writer/app.py#L2042)（第 2042 行）
GET /api/projects 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_project(filename: str) -> dict[str, Any]](mods/card writer/app.py#L2047)（第 2047 行）
GET /api/projects/{filename} 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_project(filename: str, payload: CardWriterProject) -> dict[str, Any]](mods/card writer/app.py#L2052)（第 2052 行）
POST /api/projects/{filename} 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [delete_project(filename: str) -> dict[str, Any]](mods/card writer/app.py#L2057)（第 2057 行）
DELETE /api/projects/{filename} 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_autosave() -> dict[str, Any]](mods/card writer/app.py#L2063)（第 2063 行）
GET /api/autosave 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_autosave(payload: CardWriterProject) -> dict[str, Any]](mods/card writer/app.py#L2068)（第 2068 行）
POST /api/autosave 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_workspace() -> dict[str, Any]](mods/card writer/app.py#L2073)（第 2073 行）
GET /api/workspace 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_workspace(payload: CardWriterProject) -> dict[str, Any]](mods/card writer/app.py#L2078)（第 2078 行）
POST /api/workspace 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clear_workspace() -> dict[str, Any]](mods/card writer/app.py#L2083)（第 2083 行）
DELETE /api/workspace 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_compile(payload: CardWriterProject) -> dict[str, Any]](mods/card writer/app.py#L2088)（第 2088 行）
POST /api/compile 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_validate(payload: CardWriterProject) -> dict[str, Any]](mods/card writer/app.py#L2093)（第 2093 行）
POST /api/validate 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_settings() -> dict[str, Any]](mods/card writer/app.py#L2101)（第 2101 行）
GET /api/settings 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_settings(payload: CopilotSettingsPayload) -> dict[str, Any]](mods/card writer/app.py#L2106)（第 2106 行）
POST /api/settings 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_ai_generate(payload: CopilotGeneratePayload) -> dict[str, Any]](mods/card writer/app.py#L2111)（第 2111 行）
POST /api/ai/generate 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export(payload: ExportPayload) -> Response](mods/card writer/app.py#L2116)（第 2116 行）
POST /api/export 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_import_card(payload: dict[str, Any]) -> dict[str, Any]](mods/card writer/app.py#L2128)（第 2128 行）
POST /api/import-card 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 16 节 mods/soul weaver/app.py

### 一览

- `get_resource_dir()` — 第 22 行
- `ensure_data_files()` — 第 452 行
- `read_json()` — 第 460 行
- `write_json()` — 第 469 行
- `clamp_float()` — 第 474 行
- `clamp_int()` — 第 482 行
- `parse_positive_int()` — 第 490 行
- `sanitize_settings()` — 第 508 行
- `normalize_speaker_name()` — 第 521 行
- `normalize_target_character()` — 第 534 行
- `sanitize_filename()` — 第 542 行
- `unique_path()` — 第 549 行
- `parse_script_line()` — 第 561 行
- `entry_to_script_line()` — 第 569 行
- `summarize_chunk()` — 第 575 行
- `build_entry_chunks()` — 第 584 行
- `build_speaker_chunks()` — 第 639 行
- `summarize_speaker_chunks()` — 第 664 行
- `build_text_chunks()` — 第 671 行
- `parse_script_entries()` — 第 691 行
- `extract_character_lines()` — 第 756 行
- `extract_character_chunks()` — 第 771 行
- `get_settings()` — 第 783 行
- `save_settings()` — 第 787 行
- `request_settings()` — 第 801 行
- `get_drafts()` — 第 810 行
- `save_draft()` — 第 815 行
- `build_api_url()` — 第 822 行
- `build_headers()` — 第 831 行
- `get_wbmaker_module()` — 第 838 行
- `build_wbmaker_settings()` — 第 853 行
- `generate_worldbook_with_wbmaker()` — 第 873 行
- `merge_worldbook_partials_with_wbmaker()` — 第 890 行
- `extract_json_text()` — 第 908 行
- `try_parse_json()` — 第 927 行
- `split_text()` — 第 938 行
- `request_chat_completion()` — 第 959 行
- `generate_with_segments()` — 第 997 行
- `normalize_role_card()` — 第 1075 行
- `normalize_single_preset()` — 第 1165 行
- `normalize_preset()` — 第 1259 行
- `normalize_memories()` — 第 1288 行
- `normalize_worldbook()` — 第 1302 行
- `startup_event()` — 第 1354 行
- `index()` — 第 1359 行
- `api_get_settings()` — 第 1376 行
- `api_save_settings()` — 第 1382 行
- `api_get_drafts()` — 第 1388 行
- `api_parse_script()` — 第 1393 行
- `api_probe_models()` — 第 1447 行
- `api_generate_role_card()` — 第 1486 行
- `api_generate_memory()` — 第 1524 行
- `api_generate_plot()` — 第 1562 行
- `api_generate_preset()` — 第 1598 行
- `api_generate_worldbook()` — 第 1636 行
- `task_system_prompt()` — 第 1669 行
- `task_draft_type()` — 第 1682 行
- `normalize_task_result()` — 第 1692 行
- `build_chunk_user()` — 第 1704 行
- `build_merge_user()` — 第 1728 行
- `api_generate_chunk()` — 第 1743 行
- `api_generate_merge()` — 第 1787 行
- `_proxy_import()` — 第 1858 行
- `api_import_card()` — 第 1870 行
- `api_import_preset()` — 第 1883 行
- `api_import_memories()` — 第 1895 行
- `api_import_worldbook()` — 第 1906 行
- `api_export_soul()` — 第 1919 行
- `api_export_soul_local()` — 第 1974 行

### 函数详情

#### [get_resource_dir() -> Path](mods/soul weaver/app.py#L22)（第 22 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [ensure_data_files() -> None](mods/soul weaver/app.py#L452)（第 452 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [read_json(path: Path, default: Any) -> Any](mods/soul weaver/app.py#L460)（第 460 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [write_json(path: Path, payload: Any) -> None](mods/soul weaver/app.py#L469)（第 469 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clamp_float(value: Any, minimum: float, maximum: float, default: float) -> float](mods/soul weaver/app.py#L474)（第 474 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clamp_int(value: Any, minimum: int, maximum: int, default: int) -> int](mods/soul weaver/app.py#L482)（第 482 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_positive_int(value: Any, default: int = 0) -> int](mods/soul weaver/app.py#L490)（第 490 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_settings(raw: Any) -> dict[str, Any]](mods/soul weaver/app.py#L508)（第 508 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_speaker_name(value: Any) -> str](mods/soul weaver/app.py#L521)（第 521 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_target_character(value: Any) -> str](mods/soul weaver/app.py#L534)（第 534 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sanitize_filename(value: Any, fallback: str = yusheng) -> str](mods/soul weaver/app.py#L542)（第 542 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [unique_path(path: Path) -> Path](mods/soul weaver/app.py#L549)（第 549 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_script_line(line: str) -> tuple[str, str] | None](mods/soul weaver/app.py#L561)（第 561 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [entry_to_script_line(entry: dict[str, Any]) -> str](mods/soul weaver/app.py#L569)（第 569 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [summarize_chunk(chunk: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L575)（第 575 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_entry_chunks(entries: list[dict[str, Any]], target_lines: int = CHUNK_TARGET_LINES) -> list[dict[str, Any]]](mods/soul weaver/app.py#L584)（第 584 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：flush

#### [flush() -> None（嵌套在 build_entry_chunks 内）](mods/soul weaver/app.py#L599)（第 599 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_speaker_chunks(entries: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]](mods/soul weaver/app.py#L639)（第 639 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [summarize_speaker_chunks(speaker_chunks: dict[str, list[dict[str, Any]]]) -> dict[str, list[dict[str, Any]]]](mods/soul weaver/app.py#L664)（第 664 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_text_chunks(text: str, prefix: str = chunk, target_lines: int = TEXT_CHUNK_TARGET_LINES) -> list[dict[str, Any]]](mods/soul weaver/app.py#L671)（第 671 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_script_entries(source_text: str) -> dict[str, Any]](mods/soul weaver/app.py#L691)（第 691 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [extract_character_lines(parsed: dict[str, Any], character_name: str) -> str](mods/soul weaver/app.py#L756)（第 756 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [extract_character_chunks(parsed: dict[str, Any], character_name: str) -> list[dict[str, Any]]](mods/soul weaver/app.py#L771)（第 771 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_settings() -> dict[str, Any]](mods/soul weaver/app.py#L783)（第 783 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_settings(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L787)（第 787 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [request_settings(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L801)（第 801 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_drafts() -> list[dict[str, Any]]](mods/soul weaver/app.py#L810)（第 810 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_draft(draft: dict[str, Any]) -> None](mods/soul weaver/app.py#L815)（第 815 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_api_url(base_url: str, endpoint: str) -> str](mods/soul weaver/app.py#L822)（第 822 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_headers(api_key: str) -> dict[str, str]](mods/soul weaver/app.py#L831)（第 831 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_wbmaker_module() -> Any](mods/soul weaver/app.py#L838)（第 838 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_wbmaker_settings(payload_settings: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L853)（第 853 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [generate_worldbook_with_wbmaker(settings: dict[str, Any], source_text: str, current_store: Any | None = None) -> dict[str, Any]](mods/soul weaver/app.py#L873)（第 873 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [merge_worldbook_partials_with_wbmaker(partials: list[Any]) -> dict[str, Any]](mods/soul weaver/app.py#L890)（第 890 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [extract_json_text(raw_text: str) -> str](mods/soul weaver/app.py#L908)（第 908 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [try_parse_json(raw_text: str) -> tuple[dict[str, Any] | None, str]](mods/soul weaver/app.py#L927)（第 927 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [split_text(text: str, segment_length: int = SEGMENT_LENGTH) -> list[str]](mods/soul weaver/app.py#L938)（第 938 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [request_chat_completion(settings: dict[str, Any], messages: list[dict[str, str]]) -> str](mods/soul weaver/app.py#L959)（第 959 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [generate_with_segments(settings: dict[str, Any], source_text: str, system_prompt: str, build_user_msg) -> tuple[str, list[str]]](mods/soul weaver/app.py#L997)（第 997 行）
Handle long text with segmentation. Returns (final_output, warnings)
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_role_card(raw: dict[str, Any], character_name: str) -> dict[str, Any]](mods/soul weaver/app.py#L1075)（第 1075 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_single_preset(raw: dict[str, Any], character_name: str) -> dict[str, Any]](mods/soul weaver/app.py#L1165)（第 1165 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_preset(raw: dict[str, Any], character_name: str) -> dict[str, Any]](mods/soul weaver/app.py#L1259)（第 1259 行）
Return the same preset-store shape used by Fantareal preset exports
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_memories(raw: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1288)（第 1288 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_worldbook(raw: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1302)（第 1302 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [startup_event() -> None](mods/soul weaver/app.py#L1354)（第 1354 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [index(request: Request) -> HTMLResponse](mods/soul weaver/app.py#L1359)（第 1359 行）
GET / 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_settings() -> dict[str, Any]](mods/soul weaver/app.py#L1376)（第 1376 行）
GET /api/settings 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_settings(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1382)（第 1382 行）
POST /api/settings 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_drafts() -> dict[str, Any]](mods/soul weaver/app.py#L1388)（第 1388 行）
GET /api/drafts 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_parse_script(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1393)（第 1393 行）
POST /api/parse-script 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_probe_models(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1447)（第 1447 行）
POST /api/probe-models 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_generate_role_card(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1486)（第 1486 行）
POST /api/generate/role-card 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：build_user

#### [build_user(text: str) -> str（嵌套在 api_generate_role_card 内）](mods/soul weaver/app.py#L1494)（第 1494 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_generate_memory(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1524)（第 1524 行）
POST /api/generate/memory 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：build_user

#### [build_user(text: str) -> str（嵌套在 api_generate_memory 内）](mods/soul weaver/app.py#L1532)（第 1532 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_generate_plot(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1562)（第 1562 行）
POST /api/generate/plot 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：build_user

#### [build_user(text: str) -> str（嵌套在 api_generate_plot 内）](mods/soul weaver/app.py#L1570)（第 1570 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_generate_preset(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1598)（第 1598 行）
POST /api/generate/preset 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：build_user

#### [build_user(text: str) -> str（嵌套在 api_generate_preset 内）](mods/soul weaver/app.py#L1606)（第 1606 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_generate_worldbook(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1636)（第 1636 行）
POST /api/generate/worldbook 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：build_user

#### [build_user(text: str) -> str（嵌套在 api_generate_worldbook 内）](mods/soul weaver/app.py#L1643)（第 1643 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [task_system_prompt(task: str) -> str](mods/soul weaver/app.py#L1669)（第 1669 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [task_draft_type(task: str) -> str](mods/soul weaver/app.py#L1682)（第 1682 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_task_result(task: str, parsed: dict[str, Any], character_name: str) -> dict[str, Any]](mods/soul weaver/app.py#L1692)（第 1692 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_chunk_user(task: str, source_text: str, character_name: str, chunk_meta: dict[str, Any], context: Any) -> str](mods/soul weaver/app.py#L1704)（第 1704 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_merge_user(task: str, partials: list[Any], character_name: str, context: Any) -> str](mods/soul weaver/app.py#L1728)（第 1728 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_generate_chunk(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1743)（第 1743 行）
POST /api/generate/chunk 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_generate_merge(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1787)（第 1787 行）
POST /api/generate/merge 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [_proxy_import(main_base_url: str, endpoint: str, payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1858)（第 1858 行）
内部函数。参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_import_card(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1870)（第 1870 行）
POST /api/import/card 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_import_preset(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1883)（第 1883 行）
POST /api/import/preset 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_import_memories(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1895)（第 1895 行）
POST /api/import/memories 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_import_worldbook(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1906)（第 1906 行）
POST /api/import/worldbook 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export_soul(payload: dict[str, Any]) -> FileResponse](mods/soul weaver/app.py#L1919)（第 1919 行）
POST /api/export/soul 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export_soul_local(payload: dict[str, Any]) -> dict[str, Any]](mods/soul weaver/app.py#L1974)（第 1974 行）
POST /api/export/soul-local 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 17 节 mods/status panel/app.py

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



## 第 18 节 mods/tavern-card-converter/app.py

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
- `_has_meaningful_card()` — 第 298 行
- `convert_card_general()` — 第 309 行
- `convert_worldbook_to_xuqi()` — 第 417 行
- `page()` — 第 555 行
- `convert_card()` — 第 560 行
- `convert_card_general_endpoint()` — 第 622 行
- `convert_worldbook()` — 第 666 行
- `save_card()` — 第 710 行
- `save_worldbook()` — 第 735 行

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

#### [_has_meaningful_card(src: dict) -> bool](mods/tavern-card-converter/app.py#L298)（第 298 行）
Check if the card has enough character content to be worth converting
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [convert_card_general(tavern_data: dict) -> dict](mods/tavern-card-converter/app.py#L309)（第 309 行）
General converter: auto-detects content types and returns named sections
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [convert_worldbook_to_xuqi(tavern_wb: dict) -> tuple[dict, dict]](mods/tavern-card-converter/app.py#L417)（第 417 行）
Convert a SillyTavern worldbook dict to Xuqi_LLM worldbook format
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [page(request: Request)](mods/tavern-card-converter/app.py#L555)（第 555 行）
GET / 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [convert_card(file: UploadFile = File(...))](mods/tavern-card-converter/app.py#L560)（第 560 行）
POST /api/convert/card 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [convert_card_general_endpoint(file: UploadFile = File(...))](mods/tavern-card-converter/app.py#L622)（第 622 行）
POST /api/convert/card/general 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [convert_worldbook(file: UploadFile = File(...))](mods/tavern-card-converter/app.py#L666)（第 666 行）
POST /api/convert/worldbook 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_card(payload: SaveCardPayload)](mods/tavern-card-converter/app.py#L710)（第 710 行）
POST /api/save/card 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_worldbook(payload: SaveWorldbookPayload)](mods/tavern-card-converter/app.py#L735)（第 735 行）
POST /api/save/worldbook 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]



## 第 19 节 mods/worldbook maker/app.py

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



## 第 20 节 mods/xinjian/app.py

### 一览

- `get_resource_dir()` — 第 22 行
- `now_string()` — 第 256 行
- `clone_json()` — 第 260 行
- `hash_text()` — 第 264 行
- `normalize_turn_id()` — 第 269 行
- `read_json()` — 第 275 行
- `write_json()` — 第 285 行
- `safe_id()` — 第 290 行
- `qident()` — 第 297 行
- `data_table_name()` — 第 304 行
- `sqlite_type()` — 第 308 行
- `connect_db()` — 第 316 行
- `normalize_field()` — 第 328 行
- `normalize_schema()` — 第 355 行
- `normalize_template_field()` — 第 396 行
- `default_output_line_for_template_field()` — 第 409 行
- `ensure_template_output_fields()` — 第 415 行
- `build_template_character_schema()` — 第 434 行
- `normalize_mujian_template()` — 第 449 行
- `refresh_builtin_mujian_template()` — 第 478 行
- `refresh_builtin_mujian_theme_pack()` — 第 503 行
- `refresh_builtin_assets()` — 第 514 行
- `normalize_mujian_templates()` — 第 521 行
- `active_mujian_template()` — 第 539 行
- `normalize_mujian_theme_pack()` — 第 553 行
- `normalize_mujian_theme_packs()` — 第 618 行
- `active_mujian_theme_pack()` — 第 636 行
- `normalize_config()` — 第 644 行
- `init_meta_tables()` — 第 691 行
- `table_exists()` — 第 822 行
- `field_map()` — 第 827 行
- `build_create_table_sql()` — 第 831 行
- `sync_physical_table()` — 第 851 行
- `save_schema_to_db()` — 第 890 行
- `load_schema_from_row()` — 第 934 行
- `list_schemas_from_db()` — 第 973 行
- `get_schema_from_db()` — 第 978 行
- `serialize_db_value()` — 第 988 行
- `get_table_rows_from_db()` — 第 1006 行
- `coerce_value()` — 第 1022 行
- `clean_rows()` — 第 1057 行
- `replace_table_rows()` — 第 1083 行
- `delete_table_from_db()` — 第 1098 行
- `build_table_snapshot()` — 第 1107 行
- `save_snapshot()` — 第 1118 行
- `ensure_runtime_data()` — 第 1131 行
- `get_config()` — 第 1146 行
- `save_config()` — 第 1159 行
- `get_config_value()` — 第 1171 行
- `set_config_value()` — 第 1184 行
- `build_openai_url()` — 第 1195 行
- `auth_headers()` — 第 1205 行
- `read_main_llm_config()` — 第 1213 行
- `fetch_model_list()` — 第 1241 行
- `test_chat_completion()` — 第 1271 行
- `extract_json_from_text()` — 第 1297 行
- `normalize_updates()` — 第 1318 行
- `select_row_by_pk()` — 第 1328 行
- `reverse_pair_id()` — 第 1344 行
- `resolve_relationship_pk()` — 第 1354 行
- `apply_updates()` — 第 1371 行
- `upsert_full_row()` — 第 1470 行
- `rollback_turn_effects()` — 第 1486 行
- `save_turn_record()` — 第 1535 行
- `mark_turns_stale()` — 第 1586 行
- `save_turn_effects()` — 第 1607 行
- `record_hook_event()` — 第 1621 行
- `strip_title_sequence()` — 第 1631 行
- `clean_display_text()` — 第 1637 行
- `clamp_number()` — 第 1661 行
- `format_metric_number()` — 第 1669 行
- `format_metric_delta()` — 第 1677 行
- `format_metric_value()` — 第 1683 行
- `metric_keys_by_scope()` — 第 1687 行
- `parse_metric_value()` — 第 1691 行
- `row_to_dict()` — 第 1712 行
- `get_metric_snapshot()` — 第 1718 行
- `normalize_metric_display_value()` — 第 1745 行
- `apply_display_metrics()` — 第 1749 行
- `rollback_metric_effects()` — 第 1833 行
- `metric_state_display()` — 第 1879 行
- `ensure_schema_extra_field()` — 第 1886 行
- `ensure_metric_history_schema()` — 第 1900 行
- `delta_display()` — 第 1941 行
- `sync_metric_history_table()` — 第 1945 行
- `sync_metric_summary_tables()` — 第 1973 行
- `sync_visible_metric_tables()` — 第 2031 行
- `normalize_display_payload()` — 第 2036 行
- `build_fallback_display()` — 第 2145 行
- `allocate_turn_sequence()` — 第 2197 行
- `get_turn_sequence()` — 第 2209 行
- `save_turn_display()` — 第 2213 行
- `latest_turn_display()` — 第 2264 行
- `build_update_summary()` — 第 2278 行
- `format_history()` — 第 2314 行
- `split_prompt_names()` — 第 2344 行
- `build_protagonist_prompt_rule()` — 第 2347 行
- `build_worker_custom_prompt_rule()` — 第 2361 行
- `build_worker_prompt()` — 第 2375 行
- `normalize_chat_completion_url()` — 第 2475 行
- `call_worker_model()` — 第 2484 行
- `save_worker_log()` — 第 2518 行
- `latest_worker_log()` — 第 2537 行
- `index()` — 第 2554 行
- `api_get_config()` — 第 2560 行
- `api_save_config()` — 第 2567 行
- `api_main_config()` — 第 2574 行
- `api_models()` — 第 2590 行
- `api_test_connection()` — 第 2603 行
- `api_hook_ping()` — 第 2628 行
- `api_hook_status()` — 第 2652 行
- `api_turn_start()` — 第 2660 行
- `api_turn_complete()` — 第 2674 行
- `api_turn_invalidate()` — 第 2689 行
- `api_recent_turns()` — 第 2706 行
- `api_state()` — 第 2719 行
- `api_metrics()` — 第 2733 行
- `api_create_table()` — 第 2741 行
- `api_get_table()` — 第 2753 行
- `api_save_table()` — 第 2763 行
- `get_table_rows_for_response()` — 第 2777 行
- `api_delete_table()` — 第 2784 行
- `api_import()` — 第 2793 行
- `api_export()` — 第 2814 行
- `recent_turn_displays()` — 第 2826 行
- `api_latest_display()` — 第 2854 行
- `api_recent_display()` — 第 2859 行
- `api_latest_log()` — 第 2866 行
- `redact_secret()` — 第 2870 行
- `load_json_row()` — 第 2879 行
- `api_export_debug_log()` — 第 2887 行
- `api_worker_update()` — 第 2943 行

### 函数详情

#### [get_resource_dir() -> Path](mods/xinjian/app.py#L22)（第 22 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [now_string() -> str](mods/xinjian/app.py#L256)（第 256 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clone_json(value: Any) -> Any](mods/xinjian/app.py#L260)（第 260 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [hash_text(value: Any) -> str](mods/xinjian/app.py#L264)（第 264 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_turn_id(value: Any) -> str](mods/xinjian/app.py#L269)（第 269 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [read_json(path: Path, default: Any) -> Any](mods/xinjian/app.py#L275)（第 275 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [write_json(path: Path, payload: Any) -> None](mods/xinjian/app.py#L285)（第 285 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [safe_id(value: Any, fallback: str = table) -> str](mods/xinjian/app.py#L290)（第 290 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [qident(identifier: str) -> str](mods/xinjian/app.py#L297)（第 297 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [data_table_name(table_id: str) -> str](mods/xinjian/app.py#L304)（第 304 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sqlite_type(field_type: str) -> str](mods/xinjian/app.py#L308)（第 308 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [connect_db() -> sqlite3.Connection](mods/xinjian/app.py#L316)（第 316 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_field(field: Any) -> dict[str, Any] | None](mods/xinjian/app.py#L328)（第 328 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_schema(schema: Any) -> dict[str, Any]](mods/xinjian/app.py#L355)（第 355 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_template_field(field: Any) -> dict[str, Any] | None](mods/xinjian/app.py#L396)（第 396 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [default_output_line_for_template_field(field: dict[str, Any]) -> str](mods/xinjian/app.py#L409)（第 409 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [ensure_template_output_fields(output_template: Any, fields: list[dict[str, Any]]) -> str](mods/xinjian/app.py#L415)（第 415 行）
Keep field definitions and output placeholders in sync
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_template_character_schema(fields: list[dict[str, Any]]) -> dict[str, str]](mods/xinjian/app.py#L434)（第 434 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_mujian_template(template: Any, fallback_id: str = custom) -> dict[str, Any] | None](mods/xinjian/app.py#L449)（第 449 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [refresh_builtin_mujian_template(template: dict[str, Any]) -> dict[str, Any]](mods/xinjian/app.py#L478)（第 478 行）
让旧配置中的内置标准模板跟随新版说明更新，同时不影响用户自定义模板
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [refresh_builtin_mujian_theme_pack(pack: dict[str, Any]) -> dict[str, Any]](mods/xinjian/app.py#L503)（第 503 行）
刷新内置外观包定义，保留用户导入包与自定义包
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [refresh_builtin_assets(config: dict[str, Any]) -> dict[str, Any]](mods/xinjian/app.py#L514)（第 514 行）
正式版配置收口：刷新内置模板/美化包，不覆盖用户自定义项目
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_mujian_templates(value: Any) -> list[dict[str, Any]]](mods/xinjian/app.py#L521)（第 521 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [active_mujian_template(config: dict[str, Any]) -> dict[str, Any]](mods/xinjian/app.py#L539)（第 539 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_mujian_theme_pack(pack: Any, fallback_id: str = theme) -> dict[str, Any] | None](mods/xinjian/app.py#L553)（第 553 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：json_dict, json_copy

#### [json_dict(value: Any) -> dict[str, Any]（嵌套在 normalize_mujian_theme_pack 内）](mods/xinjian/app.py#L565)（第 565 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [json_copy(value: Any) -> Any（嵌套在 normalize_mujian_theme_pack 内）](mods/xinjian/app.py#L573)（第 573 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_mujian_theme_packs(value: Any) -> list[dict[str, Any]]](mods/xinjian/app.py#L618)（第 618 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [active_mujian_theme_pack(config: dict[str, Any]) -> dict[str, Any]](mods/xinjian/app.py#L636)（第 636 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_config(config: Any) -> dict[str, Any]](mods/xinjian/app.py#L644)（第 644 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [init_meta_tables(conn: sqlite3.Connection) -> None](mods/xinjian/app.py#L691)（第 691 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [table_exists(conn: sqlite3.Connection, name: str) -> bool](mods/xinjian/app.py#L822)（第 822 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [field_map(schema: dict[str, Any]) -> dict[str, dict[str, Any]]](mods/xinjian/app.py#L827)（第 827 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_create_table_sql(schema: dict[str, Any], physical_name: str | None = None) -> str](mods/xinjian/app.py#L831)（第 831 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sync_physical_table(conn: sqlite3.Connection, schema: dict[str, Any]) -> None](mods/xinjian/app.py#L851)（第 851 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_schema_to_db(conn: sqlite3.Connection, schema: dict[str, Any]) -> dict[str, Any]](mods/xinjian/app.py#L890)（第 890 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [load_schema_from_row(conn: sqlite3.Connection, table_row: sqlite3.Row) -> dict[str, Any]](mods/xinjian/app.py#L934)（第 934 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [list_schemas_from_db(conn: sqlite3.Connection) -> list[dict[str, Any]]](mods/xinjian/app.py#L973)（第 973 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_schema_from_db(conn: sqlite3.Connection, table_id: str) -> dict[str, Any]](mods/xinjian/app.py#L978)（第 978 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [serialize_db_value(value: Any, field: dict[str, Any]) -> Any](mods/xinjian/app.py#L988)（第 988 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_table_rows_from_db(conn: sqlite3.Connection, schema: dict[str, Any]) -> list[dict[str, Any]]](mods/xinjian/app.py#L1006)（第 1006 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [coerce_value(value: Any, field: dict[str, Any]) -> Any](mods/xinjian/app.py#L1022)（第 1022 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clean_rows(schema: dict[str, Any], rows: Any) -> list[dict[str, Any]]](mods/xinjian/app.py#L1057)（第 1057 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [replace_table_rows(conn: sqlite3.Connection, schema: dict[str, Any], rows: list[dict[str, Any]]) -> None](mods/xinjian/app.py#L1083)（第 1083 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [delete_table_from_db(conn: sqlite3.Connection, table_id: str) -> None](mods/xinjian/app.py#L1098)（第 1098 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_table_snapshot(conn: sqlite3.Connection, table_ids: list[str] | None = None) -> list[dict[str, Any]]](mods/xinjian/app.py#L1107)（第 1107 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_snapshot(conn: sqlite3.Connection, table_id: str, reason: str = update) -> None](mods/xinjian/app.py#L1118)（第 1118 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [ensure_runtime_data() -> None](mods/xinjian/app.py#L1131)（第 1131 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_config() -> dict[str, Any]](mods/xinjian/app.py#L1146)（第 1146 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_config(config: dict[str, Any]) -> dict[str, Any]](mods/xinjian/app.py#L1159)（第 1159 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_config_value(key: str, default: Any = None) -> Any](mods/xinjian/app.py#L1171)（第 1171 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [set_config_value(key: str, value: Any) -> Any](mods/xinjian/app.py#L1184)（第 1184 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_openai_url(base_url: str, endpoint: str) -> str](mods/xinjian/app.py#L1195)（第 1195 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [auth_headers(api_key: str) -> dict[str, str]](mods/xinjian/app.py#L1205)（第 1205 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [read_main_llm_config() -> dict[str, Any]](mods/xinjian/app.py#L1213)（第 1213 行）
Best-effort read of Fantareal's main model config
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [fetch_model_list(base_url: str, api_key: str, timeout: int | float = 30) -> list[str]](mods/xinjian/app.py#L1241)（第 1241 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [test_chat_completion(base_url: str, api_key: str, model: str, timeout: int | float = 30) -> None](mods/xinjian/app.py#L1271)（第 1271 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [extract_json_from_text(text: str) -> Any](mods/xinjian/app.py#L1297)（第 1297 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_updates(payload: Any) -> list[dict[str, Any]]](mods/xinjian/app.py#L1318)（第 1318 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [select_row_by_pk(conn: sqlite3.Connection, schema: dict[str, Any], pk_value: str) -> dict[str, Any] | None](mods/xinjian/app.py#L1328)（第 1328 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [reverse_pair_id(value: str) -> str](mods/xinjian/app.py#L1344)（第 1344 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [resolve_relationship_pk(conn: sqlite3.Connection, schema: dict[str, Any], pk_value: str) -> tuple[str, dict[str, Any] | None, str]](mods/xinjian/app.py#L1354)（第 1354 行）
relationship 表 A-B / B-A 自动反查，避免正反主键不同导致整轮失败
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [apply_updates(updates: list[dict[str, Any]]) -> dict[str, Any]](mods/xinjian/app.py#L1371)（第 1371 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [upsert_full_row(conn: sqlite3.Connection, schema: dict[str, Any], row: dict[str, Any]) -> None](mods/xinjian/app.py#L1470)（第 1470 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [rollback_turn_effects(conn: sqlite3.Connection, turn_id: str, reason: str = reroll) -> int](mods/xinjian/app.py#L1486)（第 1486 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_turn_record(conn: sqlite3.Connection) -> dict[str, Any]](mods/xinjian/app.py#L1535)（第 1535 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [mark_turns_stale(conn: sqlite3.Connection, from_turn_id: str | None = None, reason: str = history_changed) -> dict[str, Any]](mods/xinjian/app.py#L1586)（第 1586 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_turn_effects(conn: sqlite3.Connection, turn_id: str, result: dict[str, Any]) -> None](mods/xinjian/app.py#L1607)（第 1607 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [record_hook_event(conn: sqlite3.Connection) -> None](mods/xinjian/app.py#L1621)（第 1621 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [strip_title_sequence(value: Any) -> str](mods/xinjian/app.py#L1631)（第 1631 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clean_display_text(value: Any, limit: int = 360) -> str](mods/xinjian/app.py#L1637)（第 1637 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [clamp_number(value: Any, minimum: float = 0, maximum: float = 100) -> float](mods/xinjian/app.py#L1661)（第 1661 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [format_metric_number(value: Any) -> int | float](mods/xinjian/app.py#L1669)（第 1669 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [format_metric_delta(delta: Any) -> str](mods/xinjian/app.py#L1677)（第 1677 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [format_metric_value(value: Any, max_value: Any = 100, delta: Any = 0) -> str](mods/xinjian/app.py#L1683)（第 1683 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [metric_keys_by_scope(scope: str) -> set[str]](mods/xinjian/app.py#L1687)（第 1687 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [parse_metric_value(raw_value: Any, default_max: float = 100) -> dict[str, Any] | None](mods/xinjian/app.py#L1691)（第 1691 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [row_to_dict(row: sqlite3.Row | None) -> dict[str, Any] | None](mods/xinjian/app.py#L1712)（第 1712 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_metric_snapshot(conn: sqlite3.Connection) -> dict[str, Any]](mods/xinjian/app.py#L1718)（第 1718 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_metric_display_value(parsed: dict[str, Any]) -> str](mods/xinjian/app.py#L1745)（第 1745 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [apply_display_metrics(conn: sqlite3.Connection, turn_id: str, display_payload: dict[str, Any]) -> list[dict[str, Any]]](mods/xinjian/app.py#L1749)（第 1749 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [rollback_metric_effects(conn: sqlite3.Connection, turn_id: str, metrics: list[dict[str, Any]]) -> int](mods/xinjian/app.py#L1833)（第 1833 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [metric_state_display(row: sqlite3.Row | dict[str, Any]) -> str](mods/xinjian/app.py#L1879)（第 1879 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [ensure_schema_extra_field(conn: sqlite3.Connection, table_id: str, field_def: dict[str, Any]) -> None](mods/xinjian/app.py#L1886)（第 1886 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [ensure_metric_history_schema(conn: sqlite3.Connection) -> None](mods/xinjian/app.py#L1900)（第 1900 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [delta_display(delta: Any) -> str](mods/xinjian/app.py#L1941)（第 1941 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sync_metric_history_table(conn: sqlite3.Connection) -> None](mods/xinjian/app.py#L1945)（第 1945 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sync_metric_summary_tables(conn: sqlite3.Connection) -> None](mods/xinjian/app.py#L1973)（第 1973 行）
把真实数值表镜像到用户可见表册：角色状态表、关系表、数值变化记录
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：summary_for

#### [summary_for(items: list[sqlite3.Row], allowed: set[str]) -> str（嵌套在 sync_metric_summary_tables 内）](mods/xinjian/app.py#L1994)（第 1994 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [sync_visible_metric_tables(conn: sqlite3.Connection) -> None](mods/xinjian/app.py#L2031)（第 2031 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_display_payload(payload: Any) -> dict[str, Any]](mods/xinjian/app.py#L2036)（第 2036 行）
Normalize the assistant-generated front-end display payload
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_fallback_display() -> dict[str, Any]](mods/xinjian/app.py#L2145)（第 2145 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [allocate_turn_sequence(conn: sqlite3.Connection, turn_id: str) -> int](mods/xinjian/app.py#L2197)（第 2197 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_turn_sequence(conn: sqlite3.Connection, turn_id: str) -> int](mods/xinjian/app.py#L2209)（第 2209 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_turn_display(display: dict[str, Any]) -> dict[str, Any]](mods/xinjian/app.py#L2213)（第 2213 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [latest_turn_display() -> dict[str, Any]](mods/xinjian/app.py#L2264)（第 2264 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_update_summary(result: dict[str, Any], tables: list[dict[str, Any]] | None = None) -> dict[str, Any]](mods/xinjian/app.py#L2278)（第 2278 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [format_history(history: Any, limit_turns: int) -> list[dict[str, str]]](mods/xinjian/app.py#L2314)（第 2314 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [split_prompt_names(value: object) -> list[str]](mods/xinjian/app.py#L2344)（第 2344 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_protagonist_prompt_rule(config: dict[str, Any]) -> str](mods/xinjian/app.py#L2347)（第 2347 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_worker_custom_prompt_rule(config: dict[str, Any]) -> str](mods/xinjian/app.py#L2361)（第 2361 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [build_worker_prompt() -> tuple[str, str]](mods/xinjian/app.py#L2375)（第 2375 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [normalize_chat_completion_url(base_url: str) -> str](mods/xinjian/app.py#L2475)（第 2475 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [call_worker_model() -> str](mods/xinjian/app.py#L2484)（第 2484 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [save_worker_log(payload: dict[str, Any]) -> None](mods/xinjian/app.py#L2518)（第 2518 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [latest_worker_log() -> dict[str, Any]](mods/xinjian/app.py#L2537)（第 2537 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [index(request: Request) -> HTMLResponse](mods/xinjian/app.py#L2554)（第 2554 行）
GET / 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_config() -> dict[str, Any]](mods/xinjian/app.py#L2560)（第 2560 行）
GET /api/config 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_config(request: Request) -> dict[str, Any]](mods/xinjian/app.py#L2567)（第 2567 行）
POST /api/config 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_main_config() -> dict[str, Any]](mods/xinjian/app.py#L2574)（第 2574 行）
GET /api/main-config 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_models(request: Request) -> dict[str, Any]](mods/xinjian/app.py#L2590)（第 2590 行）
POST /api/models 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_test_connection(request: Request) -> dict[str, Any]](mods/xinjian/app.py#L2603)（第 2603 行）
POST /api/test-connection 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_hook_ping(request: Request) -> dict[str, Any]](mods/xinjian/app.py#L2628)（第 2628 行）
POST /api/hook/ping 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_hook_status() -> dict[str, Any]](mods/xinjian/app.py#L2652)（第 2652 行）
GET /api/hook/status 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_turn_start(request: Request) -> dict[str, Any]](mods/xinjian/app.py#L2660)（第 2660 行）
POST /api/turn/start 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_turn_complete(request: Request) -> dict[str, Any]](mods/xinjian/app.py#L2674)（第 2674 行）
POST /api/turn/complete 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_turn_invalidate(request: Request) -> dict[str, Any]](mods/xinjian/app.py#L2689)（第 2689 行）
POST /api/turn/invalidate 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_recent_turns(limit: int = 30) -> dict[str, Any]](mods/xinjian/app.py#L2706)（第 2706 行）
GET /api/turns/recent 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_state() -> dict[str, Any]](mods/xinjian/app.py#L2719)（第 2719 行）
GET /api/state 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_metrics() -> dict[str, Any]](mods/xinjian/app.py#L2733)（第 2733 行）
GET /api/metrics 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_create_table(request: Request) -> dict[str, Any]](mods/xinjian/app.py#L2741)（第 2741 行）
POST /api/table 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_get_table(table_id: str) -> dict[str, Any]](mods/xinjian/app.py#L2753)（第 2753 行）
GET /api/table/{table_id} 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_save_table(table_id: str, request: Request) -> dict[str, Any]](mods/xinjian/app.py#L2763)（第 2763 行）
POST /api/table/{table_id} 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [get_table_rows_for_response(schema: dict[str, Any]) -> list[dict[str, Any]]](mods/xinjian/app.py#L2777)（第 2777 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_delete_table(table_id: str) -> dict[str, Any]](mods/xinjian/app.py#L2784)（第 2784 行）
DELETE /api/table/{table_id} 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_import(request: Request) -> dict[str, Any]](mods/xinjian/app.py#L2793)（第 2793 行）
POST /api/import 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export() -> JSONResponse](mods/xinjian/app.py#L2814)（第 2814 行）
GET /api/export 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [recent_turn_displays(limit: int = 20) -> list[dict[str, Any]]](mods/xinjian/app.py#L2826)（第 2826 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_latest_display() -> dict[str, Any]](mods/xinjian/app.py#L2854)（第 2854 行）
GET /api/display/latest 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_recent_display(limit: int = 20) -> dict[str, Any]](mods/xinjian/app.py#L2859)（第 2859 行）
GET /api/display/recent 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_latest_log() -> dict[str, Any]](mods/xinjian/app.py#L2866)（第 2866 行）
GET /api/logs/latest 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [redact_secret(value: Any) -> str](mods/xinjian/app.py#L2870)（第 2870 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [load_json_row(value: Any, fallback: Any) -> Any](mods/xinjian/app.py#L2879)（第 2879 行）
参见源码。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_export_debug_log(limit: int = 80) -> JSONResponse](mods/xinjian/app.py#L2887)（第 2887 行）
GET /api/logs/export 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]

#### [api_worker_update(request: Request) -> dict[str, Any]](mods/xinjian/app.py#L2943)（第 2943 行）
POST /api/worker/update 端点。
- **常见坑**：[待补充]
- **改动建议**：[待补充]
- **相关函数**：[待补充]


