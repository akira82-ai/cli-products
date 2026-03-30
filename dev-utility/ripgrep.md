# ripgrep (`rg`)

## 基本信息
- 官方文档：https://github.com/BurntSushi/ripgrep
- 安装方式：brew install ripgrep
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：14.1

## 核心命令示例
```bash
# 递归搜索
rg "pattern"

# 指定文件类型
rg "TODO" --type py

# 正则搜索
rg "function\s+\w+"

# 显示行号和上下文
rg "error" -C 3
```

## 适用场景
- 代码内容搜索（比 grep 快）
- 大型代码库搜索
- 正则表达式匹配
