# Telegram CLI (`telegram-cli`)

## 基本信息
- 官方文档：https://core.telegram.org/api
- 安装方式：`pip install telegram-cli`
- 开源：是 (GPL)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：—

## 核心命令示例
```bash
# 登录认证
telegram-cli login

# 发送消息到指定聊天
telegram-cli send --chat <id> --text "msg"

# 列出聊天列表
telegram-cli chat list
```

> `telegram-cli login` 需提供手机号和验证码。

## 适用场景
- Telegram 消息自动化发送
- 频道管理与内容发布
- 群组消息监控与处理
