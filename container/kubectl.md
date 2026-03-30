# Kubernetes CLI (`kubectl`)

## 基本信息
- 官方文档：https://kubernetes.io/docs/reference/kubectl/
- 安装方式：brew install kubectl
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：1.31

## 核心命令示例
```bash
# 查看 Pod 列表
kubectl get pods -A

# 应用配置 [需认证]
kubectl apply -f deployment.yaml

# 查看 Pod 日志
kubectl logs -f pod-name

# 进入容器执行命令 [需认证]
kubectl exec -it pod-name -- sh

# 查看 Pod 详情
kubectl describe pod pod-name
```

## 适用场景
- K8s 集群管理和应用部署
- 容器调试和排障
- 集群资源查看和操作
