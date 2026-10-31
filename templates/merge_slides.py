#!/usr/bin/env python3
"""
merge_slides.py — 将 slide_*.html 合并为一个 all_slides.html
- 使用 iframe + srcdoc 隔离每页 CSS
- 自动将本地图片转为 Base64 Data URI 内嵌
"""

import base64
import mimetypes
import re
from pathlib import Path

SLIDES_DIR = Path(__file__).parent.parent / "output"
OUTPUT = SLIDES_DIR / "all_slides.html"
NAVIGATION_SCRIPT = Path(__file__).with_name("navigation.js")
IMAGE_SUFFIX = re.compile(r"\.(?:png|jpe?g|svg|gif|webp|avif)(?:[?#].*)?$", re.I)


def natural_sort_key(p: Path):
    """按文件名中的数字排序"""
    m = re.search(r"(\d+)", p.name)
    return int(m.group(1)) if m else 0


def js_escape(s: str) -> str:
    """转义 HTML 内容，使其可以安全嵌入 srcdoc 属性。
    注意：HTML 实体（&amp; &lt; &gt; 等）中的 & 不能再次转义，
    否则会出现 &amp;amp; 的双重转义。只处理：
    - &quot; → 防止 srcdoc 属性被截断
    - 反引号/模板语法 → 防止 JS 模板字符串出错
    - 换行符 → 防止 srcdoc 属性解析异常
    """
    return (
        s.replace("&quot;", "&amp;quot;")
         .replace("\\", "\\\\")
         .replace("`", "\\`")
         .replace("${", "\\${")
         .replace('"', "&quot;")
         .replace("\r\n", "\n")
         .replace("\r", "\n")
         .replace("\n", "&#10;")
    )


def is_image_reference(src: str) -> bool:
    return bool(IMAGE_SUFFIX.search(src.strip()))


def get_asset_data_uri(src: str, base_dir: Path) -> str:
    """将一个受控目录内的本地图片转为 data URI。"""
    clean_src = re.sub(r"[?#].*$", "", src.strip())
    if clean_src.startswith(("http://", "https://", "//")):
        raise ValueError(f"不允许外部图片依赖: {src}")
    if clean_src.startswith(("/", "file:", "~")) or re.match(r"^[A-Za-z]:[\\/]", clean_src):
        raise ValueError(f"不允许绝对图片路径: {src}")

    asset_path = (base_dir / clean_src).resolve()
    try:
        asset_path.relative_to(base_dir.resolve())
    except ValueError as exc:
        raise ValueError(f"图片路径越出页面目录: {src}") from exc
    if not asset_path.is_file():
        raise FileNotFoundError(f"找不到本地图片: {asset_path}")

    mime = mimetypes.guess_type(asset_path.name)[0] or "application/octet-stream"
    data = base64.b64encode(asset_path.read_bytes()).decode()
    return f"data:{mime};base64,{data}"


def inline_local_assets(html: str, base_dir: Path) -> str:
    """内嵌本地图片；任何缺图、外链或绝对路径都中止合并。"""
    problems = []

    def replace_src(m):
        quote, src = m.group(1), m.group(2)
        if not is_image_reference(src) or src.strip().startswith("data:"):
            return m.group(0)
        try:
            return f'src={quote}{get_asset_data_uri(src, base_dir)}{quote}'
        except (FileNotFoundError, ValueError) as exc:
            problems.append(str(exc))
            return m.group(0)

    def replace_url(m):
        quote = m.group(1) or ""
        src = m.group(2).strip()
        if not is_image_reference(src) or src.startswith("data:"):
            return m.group(0)
        try:
            return f"url({quote}{get_asset_data_uri(src, base_dir)}{quote})"
        except (FileNotFoundError, ValueError) as exc:
            problems.append(str(exc))
            return m.group(0)

    html = re.sub(r'src=(["\'])([^"\']+)\1', replace_src, html)
    html = re.sub(r'url\(\s*(["\']?)([^"\')]+)\1\s*\)', replace_url, html)
    if problems:
        raise ValueError("\n".join(sorted(set(problems))))
    return html


