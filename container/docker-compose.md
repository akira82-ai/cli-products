# Docker Compose CLI (`docker compose`)

## 基本信息
- 官方文档：https://docs.docker.com/compose/
- 安装方式：随 Docker Desktop 安装
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：2.32

## 核心命令示例
```bash
# 启动所有服务（后台）
docker compose up -d

# 停止并删除容器
docker compose down

# 查看服务日志
docker compose logs -f

# 重新构建并启动
docker compose up -d --build
```

## 适用场景
- 多容器应用编排和本地开发
- 开发环境快速启动
- 微服务本地联调
