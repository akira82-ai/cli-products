# Squoosh CLI (`squoosh`)

## 基本信息
- 官方文档：https://github.com/GoogleChromeLabs/squoosh
- 安装方式：`npm install -g @nicolo-ribaudo/squoosh-cli` 或 `npx @nicolo-ribaudo/squoosh-cli`
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：v0.7.2

## 核心命令示例
```bash
# 压缩图片为 WebP 格式
npx @nicolo-ribaudo/squoosh-cli --mozjpeg '{quality:80}' input.jpg -d ./output

# 批量压缩目录下所有图片
npx @nicolo-ribaudo/squoosh-cli -d ./compressed ./images/*.jpg

# 转换为 AVIF 格式并设置质量
npx @nicolo-ribaudo/squoosh-cli --avif '{quality:60}' input.png -d ./output

# 调整尺寸并压缩
npx @nicolo-ribaudo/squoosh-cli --resize '{width:800}' --webp '{quality:75}' input.png -d ./output
```

## 适用场景
- 网页图片优化，减小文件体积提升加载速度
- 批量转换图片为 WebP/AVIF 等现代格式
- 替代复杂工具的轻量级图片压缩方案
