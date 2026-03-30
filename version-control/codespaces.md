# GitHub Codespaces CLI (`gh cs`)

## 基本信息
- 官方文档：https://docs.github.com/codespaces
- 安装方式：随 gh CLI 安装
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：随 gh 版本

## 核心命令示例
```bash
# 列出 Codespace [需认证]
gh codespace list

# 创建 Codespace [需认证]
gh codespace create -r owner/repo

# 在 VS Code 中打开 [需认证]
gh codespace code

# 删除 Codespace [需认证]
gh codespace delete
```

## 适用场景
- 远程开发环境的创建和管理
- Codespace 生命周期管理
- 在本地编辑器中连接远程环境
