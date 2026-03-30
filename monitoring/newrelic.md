# New Relic CLI (`newrelic`)

## 基本信息
- 官方文档：https://docs.newrelic.com/docs/tools/new-relic-cli
- 安装方式：`brew install newrelic-cli`
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：0.96.4

## 核心命令示例
```bash
# 查询 NRQL 数据 [需认证]
newrelic nrql query --account-id 1234567 --query "SELECT count(*) FROM Transaction SINCE 1 hour ago"

# 列出部署标记 [需认证]
newrelic deployments list --application-id 12345

# 创建告警策略 [需认证]
newrelic alerts policy create --name "My Policy" --incident-preference PER_POLICY
```

## 适用场景
- 通过 NRQL 查询和导出 New Relic 监控数据
- 自动化管理告警策略、通知渠道和 Dashboard
- CI/CD 中记录部署标记，关联性能变化
