# yt-dlp (`yt-dlp`)

## 基本信息
- 官方文档：https://github.com/yt-dlp/yt-dlp
- 安装方式：brew install yt-dlp
- 开源：是 (Unlicense)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：2024.12

## 核心命令示例
```bash
# 下载视频
yt-dlp https://www.youtube.com/watch?v=xxx

# 选择最佳画质下载
yt-dlp -f bestvideo+bestaudio URL

# 下载视频并提取英文字幕
yt-dlp --write-sub --sub-lang en URL

# 仅提取音频为 MP3
yt-dlp -x --audio-format mp3 URL
```

## 适用场景
- 下载 YouTube/B站等平台视频和字幕
- 提取音频
- 批量下载播放列表
