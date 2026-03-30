# Nomad CLI (`nomad`)

## 基本信息
- 官方文档：https://developer.hashicorp.com/nomad/docs
- 安装方式：brew install nomad
- 开源：BSL（源码可见）
- 平台支持：macOS / Linux / Windows
- 最后验证版本：1.9

## 核心命令示例
```bash
# 启动开发模式
nomad agent -dev

# 运行作业 [需认证]
nomad job run app.nomad

# 查看作业状态
nomad job status

# 查看节点状态
nomad node status
```

## 适用场景
- 工作负载编排（容器和非容器）
- 混合应用调度
- 边缘计算工作负载管理
