# Helm CLI (`helm`)

## 基本信息
- 官方文档：https://helm.sh/docs/
- 安装方式：brew install helm
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：3.16

## 核心命令示例
```bash
# 添加 Chart 仓库
helm repo add bitnami https://charts.bitnami.com/bitnami

# 安装 Release [需认证]
helm install my-release bitnami/nginx

# 升级 Release [需认证]
helm upgrade my-release bitnami/nginx

# 查看已安装的 Release
helm list
```

## 适用场景
- K8s 应用包管理
- Chart 模板化部署和升级
- 多环境配置管理
