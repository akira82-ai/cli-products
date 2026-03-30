# Clever Cloud CLI (`clever`)

## 基本信息
- 官方文档：https://www.clever-cloud.com/developers/doc/cli/
- 安装方式：npm install -g clever-tools
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：3.1

## 核心命令示例
```bash
# 登录 [需认证]
clever login

# 创建应用 [需认证]
clever create --type node myapp

# 部署 [需认证]
clever deploy

# 扩缩容 [需认证]
clever scale --flavor pico --min-instances 2
```

## 适用场景
- Clever Cloud 应用部署
- 服务扩缩容管理
- 环境变量和域名配置
