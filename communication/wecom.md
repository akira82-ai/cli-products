# 企业微信 (`wecom`)

## 基本信息
- 官方文档：https://developer.work.weixin.qq.com/
- 官网：https://work.weixin.qq.com/
- 安装方式：企业微信开发者中心
- 开源：否
- 平台支持：macOS / Linux / Windows
- 最后验证版本：—

## 核心命令示例
```bash
# 企业微信 API 调用示例（需配合 SDK）
# 发送应用消息
curl -X POST "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=ACCESS_TOKEN"

# 获取 access_token
curl "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET"

# 读取成员信息
curl "https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=TOKEN&userid=USERID"
```

> 企业微信主要通过 REST API 进行集成，支持多种编程语言 SDK。

## 适用场景
- 企业内部应用开发
- 消息推送与通知
- 组织架构管理
- 审批流程自动化
