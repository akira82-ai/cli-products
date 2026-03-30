# Twilio CLI (`twilio`)

## 基本信息
- 官方文档：https://www.twilio.com/docs/twilio-cli
- 安装方式：`npm install -g twilio-cli` 或 `brew install twilio/tap/twilio`
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：v5.22.0

## 核心命令示例
```bash
# 登录 Twilio 账户
twilio login

# 发送短信 [需认证]
twilio api:core:messages:create --to +1234567890 --from +0987654321 --body "Hello World"

# 列出所有电话号码 [需认证]
twilio api:core:incoming-phone-numbers:list

# 启动本地 Webhook 开发服务器
twilio phone-numbers:webhook:update --number +1234567890 --url http://localhost:3000/webhook [需认证]
```

## 适用场景
- 发送短信、语音通知和邮件的自动化脚本
- 管理电话号码、Webhook 和 TwiML 应用
- 本地调试 Twilio Webhook 回调
