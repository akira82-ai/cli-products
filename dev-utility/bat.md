# Bat (`bat`)

## 基本信息
- 官方文档：https://github.com/sharkdp/bat
- 安装方式：brew install bat
- 开源：是 (Apache-2.0, MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：0.24

## 核心命令示例
```bash
# 带语法高亮查看文件
bat file.py

# 显示不可打印字符
bat -A file.py

# 对比两个文件的 Git 风格差异
bat --diff file1 file2

# 查看帮助
bat --help
```

## 适用场景
- 带语法高亮查看代码文件
- 替代 cat 阅读文件
- Git diff 集成查看
