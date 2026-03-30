# TiDB CLI (`tidb`)

## 基本信息
- 官方文档：https://docs.pingcap.com/tidb/stable/
- 安装方式：curl --proto '=https' --tlsv1.2 -sSf https://tiup-mirrors.pingcap.com/install.sh | sh
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux
- 最后验证版本：8.5

## 核心命令示例
```bash
# 启动本地集群
tiup playground

# 查看集群列表
tiup cluster list

# 连接 TiDB SQL [需认证]
mysql -h 127.0.0.1 -P 4000 -u root

# 集群管理 [需认证]
tiup cluster display my-cluster
```

## 适用场景
- TiDB 分布式数据库集群管理
- HTAP（事务+分析）场景
- 集群扩缩容和运维
