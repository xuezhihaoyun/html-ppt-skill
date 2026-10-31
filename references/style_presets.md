# HTML PPT 风格预设库

> 本文件用于在用户提出颜色、气质、行业或场景偏好时快速选择视觉方向。它是“风格文本库”，不是完整 HTML 模板；生成页面时应把所选预设映射到当前模板的 `:root` 变量与版式组件中。

## 使用规则

- 先根据用户场景选择 1 套主风格，不要混用多套主色系统。
- 每套风格最多使用 1 个主色、1 个强调色、1 个背景色、1 个正文色，避免彩虹配色。
- 如果用户只说“高级”“正式”“科技”“温暖”，优先从下方预设中选择最贴近的一套。
- 若用户指定品牌色，以品牌色为主，参考本文件调整背景、字体、卡片、图表和装饰语言。
- 应用到 `page_skeleton.html` 时，可将 `--preset-primary` 映射为 `--accent`，将 `--preset-accent` 映射为 `--accent-2`。

---

## 01 墨绿金章风

**气质**：稳重、克制、权威、有章法。

**适合**：法律、金融、合规、年终总结、管理制度、传统行业汇报。

```css
:root {
  --preset-bg: #f7f2e8;
  --preset-surface: #fffaf0;
  --preset-primary: #173f35;
  --preset-primary-deep: #0b2a24;
  --preset-accent: #b88a2e;
  --preset-text: #1f2a24;
  --preset-muted: #6f786f;
  --preset-border: #d9c7a3;
}
```

**版式建议**：深绿色封面、金色细线、印章式圆形编号、米色纸底内容页、少量 serif 标题。

**禁忌**：不要大面积金色渐变，不要满屏复杂纹理。

---

## 02 象牙纸质风

**气质**：温和、文化感、书卷气、适合讲解。

**适合**：培训课、读书分享、文化主题、课程课件、内部方法论。

```css
:root {
  --preset-bg: #f6efe3;
  --preset-surface: #fffaf2;
  --preset-primary: #2b2723;
  --preset-primary-deep: #171411;
  --preset-accent: #b23a2e;
  --preset-text: #2f2a25;
  --preset-muted: #7e756a;
  --preset-border: #e0d2bd;
}
```

**版式建议**：大留白、细分割线、仿纸张纹理、朱砂红小标签、脚注式说明。

**禁忌**：不要强荧光色，不要科技网格，不要过度阴影。

---

## 03 冷灰科技风

**气质**：理性、未来感、冷静、系统化。

**适合**：AI、产品架构、技术方案、数字化转型、研发汇报。

```css
:root {
  --preset-bg: #10151d;
  --preset-surface: #18212c;
  --preset-primary: #d7dee8;
  --preset-primary-deep: #0b1118;
  --preset-accent: #27d7ff;
  --preset-accent-2: #3977ff;
  --preset-text: #edf3fb;
  --preset-muted: #8a97a8;
  --preset-border: #2b3a4a;
}
```

**版式建议**：深色背景、细网格、霓虹蓝线框、代码块、流程节点、半透明数据卡片。

**禁忌**：不要用紫色大渐变，不要过多发光效果导致廉价感。

---

## 04 深蓝咨询风

**气质**：专业、结构化、可信赖、商业分析感。

**适合**：战略咨询、商业计划、投融资、经营分析、董事会汇报。

```css
:root {
  --preset-bg: #f4f7fb;
  --preset-surface: #ffffff;
  --preset-primary: #102a4c;
  --preset-primary-deep: #071a32;
  --preset-accent: #2fb7c8;
  --preset-text: #1f2d3d;
  --preset-muted: #66758a;
  --preset-border: #d8e1ec;
}
```

**版式建议**：白底内容页、深蓝标题栏、青蓝强调数字、矩阵表、2x2 框架、简洁图表。

**禁忌**：不要花哨插画，不要过度圆角卡片。

---

## 05 暖橙增长风

**气质**：积极、亲和、增长、品牌活力。

**适合**：营销方案、增长复盘、用户运营、品牌提案、活动策划。

