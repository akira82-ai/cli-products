# Docker CLI (`docker`)

## 基本信息
- 官方文档：https://docs.docker.com/engine/reference/commandline/cli/
- 安装方式：brew install docker / apt install docker.io
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：27.4

## 核心命令示例
```bash
# 构建镜像
docker build -t myapp:latest .

# 运行容器
docker run -d -p 8080:80 --name myapp myapp:latest

# 查看运行中的容器
docker ps

# 进入容器
docker exec -it myapp sh

# 查看容器日志
docker logs -f myapp
```

## 适用场景
- 容器化应用开发和部署
- 镜像构建和管理
- 容器生命周期管理
