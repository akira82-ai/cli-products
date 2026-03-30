# Apache Kafka CLI

## 基本信息
- 官方文档：https://kafka.apache.org/documentation/
- 安装方式：brew install kafka
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux
- 最后验证版本：3.9

## 核心命令示例
```bash
# 创建 Topic
kafka-topics --create --topic my-topic --bootstrap-server localhost:9092

# 生产消息
kafka-console-producer --topic my-topic --bootstrap-server localhost:9092

# 消费消息
kafka-console-consumer --topic my-topic --from-beginning --bootstrap-server localhost:9092

# 查看消费者组
kafka-consumer-groups --list --bootstrap-server localhost:9092
```

## 适用场景
- 消息队列 Topic 管理
- 生产消费消息调试
- 消费者组监控
