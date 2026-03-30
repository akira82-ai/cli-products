# Vagrant CLI (`vagrant`)

## 基本信息
- 官方文档：https://developer.hashicorp.com/vagrant/docs
- 安装方式：brew install vagrant
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：2.4

## 核心命令示例
```bash
# 初始化 Vagrantfile
vagrant init ubuntu/jammy64

# 启动虚拟机
vagrant up

# SSH 进入虚拟机
vagrant ssh

# 销毁虚拟机
vagrant destroy
```

## 适用场景
- 可复现的开发环境
- 多平台虚拟机管理
- 团队开发环境标准化
