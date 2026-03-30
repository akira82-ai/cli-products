# Kaniko (`kaniko`)

## 基本信息
- 官方文档：https://github.com/GoogleContainerTools/kaniko
- 安装方式：Docker 镜像方式运行
- 开源：是 (Apache-2.0)
- 平台支持：Linux（容器内运行）
- 最后验证版本：1.23

## 核心命令示例
```bash
# 使用 Kaniko 执行器构建并推送
executor --dockerfile Dockerfile --context . --destination registry/myapp:latest

# 仅构建不推送
executor --dockerfile Dockerfile --context . --no-push

# 使用缓存
executor --dockerfile Dockerfile --context . --destination registry/myapp:latest --cache=true
```

## 适用场景
- CI/CD 中无需 Docker 守护进程的镜像构建
- Kubernetes Pod 内构建镜像
- 安全环境下的容器镜像构建
