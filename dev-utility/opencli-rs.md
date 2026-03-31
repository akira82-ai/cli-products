# OpenCLI-RS (`opencli-rs`)

## 基本信息
- 官方文档：https://github.com/nashsu/opencli-rs
- 安装方式：从 GitHub Releases 下载二进制文件
- 开源：是 (Apache 2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：最新

## 核心命令示例
```bash
# 公开模式 - 直接调用平台 API
opencli-rs hackernews top
opencli-rs twitter user elonmusk
opencli-rs reddit hot programming

# 浏览器模式 - 复用 Chrome 登录态
opencli-rs --mode browser twitter home
opencli-rs --mode browser zhihu hot

# 桌面模式 - 控制 Cursor/Notion/ChatGPT 等桌面应用
opencli-rs --mode desktop cursor open
opencli-rs --mode desktop notion search "CLI tools"
```

## 适用场景
- 终端快速浏览 55+ 平台内容（HackerNews、Twitter/X、Reddit、Bilibili、知乎、微博、豆瓣、YouTube 等）
- 复用浏览器登录态访问需要认证的 API
- 自动化操控桌面应用（Cursor、Notion、ChatGPT、Discord）
- Claude Code Skill 集成，作为 AI Agent 的工具扩展
