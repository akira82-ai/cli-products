# Buildkite CLI (`buildkite-agent`)

## 基本信息
- 官方文档：https://buildkite.com/docs/agent/v3
- 安装方式：`brew install buildkite/buildkite/buildkite-agent`
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：—

## 核心命令示例
```bash
# 启动 Agent
buildkite-agent start

# 设置元数据
buildkite-agent meta-data set <key> <value>

# 上传构建产物
buildkite-agent artifact upload <path>
```

> `buildkite-agent start` 需要配置 Agent Token。

## 适用场景
- Buildkite CI/CD Agent 注册与管理
- 构建产物上传与下载
- 流水线元数据管理
