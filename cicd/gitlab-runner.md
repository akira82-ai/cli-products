# GitLab Runner CLI (`gitlab-runner`)

## 基本信息
- 官方文档：https://docs.gitlab.com/runner/
- 安装方式：`brew install gitlab-runner`
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：—

## 核心命令示例
```bash
# 注册 Runner
gitlab-runner register

# 运行 Runner
gitlab-runner run

# 列出已注册的 Runner
gitlab-runner list

# 验证 Runner 连接
gitlab-runner verify
```

> `gitlab-runner register` 需提供 GitLab 实例 URL 和 Registration Token。

## 适用场景
- GitLab CI Runner 注册与配置
- Runner 运行状态管理
- CI/CD 构建节点运维
