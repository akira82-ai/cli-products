# AWS CDK CLI (`cdk`)

## 基本信息
- 官方文档：https://docs.aws.amazon.com/cdk/v2/guide/cli.html
- 安装方式：`npm install -g aws-cdk`
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：待验证

## 核心命令示例
```bash
# 初始化 CDK 项目
cdk init app --language typescript

# 合成 CloudFormation 模板
cdk synth

# 部署 CDK 堆栈 [需认证]
cdk deploy

# 销毁 CDK 堆栈 [需认证]
cdk destroy
```

> 需要认证凭据的命令标注 `[需认证]`。

## 适用场景
- 用代码定义基础设施（Infrastructure as Code）
- CDK 应用生命周期管理（初始化、构建、部署、销毁）
- 生成和审查 CloudFormation 模板
