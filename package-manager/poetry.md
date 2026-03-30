# Poetry (`poetry`) - Python

## 基本信息
- 官方文档：https://python-poetry.org/docs/
- 安装方式：`curl -sSL https://install.python-poetry.org | python3 -`
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：v1.8.5

## 核心命令示例
```bash
# 初始化新项目
poetry new myproject

# 交互式创建 pyproject.toml
poetry init

# 添加依赖
poetry add requests

# 添加开发依赖
poetry add --group dev pytest

# 安装所有依赖
poetry install

# 运行脚本
poetry run python main.py

# 构建并发布包 [需认证]
poetry publish --build
```

## 适用场景
- 现代化的 Python 项目依赖管理（替代 pip + venv）
- Python 包的构建和发布到 PyPI
- 精确的依赖版本锁定（poetry.lock）
