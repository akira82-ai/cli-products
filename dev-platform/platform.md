# Platform.sh CLI (`platform`)

## 基本信息
- 官方文档：https://docs.platform.sh/administration/cli.html
- 安装方式：brew install platformsh/tap/platformsh-cli
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：4.24

## 核心命令示例
```bash
# 登录 [需认证]
platform login

# 列出项目 [需认证]
platform project:list

# 创建环境分支 [需认证]
platform environment:branch feature main

# 推送代码并构建
platform push
```

## 适用场景
- Platform.sh PaaS 项目管理
- 环境分支和多环境管理
- 部署和服务配置
