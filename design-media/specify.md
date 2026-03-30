# Specify CLI (`specify`)

## 基本信息
- 官方文档：https://docs.specifyapp.com/
- 安装方式：`npm install -g specify-cli`
- 开源：否
- 平台支持：macOS / Linux / Windows
- 最后验证版本：v2.0.0

## 核心命令示例
```bash
# 登录 Specify 账户 [需认证]
specify login

# 从设计系统拉取最新 Token [需认证]
specify pull --repository my-design-system --output ./tokens.json

# 推送更新后的设计 Token [需认证]
specify push --repository my-design-system --input ./tokens.json

# 生成 CSS 变量文件 [需认证]
specify generate --format css-variables --output ./variables.css
```

## 适用场景
- 设计系统 Token 的版本控制和同步
- 将设计变量自动转换为代码（CSS、SCSS、JS 等）
- 多团队协作的设计系统管理
