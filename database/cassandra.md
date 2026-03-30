# Cassandra CLI (`cqlsh`)

## 基本信息
- 官方文档：https://cassandra.apache.org/doc/latest/cassandra/tools/cqlsh.html
- 安装方式：随 Cassandra 安装
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：5.1

## 核心命令示例
```bash
# 连接集群
cqlsh localhost 9042

# 查看所有 Keyspace
DESCRIBE KEYSPACES;

# 使用 Keyspace
USE mykeyspace;

# 查询数据
SELECT * FROM users;
```

## 适用场景
- Cassandra CQL 操作
- 分布式数据库管理
- 大规模数据读写
