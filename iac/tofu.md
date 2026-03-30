# OpenTofu CLI (`tofu`)

## 基本信息
- 官方文档：https://opentofu.org/docs/
- 安装方式：brew install opentofu
- 开源：是 (MPL-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：1.9

## 核心命令示例
```bash
# 初始化
tofu init

# 查看执行计划
tofu plan

# 应用变更 [需认证]
tofu apply

# 销毁资源 [需认证]
tofu destroy
```

## 适用场景
- Terraform 的开源替代方案（Linux 基金会托管）
- 避免 BSL 许可证限制
- 与 Terraform 配置兼容
