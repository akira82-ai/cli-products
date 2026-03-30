# rclone (`rclone`)

## 基本信息
- 官方文档：https://rclone.org/docs/
- 安装方式：brew install rclone
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：1.69

## 核心命令示例
```bash
# 列出远程存储
rclone lsd remote:

# 复制文件 [需认证]
rclone copy /local/path remote:bucket

# 同步目录 [需认证]
rclone sync /local/path remote:bucket

# 挂载远程存储
rclone mount remote:bucket /mnt/remote
```

## 适用场景
- 云存储同步和备份
- 多云存储统一管理
- S3/GCS/Azure Blob 等互操作
