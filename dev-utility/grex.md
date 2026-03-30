# Grex (`grex`)

## 基本信息
- 官方文档：https://github.com/pemistahl/grex
- 安装方式：brew install grex
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：1.5

## 核心命令示例
```bash
# 从示例字符串生成正则表达式
grex abcdef aghijkl

# 从文件内容生成正则表达式
grex --min-length 3 file1 file2

# 生成带捕获组的正则表达式
grex abc123 xyz789 --with-groups

# 查看帮助
grex --help
```

## 适用场景
- 给几个示例自动生成正则表达式
- 快速构建数据验证规则
- Agent 辅助正则生成
