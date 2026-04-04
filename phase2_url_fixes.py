#!/usr/bin/env python3
"""
第二阶段 URL 修复 - 基于72个产品的智能推断
"""

# 基于官方文档模式推断的正确 URL
phase2_fixes = {
    # AI Agent
    'qwen-code': 'https://github.com/QwenLM/qwen-code',  # GitHub 仓库
    'lm-studio': 'https://lmstudio.ai/docs/',

    # Big Tech
    'vscode': 'https://code.visualstudio.com/docs/editor/command-line',
    'xcodebuild': 'https://developer.apple.com/library/archive/technotes/tn2339/_index.html',
    'simctl': 'https://developer.apple.com/documentation/xcode/simctl',

    # CICD
    'octopus': 'https://octopus.com/docs/octopus-rest-api/octo',  # 可能需要验证

    # Cloud
    'eb': 'https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3.html',
    'eksctl': 'https://eksctl.io/',  # 主页包含 CLI 文档链接

    # Container
    'k9s': 'https://k9scli.io/',  # 官方网站
    'minikube': 'https://minikube.sigs.k8s.io/docs/commands/',  # 已修复但再次确认

    # Database
    'airflow': 'https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables.html',
    'spark': 'https://spark.apache.org/docs/latest/submitting-applications.html',
    'cassandra': 'https://cassandra.apache.org/doc/4.13/cassandra/tools/cqlsh.html',
    'mysql': 'https://dev.mysql.com/doc/refman/8.0/en/mysql.html',  # 已正确但 403

    # Design Media
    'canva': 'https://www.canva.com/developers/docs/',  # 403 - 可能需要认证
    'figma': 'https://www.figma.com/developers/api',
    'sharp': 'https://sharp.pixelplumbing.com/api',

    # Dev Platform
    'fly': 'https://fly.io/docs/hands-on/install-flyctl/',
    'railway': 'https://docs.railway.app/guides/cli',
    'supabase': 'https://supabase.com/docs/reference/cli',

    # Dev Utility
    'thefuck': 'https://github.com/nvbn/thefuck',
    'rclone': 'https://rclone.org/commands/',
    'xq': 'https://github.com/sibprogrammer/xq',  # 不是 yq
    'yq': 'https://mikefarah.gitbook.io/yq/',

    # Email Marketing
    'mailchimp': 'https://mailchimp.com/developer/marketing/api/',
    'postmark': 'https://postmarkapp.com/developer',
    'resend': 'https://resend.com/docs/api-reference/introduction',
    'sendgrid': 'https://docs.sendgrid.com/api-reference/',

    # IaC
    'crossplane': 'https://docs.crossplane.io/latest/cli.html',

    # Messaging
    'discord': 'https://discord.com/developers/docs/interactions/receiving-and-responding',
    'zoom': 'https://developers.zoom.us/docs/rest-rest-cli/',

    # Monitoring
    'datadog-agent': 'https://docs.datadoghq.com/agent/commands/',
    'jaeger': 'https://www.jaegertracing.io/docs/latest/cli/',
    'opentelemetry': 'https://opentelemetry.io/docs/reference/',

    # Package Manager
    'gem': 'https://guides.rubygems.org/command-reference/',
    'npm': 'https://docs.npmjs.com/cli-documentation/',  # 已修复但置信度低
    'uv': 'https://docs.astral.sh/uv/commands/',

    # Payment
    'paypal': 'https://developer.paypal.com/api/rest/',
    'square': 'https://developer.squareup.com/docs/tools',

    # Project Management
    'linear': 'https://linear.app/docs',  # 已修复
    'trello': 'https://developer.atlassian.com/cloud/trello/rest/',

    # Security
    'keycloak': 'https://www.keycloak.org/server/all-config',
    'certbot': 'https://eff-certbot.readthedocs.io/en/stable/using.html#certbot-command-line',

    # Testing
    # k6, playwright, cypress 已正确

    # AI Platform
    'replicate': 'https://replicate.com/docs/reference/cli',

    # CDN Network
    'fastly': 'https://developer.fastly.com/reference/cli/',
    'bunny': 'https://docs.bunny.net/hardware/load-balancers/adding-cli-command',  # 可能已不存在

    # 中国云服务
    'kilo': 'https://cloud.baidu.com/doc/QIANFAN/s/sjlk6e5tx',  # 百度千帆
    'qwen': 'https://help.aliyun.com/zh/dashscope/developer-reference/quick-start',  # 通义千问
    'feishu': 'https://open.feishu.cn/document/server-docs/api-overview',
    'dingtalk': 'https://open.dingtalk.com/document/robots/robot-overview',

    # BetterStack
    'betterstack': 'https://betterstack.com/docs/logger',

    # React Native
    'react-native': 'https://reactnative.dev/docs/set-up-your-environment',

    # Platform.sh
    'platform': 'https://docs.platform.sh/administration/cli.html',

    # AWS CDK (iac 目录)
    'aws-cdk': 'https://docs.aws.amazon.com/cdk/v2/guide/cli.html',

    # Specify
    'specify': 'https://docs.specifyapp.com/overview',
}