```css
:root {
  --preset-bg: #fff4e6;
  --preset-surface: #fffaf3;
  --preset-primary: #3a2618;
  --preset-primary-deep: #20130b;
  --preset-accent: #f07a2b;
  --preset-accent-2: #ffc15a;
  --preset-text: #34261d;
  --preset-muted: #8a6d58;
  --preset-border: #efd6b8;
}
```

**版式建议**：奶油底、暖橙按钮/标签、曲线箭头、增长漏斗、案例卡片、柔和阴影。

**禁忌**：不要饱和橙铺满整页，不要过多卡通元素。

---

## 06 黑金发布会风

**气质**：高端、聚焦、仪式感、发布会感。

**适合**：新品发布、闭门分享、高端品牌、颁奖、重要成果发布。

```css
:root {
  --preset-bg: #050505;
  --preset-surface: #111111;
  --preset-primary: #f5f0e6;
  --preset-primary-deep: #000000;
  --preset-accent: #caa45d;
  --preset-accent-2: #f0d28a;
  --preset-text: #f7f3ea;
  --preset-muted: #a69d8f;
  --preset-border: #3a3328;
}
```

**版式建议**：黑底大字、金色细线、聚光灯渐变、全屏图、极少文字、强对比数字。

**禁忌**：不要在正文页大量使用金色文字，不要堆满装饰。

---

## 07 青绿医疗风

**气质**：清洁、可信、温和、公益感。

**适合**：医疗健康、公益项目、心理健康、公共服务、科普宣传。

```css
:root {
  --preset-bg: #eefaf7;
  --preset-surface: #ffffff;
  --preset-primary: #0f5b68;
  --preset-primary-deep: #063c47;
  --preset-accent: #43c6a8;
  --preset-accent-2: #9be7d3;
  --preset-text: #15333a;
  --preset-muted: #668286;
  --preset-border: #cce8e2;
}
```

**版式建议**：浅青绿背景、白色圆角卡片、柔和图标、步骤说明、轻量图表。

**禁忌**：不要高压黑底，不要强烈红色大面积使用。

---

## 08 红蓝政务风

**气质**：庄重、规范、清晰、正式。

**适合**：政策解读、机关汇报、党建主题、工作总结、公共事务。

```css
:root {
  --preset-bg: #ffffff;
  --preset-surface: #f6f8fb;
  --preset-primary: #1f4e8c;
  --preset-primary-deep: #12315a;
  --preset-accent: #c62828;
  --preset-accent-2: #e7b84a;
  --preset-text: #1f2933;
  --preset-muted: #6b7280;
  --preset-border: #dbe3ef;
}
```

**版式建议**：白底、红蓝标题带、庄重几何页眉、编号模块、政策要点表格。

**禁忌**：不要娱乐化插画，不要使用过度炫光或霓虹效果。

---

## 09 数据仪表盘风

**气质**：密度高、运营感、实时监控、理性。

**适合**：经营分析、数据复盘、运营监控、增长指标、管理驾驶舱。

```css
:root {
  --preset-bg: #08111f;
  --preset-surface: #101d2e;
  --preset-primary: #e9f2ff;
  --preset-primary-deep: #050b14;
  --preset-accent: #2de2a6;
  --preset-accent-2: #4aa3ff;
  --preset-text: #eef6ff;
  --preset-muted: #8ea4bd;
  --preset-border: #24354b;
}
```

**版式建议**：深色仪表盘、KPI 大数字、折线/柱状图卡片、状态灯、细边框网格。

**禁忌**：不要把所有图表都做成同一种卡片，不要让数字缺少单位和上下文。

---

## 10 清新科普教学风

**气质**：轻松、友好、清晰、入门友好、信息图感。

**适合**：AI 入门课、产品功能说明、工具教程、给非技术人员解释技术概念、儿童/青少年科普、培训课件。

```css
:root {
  --preset-bg: #f8fbff;
  --preset-surface: #ffffff;
  --preset-primary: #1f6fe5;
  --preset-primary-deep: #1f2a44;
  --preset-accent: #54d6c8;
  --preset-accent-2: #ffd166;
  --preset-accent-3: #c9b6ff;
  --preset-text: #1f2a44;
  --preset-muted: #64748b;
  --preset-border: #dbeafe;
}
```

