# Vault CLI (`vault`)

## 基本信息
- 官方文档：https://developer.hashicorp.com/vault/docs
- 安装方式：brew install vault
- 开源：BSL（源码可见）
- 平台支持：macOS / Linux / Windows
- 最后验证版本：1.19

## 核心命令示例
```bash
# 启动开发服务器
vault server -dev

# 启用 KV 密钥引擎
vault secrets enable kv

# 写入密钥 [需认证]
vault kv put secret/myapp password=s3cret

# 读取密钥 [需认证]
vault kv get secret/myapp
```

## 适用场景
- 密钥和凭据管理
- 动态数据库凭据生成
- 加密即服务
