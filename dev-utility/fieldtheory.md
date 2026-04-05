# Field Theory CLI (`ft`)

## 基本信息
- 官方文档：https://fieldtheory.dev/cli
- 作者：[@andrewfarah](https://x.com/andrewfarah)
- 安装方式：`npm install -g fieldtheory`
- 开源：是
- 平台支持：macOS / Linux / Windows
- 最后验证版本：2026年4月

## 核心命令示例
```bash
# 同步所有书签（无需 API）
ft sync

# 全文搜索（BM25 排名）
ft search "cancer research"

# 终端可视化仪表盘
ft viz

# LLM 分类（通过 Claude 或 Codex）
ft classify

# 正则表达式快速分类
ft classify --regex

# 显示分类分布
ft categories

# 统计信息（热门作者、语言、日期范围）
ft stats

# 按作者、日期、分类过滤
ft list --author "@user" --category "ai"

# 域名分布
ft domains
```

> 所有书签存储在本地 SQLite，Agent 可直接查询和交互。

## 适用场景
- X/Twitter 书签本地化管理
- Agent 驱动的书签分析与分类
- 个人知识库构建
- 书签可视化与统计
- 收藏内容全文本搜索
