# Buildah CLI (`buildah`)

## 基本信息
- 官方文档：https://github.com/containers/buildah/blob/main/docs/buildah.1.md
- 安装方式：brew install buildah / apt install buildah
- 开源：是 (Apache-2.0)
- 平台支持：Linux（macOS 有限支持）
- 最后验证版本：1.38

## 核心命令示例
```bash
# 从基础镜像创建容器
buildah from ubuntu:22.04

# 复制文件到容器
buildah copy container-id ./app /app

# 在容器中执行命令
buildah run container-id -- apt-get update

# 提交为镜像
buildah commit container-id myapp:latest
```

## 适用场景
- OCI 镜像构建（无需 Docker 守护进程）
- 脚本化镜像构建流程
- 安全环境下的镜像制作
