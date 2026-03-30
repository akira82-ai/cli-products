# EKS CLI (`eksctl`)

## 基本信息
- 官方文档：https://eksctl.io/
- 安装方式：`brew install eksctl` / `snap install eksctl`
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：待验证

## 核心命令示例
```bash
# 创建 EKS 集群 [需认证]
eksctl create cluster --name my-cluster --nodes 3

# 删除 EKS 集群 [需认证]
eksctl delete cluster --name my-cluster

# 查看集群列表 [需认证]
eksctl get cluster

# 扩缩节点组 [需认证]
eksctl scale nodegroup --cluster my-cluster --name ng-1 --nodes 5
```

> 需要认证凭据的命令标注 `[需认证]`。

## 适用场景
- 创建和管理 Amazon EKS 集群
- 节点组扩缩容管理
- EKS 集群生命周期管理
