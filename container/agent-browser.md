# Agent Browser (`agent-browser`)

## 基本信息
- 官方文档：https://agent-browser.dev/
- GitHub：https://github.com/vercel-labs/agent-browser
- 安装方式：`npm install -g @agent-browser/cli`
- 开源：是
- 平台支持：macOS / Linux / Windows
- 最后验证版本：2026年4月

## 核心命令示例
```bash
# 启动浏览器并导航
agent-browser navigate https://example.com

# 截取页面内容（文本模式，低 token 消耗）
agent-browser capture

# 点击元素
agent-browser click "#submit-button"

# 填写表单
agent-browser fill "#email" "user@example.com"

# 等待元素加载
agent-browser wait ".loaded-content"

# 执行 JavaScript
agent-browser evaluate "document.title"

# 关闭浏览器
agent-browser close
```

> 100% 原生 Rust 编写，轻量级设计，token 消耗比 Playwright 低得多。

## 适用场景
- AI Agent 浏览器自动化
- 端到端自动化测试
- 复杂站点配置
- Electron 桌面应用操作（Discord、VSCode、Slack）
- 批量扫描消息提取信息
