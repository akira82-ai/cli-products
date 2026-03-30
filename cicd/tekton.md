# Tekton CLI (`tkn`)

## 基本信息
- 官方文档：https://tekton.dev/docs/cli/
- 安装方式：`brew install tektoncd-cli`
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：—

## 核心命令示例
```bash
# 列出 Task
tkn task list

# 启动 Pipeline
tkn pipeline start

# 列出 Pipeline 运行记录
tkn pipeline run list

# 查看 TaskRun 日志
tkn taskrun logs
```

> 需要 kubeconfig 配置以连接 Kubernetes 集群。

## 适用场景
- Tekton CI/CD 流水线管理
- Task 和 Pipeline 运行与调试
- 构建日志查看与排查
