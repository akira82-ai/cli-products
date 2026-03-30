# Google Cloud Storage CLI (`gsutil`)

## 基本信息
- 官方文档：https://cloud.google.com/storage/docs/gsutil
- 安装方式：随 gcloud SDK 安装
- 开源：否
- 平台支持：macOS / Linux / Windows
- 最后验证版本：待验证

## 核心命令示例
```bash
# 列出存储桶中的对象 [需认证]
gsutil ls gs://my-bucket

# 上传文件到存储桶 [需认证]
gsutil cp local-file.txt gs://my-bucket/

# 创建新的存储桶 [需认证]
gsutil mb gs://my-new-bucket

# 同步本地目录到存储桶 [需认证]
gsutil rsync -r ./local-dir gs://my-bucket/backup
```

> 需要认证凭据的命令标注 `[需认证]`。

## 适用场景
- GCS 对象管理（上传、下载、删除）
- 批量文件同步和迁移
- 存储桶的创建与生命周期管理
