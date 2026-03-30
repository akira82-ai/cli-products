# Crossplane CLI (`crossplane`)

## 基本信息
- 官方文档：https://docs.crossplane.io/
- 安装方式：brew install crossplane
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux
- 最后验证版本：1.18

## 核心命令示例
```bash
# 安装 Provider
crossplane install xpkg.upbound.io/crossplane-contrib/provider-aws:latest

# 推送配置
crossplane push configuration registry/my-config:latest

# 查看版本
crossplane --version

# 查看帮助
crossplane --help
```

## 适用场景
- Kubernetes 原生基础设施编排
- 控制平面管理
- 多云资源统一管理
