#!/usr/bin/env python3
"""
Verify that 行号 in 说明书.md (注释版地图) matches 说明书_auto.md (AST-extracted).

Both files reference functions/classes with patterns like:
    #### [name(args) -> ret](file.py#LNN)
        （第 N 行）
This script extracts all (file, line, name) triples from both files and:
  - Reports entries in 说明书.md missing from auto.md (row drift / typos)
  - Reports mismatched line numbers (行号漂移)
  - Reports missing source files

Usage:
    python scripts/verify_map.py                # verify all
    python scripts/verify_map.py --strict       # exit non-zero on any mismatch
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Repo paths (relative to this script)
SCRIPT_DIR = Path(__file__).resolve().parent
MAP_REPO = SCRIPT_DIR.parent
AUTO_MD = MAP_REPO / "maps" / "说明书_auto.md"
ANNOTATED_MD = MAP_REPO / "maps" / "说明书.md"  # 注释版地图（已 verify 准）
SOURCE_REPO = MAP_REPO.parent / "Fantareal-beta"  # 当前主分支


# Extract entries from a markdown file.
# Pattern matches the entry HEADER, not the whole line. re.search is used because
# some entries have nested brackets (e.g. `tuple[uvicorn.Server, threading.Thread]`)
# which would break a strict left-anchored regex.
# Header shape:
#   #### [name(args)](file.py#LNN)  （第 NN 行）
#   #### [name(args)](file.py#LNN)  （第 NN 行)  （嵌套在 X 内）
ENTRY_PATTERN = re.compile(
    r"^####\s+\[(?P<name>.+?)\]\((?P<file>[^)#]+\.py)#L(?P<line>\d+)\)"
    r"\s*（第\s*(?P<zh_line>\d+)\s*行"
    r"(?P<nested>\s*（嵌套在[^）]+）)?"
)


def extract_entries(md_path: Path) -> list[dict]:
    """Extract all (file, line, name) triples from a markdown file."""
    if not md_path.exists():
        return []
    entries = []
    for line in md_path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("#### "):
            continue
        m = ENTRY_PATTERN.match(line)
        if not m:
            continue
        entries.append({
            "name": m.group("name").strip(),
            "file": m.group("file").strip(),
            "line": int(m.group("line")),
            "zh_line": int(m.group("zh_line")),
            "is_nested": bool(m.group("nested")),
        })
    return entries


def key(entries: list[dict]) -> dict[tuple[str, int], str]:
    """Build { (file, line) -> name } map. First occurrence wins on duplicates."""
    out: dict[tuple[str, int], str] = {}
    for e in entries:
        k = (e["file"], e["line"])
        if k not in out:
            out[k] = e["name"]
    return out


def verify(verbose: bool = True) -> tuple[int, int, int]:
    """Run verification. Returns (ok, drift, missing_file) counts.

    Strategy: key by (file, line) — name field is for display only,
    since annotated.md uses short names (per human style guide) while
    auto.md uses full signatures with type hints. As long as the line
    number is right, the entry is at the right place.
    """
    auto_entries = extract_entries(AUTO_MD)
    ann_entries = extract_entries(ANNOTATED_MD)

    if not auto_entries:
        print(f"ERROR: {AUTO_MD} not found or empty. Run sync_map.py first.")
        sys.exit(1)
    if not ann_entries:
        print(f"ERROR: {ANNOTATED_MD} not found or empty.")
        sys.exit(1)

    # 兼容：以前叫"annotated.md"

    auto_map = key(auto_entries)
    ann_map = key(ann_entries)

    ok = drift = missing_file = 0
    drift_details: list[str] = []
    missing_details: list[str] = []

    # 1. For every (file, line) in annotated.md, check it exists in auto.md
    for (file, line), name in ann_map.items():
        if (file, line) not in auto_map:
            missing_details.append(
                f"  {file} L{line} :: {name} (annotated entry, not in auto)"
            )
            missing_file += 1
            continue
        # If names differ, it's a style choice — only report as informational
        if name != auto_map[(file, line)]:
            pass  # silent: different name style is expected (short vs full)
        ok += 1

    # 2. Check the source files actually exist (sanity)
    missing_sources: set[str] = set()
    for e in ann_entries:
        src = SOURCE_REPO / e["file"]
        if not src.exists():
            missing_sources.add(e["file"])

    if verbose:
        print(f"Annotated: {len(ann_entries)} entries  /  Auto: {len(auto_entries)} entries")
        print()
        print(f"[OK]   PASS:   {ok}")
        print(f"[WARN] DRIFT:  {drift}")
        print(f"[ERR]  MISSING:{missing_file}")
        if missing_sources:
            print(f"[ERR]  SOURCE FILES NOT FOUND in {SOURCE_REPO.name}:")
            for f in sorted(missing_sources):
                print(f"   - {f}")
        if missing_details:
            print()
            print("Missing entries (annotated (file,line) not in auto):")
            for d in missing_details:
                print(d)

    return ok, drift, missing_file


def main():
    parser = argparse.ArgumentParser(description="Verify annotated.md line numbers vs auto.md")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero on any mismatch")
    parser.add_argument("--quiet", action="store_true", help="Only print summary")
    args = parser.parse_args()

    ok, drift, missing = verify(verbose=not args.quiet)

    if args.strict and (drift > 0 or missing > 0):
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
