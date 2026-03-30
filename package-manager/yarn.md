# Yarn (`yarn`) - Meta

## 基本信息
- 官方文档：https://yarnpkg.com/
- 安装方式：`npm install -g yarn` 或 `corepack enable`
- 开源：是 (BSD-2-Clause)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：v4.6.0

## 核心命令示例
```bash
# 初始化新项目
yarn init

# 安装所有依赖
yarn install

# 添加依赖包
yarn add react

# 添加开发依赖
yarn add -D jest

# 运行脚本
yarn build

# 升级依赖到最新版本
yarn up --pattern "react*"
```

## 适用场景
- 大型 Node.js 项目的快速依赖安装（Plug'n'Play）
- Monorepo 多包管理（Yarn Workspaces）
- 依赖版本锁定和确定性构建
