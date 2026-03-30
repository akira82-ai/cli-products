# Vault CLI (`vault`)

## 基本信息
- 官方文档：https://developer.hashicorp.com/vault/docs/commands
- 安装方式：`brew install vault`
- 开源：是 (BSL-1.1)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：1.19.0

## 核心命令示例
```bash
# 读取密钥 [需认证]
vault kv get secret/my-app/database

# 写入密钥 [需认证]
vault kv put secret/my-app/database url="postgres://localhost:5432/mydb" username="admin" password="s3cret"

# 生成一次性动态凭证 [需认证]
vault read database/creds/my-role
```

## 适用场景
- 管理应用密钥、数据库凭证和 TLS 证书的生命周期
- 使用动态密钥按需生成短期凭证，提升安全性
- CI/CD 中通过 `vault kv get` 安全注入密钥到构建和部署流程
