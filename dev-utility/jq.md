# jq (`jq`)

## 基本信息
- 官方文档：https://jqlang.github.io/jq/
- 安装方式：brew install jq
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：1.7

## 核心命令示例
```bash
# 美化 JSON 输出
cat data.json | jq .

# 提取字段
echo '{"name":"Alice","age":30}' | jq '.name'

# 过滤数组
cat users.json | jq '.[] | select(.age > 25)'

# 聚合计算
cat data.json | jq '[.[].price] | add'
```

## 适用场景
- JSON 数据处理和查询
- Shell 脚本中的 JSON 解析
- API 响应数据提取
