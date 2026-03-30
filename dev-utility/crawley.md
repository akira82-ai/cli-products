# Crawley (`crawley`)

## 基本信息
- 官方文档：https://github.com/s0rg/crawley
- 安装方式：brew install s0rg/tap/crawley 或 go install github.com/s0rg/crawley@latest
- 开源：是 (MIT)
- 平台支持：macOS / Linux
- 最后验证版本：0.6

## 核心命令示例
```bash
# 抓取站点内容
crawley https://example.com

# 设置抓取深度
crawley -d 2 https://example.com

# 提取指定 CSS 选择器内容
crawley -e "css:.title" https://example.com

# 查看帮助
crawley --help
```

## 适用场景
- Unix 风格网页爬虫
- Agent 抓站点内容
- 管道友好的数据提取
