# Squoosh CLI (`squoosh`)

## 基本信息
- 官方文档：https://github.com/GoogleChromeLabs/squoosh
- 安装方式：`npm install -g @nicolo-ribaudo/squoosh-cli`（该包已不存在于 npm，建议使用 `sharp-cli` 替代）
- 开源：是 (Apache-2.0)
- 平台支持：—
- 最后验证版本：—（原包已下架）

## 核心命令示例
```bash
# 使用 sharp-cli 压缩图片（推荐替代方案）
npx sharp-cli --input input.jpg --output ./output/output.webp --format webp

# 转换为 AVIF 格式
npx sharp-cli --input input.png --output ./output/output.avif --format avif --quality 60

# 调整尺寸
npx sharp-cli --input input.png --output ./output/output.jpg --resize 800 --format jpeg --quality 75
```

## 适用场景
- 网页图片优化，减小文件体积提升加载速度
- 批量转换图片为 WebP/AVIF 等现代格式
- 替代复杂工具的轻量级图片压缩方案
