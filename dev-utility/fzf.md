# fzf (`fzf`)

## 基本信息
- 官方文档：https://github.com/junegunn/fzf
- 安装方式：brew install fzf
- 开源：是 (MIT)
- 平台支持：macOS / Linux
- 最后验证版本：0.56

## 核心命令示例
```bash
# 模糊搜索文件
fzf

# 搜索并打开文件
vim $(fzf)

# 搜索目录历史
cd $(fzf)

# 搜索 Git 分支
git branch | fzf
```

## 适用场景
- 模糊搜索和快速导航
- 命令行效率提升
- 与其他工具管道组合
