# MongoDB Atlas CLI (`atlas`)

## 基本信息
- 官方文档：https://www.mongodb.com/docs/atlas/cli/
- 安装方式：brew install mongodb-atlas-cli
- 开源：是 (SSPL)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：1.40

## 核心命令示例
```bash
# 登录 [需认证]
atlas auth login

# 查看集群列表 [需认证]
atlas clusters list

# 创建集群 [需认证]
atlas clusters create my-cluster --tier M10

# 创建数据库用户 [需认证]
atlas dbusers create
```

## 适用场景
- MongoDB Atlas 云集群管理
- 数据库用户和权限管理
- 备份和监控操作
