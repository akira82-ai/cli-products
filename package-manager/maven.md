# Maven (`mvn`) - Apache

## 基本信息
- 官方文档：https://maven.apache.org/guides/
- 安装方式：`brew install maven`
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：v3.9.9

## 核心命令示例
```bash
# 从原型创建新项目
mvn archetype:generate -DgroupId=com.example -DartifactId=myapp -DarchetypeArtifactId=maven-archetype-quickstart

# 编译项目
mvn compile

# 打包（生成 JAR/WAR 文件）
mvn package

# 运行测试
mvn test

# 清理构建产物
mvn clean

# 安装到本地仓库
mvn install

# 部署到远程仓库 [需认证]
mvn deploy
```

## 适用场景
- Java 项目的标准化构建和依赖管理
- 企业级 Java 项目的构建生命周期管理
- 与 IDE（IntelliJ、Eclipse）深度集成的项目管理
