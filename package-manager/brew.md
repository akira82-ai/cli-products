# Homebrew (`brew`) - macOS

## 基本信息
- 官方文档：https://docs.brew.sh/
- 安装方式：`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
- 开源：是 (BSD-2-Clause)
- 平台支持：macOS / Linux（Linuxbrew）
- 最后验证版本：v4.4.15

## 核心命令示例
```bash
# 安装软件包
brew install git

# 搜索可用包
brew search nginx

# 更新 Homebrew 和所有包
brew update && brew upgrade

# 查看已安装的包
brew list

# 清理旧版本缓存
brew cleanup

# 安装 GUI 应用
brew install --cask visual-studio-code
```

## 适用场景
- macOS 上安装和管理开发工具和系统软件
- 替代手动下载安装的统一包管理方案
- 通过 Cask 管理桌面应用程序
