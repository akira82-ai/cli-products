# Deno (`deno`)

## 基本信息
- 官方文档：https://docs.deno.com/
- 安装方式：`curl -fsSL https://deno.land/install.sh | sh` 或 `brew install deno`
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：v2.1.4

## 核心命令示例
```bash
# 直接运行远程脚本
deno run https://deno.land/std/examples/welcome.ts

# 运行本地脚本（授予权限）
deno run --allow-net --allow-read server.ts

# 安装可执行脚本
deno install --allow-net cli_tool.ts

# 格式化代码
deno fmt

# 代码静态检查
deno lint

# 添加依赖
deno add npm:express
```

## 适用场景
- 安全优先的 TypeScript/JavaScript 运行时
- 默认安全的脚本执行（权限模型）
- 开箱即用的工具链（格式化、Linter、测试、LSP）
