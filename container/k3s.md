# K3s (`k3s`)

## 基本信息
- 官方文档：https://docs.k3s.io/
- 安装方式：curl -sfL https://get.k3s.io | sh -
- 开源：是 (Apache-2.0)
- 平台支持：Linux
- 最后验证版本：1.31

## 核心命令示例
```bash
# 启动 K3s server
k3s server

# 查看 K3s agent 状态
k3s agent

# 通过嵌入式 kubectl 操作
k3s kubectl get nodes

# 查看容器运行时
k3s crictl ps
```

## 适用场景
- 轻量级 Kubernetes 部署（边缘计算、IoT）
- 开发和测试环境
- 资源受限环境下的 K8s
