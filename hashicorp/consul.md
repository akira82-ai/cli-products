# Consul CLI (`consul`)

## 基本信息
- 官方文档：https://developer.hashicorp.com/consul/docs
- 安装方式：brew install consul
- 开源：BSL（源码可见）
- 平台支持：macOS / Linux / Windows
- 最后验证版本：1.20

## 核心命令示例
```bash
# 启动开发模式
consul agent -dev

# 查看集群成员
consul members

# 注册服务
consul services register -name=myapp -port=8080

# KV 存储操作
consul kv put config/key value && consul kv get config/key
```

## 适用场景
- 服务发现和注册
- KV 配置存储
- 服务网格管理
