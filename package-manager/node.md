# Node.js (`node`)

## 基本信息
- 官方文档：https://nodejs.org/docs/latest/api/
- 安装方式：`brew install node` 或使用 nvm（`nvm install --lts`）
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：v22.12.0（LTS）

## 核心命令示例
```bash
# 运行 JavaScript 文件
node app.js

# 运行交互式 REPL
node

# 执行内联 JavaScript 代码
node -e "console.log('Hello, World!')"

# 检查 Node.js 版本
node --version

# 运行 ESM 模块
node --experimental-modules index.mjs

# 启动内置调试器
node --inspect-brk app.js
```

## 适用场景
- 服务端 JavaScript/TypeScript 应用运行时
- 开发工具链的基础运行环境
- 脚本自动化和 CLI 工具开发
