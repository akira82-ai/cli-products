# xq (`xq`)

## 基本信息
- 官方文档：https://github.com/sibprogrammer/xq
- 安装方式：brew install yq 或 pip install yq
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：3.4

## 核心命令示例
```bash
# 格式化输出 XML 文件
xq . file.xml

# 管道方式解析 XML
echo '<root><item>a</item></root>' | xq .root.item

# 提取纯文本值
xq -r '.root.item' file.xml

# 查看帮助
xq --help
```

## 适用场景
- XML/HTML 解析提取
- jq 的 XML 版本
- 爬网页结构化数据
