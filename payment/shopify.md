# Shopify CLI (`shopify`)

## 基本信息
- 官方文档：https://shopify.dev/docs/shopify-cli
- 安装方式：`npm install -g @shopify/cli @shopify/theme`
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：v3.77.0

## 核心命令示例
```bash
# 创建新的 Shopify 应用项目
shopify app init

# 启动本地开发服务器 [需认证]
shopify app dev

# 列出店铺主题 [需认证]
shopify theme list --store my-store.myshopify.com

# 推送主题文件到店铺 [需认证]
shopify theme push --store my-store.myshopify.com

# 生成应用扩展脚手架
shopify app generate extension
```

## 适用场景
- 开发和调试 Shopify 应用与主题
- 本地主题开发并实时预览变更
- 管理 Shopify 商店的部署和发布流程
