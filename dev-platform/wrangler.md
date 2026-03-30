# Cloudflare Workers CLI (`wrangler`)

## 基本信息
- 官方文档：https://developers.cloudflare.com/workers/wrangler/
- 安装方式：npm install -g wrangler
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：3.99

## 核心命令示例
```bash
# 登录 [需认证]
wrangler login

# 本地开发
wrangler dev

# 部署 Worker [需认证]
wrangler deploy

# KV 存储操作 [需认证]
wrangler kv:key list
```

## 适用场景
- Cloudflare Workers 边缘计算开发
- KV / R2 / D1 存储管理
- 本地开发调试和部署
