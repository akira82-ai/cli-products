# Heroku CLI (`heroku`)

## 基本信息
- 官方文档：https://devcenter.heroku.com/articles/heroku-cli
- 安装方式：brew install heroku/brew/heroku
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：9.2

## 核心命令示例
```bash
# 登录
heroku login

# 创建应用 [需认证]
heroku create myapp

# 部署
git push heroku main

# 查看日志
heroku logs --tail
```

## 适用场景
- PaaS 应用快速部署
- Addon 管理和扩展
- 日志查看和 Dyno 管理
