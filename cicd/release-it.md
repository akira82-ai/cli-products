# release-it (`release-it`)

## 基本信息
- 官方文档：https://github.com/release-it/release-it
- 安装方式：`npm install -g release-it`
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：17

## 核心命令示例
```bash
# 交互式发版（自动推断版本号）
release-it

# 发布 patch 版本
release-it patch

# 发布预发布版本
release-it minor --pre-release=beta

# 预演模式（不执行实际操作）
release-it --dry-run
```

## 适用场景
- 自动化发版
- 生成changelog
- 发GitHub Release
