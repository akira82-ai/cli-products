# kind (`kind`)

## 基本信息
- 官方文档：https://kind.sigs.k8s.io/
- 安装方式：brew install kind
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux
- 最后验证版本：0.24

## 核心命令示例
```bash
# 创建集群
kind create cluster --name my-cluster

# 删除集群
kind delete cluster --name my-cluster

# 加载本地镜像到集群
kind load docker-image myapp:latest --name my-cluster

# 查看集群列表
kind get clusters
```

## 适用场景
- 本地 Kubernetes 集群（CI/CD 测试）
- K8s 应用本地开发调试
- 多节点集群模拟
