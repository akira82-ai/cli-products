# AWS SAM CLI (`sam`)

## 基本信息
- 官方文档：https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli.html
- 安装方式：`brew tap aws/tap && brew install aws-sam-cli` / `pip install aws-sam-cli`
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：待验证

## 核心命令示例
```bash
# 初始化 SAM 项目
sam init

# 构建 SAM 应用
sam build

# 本地调用 Lambda 函数 [需认证]
sam local invoke

# 引导式部署 SAM 应用 [需认证]
sam deploy --guided
```

> 需要认证凭据的命令标注 `[需认证]`。

## 适用场景
- Serverless 应用开发与构建
- 本地调试 Lambda 函数
- 部署和管理 SAM 应用
