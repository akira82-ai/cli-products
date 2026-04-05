# 飞书文档管理 CLI (`feishu-docx`)

## 基本信息
- 官方文档：https://github.com/leemysw/feishu-docx
- GitHub：https://github.com/leemysw/feishu-docx
- 安装方式：`pip install feishu-docx`
- 开源：是
- 平台支持：macOS / Linux / Windows
- 最后验证版本：2026年4月

## 核心命令示例
```bash
# 读取飞书文档
feishu-docx read doc_id

# 创建文档
feishu-docx create --title "文档标题" --content "内容"

# 写入文档
feishu-docx write doc_id --content "新内容"

# Markdown 转飞书文档
feishu-docx md-to-docx README.md

# 飞书文档转 Markdown
feishu-docx docx-to-md doc_id --output output.md

# 批量操作
feishu-docx batch --file-list files.txt
```

> 为 AI Agent 设计，支持 Claude/GPT Skills 直接调用。

## 适用场景
- 飞书知识库管理
- 文档批量读写
- Markdown 双向转换
- Agent 输出美化
