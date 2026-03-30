# Canva CLI (`canva`)

## 基本信息
- 官方文档：https://www.canva.com/developers/docs/
- 安装方式：`npm install -g @canva/cli`（Canva Connect API）
- 开源：否
- 平台支持：macOS / Linux / Windows
- 最后验证版本：N/A（主要通过 Connect API 操作）

## 核心命令示例
```bash
# 通过 Connect API 创建设计 [需认证]
curl -X POST https://api.canva.com/rest/v1/designs \
  -H "Authorization: Bearer ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title":"My Design","design_type":{"type":"preset","width":1080,"height":1080}}'

# 导出设计为图片 [需认证]
curl -X POST https://api.canva.com/rest/v1/designs/DESIGN_ID/export \
  -H "Authorization: Bearer ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"format":"png","width":1080,"height":1080}'

# 获取品牌模板列表 [需认证]
curl https://api.canva.com/rest/v1/brand-templates \
  -H "Authorization: Bearer ACCESS_TOKEN"
```

## 适用场景
- 通过 API 自动创建和导出 Canva 设计
- 批量基于品牌模板生成营销素材
- 集成 Canva 设计能力到自动化工作流
