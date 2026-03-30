# Prometheus CLI (`promtool`)

## 基本信息
- 官方文档：https://prometheus.io/docs/prometheus/latest/configuration/configuration
- 安装方式：从 https://github.com/prometheus/prometheus/releases 下载
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：3.3.1

## 核心命令示例
```bash
# 验证 Prometheus 配置文件语法
promtool check config prometheus.yml

# 验证告警规则文件
promtool check rules alert_rules.yml

# 查询 Prometheus 数据（即时查询）
promtool query instant http://localhost:9090 'up'
```

## 适用场景
- CI/CD 中自动校验 Prometheus 配置和规则文件的正确性
- 调试和测试 PromQL 查询语句
- 运行单元测试验证告警规则的触发条件
