# 阿里云 CLI (`aliyun`)

## 基本信息
- 官方文档：https://help.aliyun.com/product/29991.html
- 安装方式：`brew install aliyun-cli`
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：待验证

## 核心命令示例
```bash
# 配置阿里云凭据 [需认证]
aliyun configure

# 查询 ECS 实例列表 [需认证]
aliyun ecs DescribeInstances

# 列出 OSS 存储桶 [需认证]
aliyun oss ls

# 查询容器服务集群 [需认证]
aliyun cs GET /clusters
```

> 需要认证凭据的命令标注 `[需认证]`。

## 适用场景
- 管理阿里云 ECS、OSS、CS 等资源
- 自动化运维和资源编排
- 脚本化云资源管理
