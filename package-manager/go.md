# Go (`go`) - Google

## 基本信息
- 官方文档：https://go.dev/doc/
- 安装方式：`brew install go` 或从 https://go.dev/dl/ 下载
- 开源：是 (BSD-3-Clause)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：v1.23.4

## 核心命令示例
```bash
# 初始化新模块
go mod init github.com/user/myproject

# 添加依赖
go get github.com/gin-gonic/gin

# 运行程序
go run main.go

# 构建二进制文件
go build -o myapp .

# 运行测试
go test ./...

# 格式化代码
go fmt ./...

# 整理依赖（移除未使用的）
go mod tidy
```

## 适用场景
- Go 项目的模块管理和依赖控制
- 编译构建跨平台可执行文件
- Go 工具链的统一管理（测试、格式化、文档生成）
