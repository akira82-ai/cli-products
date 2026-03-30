# Okta CLI (`okta`)

## 基本信息
- 官方文档：https://github.com/okta/okta-cli
- 安装方式：`brew tap okta/tap && brew install okta-cli`
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：0.4.0（已 deprecated）

## 核心命令示例
```bash
# 登录 Okta 组织 [需认证]
okta login

# 列出用户 [需认证]
okta users list

# 创建 SAML/OIDC 应用 [需认证]
okta apps create --app-name my-app --type web --oidc
```

## 适用场景
- 快速创建和配置 Okta 应用集成（SAML/OIDC）
- 管理 Okta 用户和组的生命周期
- 注：此 CLI 已标记为 deprecated，建议使用 Okta Management API 或 Terraform Provider
