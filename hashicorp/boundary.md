# Boundary CLI (`boundary`)

## 基本信息
- 官方文档：https://developer.hashicorp.com/boundary/docs
- 安装方式：brew install boundary
- 开源：BSL（源码可见）
- 平台支持：macOS / Linux / Windows
- 最后验证版本：0.16

## 核心命令示例
```bash
# 启动开发模式
boundary dev

# 认证 [需认证]
boundary authenticate password -login-name=admin

# 查看目标列表 [需认证]
boundary targets list -scope-id global

# 连接到目标 [需认证]
boundary connect -target-id ttcp_xxx
```

## 适用场景
- 安全远程访问基础设施
- SSH/RDP/数据库会话管理
- 零信任访问控制
