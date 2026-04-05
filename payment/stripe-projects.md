# Stripe Projects CLI (`stripe projects`)

## 基本信息
- 官方文档：https://docs.stripe.com/stripe-cli
- GitHub：https://github.com/stripe/stripe-cli
- 安装方式：`npm install -g stripe-cli`
- 开源：是
- 平台支持：macOS / Linux / Windows
- 最后验证版本：2026年4月

## 核心命令示例
```bash
# 创建项目并自动配置
stripe projects create --name "MyApp"

# 获取 API 密钥
stripe projects keys

# 本地转发 Webhook
stripe listen --forward-to localhost:3000/webhook

# 触发测试事件
stripe trigger payment_intent.succeeded

# 创建客户
stripe customers create --email user@example.com

# 创建支付意图
stripe payment_intents create --amount 1000 --currency usd

# 查看日志
stripe logs tail
```

> 一行命令自动创建账号、获取 Key、接入计费，解决 Agent "最后一公里" 浏览器操作痛点。

## 适用场景
- Stripe 集成测试
- Webhook 本地开发
- Agent 自动化支付配置
- 项目快速部署