**版式建议**：白底或极浅蓝底、圆角卡片、柔和描边、分步骤流程、彩色 token/标签块、小机器人或图标插画、提示条和类比模块。

**禁忌**：不要使用大面积深色背景，不要堆复杂图表，不要让卡片颜色过饱和；文字要短，优先解释“是什么、怎么工作、生活类比”。

---

## 11 橙白消费科技风

**气质**：干净、年轻、产品感、发布会感、亲和的科技高级感。

**适合**：消费电子、手机、智能硬件、IoT、新能源车、产品发布会、产品卖点介绍、用户体验型产品说明。

```css
:root {
  --preset-bg: #f7f8fa;
  --preset-surface: #ffffff;
  --preset-primary: #1f2933;
  --preset-primary-deep: #0b0f14;
  --preset-accent: #ff6900;
  --preset-accent-2: #ffb36b;
  --preset-text: #202124;
  --preset-muted: #6b7280;
  --preset-border: #e5e7eb;
}
```

**版式建议**：白底大留白、产品渲染图做主视觉、超大卖点标题、橙色标签或细线强调、大数字参数卡、少量圆角信息块、价格/规格/对比页结构清晰。

**禁忌**：不要把页面做成冷黑科技风，不要用复杂背景抢产品图，不要一页堆太多参数；每页只讲一个核心卖点。

---

## 12 墨水经典风

**气质**：文学、温润、内敛、思考。如翻看一本旧书。

**适合**：思想分享、个人演讲、法律人文、深度思考、创意型 PPT。

**核心思路**：全页暗底墨色 + 暖调纸白文字，衬线字（Noto Serif SC）做大标题，无衬线（Noto Sans SC）做正文，等宽字体（IBM Plex Mono）做标签/页码。开卷翻页感，不做卡片，不做表格斑马纹。

```css
:root {
  --accent: #0a0a0b;
  --accent-2: #c9a227;
  --accent-3: #8b7355;
  --bg: #0a0a0b;
  --surface: #18181a;
  --text: #f1efea;
  --text-muted: rgba(241,239,234,0.55);
  --border: rgba(241,239,234,0.15);
}
```

**版式建议**：
- 全页暗底（`#0a0a0b`），不要亮页切换。文字使用暖调纸白（`#f1efea`）而非纯白。
- 标题用衬线大字（`Noto Serif SC`），正文用无衬线（`Noto Sans SC`），标签用等宽（`IBM Plex Mono`）。
- 重要数字使用英文衬线（`Playfair Display`），大号加粗，有古典质感。
- 布局以左右分栏（`.split`）和网格（`.grid-3` `.grid-4`）为主，不用卡片类组件。
- 过渡使用平滑翻页动画（`transform translateX` + `cubic-bezier(.77,0,.175,1)`），每页内容依次淡入（stagger fadeUp）。
- 引用框使用左边框（`border-left`）+ 半透明背景，不使用填充色块。
- 可配 WebGL 动态背景（流动墨水/粒子），但需 `data-low-power` 降级选项。

**禁忌**：不要用亮色背景、不要用大量 emoji、不要让科技蓝喧宾夺主、不要让装饰强于内容。

---

## 选择建议

| 用户需求 | 优先风格 |
|----------|----------|
| 正式、稳重、法律、金融 | 墨绿金章风 / 深蓝咨询风 |
| 文化、课程、阅读、培训 | 象牙纸质风 |
| 科技、AI、架构、产品 | 冷灰科技风 |
| 商业分析、战略、投融资 | 深蓝咨询风 |
| 营销、品牌、增长 | 暖橙增长风 |
| 高端、发布、仪式感 | 黑金发布会风 |
| 医疗、公益、健康 | 青绿医疗风 |
| 政务、政策、党建 | 红蓝政务风 |
| 数据、运营、指标 | 数据仪表盘风 |
| 小白教学、AI 入门、工具教程、科普 | 清新科普教学风 |
| 消费电子、智能硬件、产品发布 | 橙白消费科技风 |
| 思想分享、深度思考、演讲、人文 | 墨水经典风 |
