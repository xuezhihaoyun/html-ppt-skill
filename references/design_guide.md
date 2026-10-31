# HTML PPT 视觉规范参考文档

> 本文件是通用风格（page_skeleton.html）的**权威视觉规范**。SKILL.md 仅保留概览，细节以本文件为准。

## 🎨 色彩变量

| 变量 | 色值 | 用途 |
|------|------|------|
| `--bg` | `#ffffff` | 背景色 |
| `--surface` | `#f8f9fa` | 卡片背景 |
| `--accent` | `#1a2a4a` | 主色（深蓝） |
| `--accent-2` | `#c9a227` | 点缀色（金色） |
| `--text` | `#2c3e50` | 正文 |
| `--text-muted` | `#6c757d` | 次要文字 |
| `--border` | `#e2e8f0` | 边框 |
| `--font-serif` | Noto Serif SC, STSong, serif | 衬线体（中文标题、大字报） |
| `--font-serif-en` | Playfair Display, Georgia, serif | 英文衬线（hero 声明、章节编号） |
| `--font-sans` | Noto Sans SC, PingFang SC, sans-serif | 无衬线（正文、副标题） |
| `--font-mono` | JetBrains Mono, SF Mono, monospace | 等宽体（kicker、标签、元信息） |

---

## 📄 页面类型

| 类型 | 背景 | 文字 | 用法 |
|------|------|------|------|
| 深色封面/结束页 | 深色主色 | 白色 + 点缀色高亮 | 封面、抛出问题、结束页 |
| 过渡页 | 左半深色 + 右半浅色 | 左白右深 | 各部分开头 |
| 标准内容页 | `#ffffff` 或 `#f8f9fa` | `#2c3e50` | 正文、工具展示 |
| 引用/警示框 | `#f5f2e8` | `#2c3e50` | 底部强调、点缀色左边框 |
| 深色卡片 | 主色背景 | 白色 | 强调未来感/重点 |
| 代码框 | 深色背景 | 白色/点缀色 | 文件树、代码展示 |

---

## 🔤 字体规范（3-font 系统）

### 字体族

| 变量 | 字体栈 | 角色 | 使用场景 |
|------|--------|------|----------|
| `--font-serif` | Noto Serif SC, STSong, Songti SC, serif | 衬线体 | 中文大字报、hero 标题、导语 |
| `--font-serif-en` | Playfair Display, Georgia, Times New Roman, serif | 英文衬线 | 英文 hero 声明、章节编号、英文大标题 |
| `--font-sans` | Noto Sans SC, PingFang SC, Microsoft YaHei, sans-serif | 无衬线 | 正文段落、副标题、内容卡片 |
| `--font-mono` | JetBrains Mono, SF Mono, Consolas, monospace | 等宽体 | 标签、kicker、元信息、代码 |

### 排版层级

| 类名 | 字号 | 字重 | 字族 | 用途 |
|------|------|------|------|------|
| `.h-hero` | 96px | 900 | serif-en | 英文大宣言、封面核心词 |
| `.h-hero-zh` | 72px | 900 | serif | 中文大字报、关键数字标题 |
| `.h-xl` | 48px | 700 | serif-en | 章节标题、Part 编号 |
| `.h1-zh` | 36px | 700 | sans | 页面主标题 |
| `.h2-zh` | 28px | 600 | sans | 副标题 |
| `.h3-zh` | 22px | 600 | sans | 区块小标题 |
| `.body-zh` | 18px | 400 | sans | 正文段落（行高 1.7） |
| `.lead` | 22px | 400 | serif | 导语、摘要段落 |
| `.kicker` | 12px | 500 | mono | 标题上方小标签（全大写） |
| `.meta` | 13px | 400 | mono | 元信息（日期、作者、页码） |

- **标题**：使用主色（`--accent`），serif 用于层级最高的两级，sans 用于页面级和区块级
- **正文**：深灰色，行距 1.5~1.8
- **点缀**：点缀色仅用于关键词和 kicker，避免大面积使用

### 装饰类

| 类名 | 说明 |
|------|------|
| `.ghost` | 绝对定位背景大字：serif-en，字号 450px，opacity 0.04，无 pointer-events。用于章节编号（01/02/03）或英文关键词作为装饰元素。放在 slide 内配合 inline 定位使用。 |
| `.hi` | 内联荧光笔效果：半透明 accent 色底部色条，模拟马克笔高亮。使用 `color-mix()` 动态适配主题色。多行自动包裹。 |

---

## ✨ 动画规范

> ⚠️ **默认不加动画**。动画在 iframe 合并后容易出现布局偏移，内容页建议直接展示。需要时在模板 CSS 中取消注释即可。

备用动画代码（取消注释启用）：
```css
.anim-1 { animation: fadeUp 0.4s ease 0.0s both; }
.anim-2 { animation: fadeUp 0.4s ease 0.1s both; }
.anim-3 { animation: fadeUp 0.4s ease 0.2s both; }
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(12px); }
  to   { opacity: 1; transform: translateY(0); }
}
```

---

## 📐 留白与边距

| 项目 | 规范 |
|------|------|
| 页边距 | 默认模式保留稳定安全边距，按 `1600px × 900px` 舞台使用固定 `px` 值 |
| 内容宽度 | 同一 deck 内保持统一；不得为了填满屏幕随页漂移 |
| 每页要点数 | 每页最多 `3` 个信息块，每块最多 `3` 条要点；内容过多必须拆页 |
