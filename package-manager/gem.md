# gem (`gem`) - Ruby

## 基本信息
- 官方文档：https://guides.rubygems.org/command-reference/
- 安装方式：随 Ruby 安装（`brew install ruby`）
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：v3.6.3

## 核心命令示例
```bash
# 安装 Ruby Gem 包
gem install rails

# 安装指定版本
gem install sinatra -v '~> 4.0'

# 列出已安装的 Gem
gem list

# 查看 Gem 详细信息
gem info rails

# 发布 Gem 到 RubyGems.org [需认证]
gem push mygem-1.0.0.gem

# 更新所有已安装的 Gem
gem update
```

## 适用场景
- Ruby 包（Gem）的安装和管理
- 发布开源 Ruby 库到 RubyGems.org
- Rails 等框架和工具的安装
