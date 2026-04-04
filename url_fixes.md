# CLI 产品网址修复清单

基于智能验证报告和网络搜索，这里是所有需要修复的产品及其正确的 CLI 文档 URL。

## 已通过搜索验证的正确 URL

| 产品 | 当前（错误）URL | 正确 URL | 状态 |
|------|----------------|----------|------|
| Claude Code CLI | `https://docs.anthropic.com/en/docs/claude-code` | `https://code.claude.com/docs/en/overview` | ✅ 已验证 |
| Cline CLI | `https://github.com/cline/cline` | `https://github.com/cline/cline` | ✅ 已验证 |
| ArgoCD CLI | `https://argo-cd.readthedocs.io/en/stable/user-guide/commands/` | `https://argo-cd.readthedocs.io/en/latest/user-guide/commands/argocd/` | ✅ 已验证 |
| Redis CLI | `https://redis.io/docs/ui/cli/` | `https://redis.io/docs/latest/develop/tools/cli/` | ✅ 已验证 |
| Snowflake CLI | `https://docs.snowflake.com/en/user-guide/snowcli` | `https://docs.snowflake.com/en/en/developer-guide/snowflake-cli/command-reference/overview` | ✅ 已验证 |
| Playwright CLI | `https://playwright.dev/docs/cli` | `https://playwright.dev/docs/test-cli` | ✅ 已验证 |
| Astro CLI | `https://docs.astro.build/en/reference/cli/` | `https://docs.astro.build/en/reference/cli-reference/` | ✅ 已验证 |
| Shopify CLI | `https://shopify.dev/docs/shopify-cli` | `https://shopify.dev/docs/api/shopify-cli` | ✅ 已验证 |
| Kubernetes CLI (kubectl) | `https://kubernetes.io/docs/reference/kubectl/` | `https://kubernetes.io/docs/reference/kubectl/` | ✅ 已验证（URL正确） |
| Helm CLI | `https://helm.sh/docs/` | `https://helm.sh/docs/helm/` | ✅ 已验证 |

## 基于官方文档的正确 URL（需要验证）

### 云服务类
| 产品 | 当前（错误）URL | 建议正确 URL |
|------|----------------|-------------|
| AWS CLI | `https://docs.aws.amazon.com/cli/` | `https://docs.aws.amazon.com/cli/latest/userguide/` |
| AWS CDK CLI | `https://docs.aws.amazon.com/cdk/` | `https://docs.aws.amazon.com/cdk/v2/guide/cli.html` |
| AWS SAM CLI | `https://docs.aws.amazon.com/serverless-application-model/` | `https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli.html` |
| Azure CLI | `https://learn.microsoft.com/cli/azure/` | `https://learn.microsoft.com/en-us/cli/azure/` |
| Google Cloud CLI | `https://cloud.google.com/cli` | `https://cloud.google.com/sdk/docs/install` |
| 阿里云 CLI | `https://help.aliyun.com/product/29991.html` | `https://help.aliyun.com/document/detail/110302.html` |
| 腾讯云 CLI | `https://cloud.tencent.com/document/product/440` | `https://cloud.tencent.com/document/product/440/64925` |

### 数据库类
| 产品 | 当前（错误）URL | 建议正确 URL |
|------|----------------|-------------|
| MySQL CLI | `https://dev.mysql.com/doc/refman/8.0/en/mysql.html` | `https://dev.mysql.com/doc/refman/8.0/en/mysql.html`（URL正确，需要验证内容） |
| PostgreSQL CLI | `https://www.postgresql.org/docs/current/app-psql.html` | `https://www.postgresql.org/docs/current/app-psql.html`（正确） |
| MongoDB CLI | `https://www.mongodb.com/docs/mongodb-shell` | `https://www.mongodb.com/docs/mongodb-shell/` |
| etcd CLI | `https://etcd.io/docs/latest/` | `https://etcd.io/docs/latest/learning-api/#etcdctl` |
| Neo4j CLI | `https://neo4j.com/docs/operations-manual/current/tools/cypher-shell/` | `https://neo4j.com/docs/operations-manual/current/cypher-shell/` |
| Cassandra CLI | `https://cassandra.apache.org/doc/latest/cassandra/tools/cqlsh.html` | `https://cassandra.apache.org/doc/latest/cassandra/tools/cqlsh.html`（404）|
| CockroachDB CLI | `https://www.cockroachlabs.com/docs/` | `https://www.cockroachlabs.com/docs/stable/build-a-cockroachdb-app.html` |

### 容器与编排
| 产品 | 当前（错误）URL | 建议正确 URL |
|------|----------------|-------------|
| Docker CLI | `https://docs.docker.com/engine/reference/commandline/cli/` | `https://docs.docker.com/engine/reference/commandline/docker/` |
| Docker Compose CLI | `https://docs.docker.com/compose/` | `https://docs.docker.com/compose/reference/` |
| Podman CLI | `https://podman.io/docs` | `https://docs.podman.io/en/latest/Commands.html` |
| Minikube | `https://minikube.sigs.k8s.io/docs/` | `https://minikube.sigs.k8s.io/docs/commands/` |
| Buildah CLI | `https://buildah.io/` | `https://github.com/containers/buildah/blob/main/buildah.1.md` |

