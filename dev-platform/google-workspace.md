# Google Workspace CLI (`gws`)

## 基本信息
- 官方文档：https://github.com/googleworkspace/cli
- GitHub：https://github.com/googleworkspace/cli
- 安装方式：`npm install -g @googleworkspace/cli`
- 开源：是
- 平台支持：macOS / Linux / Windows
- 最后验证版本：2026年3月

## 核心命令示例
```bash
# Drive 操作
gws drive list
gws drive upload file.txt
gws drive download file-id

# Gmail 操作
gws mail list
gws mail send --to user@example.com --subject "Hello"
gws mail search "query"

# Calendar 操作
gws calendar list
gws calendar create --title "Meeting" --start "2026-04-05T10:00:00"

# Docs/Sheets 操作
gws docs create --title "My Document"
gws sheets read --spreadsheet-id xyz
```

> 包含 40+ 内置 Agent skills，专为 AI Agent 设计。

## 适用场景
- Google Workspace 自动化
- Agent 驱动的办公自动化
- 跨平台协作工具集成
- 文档和表格管理
