# Hugging Face CLI (`huggingface-cli` / `hf`)

## 基本信息
- 官方文档：https://huggingface.co/docs/huggingface_hub/cli
- 安装方式：pip install huggingface_hub
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：0.27

## 核心命令示例
```bash
# 登录 [需认证]
huggingface-cli login

# 下载模型
huggingface-cli download meta-llama/Llama-3.1-8B

# 上传文件到仓库 [需认证]
huggingface-cli upload username/repo local_file remote_path

# 创建新仓库 [需认证]
hf repo create username/model-name
```

## 适用场景
- AI 模型下载和上传
- Hugging Face Hub 仓库管理
- 模型和数据集版本管理
