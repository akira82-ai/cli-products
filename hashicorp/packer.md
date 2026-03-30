# Packer CLI (`packer`)

## 基本信息
- 官方文档：https://developer.hashicorp.com/packer/docs
- 安装方式：brew install packer
- 开源：BSL（源码可见）
- 平台支持：macOS / Linux / Windows
- 最后验证版本：1.12

## 核心命令示例
```bash
# 初始化插件
packer init .

# 构建镜像
packer build template.pkr.hcl

# 验证模板
packer validate template.pkr.hcl

# 格式化 HCL
packer fmt template.pkr.hcl
```

## 适用场景
- 多平台机器镜像自动构建
- Golden Image 制作
- AWS AMI / VMware / VirtualBox 镜像管理
