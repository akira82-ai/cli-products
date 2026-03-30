# Neo4j CLI (`cypher-shell`)

## 基本信息
- 官方文档：https://neo4j.com/docs/operations-manual/current/tools/cypher-shell/
- 安装方式：brew install neo4j
- 开源：是 (GPL-3.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：5.25

## 核心命令示例
```bash
# 连接数据库 [需认证]
cypher-shell -u neo4j -p password

# 查询所有节点
MATCH (n) RETURN n LIMIT 25

# 创建节点和关系 [需认证]
CREATE (a:Person {name: "Alice"})-[:KNOWS]->(b:Person {name: "Bob"})

# 查看所有标签
CALL db.labels()
```

## 适用场景
- 图数据库 Cypher 查询
- 节点和关系管理
- 知识图谱操作
