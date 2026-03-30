# pnpm (`pnpm`)

## 基本信息
- 官方文档：https://pnpm.io/
- 安装方式：`npm install -g pnpm` 或 `brew install pnpm`
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：v9.15.1

## 核心命令示例
```bash
# 初始化新项目
pnpm init

# 安装依赖（使用硬链接节省磁盘空间）
pnpm install

# 添加依赖
pnpm add vue

# 运行脚本
pnpm dev

# 创建 Monorepo 工作区
pnpm -r --filter ./packages/** run build

# 清理缓存和未使用的依赖
pnpm store prune
```

## 适用场景
- 节省磁盘空间的高效包管理（内容寻址存储）
- Monorepo 项目的依赖管理
- 严格依赖隔离，避免幽灵依赖问题
