# Jaeger CLI (`jaeger`)

## 基本信息
- 官方文档：https://www.jaegertracing.io/docs/latest/cli
- 安装方式：从 https://github.com/jaegertracing/jaeger/releases 下载，或 `docker run jaegertracing/all-in-one`
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：1.66.0

## 核心命令示例
```bash
# 以 all-in-one 模式启动 Jaeger
jaeger-all-in-one --collector.zipkin.host-port=9411

# 查询追踪数据 [需认证]
jaeger-query --span-storage.type=elasticsearch --es.server-urls=http://localhost:9200

# 导出追踪数据
jaeger-anonymization --filename traces.json --output anonymized.json
```

## 适用场景
- 本地开发和测试分布式追踪系统
- 快速部署 Jaeger 全套组件（Agent、Collector、Query）
- 追踪数据的匿名化处理和离线分析
