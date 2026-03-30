# CockroachDB CLI (`cockroach`)

## 基本信息
- 官方文档：https://www.cockroachlabs.com/docs/
- 安装方式：brew install cockroach
- 开源：是 (BSL)
- 平台支持：macOS / Linux
- 最后验证版本：24.2

## 核心命令示例
```bash
# 启动节点
cockroach start-single-node --insecure

# SQL 客户端
cockroach sql --insecure

# 节点状态
cockroach node status --insecure

# 创建备份 [需认证]
cockroach sql --insecure -e "BACKUP DATABASE mydb TO 's3://bucket'"
```

## 适用场景
- 分布式 SQL 数据库管理
- 集群节点运维
- 备份和恢复
