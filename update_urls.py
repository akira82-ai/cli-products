#!/usr/bin/env python3
"""
批量更新 CLI 产品的官方文档 URL
"""

import os
import re
from pathlib import Path

# 已验证的正确 URL 映射
verified_urls = {
    # AI Agent
    'claude-code': 'https://code.claude.com/docs/en/overview',

    # CICD
    'argocd': 'https://argo-cd.readthedocs.io/en/latest/user-guide/commands/argocd/',

    # Database
    'redis': 'https://redis.io/docs/latest/develop/tools/cli/',

    # Data Analytics
    'snowflake': 'https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/overview',

    # Testing
    'playwright': 'https://playwright.dev/docs/test-cli',

    # Static Site
    'astro': 'https://docs.astro.build/en/reference/cli-reference/',

    # Payment
    'shopify': 'https://shopify.dev/docs/api/shopify-cli',

    # Container
    'helm': 'https://helm.sh/docs/helm/',
}

# 基于官方文档的建议 URL（高置信度）
suggested_urls = {
    # Cloud
    'aws': 'https://docs.aws.amazon.com/cli/latest/userguide/',
    'cdk': 'https://docs.aws.amazon.com/cdk/v2/guide/cli.html',
    'sam': 'https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli.html',
    'az': 'https://learn.microsoft.com/en-us/cli/azure/',
    'gcloud': 'https://cloud.google.com/sdk/docs/install',
    'aliyun': 'https://help.aliyun.com/document/detail/110302.html',
    'tccli': 'https://cloud.tencent.com/document/product/440/64925',

    # Database
    'mongodb': 'https://www.mongodb.com/docs/mongodb-shell/',
    'etcd': 'https://etcd.io/docs/latest/learning-api/#etcdctl',
    'neo4j': 'https://neo4j.com/docs/operations-manual/current/cypher-shell/',
    'cockroachdb': 'https://www.cockroachlabs.com/docs/stable/build-a-cockroachdb-app.html',

    # Container
    'docker': 'https://docs.docker.com/engine/reference/commandline/docker/',
    'docker-compose': 'https://docs.docker.com/compose/reference/',
    'podman': 'https://docs.podman.io/en/latest/Commands.html',
    'minikube': 'https://minikube.sigs.k8s.io/docs/commands/',
    'buildah': 'https://github.com/containers/buildah/blob/main/buildah.1.md',

    # Monitoring
    'datadog': 'https://docs.datadoghq.com/continuous_integration/testing_cli/',
    'newrelic': 'https://developer.newrelic.com/automate-workflows/get-started/new-relic-cli/',
    'sentry': 'https://docs.sentry.io/cli/',

    # Version Control
    'git': 'https://git-scm.com/docs/git',

    # Package Manager
    'npm': 'https://docs.npmjs.com/cli-documentation/',
    'yarn': 'https://yarnpkg.com/cli',
    'pnpm': 'https://pnpm.io/cli/add',
    'bun': 'https://bun.sh/docs/cli/bun',
    'deno': 'https://docs.deno.com/runtime/reference',
    'cargo': 'https://doc.rust-lang.org/cargo/commands/',
    'pip': 'https://pip.pypa.io/en/stable/cli/',

    # Dev Utility
    'jq': 'https://jqlang.github.io/jq/manual/',
    'yq': 'https://mikefarah.gitbook.io/yq/',
    'ffmpeg': 'https://ffmpeg.org/ffmpeg.html',

    # Project Management
    'linear': 'https://linear.app/docs',
    'asana': 'https://developers.asana.com/reference/cli',
}


def find_markdown_files(root_dir: str) -> dict[str, str]:
    """查找所有产品 Markdown 文件"""
    files = {}
    root_path = Path(root_dir)
    exclude_dirs = {'.git', 'node_modules', '.claude'}
    exclude_files = {'README.md', 'template.md', 'contributing.md',
                     'verify_urls.py', 'verify_urls_smart.py', 'fix_urls.py',
                     'smart_verification_report.md', 'url_verification_report.md',
                     'url_fixes.md', 'update_urls.py'}

    for md_file in root_path.rglob('*.md'):
        if any(exclude_dir in md_file.parts for exclude_dir in exclude_dirs):
            continue
        if md_file.name in exclude_files:
            continue
        # 使用文件名作为 key（不含扩展名）
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
        print(f"  ❌ 错误: {e}")
        return False, None


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    files = find_markdown_files(script_dir)

    print("=" * 70)
    print("批量更新 CLI 产品官方文档 URL")
    print("=" * 70)
    print()

    # 合并所有 URL 映射
    all_urls = {**verified_urls, **suggested_urls}

    updated_count = 0
    not_found_count = 0
    skipped_count = 0

    for product_name, new_url in sorted(all_urls.items()):
        if product_name in files:
            file_path = files[product_name]
            print(f"📝 {product_name}")

            success, old_url = update_file_url(file_path, new_url)
            if success:
                print(f"  ✅ 已更新")
                print(f"     旧: {old_url[:70]}...")
                print(f"     新: {new_url[:70]}...")
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


if __name__ == '__main__':
    main()
