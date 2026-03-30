# HTTPie (`http`)

## 基本信息
- 官方文档：https://httpie.io/docs/cli
- 安装方式：brew install httpie
- 开源：是 (BSD-3-Clause)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：3.2

## 核心命令示例
```bash
# 发送 GET 请求
http GET https://api.example.com/users

# 发送 POST 请求
http POST https://api.example.com/users name=Alice age:=30

# 发送 JSON
http PUT https://api.example.com/users/1 Content-Type:application/json < data.json

# 下载文件
http --download https://example.com/file.zip
```

## 适用场景
- HTTP API 调试和测试
- 友好的 JSON 请求响应展示
- 替代 curl 的便捷 HTTP 客户端
