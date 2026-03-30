# Apache Flink CLI (`flink`)

## 基本信息
- 官方文档：https://flink.apache.org/docs/
- 安装方式：brew install flink
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux
- 最后验证版本：1.20

## 核心命令示例
```bash
# 提交流处理作业 [需认证]
flink run -c com.example.MyJob my-flink-job.jar

# 列出运行中的作业
flink list --running

# 取消作业 [需认证]
flink cancel jobid

# 查看作业信息
flink info jarfile
```

## 适用场景
- 流处理作业提交和管理
- 实时数据管道监控
- Flink 集群作业运维
