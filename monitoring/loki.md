# Loki CLI (`logcli`)

## 基本信息
- 官方文档：https://grafana.com/docs/loki/latest/query/logcli
- 安装方式：从 https://github.com/grafana/loki/releases 下载
- 开源：是 (AGPL-3.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：3.4.3

## 核心命令示例
```bash
# 查询日志（LogQL） [需认证]
logcli query '{app="my-service"} |= "error"' --limit=100 --since=1h

# 查询日志标签值 [需认证]
logcli labels job --query='{namespace="production"}' --since=24h

# 统计日志条目数量 [需认证]
logcli query '{app="nginx"} | logfmt | status>=500' --limit=0 --stats
```

## 适用场景
- 在终端中快速查询和过滤 Loki 日志，无需打开 Grafana
- 脚本化日志分析和告警数据导出
- 调试 LogQL 查询语句，验证查询性能
