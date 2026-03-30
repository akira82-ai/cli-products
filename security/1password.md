# 1Password CLI (`op`)

## 基本信息
- 官方文档：https://developer.1password.com/docs/cli
- 安装方式：`brew install op`
- 开源：否
- 平台支持：macOS / Linux / Windows
- 最后验证版本：2.30.3

## 核心命令示例
```bash
# 登录 1Password 账户 [需认证]
op account add --address my.1password.com --email user@example.com

# 读取密码项 [需认证]
op item get "Production Database" --fields password

# 注入环境变量到当前 Shell [需认证]
op run --env-file=".env.op" -- python app.py
```

## 适用场景
- CI/CD 流水线中安全注入密钥和环境变量
- 脚本化读取和管理密码、证书等敏感信息
- 使用 `op run` 和 `op inject` 在开发环境中自动填充密钥
