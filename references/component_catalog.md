# 组件目录 — 默认模式

> 生成 PPT 时，必须从本目录中选择组件编号，不得自行发明新的表格/卡片/流程图样式。
> 如需新增组件，必须先在本文件中注册并更新画廊 HTML。

## 组件总览

| 编号 | 名称 | 适用场景 | 列数/结构 |
|------|------|---------|----------|
| **T1** | 表格 — 简洁线框 | 轻量对比、数据罗列 | 多列线框表 |
| **T2** | 表格 — 斑马纹 | 多行数据、扫描式阅读 | 交替行色表 |
| **T3** | 表格 — 深色表头 | 正式汇报、强调表头层级 | 深蓝表头+白底 |
| **C2** | 卡片 — 2 列 | 两个并列模块、功能对比、双视角 | 2 列卡片网格 |
| **C3** | 卡片 — 3 列 | 三要素并列、流程三步、特性展示 | 3 列卡片网格 |
| **C4** | 卡片 — 4 列 | 四象限、多维指标、特性矩阵 | 4 列卡片网格 |
| **FH** | 流程 — 横向 | 4~5 步流程、工作流、阶段推进 | 横向圆形步骤+箭头 |
| **FV** | 流程 — 纵向时间线 | 发展历程、里程碑、时间线叙事 | 纵向圆点+时间轴 |
| **BA** | 对比框 | 旧 vs 新、问题 vs 方案、传统 vs 智能 | 左浅右深双栏 |
| **ST** | 数据大字报 | 核心指标、成绩单、关键数字 | 超大数字+标注 |
| **QT** | 引用框 / 强调框 | 金句、法规引用、核心观点强调 | 左边框金色引用 |
| **IL** | 图标 + 文字列表 | 特性清单、功能列表、要点罗列 | 图标徽章+文字 |
| **KV** | 键值对列表 | 案件信息、属性展示、档案卡片 | 2 列键值对 |
| **TI** | 左文右图 | 图文混排、产品介绍、案例展示 | 左文字右图片 |
| **IT** | 右文左图 | 图先入为主、数据可视化配文 | 左图片右文字 |
| **PG** | 分阶段进度条 | 占比对比、阶段完成度、资源分配 | 水平渐变条 |
| **LR** | 法律关系图 | 合同、资金、控制、代理、担保与责任关系 | 自由定位节点 + SVG 关系线 |
| **EC** | 证据链 | 证据、待证事实、阶段结论与缺口 | 三段式证明路径 |
| **DF** | 法律判断流程 | 请求权基础、构成要件、程序与责任判断 | 带条件分支的流程图 |
| **GH** | Ghost 背景大字 | 章节过渡页、封面装饰、分区标识 | 绝对定位超大英文/数字 |
| **HI** | Highlight 荧光笔 | 关键句、核心词、需要视觉强调的短语 | 内联半透明高亮底色 |

> **注意**：GH 和 HI 是装饰增强，可与任意内容组件配合使用，不受"同一页面只使用一种内容组件"约束。

## 组件 CSS 类名速查

以下类名已在 `page_skeleton.html` 中预定义，可直接使用。

> **权威来源**：组件的实际样式以 `templates/page_skeleton.html` 的 `<style>` 为准。本文件的 CSS 与之保持同步，仅供查阅；改样式时改骨架，然后回填本文件，不要只改一边。

### 表格类

```css
/* 通用表格字号：th/td 16px */
table { width:100%; border-collapse:collapse }
th, td { padding:10px 16px; text-align:left; font-size:16px }

/* T1 简洁线框 */
.t1 th { border-bottom:2px solid var(--accent); color:var(--accent); font-weight:600 }
.t1 td { border-bottom:1px solid var(--border) }
.t1 tr:last-child td { border-bottom:none }

/* T2 斑马纹 */
.t2 th { background:var(--accent); color:#fff; font-weight:600 }
.t2 tbody tr:nth-child(even) { background:var(--surface) }

/* T3 深色表头 */
.t3 th { background:var(--accent); color:#fff; font-weight:600 }
.t3 td { border-bottom:1px solid var(--border) }
```

