# Fastly CLI (`fastly`)

## 基本信息
- 官方文档：https://developer.fastly.com/reference/cli/
- 安装方式：`brew install fastly/tap/fastly`
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：—

## 核心命令示例
```bash
# 列出服务
fastly service list

# 克隆服务版本
fastly service-version clone

# 部署 Compute@Edge 项目
fastly compute deploy

# 列出日志配置
fastly logging list
```

> 需要 Fastly API Token 进行认证。

## 适用场景
- Fastly CDN 服务配置管理
- Compute@Edge 应用部署
- 日志与缓存规则管理
