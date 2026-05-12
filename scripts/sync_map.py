"""
Sync project map from the main Fantareal repo to this map repo.

Two outputs:
  1. maps/说明书.md      — copied from main repo (hand-written, with 常见坑 etc.)
  2. maps/说明书_auto.md — fresh AST scan (line numbers always accurate)

Usage:
    python scripts/sync_map.py                         # sync with ../Fantareal
    python scripts/sync_map.py --source /path/to/Fantareal
    python scripts/sync_map.py --skip-copy              # only AST scan
    python scripts/sync_map.py --skip-scan              # only copy 说明书.md
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def find_main_repo(map_repo: Path) -> Path | None:
    """Try to locate the main Fantareal repo relative to the map repo."""
    candidates = [
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
    parser.add_argument("--skip-copy", action="store_true", help="Skip copying 说明书.md")
    parser.add_argument("--skip-scan", action="store_true", help="Skip AST scan")
    args = parser.parse_args()

    map_repo = Path(__file__).resolve().parent.parent
    source = args.source or find_main_repo(map_repo)

    if not source:
        print("ERROR: Cannot find main Fantareal repo.")
        print("  Expected at: ../Fantareal (next to this map repo)")
        print("  Or use: --source /path/to/Fantareal")
        sys.exit(1)

    if not (source / "fantareal" / "app.py").exists():
        print(f"ERROR: {source} doesn't look like a Fantareal repo")
        sys.exit(1)

    print(f"Main repo: {source}")
    print(f"Map repo:  {map_repo}")
    print()

    # Step 1: Copy hand-written 说明书
    if not args.skip_copy:
        source_map = source / "说明书.md"
        dest_map = map_repo / "maps" / "说明书.md"
        if source_map.exists():
            shutil.copy2(source_map, dest_map)
            print("  Copied: 说明书.md → maps/说明书.md")
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
        print("  SKIP: --skip-copy (not copying 说明书.md)")

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
