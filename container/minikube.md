# Minikube (`minikube`)

## 基本信息
- 官方文档：https://minikube.sigs.k8s.io/docs/
- 安装方式：brew install minikube
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：1.34

## 核心命令示例
```bash
# 启动本地 K8s 集群
minikube start

# 停止集群
minikube stop

# 打开 K8s Dashboard
minikube dashboard

# 暴露服务
minikube service my-service
```

## 适用场景
- 本地 K8s 开发环境
- 学习和测试 Kubernetes
- 快速原型验证
