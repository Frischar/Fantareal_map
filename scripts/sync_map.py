"""
Sync project map from the main Fantareal repo to this map repo.

Two outputs:
  1. maps/说明书_auto.md — fresh AST scan (line numbers always accurate)
  2. maps/说明书_legacy.md — beta 仓库的手写说明书（仅当 --with-legacy 启用；默认 maps/说明书.md 是本仓库自维护的注释版地图）

默认源：优先 ../Fantareal-beta（当前主分支），其次 ../Fantareal，最后 ../fantareal。
可显式 --source /path/to/xxx 覆盖。

Usage:
    python scripts/sync_map.py                                  # 仅 AST 扫描
    python scripts/sync_map.py --source /path/to/Fantareal-beta
    python scripts/sync_map.py --with-legacy                    # 同时把 beta 的手写说明书复制为 说明书_legacy.md
    python scripts/sync_map.py --skip-scan                      # 仅复制手写说明书
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def find_main_repo(map_repo: Path) -> Path | None:
    """Try to locate the main Fantareal repo relative to the map repo.

    Search order (first match wins):
      1. Fantareal-beta  ← 当前主分支（用户实际在用的工作分支）
      2. Fantareal       ← 主仓库名
      3. fantareal       ← 小写别名
    """
    candidates = [
        map_repo.parent / "Fantareal-beta",
        map_repo.parent / "Fantareal",
        map_repo.parent / "fantareal",
    ]
    for candidate in candidates:
        if (candidate / "fantareal" / "app.py").exists():
            return candidate
    return None


def run_ast_scan(map_repo: Path, source: Path, output: Path) -> bool:
    """Run the AST scanner to generate auto docs."""
    scanner = map_repo / "scripts" / "scan_map.py"
    try:
        subprocess.run(
            [sys.executable, str(scanner), "--source", str(source), "--output", str(output)],
            check=True,
            capture_output=True,
            text=True,
        )
        return True
    except subprocess.CalledProcessError as e:
        print(f"ERROR: AST scan failed:\n{e.stderr}")
        return False


def check_line_references(map_file: Path, main_repo: Path) -> list[str]:
    """Check if referenced files in the map still exist. Returns warnings."""
    import re

    warnings: list[str] = []
    pattern = re.compile(r"\[([^\]]+)\]\(([^#)]+\.py)(?:#L(\d+))?\)")

    seen_files: set[str] = set()
    for line in map_file.read_text(encoding="utf-8").splitlines():
        for match in pattern.finditer(line):
            file_path = match.group(2)
            if file_path in seen_files:
                continue
            seen_files.add(file_path)
            full_path = main_repo / file_path
            if not full_path.exists():
                warnings.append(f"  MISSING: {file_path}")

    return warnings


def main():
    parser = argparse.ArgumentParser(description="Sync project map from main repo")
    parser.add_argument("--source", type=Path, help="Path to main Fantareal repo")
    parser.add_argument("--with-legacy", action="store_true", help="Also copy beta's hand-written 说明书.md as 说明书_legacy.md")
    parser.add_argument("--skip-scan", action="store_true", help="Skip AST scanning (only copy legacy)")
    args = parser.parse_args()

    map_repo = Path(__file__).resolve().parent.parent
    source = args.source or find_main_repo(map_repo)

    if not source:
        print("ERROR: Cannot find main Fantareal repo.")
        print("  Searched for: ../Fantareal-beta, ../Fantareal, ../fantareal")
        print("  Or use: --source /path/to/Fantareal-beta")
        sys.exit(1)

    if not (source / "fantareal" / "app.py").exists():
        print(f"ERROR: {source} doesn't look like a Fantareal repo")
        sys.exit(1)

    print(f"Main repo: {source}")
    print(f"Map repo:  {map_repo}")
    print()

    # Step 1: Optionally copy beta's hand-written 说明书.md as 说明书_legacy.md
    if args.with_legacy:
        source_map = source / "说明书.md"
        dest_map = map_repo / "maps" / "说明书_legacy.md"
        if source_map.exists():
            shutil.copy2(source_map, dest_map)
            print("  Copied: 说明书.md → maps/说明书_legacy.md (legacy hand-written)")
            warnings = check_line_references(dest_map, source)
            if warnings:
                print("  Warnings — referenced files not found:")
                for w in warnings:
                    print(w)
            else:
                print("  All referenced files exist (line numbers may be stale).")
        else:
            print("  SKIP: 说明书.md not found in main repo.")
    else:
        print("  SKIP: --with-legacy not set (not copying beta's hand-written 说明书.md)")

    # Step 2: Run AST scanner for auto-generated map
    if not args.skip_scan:
        dest_auto = map_repo / "maps" / "说明书_auto.md"
        if run_ast_scan(map_repo, source, dest_auto):
            print(f"  Generated: maps/说明书_auto.md (AST scan)")
    else:
        print("  SKIP: --skip-scan (not running AST scanner)")

    print()
    print("Done. Review changes and commit.")


if __name__ == "__main__":
    main()
