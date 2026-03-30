# GitLab CLI (`glab`)

## 基本信息
- 官方文档：https://gitlab.com/gitlab-org/cli
- 安装方式：brew install glab
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：1.48

## 核心命令示例
```bash
# 认证登录 [需认证]
glab auth login

# 创建 Merge Request [需认证]
glab mr create --title "feat: add X"

# 列出 MR
glab mr list

# 查看 CI/CD 流水线
glab pipeline list

# 查看 Issue
glab issue list
```

## 适用场景
- GitLab MR 管理与代码审查
- CI/CD 流水线操作
- GitLab 项目和组管理
