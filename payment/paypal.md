# PayPal CLI (`paypal`)

## 基本信息
- 官方文档：https://developer.paypal.com/docs/api/overview/
- 安装方式：无官方 CLI（`@paypal/cli` 不存在于 npm），通过 REST API 操作
- 开源：否
- 平台支持：macOS / Linux / Windows
- 最后验证版本：N/A（PayPal 主要通过 API/SDK 操作）

## 核心命令示例
```bash
# 使用 PayPal REST API 创建订单 [需认证]
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ACCESS_TOKEN" \
  -d '{"intent":"CAPTURE","purchase_units":[{"amount":{"currency_code":"USD","value":"10.00"}}]}'

# 获取 OAuth 访问令牌 [需认证]
curl -v https://api-m.sandbox.paypal.com/v1/oauth2/token \
  -u "CLIENT_ID:SECRET" -d "grant_type=client_credentials"

# 查询订单详情 [需认证]
curl -v https://api-m.paypal.com/v2/checkout/orders/ORDER_ID \
  -H "Authorization: Bearer ACCESS_TOKEN"
```

## 适用场景
- 电商平台集成 PayPal 支付流程
- 使用 Sandbox 环境进行支付集成测试
- 自动化批量退款和订单管理
