# Google Cloud CLI (`gcloud`)

## 基本信息
- 官方文档：https://cloud.google.com/sdk/docs
- 安装方式：`brew install google-cloud-sdk`
- 开源：否
- 平台支持：macOS / Linux / Windows
- 最后验证版本：待验证

## 核心命令示例
```bash
# 登录 Google Cloud 账户 [需认证]
gcloud auth login

# 列出 Compute Engine 实例 [需认证]
gcloud compute instances list

# 部署 Cloud Functions [需认证]
gcloud functions deploy my-function --runtime nodejs18 --trigger-http

# 部署 App Engine 应用 [需认证]
gcloud app deploy
```

> 需要认证凭据的命令标注 `[需认证]`。

## 适用场景
- 管理 GCP 资源（Compute Engine、Cloud Functions 等）
- 部署 Cloud Functions 和 App Engine 应用
- IAM 和项目管理
