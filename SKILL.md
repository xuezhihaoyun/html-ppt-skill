# HTML PPT 制作 Skill

## 一、触发条件

当用户提出以下需求时，调用本 Skill：
- "帮我做一个 HTML 格式的 PPT"
- "做一个可以在浏览器里播放的幻灯片"
- "生成一组网页版演示文稿"
- "用 HTML/CSS 做 PPT"
- "把这个 Markdown 转成 PPT"

## 二、核心原则

1. **一切始于 Markdown 文档**：在写任何一行 HTML 之前，必须先共建或拆解出一份结构清晰的 `.md` 文档。
2. **迭代是常态**：用户随时可能中途调整内容、顺序、配色、版式。每次调整优先改 MD，再同步生成对应 HTML。
3. **为分享而生**：所有本地资源（图片、图标等）必须默认内嵌为 Base64 Data URI，最终输出一个可断网运行的 `all_slides.html`。

## 三、制作流程

### Step 0：共建 Markdown 文档
这是整个流程的**起点和锚点**。

**如果用户只给了一个粗略想法**：
- 主动向用户确认：页数、演讲时长、目标受众、核心章节
- 提供一份 Markdown 大纲草稿，让用户填充内容

**如果用户给了一份不完善的 Markdown**：
- 先阅读并拆解文档
- 提出需要补充的信息：
  - 每页的**设计要求**（版式、图标意象、配色微调）
  - 是否有**截图/图片**需要插入及对应页码
  - 封面/结束页/过渡页的特殊视觉效果
  - 是否有表格、流程图、代码展示等特殊元素
- 将拆解结果整理成规范的 Markdown 后，**等待用户确认或修改**

**如果用户给了一份完整的 Markdown**：
- 核对清单：页数、工具清单完整性、图片引用路径、色彩规范
- 确认无误后进入下一步

**Markdown 文档标准结构**：
```markdown
# 《标题》

## 【色彩规范】
| 元素 | 颜色 | 色值 |

## 【整体结构】（N 页）
| 页码 | 类型 | 内容 |

## 【第 1 页】封面
**设计要求：** ...
**页面内容：** ...

## 【第 N 页】结束页
...
```

### Step 1：明确演讲规格（基于确认后的 MD）
- 总页数
- 每页内容/结构/版式
- 色彩偏好（主色、点缀色、背景色）
- 需要插入的图片清单及对应页码
- 是否需要输出为单文件分享版（默认：是）

### Step 2：初始化文件结构
```
slides/
├── slide_01.html      # 封面
├── slide_02.html      # 内容页
├── ...
├── slide_NN.html      # 结束页
├── navigation.js      # 统一的翻页控制器
├── merge_slides.py    # 合并为单文件的脚本
├── scale_slides.py    # 批量调整字号/边距的脚本（可选）
└── all_slides.html    # 最终合并版（内嵌所有资源）
```

### Step 3：逐页生成 HTML
每页都是一个独立的、零依赖的 HTML 文件：
- 内联 CSS（不依赖外部样式表）
- 使用 CSS Variables 统一主题
- 通过 `.anim-1` ~ `.anim-4` + `@keyframes fadeUp` 实现入场动画
- 固定底部导航条（引用 `navigation.js`）
- 如果某页需要插入图片，HTML 中先用相对路径引用（如 `src="pdf_page_20.png"`）

### Step 4：配置 navigation.js
```javascript
const total = NN;  // 与实际页数保持一致
```

### Step 5：合并为单文件（默认执行）
运行 `merge_slides.py`：
- 使用 **iframe + srcdoc** 隔离每页 CSS，避免 N 份样式互相覆盖
- **自动将所有本地图片转为 Base64 Data URI 内嵌**
- 输出 `all_slides.html`，实现：
  - 断网可运行
  - 微信/邮件直传
  - 双击即用

### Step 6：全屏与播放测试
- 按 `F` 键切换全屏
- 按 `→` / `←` 翻页
- 触摸设备支持左右滑动

### Step 7：响应迭代调整
- 如果用户中途要求修改内容/顺序/样式：
  1. **先回改 Markdown 文档**（保持源文档为唯一真相源）
  2. 修改对应 `slide_XX.html`
  3. 重新运行 `merge_slides.py` 生成新的 `all_slides.html`

## 四、设计规范

### 色彩变量
```css
:root {
  --bg:         #ffffff;      /* 背景色 */
  --surface:    #f8f9fa;      /* 卡片背景 */
  --accent:     #1a2a4a;      /* 主色：深海军蓝 */
  --accent-2:   #c9a227;      /* 点缀色：香槟金 */
  --text:       #2c3e50;      /* 正文 */
  --text-muted: #6c757d;      /* 次要文字 */
  --border:     #e2e8f0;      /* 边框 */
}
```

### 页面类型与版式
| 类型 | 特征 | 典型页 |
|------|------|--------|
| 深色封面页 | `#0d1b2a` 背景，白色大字，香槟金点缀 | 封面、结束页 |
| 过渡页 | 左右半屏分割（左深蓝 + 右白） | 各部分开头 |
| 内容页 | 白色/浅灰背景，卡片/表格/流程图 | 正文页 |
| 代码页 | 深色代码框 + 浅色说明 | 技术揭秘页 |

### 动画规范
- 入场动画统一使用 `fadeUp`
-  stagger 延迟：`anim-1` (0s) → `anim-2` (0.1s) → `anim-3` (0.2s)
- 只有 `.slide.active` 才触发动画

### 屏占比与留白
- 内容 `max-width` 建议 `1400px ~ 1900px`
- 页边距使用 `vw` 单位，保持响应式
- 留白是一种高级感，不堆砌文字

