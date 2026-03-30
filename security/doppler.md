# Doppler CLI (`doppler`)

## 基本信息
- 官方文档：https://docs.doppler.com/docs/install-cli
- 安装方式：`brew install dopplerhq/cli/doppler`
- 开源：否（CLI 开源，MIT）
- 平台支持：macOS / Linux / Windows
- 最后验证版本：3.72.0

## 核心命令示例
```bash
# 登录 Doppler [需认证]
doppler login

# 在项目中设置密钥 [需认证]
doppler secrets set DATABASE_URL="postgres://localhost:5432/mydb"

# 运行命令并注入密钥到环境变量 [需认证]
doppler run -- python app.py
```

## 适用场景
- 跨环境（dev/staging/prod）统一管理应用密钥和环境变量
- CI/CD 中使用 `doppler run` 安全注入密钥，替代 .env 文件
- 团队共享密钥，支持审计和访问控制
