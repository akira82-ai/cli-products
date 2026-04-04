# Snowflake CLI (`snow`)

## 基本信息
- 官方文档：https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/overview
- 安装方式：pip install snowflake-cli
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：3.1

## 核心命令示例
```bash
# 添加连接 [需认证]
snow connection add myconn

# 执行 SQL [需认证]
snow sql -c myconn -q "SELECT * FROM my_table LIMIT 10"

# 查看 Stage [需认证]
snow stage list

# 部署 Streamlit 应用 [需认证]
snow streamlit deploy
```

## 适用场景
- Snowflake 数据仓库操作
- SQL 查询和脚本执行
- Streamlit 应用部署
