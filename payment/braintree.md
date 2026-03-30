# Braintree CLI (`braintree`)

## 基本信息
- 官方文档：https://developer.paypal.com/braintree/docs
- 安装方式：`npm install -g braintree-cli`（社区方案）
- 开源：否（SDK 开源，CLI 为社区维护）
- 平台支持：macOS / Linux / Windows
- 最后验证版本：N/A（主要通过 SDK 操作）

## 核心命令示例
```bash
# 使用 Braintree API 创建客户 [需认证]
curl -v -X POST https://api.sandbox.braintreegateway.com/merchants/MERCHANT_ID/customers \
  -H "Content-Type: application/json" \
  -d '{"first_name": "John", "last_name": "Doe"}'

# 生成客户端令牌 [需认证]
curl -v -X POST https://api.sandbox.braintreegateway.com/merchants/MERCHANT_ID/client_token

# 查找交易记录 [需认证]
curl -v https://api.sandbox.braintreegateway.com/merchants/MERCHANT_ID/transactions/TRANSACTION_ID
```

## 适用场景
- 集成 PayPal 旗下 Braintree 支付网关
- 在 Sandbox 环境中测试信用卡和 PayPal 交易
- 管理客户支付方式和订阅计费
