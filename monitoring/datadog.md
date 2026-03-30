# Datadog CLI (`datadog-ci`)

## 基本信息
- 官方文档：https://docs.datadoghq.com/continuous_integration/cli
- 安装方式：`npm install -g @datadog/datadog-ci`
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：3.10.0

## 核心命令示例
```bash
# 上传 Sourcemap 到 Datadog [需认证]
datadog-ci sourcemaps upload --service my-app --release-version 1.0.0 --source-map-dir ./dist --minified-path ./dist/bundle.js

# 管理 Synthetics 测试 [需认证]
datadog-ci synthetics run-tests --config ./synthetics-config.json

# 上传 JUnit 测试报告 [需认证]
datadog-ci junit upload --service my-service --env ci ./test-results.xml
```

## 适用场景
- CI/CD 流水线中集成 Datadog Synthetics 测试、Sourcemaps 上传、测试报告收集
- 自动化部署前运行性能和可用性测试
- 批量管理 Datadog 监控资源（Dashboard、Monitor 等）
