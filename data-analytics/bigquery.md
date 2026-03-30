# BigQuery CLI (`bq`)

## 基本信息
- 官方文档：https://cloud.google.com/bigquery/docs/bq-command-line-tool
- 安装方式：随 gcloud SDK 安装
- 开源：否
- 平台支持：macOS / Linux / Windows
- 最后验证版本：2.1

## 核心命令示例
```bash
# 执行 SQL 查询 [需认证]
bq query "SELECT * FROM dataset.table LIMIT 100"

# 列出数据集 [需认证]
bq ls

# 创建数据集 [需认证]
bq mk my_dataset

# 加载数据 [需认证]
bq load dataset.table file.csv
```

## 适用场景
- 大规模数据查询和分析
- 数据集和表管理
- 批量数据导入导出
