# Postmark CLI (`postmark`)

## 基本信息
- 官方文档：https://postmarkapp.com/developer
- 安装方式：`npm install -g postmark-cli`（社区方案）
- 开源：否（主要通过 API 操作）
- 平台支持：macOS / Linux / Windows
- 最后验证版本：N/A（主要通过 API 操作）

## 核心命令示例
```bash
# 使用 API 发送邮件 [需认证]
curl -X POST https://api.postmarkapp.com/email \
  -H "X-Postmark-Server-Token: SERVER_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"From":"sender@example.com","To":"recipient@example.com","Subject":"Hello","TextBody":"Test email"}'

# 发送模板邮件 [需认证]
curl -X POST https://api.postmarkapp.com/email/withTemplate \
  -H "X-Postmark-Server-Token: SERVER_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"From":"sender@example.com","To":"recipient@example.com","TemplateId":1234,"TemplateModel":{"name":"John"}}'

# 获取邮件发送统计 [需认证]
curl "https://api.postmarkapp.com/stats/outbound?fromdate=2024-01-01" \
  -H "X-Postmark-Server-Token: SERVER_TOKEN"
```

## 适用场景
- 高送达率的事务性邮件发送
- 使用预定义模板批量发送个性化邮件
- 监控邮件送达率和退信情况
