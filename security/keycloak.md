# Keycloak CLI (`kcadm`)

## 基本信息
- 官方文档：https://www.keycloak.org/server/all-config
- 安装方式：Keycloak 安装包自带（`bin/kcadm.sh`）
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：26.1.0

## 核心命令示例
```bash
# 登录 Keycloak [需认证]
kcadm.sh config credentials --server http://localhost:8080 --realm master --user admin

# 列出 Realm 中的用户 [需认证]
kcadm.sh get users -r my-realm

# 创建新 Client [需认证]
kcadm.sh create clients -r my-realm -s clientId=my-app -s enabled=true -s protocol=openid-connect
```

## 适用场景
- 自动化管理 Keycloak Realm、Users、Roles 和 Clients
- 批量迁移用户数据和权限配置
- CI/CD 中初始化和配置 Keycloak 实例
