# 小红书 CLI (`xiaohongshu`)

## 基本信息
- 官方文档：https://github.com/jackwener/xiaohongshu-cli
- GitHub：https://github.com/jackwener/xiaohongshu-cli
- 作者：@jakevin7（卡比卡比）
- 安装方式：`pip install xiaohongshu-cli`
- 开源：是
- 平台支持：macOS / Linux / Windows
- 最后验证版本：2026年4月

## 核心命令示例
```bash
# 搜索笔记
xiaohongshu search "AI工具" --json

# 阅读笔记详情
xiaohongshu note note_id

# 获取用户信息
xiaohongshu user user_id

# 发布笔记
xiaohongshu post --title "标题" --content "内容" --images img1.jpg,img2.jpg

# 评论
xiaohongshu comment note_id "评论内容"

# 点赞
xiaohongshu like note_id

# 收藏
xiaohongshu favorite note_id
```

> 支持结构化输出（--json/--yaml），内置 SKILL.md 供 Agent 直接调用。

## 适用场景
- 小红书内容监控
- 批量互动与数据采集
- Agent 自动化内容管理
- 社交媒体运营
