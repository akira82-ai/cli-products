# Waypoint CLI (`waypoint`)

## 基本信息
- 官方文档：https://developer.hashicorp.com/waypoint/docs
- 安装方式：brew install waypoint
- 开源：BSL（源码可见）
- 平台支持：macOS / Linux / Windows
- 最后验证版本：0.12

## 核心命令示例
```bash
# 初始化项目
waypoint init

# 构建并部署
waypoint up

# 部署到指定平台
waypoint deploy

# 发布版本
waypoint release
```

## 适用场景
- 应用构建-部署-发布一体化工作流
- 多平台部署（K8s/Docker/Nomad 等）
- 版本发布管理
