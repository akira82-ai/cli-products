# Square CLI (`square`)

## 基本信息
- 官方文档：https://developer.squareup.com/docs/tools/cli
- 安装方式：`npm install -g square-cli`
- 开源：是 (Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：v2.0.0

## 核心命令示例
```bash
# 初始化 Square CLI 并设置凭据 [需认证]
square init

# 列出所有支付记录 [需认证]
square payments list

# 创建客户 [需认证]
square customers create --given-name "John" --family-name "Doe"

# 查看目录中的商品 [需认证]
square catalog list --types ITEM
```

## 适用场景
- 快速测试 Square API 端点而无需编写代码
- 管理商品目录、客户和订单数据
- 脚本化批量操作 Square 商户数据
