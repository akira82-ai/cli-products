# CloudFormation CLI (`cloudformation`)

## 基本信息
- 官方文档：https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/
- 安装方式：pip install cloudformation-cli
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：0.2

## 核心命令示例
```bash
# 部署模板 [需认证]
aws cloudformation deploy --template-file template.yaml --stack-name my-stack

# 查看堆栈状态 [需认证]
aws cloudformation describe-stacks --stack-name my-stack

# 验证模板
aws cloudformation validate-template --template-body file://template.yaml

# 删除堆栈 [需认证]
aws cloudformation delete-stack --stack-name my-stack
```

## 适用场景
- AWS 基础设施模板化管理
- 堆栈生命周期管理
- 基础设施变更追踪
