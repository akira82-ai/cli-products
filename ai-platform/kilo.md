# 百度千帆 CLI (`kilo`)

## 基本信息
- 官方文档：https://cloud.baidu.com/doc/QIANFAN/index.html
- 安装方式：pip install qianfan
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：0.4

## 核心命令示例
```bash
# 配置认证 [需认证]
kilo configure

# 模型列表 [需认证]
kilo model list

# 对话推理 [需认证]
kilo chat --model ernie-bot-4 "你好"

# 查看帮助
kilo --help
```

## 适用场景
- 百度千帆大模型平台操作
- ERNIE Bot 模型推理
- 国内 AI 平台开发
