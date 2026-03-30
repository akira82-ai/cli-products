# Better Stack CLI (`betterstack`)

## 基本信息
- 官方文档：https://betterstack.com/docs/cli
- 安装方式：`brew install betterstack/tap/betterstack`
- 开源：否
- 平台支持：macOS / Linux
- 最后验证版本：1.5.14

## 核心命令示例
```bash
# 登录 Better Stack 账户 [需认证]
betterstack login

# 创建 Heartbeat 监控 [需认证]
betterstack heartbeats create --name "cron-job-monitor" --interval 300

# 查询日志 [需认证]
betterstack logs query "service=api status=500" --limit 50
```

## 适用场景
- 管理 Better Stack Uptime 监控和 Heartbeat
- 在终端中快速查询和分析日志
- CI/CD 中自动化创建和管理监控资源
