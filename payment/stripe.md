# Stripe CLI (`stripe`)

## 基本信息
- 官方文档：https://docs.stripe.com/stripe-cli
- 安装方式：`brew tap stripe/stripe-cli && brew install stripe`
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：v1.22.3

## 核心命令示例
```bash
# 登录 Stripe 账户
stripe login

# 监听 Stripe Webhook 事件并转发到本地服务器 [需认证]
stripe listen --forward-to localhost:3000/webhooks

# 触发测试事件（模拟支付）
stripe trigger payment_intent.succeeded [需认证]

# 查看近期 API 请求日志 [需认证]
stripe logs tail

# 创建支付意图 [需认证]
stripe payments create --amount 2000 --currency usd
```

## 适用场景
- 本地开发调试 Stripe Webhook，无需暴露公网端口
- 模拟各种支付事件进行集成测试
- 管理 Stripe 资源（客户、订阅、发票等）的快速操作
