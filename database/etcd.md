# etcd CLI (`etcdctl`)

## 基本信息
- 官方文档：https://etcd.io/docs/latest/
- 安装方式：brew install etcd
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux
- 最后验证版本：3.5

## 核心命令示例
```bash
# 写入键值
etcdctl put mykey "hello"

# 读取键值
etcdctl get mykey

# 删除键值
etcdctl del mykey

# 查看集群健康状态
etcdctl endpoint health
```

## 适用场景
- 分布式 KV 存储
- K8s 底层数据存储管理
- 配置中心和服务发现
