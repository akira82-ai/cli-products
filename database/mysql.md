# MySQL CLI (`mysql`)

## 基本信息
- 官方文档：https://dev.mysql.com/doc/refman/8.0/en/mysql.html
- 安装方式：brew install mysql
- 开源：是 (GPL-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：9.1

## 核心命令示例
```bash
# 连接数据库 [需认证]
mysql -u root -p

# 查看所有数据库
SHOW DATABASES;

# 使用数据库
USE mydb;

# 查询数据
SELECT * FROM users LIMIT 10;
```

## 适用场景
- MySQL 数据库管理
- SQL 查询和数据分析
- 数据库用户权限管理
