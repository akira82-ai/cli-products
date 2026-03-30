# simctl (`simctl`)

## 基本信息
- 官方文档：https://developer.apple.com/documentation/xcode-release-notes/xcode-16-release-notes
- 安装方式：随 Xcode 安装
- 开源：否
- 平台支持：macOS
- 最后验证版本：随 Xcode 版本

## 核心命令示例
```bash
# 列出所有模拟器
xcrun simctl list devices

# 启动模拟器
xcrun simctl boot "iPhone 16"

# 安装应用到模拟器
xcrun simctl install booted /path/to/MyApp.app

# 打开模拟器应用
xcrun simctl launch booted com.example.MyApp
```

## 适用场景
- iOS 模拟器管理
- CI/CD 中自动化测试
- 应用安装和启动
