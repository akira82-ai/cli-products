# ArgoCD CLI (`argocd`)

## 基本信息
- 官方文档：https://argo-cd.readthedocs.io/en/latest/user-guide/commands/argocd/
- 安装方式：`brew install argocd`
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：—

## 核心命令示例
```bash
# 登录 ArgoCD 服务器
argocd login <server>

# 创建应用
argocd app create

# 同步应用
argocd app sync <appname>

# 列出应用
argocd app list
```

> `argocd login` 需提供 ArgoCD 服务器地址和凭据。

## 适用场景
- GitOps 持续交付管理
- Kubernetes 应用同步与部署
- 应用状态监控与差异排查
