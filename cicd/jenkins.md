# Jenkins CLI (`jenkins-cli`)

## 基本信息
- 官方文档：https://www.jenkins.io/doc/book/managing/cli/
- 安装方式：从 Jenkins 服务器下载 `jenkins-cli.jar`
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows (需要 Java)
- 最后验证版本：—

## 核心命令示例
```bash
# 触发构建任务
java -jar jenkins-cli.jar -s <URL> build <job>

# 列出所有任务
java -jar jenkins-cli.jar list-jobs

# 查看任务控制台输出
java -jar jenkins-cli.jar console <job>
```

> 需要通过 SSH 或用户名/API Token 进行认证。

## 适用场景
- Jenkins 任务远程触发
- 构建日志查看与排查
- 批量任务管理
