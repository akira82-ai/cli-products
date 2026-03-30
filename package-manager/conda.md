# conda (`conda`) - Anaconda

## 基本信息
- 官方文档：https://docs.conda.io/projects/conda/
- 安装方式：从 https://www.anaconda.com/ 安装 Anaconda 或 Miniconda
- 开源：是 (BSD-3-Clause)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：v24.11.0

## 核心命令示例
```bash
# 创建新的虚拟环境
conda create -n myproject python=3.12

# 激活环境
conda activate myproject

# 安装包（支持 Python 和非 Python 包）
conda install numpy pandas matplotlib

# 列出所有环境
conda env list

# 导出环境配置
conda env export > environment.yml

# 从配置文件创建环境
conda env create -f environment.yml
```

## 适用场景
- 数据科学和机器学习环境管理
- 管理 Python 多版本共存和虚拟环境
- 安装科学计算相关的 C/Fortran 依赖库
