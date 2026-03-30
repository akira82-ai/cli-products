# Flux CLI (`flux`)

## 基本信息
- 官方文档：https://fluxcd.io/flux/cmd/
- 安装方式：`brew install flux`
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：—

## 核心命令示例
```bash
# 引导 GitHub 仓库
flux bootstrap github

# 创建 Git 源
flux create source git <name>

# 协调 Kustomization
flux reconcile kustomization

# 查看 Kustomization 列表
flux get kustomizations
```

> 需要 kubeconfig 配置以连接 Kubernetes 集群。

## 适用场景
- GitOps 自动化部署
- Kubernetes 集群引导与配置
- 持续交付流水线管理