### 卡片类

```css
.card { background:var(--surface); border:1px solid var(--border); border-radius:10px; padding:22px }
.card-icon { font-size:32px; margin-bottom:8px }
.card-title { font-size:20px; font-weight:600; color:var(--accent); margin-bottom:6px }
.card-text { font-size:15px; color:var(--text-muted); line-height:1.6 }
.cards-grid { display:grid; gap:18px }
.cards-grid.c2 { grid-template-columns:1fr 1fr }
.cards-grid.c3 { grid-template-columns:1fr 1fr 1fr }
.cards-grid.c4 { grid-template-columns:1fr 1fr 1fr 1fr }
```

### 流程类

```css
/* FH 横向 */
.flow-h { display:flex; align-items:center; justify-content:center; gap:0 }
.flow-step { display:flex; flex-direction:column; align-items:center; gap:8px; flex:1 }
.flow-circle { width:56px; height:56px; border-radius:50%; background:var(--accent-3); color:#fff;
  display:flex; align-items:center; justify-content:center; font-size:22px; font-weight:700 }
.flow-label { font-size:18px; color:var(--accent); font-weight:600; text-align:center }
.flow-desc { font-size:15px; color:var(--text-muted); text-align:center; max-width:150px }
.flow-arrow { font-size:24px; color:var(--accent-2); margin:0 -4px; align-self:center; margin-bottom:24px }

/* FV 纵向时间线 */
.timeline { display:flex; flex-direction:column; gap:0; position:relative; padding-left:40px }
.timeline::before { content:''; position:absolute; left:16px; top:28px; bottom:28px; width:2px; background:var(--border) }
.tl-item { display:flex; align-items:flex-start; gap:18px; padding:10px 0; position:relative }
.tl-dot { width:14px; height:14px; border-radius:50%; background:var(--accent); border:3px solid var(--accent-2);
  position:absolute; left:-40px; top:18px }
.tl-year { font-size:18px; font-weight:700; color:var(--accent-2); min-width:64px }
.tl-content { flex:1 }
.tl-title { font-size:20px; font-weight:600; color:var(--accent); margin-bottom:3px }
.tl-desc { font-size:16px; color:var(--text-muted) }
```

### 对比框

```css
.compare { display:grid; grid-template-columns:1fr 1fr; gap:24px }
.compare-side { border-radius:10px; padding:22px 26px }
.compare-left { background:var(--surface); border:1px solid var(--border) }
.compare-right { background:var(--accent); color:#fff }
.compare-label { font-size:16px; font-weight:700; text-transform:uppercase; letter-spacing:2px; margin-bottom:12px; opacity:0.7 }
.compare-right .compare-label { color:var(--accent-2) }
.compare-item { font-size:18px; margin-bottom:8px; display:flex; align-items:center; gap:10px }
.compare-left .compare-item::before { content:'✕'; color:#e74c3c; font-weight:700 }
.compare-right .compare-item::before { content:'✓'; color:var(--accent-2); font-weight:700 }
```

### 数据大字报

```css
.stats-grid { display:grid; gap:24px }
.stats-grid.s3 { grid-template-columns:1fr 1fr 1fr }
.stats-grid.s4 { grid-template-columns:1fr 1fr 1fr 1fr }
.stat-box { text-align:center; padding:20px }
.stat-number { font-size:56px; font-weight:800; color:var(--accent); line-height:1 }
.stat-unit { font-size:20px; color:var(--accent-2); font-weight:600 }
.stat-label { font-size:16px; color:var(--text-muted); margin-top:6px }
```

### 引用框

