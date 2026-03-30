# Bitwarden CLI (`bw`)

## 基本信息
- 官方文档：https://bitwarden.com/help/cli
- 安装方式：`npm install -g @bitwarden/cli`
- 开源：是 (GPL-3.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：2025.1.0

## 核心命令示例
```bash
# 登录 Bitwarden 账户 [需认证]
bw login user@example.com

# 获取密码项 [需认证]
bw get password "API Key"

# 同步 Vault 数据 [需认证]
bw sync
```

## 适用场景
- 在 CI/CD 和脚本中安全获取密钥、密码和令牌
- 自动化管理 Vault 中的密码项目（创建、编辑、删除）
- 与企业密钥管理流程集成，实现密钥轮换自动化