### 监控与可观测性
| 产品 | 当前（错误）URL | 建议正确 URL |
|------|----------------|-------------|
| Datadog CLI | `https://docs.datadoghq.com/continuous_integration/cli` | `https://docs.datadoghq.com/continuous_integration/testing_cli/` |
| New Relic CLI | `https://docs.newrelic.com/docs/tools/new-relic-cli` | `https://developer.newrelic.com/automate-workflows/get-started/new-relic-cli/` |
| Jaeger CLI | `https://www.jaegertracing.io/docs/latest/cli` | `https://www.jaegertracing.io/docs/latest/cli/`（需要验证）|
| Sentry CLI | `https://docs.sentry.io/product/cli` | `https://docs.sentry.io/cli/` |
| PagerDuty CLI | `https://github.com/PagerDuty/pd-cli` | `https://developer.pagerduty.com/docs/ZG9jOjExMDI5NTgw-pagerduty-cli` |

### 开发工具
| 产品 | 当前（错误）URL | 建议正确 URL |
|------|----------------|-------------|
| Git | `https://git-scm.com/doc` | `https://git-scm.com/docs/git` |
| VS Code CLI | `https://code.visualstudio.com/docs/editor/command-line` | `https://code.visualstudio.com/docs/editor/command-line`（正确）|
| Flutter CLI | `https://docs.flutter.dev/` | `https://docs.flutter.dev/tools/flutter/cmd` |
| React Native CLI | `https://reactnative.dev/docs/environment-setup` | `https://reactnative.dev/docs/set-up-your-environment` |

### 包管理器
| 产品 | 当前（错误）URL | 建议正确 URL |
|------|----------------|-------------|
| npm | `https://docs.npmjs.com/` | `https://docs.npmjs.com/cli-documentation/` |
| Yarn | `https://yarnpkg.com/` | `https://yarnpkg.com/cli` |
| pnpm | `https://pnpm.io/` | `https://pnpm.io/cli/add` |
| Bun | `https://bun.sh/docs` | `https://bun.sh/docs/cli/bun` |
| Deno | `https://docs.deno.com/` | `https://docs.deno.com/runtime/reference` |
| Cargo | `https://doc.rust-lang.org/cargo/` | `https://doc.rust-lang.org/cargo/commands/` |
| pip | `https://pip.pypa.io/en/stable/` | `https://pip.pypa.io/en/stable/cli/` |

### 其他工具
| 产品 | 当前（错误）URL | 建议正确 URL |
|------|----------------|-------------|
| jq | `https://jqlang.github.io/jq/` | `https://jqlang.github.io/jq/manual/` |
| yq | `https://mikefarah.gitbook.io/yq/` | `https://mikefarah.gitbook.io/yq/` |
| FFmpeg | `https://ffmpeg.org/documentation.html` | `https://ffmpeg.org/ffmpeg.html` |
| ImageMagick | `https://imagemagick.org/script/command-line-tools.php` | `https://imagemagick.org/script/command-line-tools.php`（正确）|
| ExifTool | `https://exiftool.org/` | `https://exiftool.org/`（正确）|

### 社交/通讯
| 产品 | 当前（错误）URL | 建议正确 URL |
|------|----------------|-------------|
| Discord CLI | `https://discord.com/developers/docs` | `https://discord.com/developers/docs/interactions/receiving-and-responding` |
| Telegram CLI | `https://core.telegram.org/api` | `https://core.telegram.org/bots/api` |
| 钉钉 CLI | `https://github.com/open-dingtalk/dingtalk-cli` | 需要验证 |
| 飞书 CLI | `https://open.feishu.cn/document/cli` | `https://open.feishu.cn/document/common-capabilities/single-sign-on/overview` |

### 支付/电商
| 产品 | 当前（错误）URL | 建议正确 URL |
|------|----------------|-------------|
| Stripe CLI | `https://docs.stripe.com/stripe-cli` | `https://docs.stripe.com/stripe-cli`（正确）|
| PayPal CLI | `https://developer.paypal.com/docs/api/overview/` | `https://developer.paypal.com/tools/` |
| Square CLI | `https://developer.squareup.com/docs/tools/cli` | 需要验证 |

### 项目管理
| 产品 | 当前（错误）URL | 建议正确 URL |
|------|----------------|-------------|
| Jira CLI | `https://github.com/ankitpokhrel/jira-cli` | `https://github.com/ankitpokhrel/jira-cli`（正确）|
| Linear CLI | `https://github.com/linear/linear-cli` | `https://linear.app/docs` |
| Asana CLI | `https://developers.asana.com/docs/` | `https://developers.asana.com/reference/cli` |

## 404 产品（已不存在或迁移）

| 产品 | 说明 |
|------|------|
| Bunny CLI | GitHub 仓库不存在 |
| Octopus Deploy CLI | 文档 404 |
| 通义千问 CLI | 文档 404 |
| 钉钉 CLI | GitHub 仓库不存在 |
| Better Stack CLI | 文档 404 |
| OpenTelemetry CLI | GitHub 仓库可能已归档 |
| Trello CLI | GitHub 仓库不存在 |

## 需要人工确认的产品

以下产品的 URL 可能正确，但页面内容不匹配产品名称，需要人工验证：
1. LM Studio CLI - URL 可访问但内容不匹配
2. Qwen Code CLI - GitHub 仓库存在
3. 百度千帆 CLI - URL 可能已变更
4. simctl - Apple 文档位置可能已变更
5. xcodebuild - URL 正确但验证脚本判断为不匹配
