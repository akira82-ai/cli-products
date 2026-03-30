# Terraform CLI (`terraform`)

## 基本信息
- 官方文档：https://developer.hashicorp.com/terraform/cli
- 安装方式：brew install terraform
- 开源：BSL（源码可见）
- 平台支持：macOS / Linux / Windows
- 最后验证版本：1.10

## 核心命令示例
```bash
# 初始化工作目录
terraform init

# 查看执行计划
terraform plan

# 应用变更 [需认证]
terraform apply

# 销毁资源 [需认证]
terraform destroy
```

## 适用场景
- 多云基础设施即代码管理
- 基础设施版本控制和审计
- 自动化基础设施变更
