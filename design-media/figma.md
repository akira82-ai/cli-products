# Figma CLI (`figma`)

## 基本信息
- 官方文档：https://www.figma.com/developers/api
- 安装方式：`npm install -g @figma/cli`（社区方案）
- 开源：否（Figma API 为官方提供）
- 平台支持：macOS / Linux / Windows
- 最后验证版本：N/A（主要通过 API 操作）

## 核心命令示例
```bash
# 导出 Figma 文件为图片 [需认证]
curl -H "X-Figma-Token: YOUR_TOKEN" \
  "https://api.figma.com/v1/images/FILE_KEY?format=png&scale=2"

# 获取 Figma 文件结构 [需认证]
curl -H "X-Figma-Token: YOUR_TOKEN" \
  "https://api.figma.com/v1/files/FILE_KEY"

# 获取特定节点的样式信息 [需认证]
curl -H "X-Figma-Token: YOUR_TOKEN" \
  "https://api.figma.com/v1/files/FILE_KEY/nodes?ids=NODE_ID"

# 导出组件列表 [需认证]
curl -H "X-Figma-Token: YOUR_TOKEN" \
  "https://api.figma.com/v1/files/FILE_KEY/components"
```

## 适用场景
- 从 Figma 设计稿自动导出切图资源
- 提取设计 Token（颜色、字体、间距）用于开发
- CI/CD 中自动化设计稿与代码对比
