# Spinnaker CLI (`spin`)

## 基本信息
- 官方文档：https://spinnaker.io/docs/setup/other_config/spin/
- 安装方式：下载 `spin` 二进制文件
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux
- 最后验证版本：—

## 核心命令示例
```bash
# 列出流水线
spin pipeline list

# 列出应用
spin application list

# 执行流水线
spin pipeline execute

# 保存流水线配置
spin pipeline save
```

> 需要配置 Spinnaker Gate API 端点和认证信息。

## 适用场景
- Spinnaker 持续交付流水线管理
- 应用部署与发布编排
- 流水线配置批量管理
