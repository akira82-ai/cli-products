# Skopeo CLI (`skopeo`)

## 基本信息
- 官方文档：https://github.com/containers/skopeo
- 安装方式：brew install skopeo
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux
- 最后验证版本：1.17

## 核心命令示例
```bash
# 检查远程镜像信息
skopeo inspect docker://docker.io/library/nginx:latest

# 复制镜像到本地
skopeo copy docker://nginx:latest oci:nginx:latest

# 列出镜像标签
skopeo list-tags docker://docker.io/library/nginx

# 登录镜像仓库 [需认证]
skopeo login registry.example.com
```

## 适用场景
- 容器镜像仓库操作（无需拉取完整镜像）
- 镜像在仓库间迁移和复制
- CI/CD 中镜像检查和验证
