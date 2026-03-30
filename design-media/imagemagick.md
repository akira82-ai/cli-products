# ImageMagick (`magick`)

## 基本信息
- 官方文档：https://imagemagick.org/script/command-line-tools.php
- 安装方式：`brew install imagemagick`
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：v7.1.1

## 核心命令示例
```bash
# 调整图片大小
magick input.jpg -resize 800x600 output.jpg

# 批量转换图片格式
magick *.png -quality 90 output.jpg

# 图片加水印
magick input.jpg -gravity southeast -draw "text 10,10 'Watermark'" output.jpg

# 创建 GIF 动画
magick -delay 100 frame1.png frame2.png frame3.png animation.gif

# 图片模糊处理
magick input.jpg -blur 0x5 output.jpg
```

## 适用场景
- 批量图片格式转换和尺寸调整
- 图片特效处理（模糊、锐化、水印等）
- 自动化图片处理流水线
