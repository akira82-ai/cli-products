# SendGrid CLI (`sendgrid`)

## 基本信息
- 官方文档：https://docs.sendgrid.com/for-developers/sending-email
- 安装方式：无官方 CLI（`sendgrid-cli` 不存在于 npm），通过 REST API 操作
- 开源：否（官方主要通过 API/SDK）
- 平台支持：macOS / Linux / Windows
- 最后验证版本：N/A（主要通过 API 操作）

## 核心命令示例
```bash
# 使用 API 发送邮件 [需认证]
curl -X POST https://api.sendgrid.com/v3/mail/send \
  -H "Authorization: Bearer SG.API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"personalizations":[{"to":[{"email":"to@example.com"}]}],"from":{"email":"from@example.com"},"subject":"Hello","content":[{"type":"text/plain","value":"Test email"}]}'

# 获取发送统计信息 [需认证]
curl https://api.sendgrid.com/v3/stats?start_date=2024-01-01 \
  -H "Authorization: Bearer SG.API_KEY"

# 验证邮箱地址 [需认证]
curl -X POST https://api.sendgrid.com/v3/validations/email \
  -H "Authorization: Bearer SG.API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com"}'
```

## 适用场景
- 批量发送事务性邮件和营销邮件
- 监控邮件发送状态和送达率统计
- 邮箱地址验证和邮件模板管理
