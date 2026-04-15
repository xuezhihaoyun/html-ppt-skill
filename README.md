# 🎞️ html-ppt-skill

> 用 Markdown + HTML 打造零依赖、可离线分享的专业级网页幻灯片。

[![GitHub](https://img.shields.io/badge/GitHub-xuezhihaoyun%2Fhtml--ppt--skill-1a2a4a?logo=github)](https://github.com/xuezhihaoyun/html-ppt-skill)

---

## ✨ 核心特点

| 特性 | 说明 |
|------|------|
| **📄 Markdown 先行** | 一切始于 `.md` 文档，内容为王，结构清晰 |
| **🎨 专业视觉** | 配色、风格完全可定制，在 Markdown 中指定后即可全局应用 |
| **🚀 零依赖** | 每页独立 HTML，内联 CSS，任意浏览器直接打开 |
| **📦 单文件分享** | 自动合并为 `all_slides.html`，内嵌图片 Base64，断网可用 |
| **⌨️ 键盘控制** | `→/←` 翻页、`F` 全屏、`Home/End` 跳转、触摸滑动 |
| **🔄 迭代友好** | 中途改需求？先改 Markdown，再批量重生成 |

---

## 🏗️ 项目结构

```
html-ppt-skill/
├── SKILL.md                    # 完整 Skill 文档（工作流程 + 设计规范）
├── README.md                   # 本文件
├── references/
│   └── design_guide.md         # 色彩、字体、动画、留白规范
├── templates/
│   ├── page_skeleton.html      # 单页 HTML 骨架模板
│   ├── navigation.js           # 翻页控制器（键盘/触摸/进度条）
│   ├── merge_slides.py         # 合并为单文件（iframe + Base64 内嵌）
│   ├── scale_slides.py         # 批量放大字号/边距/图标
│   └── quick_ref.md            # 一页纸速查卡
└── output/                     # 最终生成的幻灯片目录
    ├── slide_01.html
    ├── slide_02.html
    ├── ...
    └── all_slides.html         # ⭐ 最终交付物
```

---

## 🎯 适用场景

- 律所/企业讲座演示
- 产品介绍、方案汇报
- 学术分享、技术路演
- 任何需要**轻量、跨平台、易传播**的幻灯片场景

---

## ⚡ 快速开始

### 1. 准备 Markdown 文档

先写一份结构化的 `.md` 文档，包含：
- 色彩规范
- 整体结构（页码、类型、内容）
- 每页的设计要求 + 具体内容

> 💡 **提示**：如果只有粗略想法，可以先让 AI 帮你把大纲扩写成标准 Markdown。

### 2. 逐页生成 HTML

按 `slide_01.html` ~ `slide_NN.html` 的规范命名，每页引用 `navigation.js`。

### 3. 修改 navigation.js

```javascript
const total = 28;  // ← 改为实际总页数
```

### 4. 合并为单文件

```bash
cd output
python3 ../templates/merge_slides.py
```

输出 `all_slides.html`，**直接发给朋友即可**。

---

## 🎮 播放控制

| 按键 | 功能 |
|------|------|
| `→` / `Space` | 下一张 |
| `←` | 上一张 |
| `F` | 全屏切换 |
| `Home` | 跳到首页 |
| `End` | 跳到末页 |
| 触摸滑动 | 左右滑动翻页 |

---

## 🛠️ 高级脚本

### 调整屏占比

如果播放时感觉内容太小，一键批量放大：

```bash
python3 templates/scale_slides.py
```

会自动调整：
- 页边距压缩
- 内容最大宽度放宽（`1600px+`）
- 标题、正文、图标整体放大

---

## 🎨 设计规范速览

> 以下为一组**示例配色**，实际项目中可在 Markdown 文档里自由替换为你想要的主题色。

```css
:root {
  --accent:     #1a2a4a;   /* 主色 */
  --accent-2:   #c9a227;   /* 点缀色 */
  --bg:         #ffffff;   /* 背景 */
  --surface:    #f8f9fa;   /* 卡片背景 */
  --text:       #2c3e50;   /* 正文 */
  --text-muted: #6c757d;   /* 次要文字 */
  --border:     #e2e8f0;   /* 边框 */
}
```

### 页面类型（示例）
- **深色封面页**：深色背景，白色大字，点缀色高亮
- **过渡页**：左右半屏分割（深色 + 浅色对比）
- **内容页**：卡片、表格、流程图
- **代码页**：深色代码框 + 浅色说明

### 动画
统一使用 `fadeUp` 入场动画，支持 `.anim-1` ~ `.anim-4` 延迟触发。

---

## 📌 关键经验

1. **Markdown 是唯一真相源** — 任何迭代先改 `.md`，再同步 HTML
2. **合并必须用 iframe + srcdoc** — 直接用 CSS 拼接会导致 28 页样式互相覆盖
3. **图片必须内嵌为 Base64** — 否则分享的 `all_slides.html` 在别人电脑上会丢图
4. **命名严格统一** — `slide_01.html` ~ `slide_NN.html`，`navigation.js` 才能自动识别

---

## 📝 License

MIT © [xuezhihaoyun](https://github.com/xuezhihaoyun)