## 五、代码模板

### 单页 HTML 骨架
```html
<!DOCTYPE html>
<html lang="zh">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>页面标题</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    :root {
      --accent: #1a2a4a;
      --accent-2: #c9a227;
      --text-muted: #6c757d;
    }
    html, body {
      width: 100%; height: 100%;
      background: #ffffff;
      color: var(--text);
      font-family: 'Noto Sans SC', 'PingFang SC', 'Microsoft YaHei', sans-serif;
      overflow: hidden;
    }
    .slide {
      position: absolute;
      inset: 0;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      padding: 2vw 4vw;
      opacity: 0;
      pointer-events: none;
    }
    .slide.active {
      opacity: 1;
      pointer-events: auto;
    }
    .slide.active .anim-1 { animation: fadeUp 0.5s ease 0.0s both; }
    .slide.active .anim-2 { animation: fadeUp 0.5s ease 0.1s both; }
    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(18px); }
      to   { opacity: 1; transform: translateY(0); }
    }
    /* 进度条 */
    #progress {
      position: fixed;
      top: 0; left: 0;
      height: 3px;
      background: linear-gradient(90deg, var(--accent), var(--accent-2));
      z-index: 100;
    }
    /* 幻灯片编号 */
    #slide-num {
      position: fixed;
      bottom: 28px; left: 32px;
      font-size: 12px;
      color: var(--text-muted);
      z-index: 100;
    }
    /* 导航 */
    #nav {
      position: fixed;
      bottom: 28px; right: 32px;
      display: flex;
      align-items: center;
      gap: 10px;
      z-index: 100;
    }
    #nav button {
      width: 40px; height: 40px;
      background: rgba(26,42,74,0.06);
      border: 1px solid var(--border);
      color: var(--accent);
      border-radius: 10px;
      cursor: pointer;
      font-size: 20px;
    }
    #counter {
      font-size: 13px;
      color: var(--text-muted);
      min-width: 50px;
      text-align: center;
    }
  </style>
</head>
<body>
  <div id="progress"></div>
  <div id="slide-num">01</div>

  <div class="slide active" id="s0">
    <!-- 页面内容 -->
  </div>

  <div id="nav">
    <button onclick="prev()" title="上一张">‹</button>
    <span id="counter">1 / N</span>
    <button onclick="next()" title="下一张">›</button>
  </div>

  <script src="navigation.js"></script>
</body>
</html>
```

### navigation.js 模板
```javascript
(function() {
  const match = location.pathname.match(/slide_(\d+)\.html$/);
  const current = match ? parseInt(match[1], 10) : 1;
  const total = NN;  // ← 修改为实际总页数

  function updateUI() {
    const counter = document.getElementById('counter');
    const progress = document.getElementById('progress');
    const slideNum = document.getElementById('slide-num');
    if (counter) counter.textContent = `${current} / ${total}`;
    if (progress) progress.style.width = `${(current / total) * 100}%`;
    if (slideNum) slideNum.textContent = String(current).padStart(2, '0');
  }

  function go(n) {
    if (n < 1 || n > total) return;
    const filename = `slide_${String(n).padStart(2, '0')}.html`;
    location.href = filename;
  }

  window.next = function() { go(current + 1); };
  window.prev = function() { go(current - 1); };

  document.addEventListener('keydown', e => {
    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'Space') {
      e.preventDefault(); window.next();
    }
    if (e.key === 'ArrowLeft') {
      e.preventDefault(); window.prev();
    }
    if (e.key === 'Home') { e.preventDefault(); go(1); }
    if (e.key === 'End')  { e.preventDefault(); go(total); }
    if (e.key === 'f' || e.key === 'F') {
      e.preventDefault();
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(()=>{});
      } else {
        document.exitFullscreen().catch(()=>{});
      }
    }
  });

  let touchStartX = 0;
  document.addEventListener('touchstart', e => {
    touchStartX = e.touches[0].clientX;
  });
  document.addEventListener('touchend', e => {
    const dx = e.changedTouches[0].clientX - touchStartX;
    if (dx < -50) window.next();
    if (dx > 50) window.prev();
  });

  updateUI();
})();
```

## 六、关键经验

1. **一切始于 Markdown**：MD 文档是唯一真相源，任何迭代都先改 MD 再同步 HTML
2. **零依赖**：每页 HTML 自带 CSS，不依赖 Tailwind / Bootstrap，拷到任何浏览器都能打开
3. **命名规范**：统一用 `slide_01.html` ~ `slide_NN.html`，`navigation.js` 才能自动识别页码
4. **单页隔离**：合并时必须用 **iframe + srcdoc**，不要用简单的 CSS 拼接，否则多页样式会互相覆盖
5. **图片必须内嵌**：分享的 `all_slides.html` 必须将本地图片转为 Base64 Data URI，否则接收方看不到图
6. **屏占比**：按主流 16:9 投影尺寸设计，内容区宽度尽量放宽到 `1600px+`，避免中间一小块
7. **迭代友好**：保留 `merge_slides.py` 和 `scale_slides.py`，便于随时批量重生成或调整字号

## 七、文件结构（标准 Skill 树）

```
html-ppt/
├── SKILL.md              ← 本文件
├── references/
│   └── design_guide.md   ← 用户提供的视觉规范
├── templates/
│   ├── page_skeleton.html
│   ├── navigation.js
│   ├── merge_slides.py
│   └── scale_slides.py
├── source.md             ← 用户原始/共建的 Markdown 文档
└── output/
    ├── slide_01.html
    ├── ...
    └── all_slides.html   ← 最终交付物（内嵌所有资源）
```
