# Let's Encrypt CLI (`certbot`)

## 基本信息
- 官方文档：https://certbot.eff.org/instructions
- 安装方式：`brew install certbot` 或 `apt install certbot`
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux
- 最后验证版本：4.0.0

## 核心命令示例
```bash
# 获取并安装 SSL 证书
sudo certbot --nginx -d example.com -d www.example.com

# 仅获取证书（手动安装） [需认证]
sudo certbot certonly --standalone -d example.com

# 续期所有证书
sudo certbot renew
```

## 适用场景
- 自动化申请和续期 Let's Encrypt 免费 SSL/TLS 证书
- 与 Nginx/Apache 集成，自动配置 HTTPS
- 使用 DNS 验证方式为内网服务获取证书
