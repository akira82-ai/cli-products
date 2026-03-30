# CircleCI CLI (`circleci`)

## 基本信息
- 官方文档：https://circleci.com/docs/local-cli/
- 安装方式：`brew install circleci`
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：—

## 核心命令示例
```bash
# 验证配置文件
circleci config validate

# 本地执行任务
circleci local execute --job <jobname>

# 创建 Orb
circleci orb create

# 列出流水线
circleci pipeline list
```

> 本地执行需要 Docker 环境。

## 适用场景
- CI 配置文件验证与调试
- 本地执行流水线任务
- Orb 开发与管理
