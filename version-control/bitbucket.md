# Bitbucket CLI (`bitbucket`)

## 基本信息
- 官方文档：https://developer.atlassian.com/cloud/bitbucket/
- 安装方式：pip install bitbucket-cli
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：0.6

## 核心命令示例
```bash
# 认证登录 [需认证]
bitbucket auth login

# 列出仓库 [需认证]
bitbucket repo list

# 创建 Pull Request [需认证]
bitbucket pr create --title "feat: add X"

# 查看 Pipeline
bitbucket pipeline list
```

## 适用场景
- Bitbucket 仓库管理
- PR 操作与代码审查
- Pipeline 自动化
