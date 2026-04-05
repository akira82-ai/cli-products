# Bilibili CLI (`bilibili`)

## 基本信息
- 官方文档：https://github.com/jackwener/bilibili-cli
- GitHub：https://github.com/jackwener/bilibili-cli
- 作者：@jakevin7（卡比卡比）
- 安装方式：`pip install bilibili-cli`
- 开源：是
- 平台支持：macOS / Linux / Windows
- 最后验证版本：2026年4月

## 核心命令示例
```bash
# 搜索视频
bilibili search "编程教程" --json

# 获取视频信息
bilibili video video_id

# 下载视频
bilibili download video_id

# 获取用户信息
bilibili user user_id

# 发送弹幕
bilibili danmaku video_id "弹幕内容"

# 点赞/投币/收藏
bilibili like video_id
bilibili coin video_id
bilibili favorite video_id

# 查看动态
bilibili feed
```

> 支持结构化输出（--json/--yaml），内置 SKILL.md 供 Agent 直接调用。

## 适用场景
- B站视频内容监控
- 批量视频信息采集
- Agent 自动化内容管理
- 视频数据下载
