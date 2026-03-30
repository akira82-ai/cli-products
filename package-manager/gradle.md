# Gradle (`gradle`) - Java/Kotlin

## 基本信息
- 官方文档：https://docs.gradle.org/
- 安装方式：`brew install gradle` 或使用项目自带的 Gradle Wrapper (`./gradlew`)
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：v8.12

## 核心命令示例
```bash
# 初始化新项目
gradle init

# 构建项目
gradle build

# 运行测试
gradle test

# 运行应用
gradle bootRun

# 查看依赖树
gradle dependencies

# 清理构建产物
gradle clean

# 发布到 Maven 仓库 [需认证]
gradle publish
```

## 适用场景
- Java/Kotlin/Android 项目的构建和依赖管理
- 多模块项目的灵活构建配置（Groovy/Kotlin DSL）
- CI/CD 流水线中的自动化构建和发布
