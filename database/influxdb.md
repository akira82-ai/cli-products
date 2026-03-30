# InfluxDB CLI (`influx`)

## 基本信息
- 官方文档：https://docs.influxdata.com/influxdb/v2/tools/influx-cli/
- 安装方式：brew install influxdb-cli
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：2.7

## 核心命令示例
```bash
# 初始化配置
influx setup

# 写入数据 [需认证]
influx write --bucket mybucket "temperature,location=beijing value=23.5"

# 查询数据 [需认证]
influx query 'from(bucket:"mybucket") |> range(start: -1h)'

# 查看 bucket 列表
influx bucket list
```

## 适用场景
- 时序数据写入和查询
- InfluxDB bucket 和组织管理
- IoT 和监控数据存储
