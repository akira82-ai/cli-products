# Cloudflare Access CLI (`cloudflared`)

## 基本信息
- 官方文档：https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/downloads
- 安装方式：`brew install cloudflared`
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：2025.4.0

## 核心命令示例
```bash
# 登录 Cloudflare 账户 [需认证]
cloudflared tunnel login

# 创建隧道 [需认证]
cloudflared tunnel create my-tunnel

# 运行隧道，将本地服务暴露到公网 [需认证]
cloudflared tunnel run --url http://localhost:3000 my-tunnel
```

## 适用场景
- 创建 Cloudflare Tunnel 安全暴露内网服务，无需开放公网端口
- 替代传统 VPN，通过 Cloudflare Access 实现零信任网络访问
- 开发调试时将本地服务临时暴露给外部（Webhook 回调测试等）
