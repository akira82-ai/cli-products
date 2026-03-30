# MongoDB Shell (`mongosh`)

## 基本信息
- 官方文档：https://www.mongodb.com/docs/mongodb-shell/
- 安装方式：brew install mongosh
- 开源：是 (SSPL)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：2.3

## 核心命令示例
```bash
# 连接数据库 [需认证]
mongosh "mongodb://localhost:27017"

# 查看所有数据库
show dbs

# 插入文档 [需认证]
db.users.insertOne({ name: "Alice", age: 30 })

# 查询文档
db.users.find({ age: { $gt: 25 } })
```

## 适用场景
- MongoDB 文档数据库操作
- 数据插入、查询、更新、删除
- 聚合管道和索引管理
