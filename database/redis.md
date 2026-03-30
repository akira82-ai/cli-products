# Redis CLI (`redis-cli`)

## 基本信息
- 官方文档：https://redis.io/docs/ui/cli/
- 安装方式：brew install redis
- 开源：是 (BSD-3-Clause)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：7.4

## 核心命令示例
```bash
# 连接 Redis
redis-cli

# 测试连接
ping

# 设置键值
SET mykey "hello"

# 获取值
GET mykey

# 查看所有键 [需认证]
KEYS *
```

## 适用场景
- Redis 缓存操作
- 键值对管理和查询
- 性能调试和基准测试