def assert_no_external_dependencies(html: str, source_name: str) -> None:
    """阻止会破坏离线交付的外部 CSS、JS 和字体导入。"""
    patterns = [
        r"@import\s+(?:url\()?['\"]?(?:https?:)?//",
        r"<script\b[^>]*\bsrc=['\"](?:https?:)?//",
        r"<link\b[^>]*\bhref=['\"](?:https?:)?//",
    ]
    if any(re.search(pattern, html, re.I) for pattern in patterns):
        raise ValueError(f"{source_name} 含外部 CSS、JS 或字体依赖，无法离线交付")


def build():
    files = sorted(SLIDES_DIR.glob("slide_*.html"), key=natural_sort_key)
    if not files:
        print("❌ 未找到 slide_*.html 文件"); return

    # 检查页码连续性
    nums = [natural_sort_key(f) for f in files]
    expected = list(range(1, len(nums) + 1))
    if nums != expected:
        missing = [n for n in range(1, max(nums) + 1) if n not in nums]
        if missing:
            print(f"⚠️  检测到缺失页码: {missing}，合并可能不完整")
        if nums[0] != 1:
            print(f"⚠️  首页不是 slide_01.html（实际从 slide_{nums[0]:02d}.html 开始）")

    slides = []
    for fpath in files:
        html = fpath.read_text(encoding="utf-8")
        assert_no_external_dependencies(html, fpath.name)

        # 移除 navigation.js 引用
        html = re.sub(r'<script\s+src="navigation\.js"></script>', '', html)

        # 移除 #nav 导航块
        html = re.sub(r'<div id="nav">.*?</div>', '', html, flags=re.DOTALL)

        # 移除 #slide-num 页码（合并后由外层统一显示）
        html = re.sub(r'<div id="slide-num">.*?</div>', '', html, flags=re.DOTALL)

        # 替换本地图片为 Base64，包括 <img src> 和 CSS background url(...)
        try:
            html = inline_local_assets(html, fpath.parent)
        except (FileNotFoundError, ValueError) as exc:
            raise RuntimeError(f"{fpath.name} 资源校验失败：{exc}") from exc

        slides.append(html)

    total = len(slides)
    navigation_script = NAVIGATION_SCRIPT.read_text(encoding="utf-8")
    iframe_blocks = []
    for i, s in enumerate(slides, 1):
        escaped = js_escape(s)
        iframe_blocks.append(
            f'<iframe id="f{i}" class="frame" srcdoc="{escaped}" '
            f'allow="fullscreen" allowfullscreen style="display:none"></iframe>'
        )

    merged = f"""<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>幻灯片</title>
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{--deck-width:1600px;--deck-height:900px;--deck-scale:1}}
html,body{{width:100%;height:100%;overflow:hidden;background:#000}}
.frame{{position:absolute;top:50%;left:50%;width:var(--deck-width);height:var(--deck-height);border:none;background:#fff;transform:translate(-50%,-50%) scale(var(--deck-scale));transform-origin:center center}}
#progress{{position:fixed;top:0;left:0;height:3px;background:linear-gradient(90deg,#1a2a4a,#c9a227);z-index:100}}
#nav{{position:fixed;bottom:28px;right:32px;display:flex;align-items:center;gap:10px;z-index:100}}
#nav button{{width:40px;height:40px;background:rgba(26,42,74,0.06);border:1px solid #e2e8f0;color:#1a2a4a;border-radius:10px;cursor:pointer;font-size:20px}}
#counter{{font-size:13px;color:#6c757d;min-width:50px;text-align:center}}
</style>
</head>
<body>
<div id="progress"></div>
{''.join(iframe_blocks)}
<div id="nav">
<button onclick="prev()" title="上一张">‹</button>
<span id="counter">1 / {total}</span>
<button onclick="next()" title="下一张">›</button>
</div>
<script>
{navigation_script}
</script>
</body>
</html>"""

    OUTPUT.write_text(merged, encoding="utf-8")
    print(f"✅ 已合并 {total} 页幻灯片到: {OUTPUT}")


if __name__ == "__main__":
    build()
