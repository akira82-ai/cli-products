# PagerDuty CLI (`pd`)

## 基本信息
- 官方文档：https://github.com/PagerDuty/pd-cli
- 安装方式：从 GitHub Releases 下载
- 开源：是 (MIT)
- 平台支持：macOS / Linux
- 最后验证版本：0.1.7

## 核心命令示例
```bash
# 列出当前值班安排 [需认证]
pd oncall list

# 触发一个 Incident [需认证]
pd incident trigger --service-id PXXXXXX --title "Production outage"

# 确认 (Acknowledge) 一个 Incident [需认证]
pd incident acknowledge --id PXXXXXX
```

## 适用场景
- 终端中快速查看值班表和处理 PagerDuty 告警
- 自动化脚本中触发、确认和解决 Incident
- 与 ChatOps 工具集成，通过命令行管理 On-Call 流程
