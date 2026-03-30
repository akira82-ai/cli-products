# ExFig CLI (`exfig`)

## 基本信息
- 官方文档：https://github.com/nicojones/exfig
- 安装方式：`npm install -g exfig`
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：v1.0.0

## 核心命令示例
```bash
# 从 Figma 文件导出资源 [需认证]
exfig export --file-key FILE_KEY --format png --output ./assets

# 导出特定画板 [需认证]
exfig export --file-key FILE_KEY --node-id "1:2" --format svg

# 批量导出所有图标 [需认证]
exfig icons --file-key FILE_KEY --frame "Icons" --format svg --output ./icons

# 查看文件页面列表 [需认证]
exfig pages --file-key FILE_KEY
```

## 适用场景
- 从 Figma 设计稿批量导出图标和图片资源
- 自动化设计资源导出流水线
- 设计系统组件的版本化管理
