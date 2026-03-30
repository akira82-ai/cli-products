# Sentry CLI (`sentry-cli`)

## 基本信息
- 官方文档：https://docs.sentry.io/product/cli
- 安装方式：`brew install getsentry/tools/sentry-cli`
- 开源：是 (BSD-3-Clause)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：2.42.0

## 核心命令示例
```bash
# 上传 Debug Symbols (dSYM/Proguard) [需认证]
sentry-cli upload-dif --org my-org --project my-project ./build/symbols/

# 创建新 Release [需认证]
sentry-cli releases --org my-org new 1.0.0

# 设置 Release 提交关联 [需认证]
sentry-cli releases --org my-org set-commits 1.0.0 --auto
```

## 适用场景
- CI/CD 中自动上传 Debug Symbols 和 Source Maps
- 管理 Sentry Release，关联代码提交与错误事件
- 批量操作 Issues（分配、解决、忽略）
