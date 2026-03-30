# PowerShell (`pwsh`)

## 基本信息
- 官方文档：https://learn.microsoft.com/powershell/
- 安装方式：brew install powershell
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：7.5

## 核心命令示例
```bash
# 执行命令
Get-Process

# 列出文件
Get-ChildItem -Path . -Recurse

# 管道操作
Get-Process | Where-Object { $_.CPU -gt 10 } | Sort-Object CPU -Descending

# 远程执行
Invoke-Command -ComputerName server01 -ScriptBlock { Get-Service }
```

## 适用场景
- 跨平台自动化脚本编写
- 系统管理和运维
- CI/CD 流水线脚本
