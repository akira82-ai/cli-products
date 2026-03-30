# uv (`uv`) - Astral

## 基本信息
- 官方文档：https://docs.astral.sh/uv/
- 安装方式：`curl -LsSf https://astral.sh/uv/install.sh | sh` 或 `brew install uv`
- 开源：是 (MIT / Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：v0.5.11

## 核心命令示例
```bash
# 创建新项目
uv init myproject

# 添加依赖
uv add requests

# 安装所有依赖
uv sync

# 运行 Python 脚本（自动安装依赖）
uv run main.py

# 管理Python版本
uv python install 3.12

# 从 requirements.txt 安装
uv pip install -r requirements.txt

# 发布包 [需认证]
uv publish
```

## 适用场景
- 极速 Python 包安装和管理（Rust 编写，比 pip 快 10-100 倍）
- 替代 pip、pip-tools、poetry、pyenv 等多个工具
- 统一管理 Python 版本和项目依赖
