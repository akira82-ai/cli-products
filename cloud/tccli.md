# 腾讯云 CLI (`tccli`)

## 基本信息
- 官方文档：https://cloud.tencent.com/document/product/440
- 安装方式：`pip install tccli`
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：待验证

## 核心命令示例
```bash
# 配置腾讯云凭据 [需认证]
tccli configure

# 查询 CVM 实例列表 [需认证]
tccli cvm DescribeInstances

# 列出 COS 存储桶 [需认证]
tccli cos ls

# 列出云函数 [需认证]
tccli scf ListFunctions
```

> 需要认证凭据的命令标注 `[需认证]`。

## 适用场景
- 管理腾讯云 CVM、COS、SCF 等资源
- 自动化运维和批量操作
- 脚本化云资源管理