```css
.quote-box { border-left:4px solid var(--accent-2); background:var(--surface); padding:20px 24px; border-radius:0 8px 8px 0 }
.quote-text { font-size:22px; color:var(--accent); line-height:1.6 }
.quote-source { font-size:15px; color:var(--text-muted); margin-top:10px }
```

### 图标列表

```css
.icon-list { display:flex; flex-direction:column; gap:14px }
.icon-item { display:flex; align-items:center; gap:14px; font-size:18px }
.icon-badge { width:36px; height:36px; border-radius:8px; background:var(--accent); color:#fff;
  display:flex; align-items:center; justify-content:center; font-size:18px; flex-shrink:0 }
.icon-item-text { color:var(--text) }
.icon-item-text strong { color:var(--accent) }
```

### 键值对

```css
.kv-list { display:grid; grid-template-columns:1fr 1fr; gap:12px 32px }
.kv-item { display:flex; justify-content:space-between; align-items:center; padding:10px 16px; border-radius:6px }
.kv-item:nth-child(odd) { background:var(--surface) }
.kv-key { font-size:15px; color:var(--text-muted) }
.kv-value { font-size:18px; font-weight:600; color:var(--accent) }
```

### 图文分栏

```css
.split-layout { display:grid; gap:32px; align-items:center; height:100% }
.split-layout.ti { grid-template-columns:1.2fr 1fr }
.split-layout.it { grid-template-columns:1fr 1.2fr }
.split-text { display:flex; flex-direction:column; gap:14px }
.split-text h3 { font-size:24px; color:var(--accent); font-weight:700 }
.split-text p { font-size:17px; color:var(--text-muted); line-height:1.7 }
.split-image { background:var(--surface); border:2px dashed var(--border); border-radius:10px;
  height:300px; display:flex; align-items:center; justify-content:center; color:var(--text-muted); font-size:15px }
```

### 进度条

```css
.phases { display:flex; flex-direction:column; gap:16px }
.phase-row { display:flex; align-items:center; gap:16px }
.phase-bar { height:12px; border-radius:6px; background:linear-gradient(90deg,var(--accent),var(--accent-3)) }
.phase-label { font-size:17px; color:var(--accent); font-weight:600; min-width:90px }
.phase-value { font-size:16px; color:var(--text-muted); margin-left:auto }
```

### 法律可视化

详细绘制方法、颜色与线条语义见 `references/legal_visualization.md`。

