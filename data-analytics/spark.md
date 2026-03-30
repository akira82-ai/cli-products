# Apache Spark CLI (`spark-submit`)

## 基本信息
- 官方文档：https://spark.apache.org/docs/latest/submitting-applications.html
- 安装方式：brew install apache-spark
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux
- 最后验证版本：3.5

## 核心命令示例
```bash
# 提交 PySpark 作业
spark-submit --master local[4] my_job.py

# 交互式 Python
pyspark

# 交互式 SQL
spark-sql

# 带资源提交 [需认证]
spark-submit --executor-memory 4G --executor-cores 2 my_job.py
```

## 适用场景
- 大规模数据处理作业提交
- 交互式数据分析和查询
- ETL 管道开发
