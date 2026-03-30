# Databricks CLI (`databricks`)

## 基本信息
- 官方文档：https://docs.databricks.com/dev-tools/cli/
- 安装方式：pip install databricks-cli
- 开源：是 (Databricks License)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：0.232

## 核心命令示例
```bash
# 配置认证 [需认证]
databricks configure

# 列出集群 [需认证]
databricks clusters list

# 列出作业 [需认证]
databricks jobs list

# 运行 Notebook [需认证]
databricks workspace import
```

## 适用场景
- Databricks 工作区和集群管理
- 作业调度和监控
- 数据管道自动化
