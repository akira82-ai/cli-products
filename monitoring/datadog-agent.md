# Datadog Agent CLI (`datadog-agent`)

## 基本信息
- 官方文档：https://docs.datadoghq.com/agent/configuration/agent-commands
- 安装方式：通过 Datadog Agent 安装包（https://app.datadoghq.com/account/settings/agent）
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：7.64.0

## 核心命令示例
```bash
# 检查 Agent 运行状态 [需认证]
datadog-agent status

# 检查特定集成的配置 [需认证]
datadog-agent check nginx

# flare 发送诊断信息给 Datadog 支持 [需认证]
datadog-agent flare
```

## 适用场景
- 排查 Datadog Agent 数据采集和发送问题
- 验证特定集成 (Integration) 的配置是否正确
- 收集 Agent 诊断日志提交给 Datadog 技术支持
