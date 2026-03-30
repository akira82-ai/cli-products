# 企业微信 CLI (`wecom`)

## 基本信息
- 官方文档：https://developer.work.weixin.qq.com/document/
- 安装方式：`pip install wecom-cli`
- 开源：否
- 平台支持：macOS / Linux / Windows
- 最后验证版本：—

## 核心命令示例
```bash
# 发送消息到指定会话
wecom send --chatid <id> --msg "text"

# 登录认证
wecom auth login

# 查看帮助
wecom --help
```

> `wecom auth login` 需提供企业微信应用凭据。

## 适用场景
- 企业微信消息推送
- 自动化通知与告警
- 企业内部工具集成
