#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批量放大所有幻灯片的屏占比：减少页边距、放宽内容宽度、整体放大字号和图标。"""

import re
from pathlib import Path

DIR = Path(__file__).parent.parent / "output"
files = sorted(DIR.glob("slide_*.html"), key=lambda p: int(re.search(r'(\d+)', p.name).group(1)))

replacements = [
    # 页边距放大版（若需要更大可继续调）
    ("padding: 4vw 6vw;", "padding: 1.5vw 3vw;"),
    ("padding: 4vw 5vw;", "padding: 1.5vw 2.5vw;"),
    ("padding: 3vw 5vw;", "padding: 1.2vw 2.5vw;"),

    # 内容最大宽度放宽
    ("max-width: 1000px;", "max-width: 1700px;"),
    ("max-width: 1100px;", "max-width: 1800px;"),
    ("max-width: 1200px;", "max-width: 1900px;"),
    ("max-width: 1400px;", "max-width: 1700px;"),
    ("max-width: 1500px;", "max-width: 1800px;"),
    ("max-width: 1600px;", "max-width: 1900px;"),

    # 标题字号放大
    ("font-size: clamp(1.8rem, 3.5vw, 2.6rem);", "font-size: clamp(3rem, 5.5vw, 4.2rem);"),
    ("font-size: clamp(1.6rem, 3vw, 2.2rem);", "font-size: clamp(2.8rem, 5vw, 3.8rem);"),
    ("font-size: clamp(3.2rem, 6.5vw, 5.5rem);", "font-size: clamp(5.5rem, 10vw, 9rem);"),
    ("font-size: clamp(3rem, 6vw, 5rem);", "font-size: clamp(5.2rem, 9.5vw, 8.5rem);"),
    ("font-size: clamp(2.4rem, 4.5vw, 3.4rem);", "font-size: clamp(3rem, 5.5vw, 4.2rem);"),
    ("font-size: clamp(2.2rem, 4vw, 3rem);", "font-size: clamp(2.8rem, 5vw, 3.8rem);"),
    ("font-size: clamp(4.5rem, 8.5vw, 7.5rem);", "font-size: clamp(5.5rem, 10vw, 9rem);"),
    ("font-size: clamp(4.2rem, 8vw, 7rem);", "font-size: clamp(5.2rem, 9.5vw, 8.5rem);"),

    # 副标题/横幅
    ("font-size: clamp(1.3rem, 2.5vw, 1.8rem);", "font-size: clamp(2rem, 3.8vw, 2.8rem);"),
    ("font-size: clamp(1rem, 1.8vw, 1.2rem);", "font-size: clamp(1.5rem, 2.8vw, 2rem);"),
    ("font-size: clamp(0.9rem, 1.6vw, 1.05rem);", "font-size: clamp(1.4rem, 2.6vw, 1.7rem);"),
    ("font-size: clamp(1.2rem, 2vw, 1.4rem);", "font-size: clamp(1.8rem, 3.2vw, 2.4rem);"),
    ("font-size: clamp(1.6rem, 3vw, 2.2rem);", "font-size: clamp(2rem, 3.8vw, 2.8rem);"),
    ("font-size: clamp(1.1rem, 2vw, 1.3rem);", "font-size: clamp(1.4rem, 2.6vw, 1.7rem);"),
    ("font-size: clamp(1.5rem, 2.6vw, 2rem);", "font-size: clamp(1.8rem, 3.2vw, 2.4rem);"),

    # 卡片/列表内文字
    (".card h4 {\n      font-size: 1.1rem;", ".card h4 {\n      font-size: 1.55rem;"),
    (".card h4 {\n      font-size: 1.3rem;", ".card h4 {\n      font-size: 1.55rem;"),
    (".card h4 {\n      font-size: clamp(1.5rem, 2.6vw, 2rem);", ".card h4 {\n      font-size: clamp(1.8rem, 3.2vw, 2.4rem);"),
    (".card p {\n      font-size: 0.9rem;", ".card p {\n      font-size: 1.25rem;"),
    (".card p {\n      font-size: 0.95rem;", ".card p {\n      font-size: 1.25rem;"),
    (".card p {\n      font-size: 1.05rem;", ".card p {\n      font-size: 1.25rem;"),
    (".card p {\n      font-size: 1.1rem;", ".card p {\n      font-size: 1.3rem;"),
    (".step h4 {\n      font-size: 1rem;", ".step h4 {\n      font-size: 1.45rem;"),
    (".step h4 {\n      font-size: 1.2rem;", ".step h4 {\n      font-size: 1.45rem;"),
    (".step p {\n      font-size: 0.85rem;", ".step p {\n      font-size: 1.25rem;"),
    (".step p {\n      font-size: 1.05rem;", ".step p {\n      font-size: 1.25rem;"),
    (".feature-item h4 {\n      font-size: 1rem;", ".feature-item h4 {\n      font-size: 1.45rem;"),
    (".feature-item h4 {\n      font-size: 1.2rem;", ".feature-item h4 {\n      font-size: 1.45rem;"),
    (".feature-item h4 {\n      font-size: 1.25rem;", ".feature-item h4 {\n      font-size: 1.5rem;"),
    (".feature-item h4 {\n      font-size: 1.3rem;", ".feature-item h4 {\n      font-size: 1.55rem;"),
    (".feature-item p {\n      font-size: 0.9rem;", ".feature-item p {\n      font-size: 1.25rem;"),
    (".feature-item p {\n      font-size: 0.95rem;", ".feature-item p {\n      font-size: 1.25rem;"),
    (".feature-item p {\n      font-size: 1.05rem;", ".feature-item p {\n      font-size: 1.25rem;"),
    (".feature-item p {\n      font-size: 1.1rem;", ".feature-item p {\n      font-size: 1.3rem;"),
    (".explain-item h4 {\n      font-size: 1rem;", ".explain-item h4 {\n      font-size: 1.45rem;"),
    (".explain-item h4 {\n      font-size: 1.2rem;", ".explain-item h4 {\n      font-size: 1.45rem;"),
    (".explain-item p {\n      font-size: 0.9rem;", ".explain-item p {\n      font-size: 1.25rem;"),
    (".explain-item p {\n      font-size: 1.05rem;", ".explain-item p {\n      font-size: 1.25rem;"),

    # 图标放大
    ("width: 80px;\n      height: 80px;", "width: 120px;\n      height: 120px;"),
    ("width: 96px;\n      height: 96px;", "width: 120px;\n      height: 120px;"),
    ("width: 88px;\n      height: 88px;", "width: 110px;\n      height: 110px;"),
    ("width: 72px;\n      height: 72px;", "width: 110px;\n      height: 110px;"),
    ("width: 40px;\n      height: 40px;", "width: 64px;\n      height: 64px;"),
    ("width: 50px;\n      height: 50px;", "width: 64px;\n      height: 64px;"),
    ("width: 32px;\n      height: 32px;", "width: 52px;\n      height: 52px;"),
    ("width: 40px; height: 40px;", "width: 64px; height: 64px;"),
    ("width: 44px;\n      height: 44px;", "width: 66px;\n      height: 66px;"),
    ("width: 54px;\n      height: 54px;", "width: 66px;\n      height: 66px;"),
    ("width: 42px;\n      height: 42px;", "width: 64px;\n      height: 64px;"),
    ("width: 52px;\n      height: 52px;", "width: 64px;\n      height: 64px;"),
    ("width: 48px;\n      height: 48px;", "width: 72px;\n      height: 72px;"),
    ("width: 58px;\n      height: 58px;", "width: 72px;\n      height: 72px;"),
    ("width: 24px;\n      height: 24px;", "width: 34px;\n      height: 34px;"),
    ("width: 28px;\n      height: 28px;", "width: 34px;\n      height: 34px;"),
    ("width: 22px;\n      height: 22px;", "width: 32px;\n      height: 32px;"),
    ("width: 26px;\n      height: 26px;", "width: 32px;\n      height: 32px;"),
    ("width: 50px; height: 50px;", "width: 64px; height: 64px;"),

    # 卡片间距/内边距放大
    ("gap: 1.5rem;", "gap: 2.5rem;"),
    ("gap: 2rem;", "gap: 2.5rem;"),
    ("gap: 1.6rem;", "gap: 2rem;"),
    ("gap: 1.4rem;", "gap: 1.8rem;"),
    ("gap: 1.2rem;", "gap: 1.6rem;"),
    ("gap: 1rem;", "gap: 1.4rem;"),
    ("gap: 0.75rem;", "gap: 1rem;"),
    ("padding: 2.5rem 1.5rem;", "padding: 3.2rem 2.2rem;"),
    ("padding: 2.2rem;", "padding: 2.8rem;"),
    ("padding: 1.8rem;", "padding: 2.4rem;"),
    ("padding: 1.1rem 1.3rem;", "padding: 1.6rem 1.9rem;"),
    ("padding: 1.2rem 1.4rem;", "padding: 1.5rem 1.8rem;"),
    ("padding: 1.2rem 1.8rem;", "padding: 1.5rem 2.2rem;"),

    # 其他元素间距
    ("margin-bottom: 2.5rem;", "margin-bottom: 3.8rem;"),
    ("margin-bottom: 3rem;", "margin-bottom: 3.8rem;"),
    ("margin-bottom: 2rem;", "margin-bottom: 2.6rem;"),
    ("margin-bottom: 1.5rem;", "margin-bottom: 2rem;"),
    ("margin-bottom: 1.25rem;", "margin-bottom: 1.5rem;"),
    ("margin-bottom: 1rem;", "margin-bottom: 1.3rem;"),
    ("margin-bottom: 1.3rem;", "margin-bottom: 1.7rem;"),

    # 代码框/表格
    ("font-size: 0.95rem;", "font-size: 1.15rem;"),
    ("font-size: 0.8rem;", "font-size: 1rem;"),
    ("font-size: 0.85rem;", "font-size: 1.05rem;"),
    ("font-size: 1.1rem;", "font-size: 1.35rem;"),

    # window 相关（截图外框）
    ("height: 34px;", "height: 42px;"),
    ("padding: 0 14px;", "padding: 0 18px;"),
]

for fpath in files:
    text = fpath.read_text(encoding="utf-8")
    original = text
    for old, new in replacements:
        text = text.replace(old, new)
    if text != original:
        fpath.write_text(text, encoding="utf-8")
        print(f"  已更新: {fpath.name}")

print("✅ 批量放大完成")
