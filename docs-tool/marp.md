# Marp CLI (`marp`)

## 基本信息
- 官方文档：https://github.com/marp-team/marp
- 安装方式：npm install -g @marp-team/marp-cli
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：4.0

## 核心命令示例
```bash
# 导出为 HTML 演示文稿
marp slides.md

# 导出为 PDF
marp slides.md -o slides.pdf

# 导出为 PPTX（允许本地文件引用）
marp slides.md -o slides.pptx --allow-local-files

# 监听模式，实时预览
marp -s slides.md
```

## 适用场景
- Markdown 直接导出 HTML/PDF/PPT 演示文稿
- 技术分享快速制作 slides
- 文档转演示文稿
