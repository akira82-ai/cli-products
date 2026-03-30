# K9s (`k9s`)

## 基本信息
- 官方文档：https://k9sro.io/
- 安装方式：brew install k9s
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux
- 最后验证版本：0.32

## 核心命令示例
```bash
# 启动 K9s TUI
k9s

# 指定命名空间启动
k9s -n production

# 指定 kubeconfig
k9s --kubeconfig /path/to/config

# 只读模式
k9s --readonly
```

## 适用场景
- K8s 集群可视化 TUI 管理
- 实时资源监控和日志查看
- 快速排查 K8s 集群问题
