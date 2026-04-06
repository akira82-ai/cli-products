# 添加新工具的完整工作流程

## 问题描述

2026年4月6日发现：添加新工具后，虽然创建了 markdown 文件并更新了 README，但网站搜索功能找不到新工具。

## 根本原因

网站的搜索功能使用 `_data/tools.json` 作为数据源，而不是直接读取 markdown 文件。因此添加新工具时必须同步更新这个文件。

## 完整工作流程（添加新工具时必须完成以下步骤）

### 1. 创建工具 markdown 文件
在对应分类目录下创建 `工具名.md` 文件

### 2. 更新分类 README.md
更新 `分类目录/README.md`：
- 工具总数（如：共收录 X 个 CLI 工具）
- 工具列表（添加新工具条目）

### 3. 更新分类 index.md
更新 `分类目录/index.md`：
- 工具总数
- 工具列表表格（包含官方文档链接）

### 4. 更新搜索数据源 ⚠️ **关键步骤**
更新 `_data/tools.json`，在对应分类的 `tools` 数组中添加：
```json
{
  "name": "[工具名](文件名.md)",
  "command": "`命令`",
  "description": "工具描述",
  "official_url": "官方文档URL"
}
```

### 5. 更新主 README.md
- 工具总数统计
- 各分类工具数量

### 6. 提交并推送
```bash
git add .
git commit -m "描述"
git push origin main
```

### 7. 触发部署（如需要）
```bash
gh workflow run jekyll.yml --repo akira82-ai/cli-products
```

## 检查清单

添加新工具后，检查以下文件是否全部更新：
- [ ] `分类目录/工具名.md` - 新建
- [ ] `分类目录/README.md` - 更新
- [ ] `分类目录/index.md` - 更新
- [ ] `_data/tools.json` - **更新（搜索功能）**
- [ ] `README.md` - 更新

## 验证方法

部署完成后：
1. 访问 https://akira82-ai.github.io/cli-products/
2. 使用搜索功能搜索新工具名称
3. 确认能找到并显示正确结果
