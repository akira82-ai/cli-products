# Trello CLI (`trello`)

## 基本信息
- 官方文档：https://developer.atlassian.com/cloud/trello/rest/
- 安装方式：`npm install -g trello-cli`
- 开源：是 (ISC)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：—

## 核心命令示例
```bash
# 列出看板
trello boards

# 在指定列表添加卡片
trello add-card "title" --list "To Do"

# 列出看板中的卡片
trello list-cards --board "name"
```

> 需要配置 Trello API Key 和 Token。

## 适用场景
- Trello 看板管理
- 卡片批量创建与操作
- 自动化看板流程
