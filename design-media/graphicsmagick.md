# GraphicsMagick (`gm`)

## 基本信息
- 官方文档：http://www.graphicsmagick.org/
- 安装方式：`brew install graphicsmagick`
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：v1.3.45

## 核心命令示例
```bash
# 调整图片大小
gm convert input.jpg -resize 800x600 output.jpg

# 批量转换图片格式
gm mogrify -format png *.jpg

# 图片旋转
gm convert input.jpg -rotate 90 output.jpg

# 创建缩略图
gm convert input.jpg -thumbnail 150x150^ -gravity center -extent 150x150 thumb.jpg

# 拼接多张图片
gm montage image1.jpg image2.jpg image3.jpg -geometry +2+2 output.jpg
```

## 适用场景
- ImageMagick 的轻量级替代方案，处理速度更快
- 服务器端批量图片处理和缩略图生成
- 图片格式转换和基础编辑操作
