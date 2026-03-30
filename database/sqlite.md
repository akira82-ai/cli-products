# SQLite CLI (`sqlite3`)

## 基本信息
- 官方文档：https://www.sqlite.org/cli.html
- 安装方式：系统自带 / brew install sqlite
- 开源：是 (Public Domain)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：3.47

## 核心命令示例
```bash
# 打开/创建数据库
sqlite3 mydb.sqlite

# 查看所有表
.tables

# 查看表结构
.schema users

# 执行查询
SELECT * FROM users;
```

## 适用场景
- 轻量级本地数据库
- 应用数据存储和原型开发
- 数据分析和导出
