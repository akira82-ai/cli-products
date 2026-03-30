# Ansible CLI (`ansible`)

## 基本信息
- 官方文档：https://docs.ansible.com/ansible/latest/command_guide/index.html
- 安装方式：pip install ansible
- 开源：是 (GPL-3.0)
- 平台支持：macOS / Linux
- 最后验证版本：2.18

## 核心命令示例
```bash
# 执行 Playbook
ansible-playbook site.yml

# Ping 所有主机
ansible all -m ping

# 安装 Galaxy 角色
ansible-galaxy install geerlingguy.docker

# 加密敏感数据
ansible-vault encrypt secrets.yml
```

## 适用场景
- 批量服务器配置管理
- 自动化运维和应用部署
- 配置文件和密钥管理
