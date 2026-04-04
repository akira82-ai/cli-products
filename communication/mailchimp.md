# Mailchimp CLI (`mailchimp`)

## 基本信息
- 官方文档：https://mailchimp.com/developer/marketing/api/
- 安装方式：`npm install -g mailchimp-cli`（社区方案）
- 开源：否（官方主要通过 API/SDK）
- 平台支持：macOS / Linux / Windows
- 最后验证版本：N/A（主要通过 API 操作）

## 核心命令示例
```bash
# 使用 API 添加订阅者到列表 [需认证]
curl -X POST https://server.api.mailchimp.com/3.0/lists/LIST_ID/members \
  -H "Authorization: apikey YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"email_address":"test@example.com","status":"subscribed"}'

# 获取营销活动列表 [需认证]
curl https://server.api.mailchimp.com/3.0/campaigns \
  -H "Authorization: apikey YOUR_API_KEY"

# 创建并发送营销活动 [需认证]
curl -X POST https://server.api.mailchimp.com/3.0/campaigns \
  -H "Authorization: apikey YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"type":"regular","recipients":{"list_id":"LIST_ID"},"settings":{"subject_line":"Newsletter","title":"My Campaign"}}'
```

## 适用场景
- 管理邮件列表和订阅者数据
- 创建和发送营销活动邮件
- 自动化邮件营销工作流和受众细分
