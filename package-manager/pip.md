# pip (`pip`) - Python

## 基本信息
- 官方文档：https://pip.pypa.io/en/stable/cli/
- 安装方式：随 Python 安装或 `python -m ensurepip`
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：v24.3.1

## 核心命令示例
```bash
# 安装 Python 包
pip install requests

# 安装指定版本
pip install django==5.0

# 导出依赖列表
pip freeze > requirements.txt

# 从文件批量安装依赖
pip install -r requirements.txt

# 升级已安装的包
pip install --upgrade requests

# 卸载包
pip uninstall requests
```

## 适用场景
- Python 项目依赖管理和虚拟环境配置
- 安装和管理 Python 命令行工具
- 服务器部署时批量安装依赖
