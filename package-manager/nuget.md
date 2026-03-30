# NuGet CLI (`nuget`) - Microsoft

## 基本信息
- 官方文档：https://docs.microsoft.com/nuget/reference/nuget-exe-cli-reference
- 安装方式：从 https://www.nuget.org/downloads 下载 nuget.exe 或 `brew install nuget`
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：v6.12.1

## 核心命令示例
```bash
# 安装 NuGet 包
nuget install Newtonsoft.Json

# 创建 NuGet 包
nuget pack MyPackage.nuspec

# 发布包到 nuget.org [需认证]
nuget push MyPackage.1.0.0.nupkg -Source https://api.nuget.org/v3/index.json -ApiKey YOUR_API_KEY

# 添加包源
nuget sources add -Name "MyFeed" -Source https://myfeed.com/v3/index.json

# 还原项目依赖
nuget restore MySolution.sln
```

## 适用场景
- .NET 包的创建、发布和管理
- 配置私有 NuGet 源和企业包仓库
- CI/CD 流水线中的包还原和发布
