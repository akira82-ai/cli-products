# yq (`yq`)

## 基本信息
- 官方文档：https://mikefarah.gitbook.io/yq/
- 安装方式：brew install yq
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：4.45

## 核心命令示例
```bash
# 读取 YAML 字段
yq '.database.host' config.yaml

# 更新字段
yq -i '.database.port = 5432' config.yaml

# YAML 转 JSON
yq -o=json config.yaml

# 合并文件
yq ea -a '.[]' file1.yaml file2.yaml
```

## 适用场景
- YAML/TOML/JSON 文件处理
- 配置文件批量修改
- 格式转换
