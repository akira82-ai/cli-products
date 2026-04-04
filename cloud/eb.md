# AWS EB CLI (`eb`)

## 基本信息
- 官方文档：https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3.html
- 安装方式：`pip install awsebcli`
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：待验证

## 核心命令示例
```bash
# 初始化 Elastic Beanstalk 项目 [需认证]
eb init

# 创建 EB 环境 [需认证]
eb create my-env

# 部署应用到 EB [需认证]
eb deploy

# 在浏览器中打开应用 [需认证]
eb open
```

> 需要认证凭据的命令标注 `[需认证]`。

## 适用场景
- Elastic Beanstalk 应用部署和管理
- 快速创建和切换部署环境
- Web 应用和 API 的托管部署
