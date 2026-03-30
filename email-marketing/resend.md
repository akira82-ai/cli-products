# Resend CLI (`resend`)

## 基本信息
- 官方文档：https://resend.com/docs
- 安装方式：`npm install -g resend` 或 `npx resend`
- 开源：否
- 平台支持：macOS / Linux / Windows
- 最后验证版本：v4.0.0

## 核心命令示例
```bash
# 使用 API 发送邮件 [需认证]
curl -X POST https://api.resend.com/emails \
  -H "Authorization: Bearer re_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"from":"onboarding@resend.dev","to":["recipient@example.com"],"subject":"Hello","html":"<p>Test email</p>"}'

# 发送带附件的邮件 [需认证]
curl -X POST https://api.resend.com/emails \
  -H "Authorization: Bearer re_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"from":"sender@example.com","to":["recipient@example.com"],"subject":"Report","html":"<p>See attached</p>","attachments":[{"filename":"report.pdf","content":"BASE64_CONTENT"}]}'

# 获取邮件列表 [需认证]
curl https://api.resend.com/emails \
  -H "Authorization: Bearer re_API_KEY"
```

## 适用场景
- 面向开发者的现代事务性邮件服务
- 快速集成 React Email 模板发送邮件
- 域名验证和邮件送达追踪
