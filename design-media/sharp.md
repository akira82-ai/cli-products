# Sharp CLI (`sharp`)

## 基本信息
- 官方文档：https://sharp.pixelplumbing.com/
- 安装方式：`npm install -g sharp-cli`
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：v4.0.0

## 核心命令示例
```bash
# 调整图片大小
sharp -i input.jpg -o output.jpg resize 800 600

# 批量转换 PNG 为 WebP
sharp -i "*.png" -o "./output" --format webp

# 图片旋转并调整质量
sharp -i input.jpg -o output.jpg rotate 90 --quality 80

# 提取图片元数据
sharp -i input.jpg metadata
```

## 适用场景
- 高性能图片处理（基于 libvips，速度快内存低）
- 批量图片格式转换，特别是 WebP/AVIF 等现代格式
- Node.js 项目中的图片处理流水线
