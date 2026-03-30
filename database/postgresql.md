# PostgreSQL CLI (`psql`)

## 基本信息
- 官方文档：https://www.postgresql.org/docs/current/app-psql.html
- 安装方式：brew install postgresql
- 开源：是 (PostgreSQL License)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：17.2

## 核心命令示例
```bash
# 连接数据库 [需认证]
psql -U user -h localhost -d mydb

# 列出所有表
\dt

# 列出所有用户
\du

# 执行 SQL 查询
SELECT * FROM users LIMIT 10;

# 导入 SQL 文件
\i backup.sql
```

## 适用场景
- PostgreSQL 数据库管理
- SQL 查询和数据操作
- 数据库备份和恢复
