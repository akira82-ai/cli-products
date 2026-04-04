# xcodebuild (`xcodebuild`)

## 基本信息
- 官方文档：https://developer.apple.com/library/archive/technotes/tn2339/_index.html
- 安装方式：随 Xcode 安装
- 开源：否
- 平台支持：macOS
- 最后验证版本：16.2

## 核心命令示例
```bash
# 列出可用 Scheme
xcodebuild -list

# 构建 Xcode 项目
xcodebuild -project MyApp.xcodeproj -scheme MyApp -configuration Debug build

# 运行测试 [需认证]
xcodebuild test -scheme MyApp -destination 'platform=iOS Simulator,name=iPhone 16'

# 导出 IPA [需认证]
xcodebuild -exportArchive -archivePath MyApp.xcarchive -exportOptionsPlist Export.plist
```

## 适用场景
- iOS/macOS 项目构建
- CI/CD 中自动化 Xcode 构建
- 测试和归档管理