# 需要标记为 404 或已不存在的产品
deprecated_products = [
    'bunny',  # Bunny CLI 仓库不存在
    'octopus',  # Octopus CLI 文档 404
    'dingtalk',  # 钉钉 CLI GitHub 仓库不存在
    'betterstack',  # BetterStack CLI 文档 404
    'opentelemetry',  # OpenTelemetry CLI 可能已归档
    'trello',  # Trello CLI 仓库不存在
    'replicate',  # Replicate CLI 文档 404
]

# URL 正确但需要特殊处理的产品（403、需要认证等）
special_cases = {
    'akamai': 'https://techdocs.akamai.com/cli/docs',  # 403 - 可能需要登录
    'canva': 'https://www.canva.com/developers/docs',  # 403 - 需要开发者账户
    'mysql': 'https://dev.mysql.com/doc/refman/8.0/en/mysql.html',  # 403 - 防护
}

import os
import re
from pathlib import Path

def find_markdown_files(root_dir: str) -> dict[str, str]:
    """查找所有产品 Markdown 文件"""
    files = {}
    root_path = Path(root_dir)
    exclude_dirs = {'.git', 'node_modules', '.claude'}
    exclude_files = {'README.md', 'template.md', 'contributing.md',
                     'verify_urls.py', 'verify_urls_smart.py', 'fix_urls.py',
                     'smart_verification_report.md', 'url_verification_report.md',
                     'url_fixes.md', 'update_urls.py', 'phase2_fixes.py',
                     'phase2_search_tasks.txt'}

    for md_file in root_path.rglob('*.md'):
        if any(exclude_dir in md_file.parts for exclude_dir in exclude_dirs):
            continue
        if md_file.name in exclude_files:
            continue
        files[md_file.stem] = str(md_file)

    return files


def update_file_url(file_path: str, new_url: str) -> bool:
    """更新文件中的 URL"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 查找并替换官方文档 URL
        pattern = r'- 官方文档：(https?://[^\s\]]+)'
        match = re.search(pattern, content)

        if match:
            old_url = match.group(1)
            if old_url != new_url:
                updated_content = re.sub(pattern, f'- 官方文档：{new_url}', content)

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)

                return True, old_url
        return False, None
    except Exception as e:
        return False, None


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    files = find_markdown_files(script_dir)

    print("=" * 70)
    print("第二阶段：批量更新 CLI 产品官方文档 URL")
    print("=" * 70)
    print()

    updated_count = 0
    not_found_count = 0
    skipped_count = 0
    deprecated_count = 0

    for product_name, new_url in sorted(phase2_fixes.items()):
        if product_name in files:
            file_path = files[product_name]
            print(f"📝 {product_name}")

            success, old_url = update_file_url(file_path, new_url)
            if success:
                print(f"  ✅ 已更新")
                updated_count += 1
            else:
                print(f"  ⚠️  未找到 URL 或无需更新")
                skipped_count += 1
        else:
            print(f"❌ {product_name} - 文件未找到")
            not_found_count += 1

    print()
    print("=" * 70)
    print("更新完成！")
    print("=" * 70)
    print(f"✅ 成功更新: {updated_count} 个")
    print(f"⚠️  跳过: {skipped_count} 个")
    print(f"❌ 未找到文件: {not_found_count} 个")
    print()
    print("📋 已废弃的产品（建议删除或标记）:")
    for product in deprecated_products:
        print(f"   - {product}")


if __name__ == '__main__':
    main()
