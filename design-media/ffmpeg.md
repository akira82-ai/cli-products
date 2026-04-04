# FFmpeg (`ffmpeg`)

## 基本信息
- 官方文档：https://ffmpeg.org/ffmpeg-all.html
- 安装方式：`brew install ffmpeg`
- 开源：是 (LGPL-2.1 / GPL-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：v7.1

## 核心命令示例
```bash
# 转换视频格式
ffmpeg -i input.mov output.mp4

# 压缩视频并指定码率
ffmpeg -i input.mp4 -b:v 1M -b:a 128k output.mp4

# 从视频中提取音频
ffmpeg -i input.mp4 -vn -acodec libmp3lame output.mp3

# 视频裁剪（从第 10 秒开始，持续 30 秒）
ffmpeg -i input.mp4 -ss 00:00:10 -t 00:00:30 -c copy output.mp4

# 调整视频分辨率
ffmpeg -i input.mp4 -vf scale=1280:720 output_720p.mp4

# 批量转换当前目录下所有 MOV 文件为 MP4
for f in *.mov; do ffmpeg -i "$f" "${f%.mov}.mp4"; done
```

## 适用场景
- 视频/音频格式转换和压缩
- 视频剪辑、裁剪和拼接处理
- 媒体文件元数据查看与批量处理
