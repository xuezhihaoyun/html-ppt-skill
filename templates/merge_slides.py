#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将所有 slide_*.html 合并成一个独立的 all_slides.html。
使用 iframe + srcdoc 实现每页 CSS 完全隔离，自动将本地图片转为 Base64 内嵌。
"""

import base64
import re
from pathlib import Path

SLIDES_DIR = Path(__file__).parent.parent / "output"
OUTPUT = SLIDES_DIR / "all_slides.html"


def natural_sort_key(p: Path):
    m = re.search(r'(\d+)', p.name)
    return (int(m.group(1)), p.name) if m else (0, p.name)


def js_escape(s: str) -> str:
    return s.replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n').replace('\r', '')


def get_img_data_uri(filename: str) -> str:
    fpath = SLIDES_DIR / filename
    if not fpath.exists():
        return filename
    ext = fpath.suffix.lower().replace('.', '')
    mime = 'image/png' if ext == 'png' else 'image/jpeg' if ext in ('jpg', 'jpeg') else 'image/svg+xml'
    b64 = base64.b64encode(fpath.read_bytes()).decode('ascii')
    return f"data:{mime};base64,{b64}"


def build():
    slide_files = sorted(SLIDES_DIR.glob("slide_*.html"), key=natural_sort_key)
    slide_htmls = []

    for fpath in slide_files:
        html = fpath.read_text(encoding="utf-8")

        # 移除 navigation.js
        html = re.sub(r'<script\s+src="navigation\.js"\s*>\s*</script>', '', html)

        # 移除 #nav 块
        html = re.sub(r'<div\s+id="nav"[^>]*>.*?</div>\s*', '', html, flags=re.DOTALL)

        # 将所有本地图片引用替换为 Base64 Data URI
        for m in re.finditer(r'src="([^"]+\.(?:png|jpg|jpeg|svg|gif))"', html):
            filename = m.group(1)
            data_uri = get_img_data_uri(filename)
            html = html.replace(f'src="{filename}"', f'src="{data_uri}"')

        slide_htmls.append(html.strip())

    total = len(slide_htmls)
    escaped_slides = ',\n'.join([f"  '{js_escape(h)}'" for h in slide_htmls])

    merged = f'''<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>从工具到思维——法律人的AI原生认知</title>
<style>
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
html, body {{ width: 100%; height: 100%; overflow: hidden; font-family: 'Noto Sans SC', 'PingFang SC', 'Microsoft YaHei', 'Helvetica Neue', sans-serif; }}
iframe.slide-frame {{ position: absolute; inset: 0; width: 100%; height: 100%; border: none; display: none; background: #fff; }}
iframe.slide-frame.active {{ display: block; }}
#progress {{
  position: fixed;
  top: 0; left: 0;
  height: 3px;
  background: linear-gradient(90deg, #1a2a4a, #c9a227);
  transition: width 0.4s cubic-bezier(0.4,0,0.2,1);
  z-index: 100;
}}
#slide-num {{
  position: fixed;
  bottom: 28px; left: 32px;
  font-size: 12px;
  color: #fff;
  background: rgba(0,0,0,0.35);
  padding: 4px 10px;
  border-radius: 6px;
  z-index: 100;
}}
#nav {{
  position: fixed;
  bottom: 20px; right: 24px;
  display: flex;
  align-items: center;
  gap: 10px;
  z-index: 100;
  background: rgba(0,0,0,0.35);
  padding: 6px 10px;
  border-radius: 10px;
}}
#nav button {{
  width: 40px; height: 40px;
  background: rgba(255,255,255,0.9);
  border: none;
  color: #1a2a4a;
  border-radius: 10px;
  cursor: pointer;
  font-size: 20px;
  display: flex; align-items: center; justify-content: center;
  transition: background 0.2s;
}}
#nav button:hover {{ background: #fff; }}
#counter {{
  font-size: 13px;
  color: #fff;
  min-width: 50px;
  text-align: center;
}}
</style>
</head>
<body>

<div id="progress"></div>
<div id="slide-num">01</div>
<div id="frames"></div>

<div id="nav">
  <button onclick="prev()" title="上一张">‹</button>
  <span id="counter">1 / {total}</span>
  <button onclick="next()" title="下一张">›</button>
</div>

<script>
(function() {{
  const total = {total};
  let current = 1;
  const slideHtmls = [
{escaped_slides}
  ];

  const container = document.getElementById('frames');
  const iframes = [];

  slideHtmls.forEach((html) => {{
    const iframe = document.createElement('iframe');
    iframe.className = 'slide-frame';
    iframe.srcdoc = html;
    container.appendChild(iframe);
    iframes.push(iframe);
  }});

  function updateUI() {{
    document.getElementById('counter').textContent = current + ' / ' + total;
    document.getElementById('progress').style.width = (current / total * 100) + '%';
    document.getElementById('slide-num').textContent = String(current).padStart(2, '0');

    iframes.forEach((iframe, i) => {{
      const slide = iframe.contentDocument && iframe.contentDocument.querySelector('.slide');
      if (i + 1 === current) {{
        iframe.classList.add('active');
        if (slide) {{
          slide.classList.remove('active');
          void slide.offsetWidth;
          slide.classList.add('active');
        }}
      }} else {{
        iframe.classList.remove('active');
        if (slide) slide.classList.remove('active');
      }}
    }});
  }}

  window.next = function() {{ if (current < total) {{ current++; updateUI(); }} }};
  window.prev = function() {{ if (current > 1) {{ current--; updateUI(); }} }};

  document.addEventListener('keydown', e => {{
    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'Space') {{
      e.preventDefault(); window.next();
    }}
    if (e.key === 'ArrowLeft') {{
      e.preventDefault(); window.prev();
    }}
    if (e.key === 'Home') {{ e.preventDefault(); current = 1; updateUI(); }}
    if (e.key === 'End')  {{ e.preventDefault(); current = total; updateUI(); }}
    if (e.key === 'f' || e.key === 'F') {{
      e.preventDefault();
      if (!document.fullscreenElement) {{
        document.documentElement.requestFullscreen().catch(()=>{{}});
      }} else {{
        document.exitFullscreen().catch(()=>{{}});
      }}
    }}
  }});

  let touchStartX = 0;
  document.addEventListener('touchstart', e => {{
    touchStartX = e.touches[0].clientX;
  }});
  document.addEventListener('touchend', e => {{
    const dx = e.changedTouches[0].clientX - touchStartX;
    if (dx < -50) window.next();
    if (dx > 50) window.prev();
  }});

  iframes[0].addEventListener('load', updateUI);
  setTimeout(updateUI, 50);
}})();
</script>

</body>
</html>
'''

    OUTPUT.write_text(merged, encoding="utf-8")
    print(f"✅ 已合并 {total} 页幻灯片到: {OUTPUT}")


if __name__ == '__main__':
    build()
