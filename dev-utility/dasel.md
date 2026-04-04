# Dasel (`dasel`)

## 基本信息
- 官方文档：https://github.com/tomwright/dasel
- 安装方式：brew install dasel
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：2.8

## 核心命令示例
```bash
# 从 JSON 中查询字段
dasel select -f data.json '.name'

# 修改 JSON 中的字段值
dasel put -f data.json '.age' 30

# YAML 转 JSON
dasel -r yaml -w json < input.yaml

# 查看帮助
dasel --help
```

## 适用场景
- JSON/YAML/TOML/XML 通吃的数据处理器
- 配置文件格式转换
- 统一数据查询和修改
