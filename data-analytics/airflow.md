# Apache Airflow CLI (`airflow`)

## 基本信息
- 官方文档：https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables.html
- 安装方式：pip install apache-airflow
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux
- 最后验证版本：2.10

## 核心命令示例
```bash
# 初始化数据库
airflow db init

# 启动调度器
airflow scheduler

# 列出 DAG
airflow dags list

# 触发 DAG 运行
airflow dags trigger my_dag
```

## 适用场景
- 工作流 DAG 管理和调度
- 任务依赖编排
- ETL 管道自动化
