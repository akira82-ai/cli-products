# Git (`git`)

## 基本信息
- 官方文档：https://git-scm.com/doc
- 安装方式：brew install git / apt install git
- 开源：是 (GPL-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：2.47

## 核心命令示例
```bash
# 初始化仓库
git init

# 克隆远程仓库
git clone https://github.com/user/repo.git

# 提交更改
git add . && git commit -m "feat: add new feature"

# 推送到远程
git push origin main

# 查看提交历史
git log --oneline -10
```

## 适用场景
- 源代码版本控制与团队协作
- 分支管理与代码合并
- 变更历史追踪与回滚
