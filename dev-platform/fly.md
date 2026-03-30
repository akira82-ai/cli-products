# Fly.io CLI (`fly`)

## 基本信息
- 官方文档：https://fly.io/docs/hands-on/install-flyctl/
- 安装方式：curl -L https://fly.io/install.sh | sh
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：0.3

## 核心命令示例
```bash
# 登录 [需认证]
fly auth login

# 启动并部署 [需认证]
fly launch

# 部署 [需认证]
fly deploy

# 管理密钥 [需认证]
fly secrets set API_KEY=xxx
```

## 适用场景
- 部署应用到全球边缘节点
- 容器化应用快速上线
- 密钥和环境变量管理
