# Auth0 CLI (`auth0`)

## 基本信息
- 官方文档：https://auth0.github.io/auth0-cli
- 安装方式：`brew tap auth0/auth0-cli && brew install auth0-cli`
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：1.8.0

## 核心命令示例
```bash
# 登录 Auth0 租户 [需认证]
auth0 login

# 列出所有应用 (Application) [需认证]
auth0 apps list

# 创建测试用户 [需认证]
auth0 users create --connection Username-Password-Authentication --email test@example.com --password "SecureP@ss1" --name "Test User"
```

## 适用场景
- 管理 Auth0 租户中的 Applications、APIs、Users 和 Rules
- 快速创建和配置测试用户，用于开发和 QA
- CI/CD 中自动化 Auth0 资源的创建和配置
