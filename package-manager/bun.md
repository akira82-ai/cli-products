# Bun (`bun`)

## 基本信息
- 官方文档：https://bun.sh/docs
- 安装方式：`curl -fsSL https://bun.sh/install | bash`
- 开源：是 (MIT)
- 平台支持：macOS / Linux（Windows 通过 WSL）
- 最后验证版本：v1.1.38

## 核心命令示例
```bash
# 初始化新项目
bun init

# 安装依赖（极快速度）
bun install

# 运行 JavaScript/TypeScript 文件
bun run index.ts

# 添加依赖
bun add express

# 运行 package.json 脚本
bun run dev

# 创建新项目脚手架
bun create react-app my-app
```

## 适用场景
- 追求极致性能的 JavaScript/TypeScript 运行时
- 替代 Node.js + npm/yarn 的全能开发工具链
- 原生支持 TypeScript 和 JSX 执行
