# Grafana CLI (`grafanactl`)

## 基本信息
- 官方文档：https://grafana.com/docs/grafana/latest/cli
- 安装方式：Grafana 自带，或从 GitHub Releases 下载
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：11.5.0

## 核心命令示例
```bash
# 查看服务器管理员设置 [需认证]
grafana-cli admin show-settings

# 安装插件
grafana-cli plugins install grafana-clock-panel

# 重置管理员密码 [需认证]
grafana-cli admin reset-admin-password new-password
```

## 适用场景
- 管理 Grafana 插件的安装、更新和卸载
- 自动化 Grafana 实例的初始配置和密码管理
- CI/CD 中批量导出/导入 Dashboard
