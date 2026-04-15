# HTML PPT 速查卡

## 启动工作流
1. 拿到/共建 Markdown 文档
2. 确认页数、配色、图片清单
3. 逐页生成 `slide_01.html` ~ `slide_NN.html`
4. 修改 `navigation.js` 中的 `const total = NN`
5. 运行 `python3 merge_slides.py`
6. 交付 `all_slides.html`

## 常用按键
| 按键 | 作用 |
|------|------|
| `→` / `Space` | 下一张 |
| `←` | 上一张 |
| `F` | 全屏切换 |
| `Home` | 跳到首页 |
| `End` | 跳到末页 |

## 页面类型速查
- **封面/结束页**：`#0d1b2a` 背景，白色大字，香槟金点缀
- **过渡页**：左右半屏分割（左深蓝 + 右白）
- **内容页**：白色/浅灰背景，卡片/表格/流程图
- **代码页**：深色代码框 + 浅色说明

## 动画类名
```html
<div class="top-bar anim-1">...</div>
<h2 class="anim-1">...</h2>
<div class="grid anim-2">...</div>
<p class="anim-3">...</p>
```

## 核心禁忌
- ❌ 不要把 28 页 CSS 直接拼在一起（会串色）
- ❌ 不要把图片单独发给别人（会丢图）
- ✅ 合并必须用 `iframe + srcdoc`
- ✅ 图片必须 Base64 内嵌
- ✅ 迭代先改 MD，再同步 HTML
