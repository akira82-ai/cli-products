# Twitter/X CLI (`twitter`)

## 基本信息
- 官方文档：https://github.com/jackwener/twitter-cli
- GitHub：https://github.com/jackwener/twitter-cli
- 作者：@jakevin7（卡比卡比）
- 安装方式：`pip install twitter-cli`
- 开源：是
- 平台支持：macOS / Linux / Windows
- 最后验证版本：2026年4月

## 核心命令示例
```bash
# 查看时间线
twitter timeline --json

# 发推
twitter post "Hello, World!"

# 搜索推文
twitter search "AI工具" --json

# 查看书签
twitter bookmarks

# 回复推文
twitter reply tweet_id "回复内容"

# 点赞/转推
twitter like tweet_id
twitter retweet tweet_id

# 查看用户信息
twitter user username
```

> 支持结构化输出（--json/--yaml），内置 SKILL.md 供 Agent 直接调用。

## 适用场景
- Twitter 内容监控
- 批量互动与数据采集
- Agent 自动化内容管理
- 社交媒体运营
