# Render CLI (`render`)

## 基本信息
- 官方文档：https://render.com/docs/cli
- 安装方式：brew install render-oss/render/render
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux
- 最后验证版本：0.23

## 核心命令示例
```bash
# 登录
render login

# 查看服务列表 [需认证]
render services list

# 创建部署 [需认证]
render deploys create --service-id svc_xxx
```

## 适用场景
- Render 平台服务管理
- 部署和日志查看
- Web/Worker/Cron 服务操作
