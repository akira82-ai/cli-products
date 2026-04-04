# Translate Shell (`trans`)

## 基本信息
- 官方文档：https://github.com/soimort/translate-shell
- 安装方式：brew install translate-shell
- 开源：是 (Public Domain)
- 平台支持：macOS / Linux
- 最后验证版本：0.9

## 核心命令示例
```bash
# 自动检测语言并翻译
trans "Hello World"

# 翻译为中文
trans :zh "Hello World"

# 翻译为英文
trans :en "你好世界"

# 简洁模式（仅输出译文）
trans -b "Hello World"
```

## 适用场景
- 命令行调用 Google 翻译
- 多语言内容生产
- Agent 多语言内容翻译
