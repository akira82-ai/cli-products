# Azure CLI (`az`)

## 基本信息
- 官方文档：https://learn.microsoft.com/en-us/cli/azure/
- 安装方式：`brew install azure-cli`
- 开源：是 (MIT)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：待验证

## 核心命令示例
```bash
# 登录 Azure 账户 [需认证]
az login

# 创建虚拟机 [需认证]
az vm create --resource-group myRG --name myVM --image Ubuntu2204

# 上传文件到 Blob Storage [需认证]
az storage blob upload --account-name myaccount --container-name mycontainer --name file.txt --file ./file.txt

# 创建 Function App [需认证]
az functionapp create --resource-group myRG --consumption-plan-location eastus --runtime node --functions-version 4 --name myfuncapp
```

> 需要认证凭据的命令标注 `[需认证]`。

## 适用场景
- 管理 Azure 资源（虚拟机、存储、网络等）
- 虚拟机创建和配置
- Azure Functions 部署和管理
