# AWS SES (`aws ses`)

## 基本信息
- 官方文档：https://docs.aws.amazon.com/cli/latest/reference/ses/
- 安装方式：`pip install awscli` 或 `brew install awscli`
- 开源：否（AWS CLI 为开源，Apache-2.0）
- 平台支持：macOS / Linux / Windows
- 最后验证版本：AWS CLI v2.22.30

## 核心命令示例
```bash
# 发送纯文本邮件 [需认证]
aws ses send-email \
  --from "sender@example.com" \
  --destination "ToAddresses=recipient@example.com" \
  --message "Subject={Data=Test Subject},Body={Text={Data=Hello World}}"

# 发送 HTML 格式邮件 [需认证]
aws ses send-email \
  --from "sender@example.com" \
  --destination "ToAddresses=recipient@example.com" \
  --message "Subject={Data=Newsletter},Body={Html={Data=<h1>Hello</h1>}}"

# 查看发送配额 [需认证]
aws ses get-send-quota

# 验证发件人邮箱地址 [需认证]
aws ses verify-email-identity --email-address sender@example.com
```

## 适用场景
- 通过命令行批量发送事务性邮件
- 管理 SES 发件人验证和发送配额
- 集成到 CI/CD 流水线中的邮件通知
