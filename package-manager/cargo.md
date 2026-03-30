# Cargo (`cargo`) - Rust

## 基本信息
- 官方文档：https://doc.rust-lang.org/cargo/
- 安装方式：`curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`
- 开源：是 (MIT / Apache-2.0)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：v1.83.0（随 Rust 1.83.0）

## 核心命令示例
```bash
# 创建新项目
cargo new myproject

# 构建项目
cargo build

# 构建并运行
cargo run

# 运行测试
cargo test

# 添加依赖到 Cargo.toml
cargo add serde --features derive

# 发布包到 crates.io [需认证]
cargo publish

# 代码格式化
cargo fmt
```

## 适用场景
- Rust 项目的构建、测试和发布全生命周期管理
- crates.io 生态系统的包依赖管理
- Rust 工具链和交叉编译配置
