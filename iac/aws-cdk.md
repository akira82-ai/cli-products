# AWS CDK CLI (`cdk`)

## 基本信息
- 官方文档：https://docs.aws.amazon.com/cdk/
- 安装方式：npm install -g aws-cdk
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：2.172

## 核心命令示例
```bash
# 初始化项目
cdk init app --language typescript

# 生成 CloudFormation 模板
cdk synth

# 部署 [需认证]
cdk deploy

# 查看差异
cdk diff
```

## 适用场景
- 用代码定义 AWS 基础设施
- CloudFormation 模板自动生成
- 多环境部署管理
