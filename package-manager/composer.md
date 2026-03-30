# Composer (`composer`) - PHP

## 基本信息
- 官方文档：https://getcomposer.org/doc/
- 安装方式：`brew install composer` 或从 https://getcomposer.org/ 下载
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：v2.8.4

## 核心命令示例
```bash
# 初始化新项目
composer init

# 安装所有依赖
composer install

# 添加依赖包
composer require laravel/framework

# 添加开发依赖
composer require --dev phpunit/phpunit

# 更新依赖到最新版本
composer update

# 自动加载优化
composer dump-autoload -o

# 发布包到 Packagist [需认证]
# 通过 Git 推送到 GitHub，Packagist 自动同步
```

## 适用场景
- PHP 项目依赖管理和自动加载
- Laravel、Symfony 等 PHP 框架项目搭建
- PHP 包的开发和发布到 Packagist
