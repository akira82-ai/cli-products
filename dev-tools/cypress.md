# Cypress CLI (`cypress`)

## 基本信息
- 官方文档：https://docs.cypress.io/guides/guides/command-line
- 安装方式：npm install -g cypress
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：13.17

## 核心命令示例
```bash
# 打开测试运行器
cypress open

# 运行所有测试（无头模式）
cypress run

# 运行指定测试文件
cypress run --spec "cypress/e2e/login.cy.js"

# 录制测试
cypress run --record [需认证]
```

## 适用场景
- Web 应用端到端测试
- 自动化回归测试
- 测试录制和重放
