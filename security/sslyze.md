# SSLyze CLI (`sslyze`)

## 基本信息
- 官方文档：https://github.com/nabla-c0d3/sslyze
- 安装方式：`pip install sslyze`
- 开源：是 (AGPL-3.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：6.0.0

## 核心命令示例
```bash
# 扫描目标的 SSL/TLS 配置
sslyze --regular example.com

# 检查是否支持 HTTP Strict Transport Security (HSTS)
sslyze --hsts example.com

# 检查证书是否满足 Apple CT (Certificate Transparency) 要求
sslyze --apple example.com
```

## 适用场景
- 安全审计和合规检查，评估服务器 SSL/TLS 配置强度
- 验证证书链完整性和到期时间
- CI/CD 中集成 SSL 安全扫描，确保部署的服务符合安全基线
