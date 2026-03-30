# Octopus Deploy CLI (`octo`)

## 基本信息
- 官方文档：https://octopus.com/docs/octopus-rest-api/octo
- 安装方式：`brew install octopusdeploy/taps/octo`
- 开源：否
- 平台支持：macOS / Linux / Windows
- 最后验证版本：—

## 核心命令示例
```bash
# 创建发布
octo create-release --project <project> --version <version>

# 部署发布
octo deploy-release --project <project> --version <version> --environment <env>

# 列出环境
octo list-environments

# 推送包
octo push --package <pkg>
```

> 需要配置 Octopus Server URL 和 API Key。

## 适用场景
- Octopus 部署发布管理
- 环境部署与晋升
- 包上传与发布编排
