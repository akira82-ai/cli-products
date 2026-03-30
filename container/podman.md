# Podman CLI (`podman`)

## 基本信息
- 官方文档：https://podman.io/docs
- 安装方式：brew install podman
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：5.3

## 核心命令示例
```bash
# 运行容器（Rootless）
podman run -d -p 8080:80 nginx

# 构建镜像
podman build -t myapp .

# 查看 running 容器
podman ps

# 创建 Pod（类似 K8s Pod）
podman pod create --name mypod -p 8080:80
```

## 适用场景
- 无守护进程的容器运行（更安全）
- Rootless 容器运行
- Docker CLI 兼容替代方案
