# AWS CLI (`aws`)

## 基本信息
- 官方文档：https://docs.aws.amazon.com/cli/
- 安装方式：`pip install awscli` / `brew install awscli`
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：待验证

## 核心命令示例
```bash
# 配置 AWS 凭据 [需认证]
aws configure

# 列出 S3 存储桶 [需认证]
aws s3 ls

# 查询 EC2 实例列表 [需认证]
aws ec2 describe-instances

# 列出 Lambda 函数 [需认证]
aws lambda list-functions
```

> 需要认证凭据的命令标注 `[需认证]`。

## 适用场景
- 管理 AWS 资源（EC2、S3、Lambda 等）
- 自动化部署和运维脚本
- 脚本化云操作和批量资源管理
