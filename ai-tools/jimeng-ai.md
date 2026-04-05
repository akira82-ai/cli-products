# 即梦AI CLI (`jimeng`)

## 基本信息
- 官方文档：https://jimeng.jianying.com/
- 官网：https://jimo.studio/
- 安装方式：curl 一键部署
- 开源：部分开源
- 平台支持：macOS / Linux / Windows
- 最后验证版本：2026年4月

## 核心命令示例
```bash
# 文生图
jimeng image generate --prompt "a beautiful sunset"

# 文生视频
jimeng video generate --prompt "a cat playing"

# 图生图
jimeng image transform --input image.jpg --prompt "oil painting style"

# 图片超分
jimeng image upscale --input image.jpg

# 多帧合成
jimeng video compose --frames frame1.jpg,frame2.jpg
```

> 需要即梦AI账号授权，支持 Seedance 2.0 旗舰模式。

## 适用场景
- AI 驱动的内容创作
- 营销素材批量生成
- 视频自动化生产
- Agent 直接调用生成内容
