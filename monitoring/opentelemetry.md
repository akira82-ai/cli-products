# OpenTelemetry CLI (`otel`)

## 基本信息
- 官方文档：https://github.com/open-telemetry/opentelemetry-cli
- 安装方式：从 GitHub Releases 下载，或 `go install github.com/open-telemetry/opentelemetry-cli@latest`
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：0.7.0

## 核心命令示例
```bash
# 发送测试 Span 到 OTel Collector [需认证]
otel span --name "test-span" --kind client --endpoint http://localhost:4317

# 发送测试指标 (Metric) [需认证]
otel metric --name "request.count" --value 42 --endpoint http://localhost:4317

# 查询 OTel Collector 状态
otel collector --endpoint http://localhost:4317 status
```

## 适用场景
- 开发和调试时向 OpenTelemetry Collector 发送测试遥测数据
- 验证 OTel Pipeline 配置是否正确接收和处理数据
- 脚本化生成指标和追踪数据用于集成测试