```css
/* LR 法律关系图 */
.legal-map { position:relative; height:480px; background:#fff; border:1px solid var(--border); border-radius:14px; overflow:hidden }
.legal-map svg { position:absolute; inset:0; width:100%; height:100%; z-index:1 }
.legal-entity { position:absolute; z-index:2; min-width:190px; min-height:92px; padding:16px 20px; border-radius:12px; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; background:var(--accent); color:#fff; box-shadow:0 12px 26px rgba(26,42,74,.14) }
.legal-entity strong { font-size:20px }            /* 主体名称 */
.legal-entity span { margin-top:5px; font-size:14px; opacity:.78 }  /* 法律身份/角色 */
.legal-entity.neutral { background:var(--accent-3) }
.legal-entity.risk { background:#C84C4C }
.legal-entity.result { background:#4E8B72 }
.legal-line-label { position:absolute; z-index:3; padding:5px 10px; border-radius:16px; background:var(--bg); border:1px solid var(--border); color:var(--accent); font-size:14px; font-weight:600 }
.legal-legend { position:absolute; left:20px; bottom:16px; z-index:3; display:flex; gap:18px; color:var(--text-muted); font-size:13px }
.legal-legend i { display:inline-block; width:28px; height:3px; margin-right:6px; vertical-align:middle; background:var(--accent) }

/* EC 证据链 */
.evidence-chain { display:grid; grid-template-columns:1fr 100px 1fr 100px 1fr; align-items:center; gap:10px }
.evidence-stack { display:flex; flex-direction:column; gap:12px }
.evidence-item { padding:16px 18px; background:#fff; border:1px solid var(--border); border-radius:10px }
.evidence-item strong { display:block; color:var(--accent); font-size:18px }   /* 证据名称 */
.evidence-item span { display:block; margin-top:4px; color:var(--text-muted); font-size:14px }  /* 证明事项 */
.chain-arrow { color:var(--accent-2); font-size:38px; text-align:center }
.fact-node { padding:24px; border-radius:14px; background:#eaf2fb; border:2px solid #9fc9ef; color:var(--accent); text-align:center }
.result-node { padding:28px; border-radius:14px; background:var(--accent); color:#fff; text-align:center }
.fact-node strong, .result-node strong { display:block; font-size:22px }
.fact-node span, .result-node span { display:block; margin-top:8px; font-size:14px; line-height:1.5 }

/* DF 法律判断流程 */
.decision-flow { position:relative; height:480px; background:#fff; border:1px solid var(--border); border-radius:14px; overflow:hidden }
.decision-flow svg { position:absolute; inset:0; width:100%; height:100%; z-index:1 }
.decision-node { position:absolute; z-index:2; width:200px; min-height:82px; padding:14px 16px; border-radius:10px; display:grid; place-items:center; text-align:center; background:#eaf2fb; border:2px solid #9fc9ef; color:var(--accent); font-size:17px; font-weight:600 }
.decision-node.start { background:var(--accent); border-color:var(--accent); color:#fff }
.decision-node.risk { background:#C84C4C; border-color:#C84C4C; color:#fff }
.decision-node.result { background:#4E8B72; border-color:#4E8B72; color:#fff }
.decision-tag { position:absolute; z-index:3; padding:4px 8px; border-radius:12px; background:var(--bg); font-size:13px; font-weight:700 }
```

---

## 使用方式

### 在 Markdown 文档中标注组件编号

```markdown
## 【第 3 页】核心能力
**组件：** C3
**内容：**
- 卡片1：智能检索 — 语义匹配法条与案例
- 卡片2：文书生成 — 要素驱动自动输出
- 卡片3：风险预警 — 合同条款自动审查
```

### 口头指定

> "第5页用 BA 对比框，左边是传统模式，右边是 AI 模式"

### 约束

- 同一页面只能使用**一种**内容组件（如 C3 和 ST 不能混用）
- 内容超出组件容量时必须**拆页**，不得压缩字号
- 组件编号缺失时，默认使用 C3（3 列卡片）

---

### 装饰增强

#### GH — Ghost 背景大字

```css
.ghost {
  position: absolute;
  font-family: var(--font-serif-en);
  font-size: 450px;
  font-weight: 900;
  color: var(--accent);
  opacity: 0.04;
  pointer-events: none;
  user-select: none;
  white-space: nowrap;
  line-height: 1;
  z-index: 0;
}
```

**使用方式**：在 `.slide` 内放置，用 inline style 控制位置。配合 Ghost 的页面，其他内容需加 `position: relative; z-index: 1` 确保不被遮挡。

```html
<div class="ghost" style="bottom: -40px; right: -20px;">03</div>
<div class="ghost" style="top: 50%; left: 50%; transform: translate(-50%,-50%);">ANALYSIS</div>
```

#### HI — Highlight 荧光笔

```css
.hi {
  background: linear-gradient(180deg, transparent 58%, color-mix(in srgb, var(--accent-2) 35%, transparent) 58%);
  padding: 0 3px;
  -webkit-box-decoration-break: clone;
  box-decoration-break: clone;
}
```

**使用方式**：包裹需要高亮的内联文字。颜色自动跟随主题色 `--accent-2`，无需手动指定。

```html
<p class="body-zh">本案涉及<span class="hi">多方主体</span>的请求权竞合问题。</p>
```

> 浏览器不支持 `color-mix()` 时，高亮背景自动消失，文字正常显示，优雅降级。
