# HTML PPT Skill

用 Markdown 和零依赖 HTML 制作专业级网页幻灯片，适用于正式汇报、培训课程、法律实务分享与案件可视化。

## 核心能力

- Markdown 先行，内容结构与页面设计保持同步。
- 固定 `1600 × 900` 舞台，按窗口整体等比缩放。
- 支持键盘翻页、触摸滑动、`F` 全屏和进度显示。
- 逐页 HTML 使用 iframe 隔离，避免样式互相污染。
- 本地图片自动内嵌为 Base64，最终生成可离线分享的单文件。
- 提供 12 套视觉预设和 19 个标准内容组件。
- 支持法律关系图、证据链和法律判断流程。
- 提供交互式编排器，可拖拽换页、删除页面和轻量编辑。
- 支持对既有合并版 HTML 做局部删除、换页和文字修改。

## 目录结构

```text
html-ppt-skill/
├── SKILL.md
├── README.md
├── references/
│   ├── component_catalog.md
│   ├── design_guide.md
│   ├── legal_visualization.md
│   └── style_presets.md
└── templates/
    ├── component_gallery.html
    ├── create_deck_editor.py
    ├── deck_editor.html
    ├── merge_slides.py
    ├── navigation.js
    ├── page_skeleton.html
    └── quick_ref.md
```

## 快速开始

1. 根据 `SKILL.md` 整理一份逐页 Markdown 大纲。
2. 从 `references/component_catalog.md` 选择页面组件。
3. 复制 `templates/page_skeleton.html` 生成 `output/slide_01.html` 等页面。
4. 将 `templates/navigation.js` 与页面放在同一目录。
5. 运行 `python3 templates/merge_slides.py` 生成单文件。
6. 运行 `python3 templates/create_deck_editor.py output/all_slides.html` 生成编排版。

## 播放控制

| 按键 | 功能 |
|---|---|
| `→` / `Space` | 下一页 |
| `←` | 上一页 |
| `Home` / `End` | 首页 / 末页 |
| `F` | 进入或退出全屏 |
| 左右滑动 | 触摸设备翻页 |

## 稳定性交付

- 最终交付物默认是 `output/all_slides.html`。
- 核心展示不得依赖外部 CSS、外部 JavaScript、CDN 字体或外部图片。
- HTML 中不得保留 `/Users/...`、`C:\\...` 等本机绝对路径。
- 内容过多时应拆页，不得依靠缩小字号强行塞入。
- 修改既有合并版时遵循局部修改协议，不重建未被点名的页面。

详细流程、设计规范和验收规则见 [SKILL.md](SKILL.md)。

## License

MIT © [xuezhihaoyun](https://github.com/xuezhihaoyun)
