# Glow (`glow`)

## 基本信息
- 官方文档：https://github.com/charmbracelet/glow
- 安装方式：brew install glow
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：2.0

## 核心命令示例
```bash
# 渲染 Markdown 文件
glow README.md

# 使用内置 pager 查看文件
glow -p file.md

# 指定暗色主题渲染
glow -w file.md

# 渲染远程 Markdown
glow https://raw.githubusercontent.com/user/repo/main/README.md
```

## 适用场景
- 终端渲染 Markdown 预览
- 替代 cat 查看 .md 文件
- Agent 写完文章直接终端预览排版
