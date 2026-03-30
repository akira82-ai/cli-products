# GitHub CLI (`gh`)

## 基本信息
- 官方文档：https://cli.github.com/
- 安装方式：brew install gh
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：2.67

## 核心命令示例
```bash
# 认证登录 [需认证]
gh auth login

# 创建 Pull Request [需认证]
gh pr create --title "feat: add X" --body "描述"

# 列出 PR
gh pr list

# 创建 Issue [需认证]
gh issue create --title "Bug: X 不工作"

# 克隆仓库
gh repo clone owner/repo
```

## 适用场景
- 在终端管理 PR/Issue，无需打开浏览器
- CI/CD 中自动化 GitHub 操作
- 批量管理仓库和 GitHub Actions
