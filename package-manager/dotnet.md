# .NET CLI (`dotnet`) - Microsoft

## 基本信息
- 官方文档：https://docs.microsoft.com/dotnet/core/tools/
- 安装方式：`brew install dotnet` 或从 https://dotnet.microsoft.com/download 安装
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：v9.0.1（SDK 9.0.102）

## 核心命令示例
```bash
# 创建新控制台项目
dotnet new console -n MyApp

# 创建 Web API 项目
dotnet new webapi -n MyApi

# 构建项目
dotnet build

# 运行项目
dotnet run

# 添加 NuGet 包
dotnet add package Newtonsoft.Json

# 运行测试
dotnet test

# 发布项目
dotnet publish -c Release -o ./publish
```

## 适用场景
- .NET/C#/F# 项目的创建、构建和发布
- 管理项目依赖和 NuGet 包
- 跨平台 .NET 应用的全生命周期管理
