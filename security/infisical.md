# Infisical CLI (`infisical`)

## 基本信息
- 官方文档：https://infisical.com/docs/cli/overview
- 安装方式：`brew install infisical`
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：0.37.0

## 核心命令示例
```bash
# 登录 Infisical [需认证]
infisical login

# 获取当前项目的密钥 [需认证]
infisical secrets get DATABASE_URL --env=production

# 运行命令并自动注入密钥 [需认证]
infisical run --env=staging -- node server.js
```

## 适用场景
- 管理和同步项目级密钥，支持多环境切换
- 使用 `infisical run` 在本地开发时自动注入密钥
- CI/CD 中替代硬编码密钥，统一从 Infisical 拉取
