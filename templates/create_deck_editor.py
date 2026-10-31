#!/usr/bin/env python3
"""
create_deck_editor.py

Create a self-contained review/editor HTML for an iframe-based HTML PPT deck.

Usage:
  python3 create_deck_editor.py path/to/all_slides.html
  python3 create_deck_editor.py path/to/all_slides.html -o path/to/all_slides_editor.html

The generated editor preloads the selected deck, so the user can double-click it,
drag/delete pages, and export a new edited HTML without choosing a file first.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TEMPLATE = ROOT / "deck_editor.html"


def js_string(value: str) -> str:
    # Avoid accidentally closing the surrounding <script> tag.
    return json.dumps(value, ensure_ascii=False).replace("</", "<\\/")


def build(deck_path: Path, output_path: Path) -> None:
    if not deck_path.exists():
        raise FileNotFoundError(deck_path)
    if not TEMPLATE.exists():
        raise FileNotFoundError(TEMPLATE)

    deck_html = deck_path.read_text(encoding="utf-8")
    editor_html = TEMPLATE.read_text(encoding="utf-8")

    preload = (
        "<script>\n"
        f"window.__DECK_FILENAME__ = {js_string(deck_path.name)};\n"
        f"window.__DECK_SOURCE__ = {js_string(deck_html)};\n"
        "</script>\n"
    )

    marker = "<script>\n(function () {"
    if marker not in editor_html:
        raise RuntimeError("deck_editor.html changed: cannot find injection marker")

    editor_html = editor_html.replace(marker, preload + marker, 1)
    output_path.write_text(editor_html, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Create preloaded HTML PPT deck editor.")
    parser.add_argument("deck", help="Path to iframe-based HTML PPT deck")
    parser.add_argument("-o", "--output", help="Output editor HTML path")
    args = parser.parse_args()

    deck_path = Path(args.deck).expanduser().resolve()
    output_path = (
        Path(args.output).expanduser().resolve()
        if args.output
        else deck_path.with_name(deck_path.stem + "_editor.html")
    )
    build(deck_path, output_path)
    print(f"Created: {output_path}")


if __name__ == "__main__":
    main()
