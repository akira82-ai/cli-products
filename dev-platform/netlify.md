# Netlify CLI (`netlify`)

## 基本信息
- 官方文档：https://docs.netlify.com/cli/get-started/
- 安装方式：npm install -g netlify-cli
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：17

## 核心命令示例
```bash
# 登录
netlify login

# 本地开发调试
netlify dev

# 部署 [需认证]
netlify deploy --prod

# 管理函数
netlify functions:invoke my-function
```

## 适用场景
- 静态站点和 Serverless 函数部署
- 本地开发与 Netlify 平台联调
- 持续部署配置
