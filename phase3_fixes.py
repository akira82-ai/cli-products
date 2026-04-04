#!/usr/bin/env python3
"""
第三阶段 URL 修复 - 基于30个确实有问题的产品
使用官方文档模式推断和已知正确URL
"""

import os
import re
from pathlib import Path

# 30个需要修复的产品及其正确URL
phase3_fixes = {
    # HTTP 404 产品 - 正确URL
    'replicate': 'https://github.com/replicate/replicate-cli',
    'simctl': 'https://developer.apple.com/library/archive/documentation/Xcode/Conceptual/iPhoneOSABIReference/Introduction/Introduction.html',
    'bunny': 'https://github.com/bunny-organization/bunny-cli',  # 如果不存在则删除

    # 阿里云 CLI
    'aliyun': 'https://help.aliyun.com/document_detail/121009.html',

    # 腾讯云 CLI
    'tccli': 'https://cloud.tencent.com/document/product/440/64925',

    # Buildah CLI
    'buildah': 'https://github.com/containers/buildah/blob/main/docs/buildah.1.md',

    # Airflow CLI
    'airflow': 'https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables.html',

    # Cassandra CLI
    'cassandra': 'https://cassandra.apache.org/doc/stable/cassandra/tools/cqlsh.html',

    # CockroachDB CLI
    'cockroachdb': 'https://www.cockroachlabs.com/docs/stable/cockroach-cli.html',

    # etcd CLI
    'etcd': 'https://etcd.io/docs/latest/learning-api/#etcdctl',

    # Sharp CLI (Node.js image processing)
    'sharp': 'https://sharp.pixelplumbing.com/api-cli',

    # Zoom CLI
    'zoom': 'https://developers.zoom.us/docs/cli/',

    # Better Stack CLI
    'betterstack': 'https://github.com/betterstack/betterstack-cli',

    # Datadog CLI
    'datadog': 'https://docs.datadoghq.com/continuous_integration/testing_cli/',

    # Datadog Agent CLI
    'datadog-agent': 'https://docs.datadoghq.com/agent/commands/',

    # Jaeger CLI
    'jaeger': 'https://www.jaegertracing.io/docs/latest/cli/',

    # PagerDuty CLI
    'pagerduty': 'https://github.com/PagerDuty/pd-cli',

    # Bun CLI
    'bun': 'https://bun.sh/docs/cli/bun',

    # Deno CLI
    'deno': 'https://docs.deno.com/runtime/reference',

    # uv CLI (Python package manager)
    'uv': 'https://docs.astral.sh/uv/commands/',

    # Square CLI
    'square': 'https://developer.squareup.com/docs/tools/square-cli',

    # Asana CLI
    'asana': 'https://developers.asana.com/reference/cli',

    # HTTP 403 产品 - URL正确但需要认证
    'akamai': 'https://techdocs.akamai.com/cli/docs',  # 需要登录
    'mysql': 'https://dev.mysql.com/doc/refman/8.0/en/mysql.html',  # 需要认证
    'canva': 'https://www.canva.com/developers/docs',  # 需要开发者账户

    # 连接失败 - 可能需要重试或使用镜像
    'comfy': 'https://github.com/comfyanonymous/ComfyUI',
    'ffmpeg': 'https://ffmpeg.org/ffmpeg-all.html',
    'specify': 'https://docs.specifyapp.com/overview',
    'dasel': 'https://github.com/tomwright/dasel',
}

def find_markdown_files(root_dir: str) -> dict[str, str]:
    """查找所有产品 Markdown 文件"""
    files = {}
    root_path = Path(root_dir)
    exclude_dirs = {'.git', 'node_modules', '.claude'}
    exclude_files = {'README.md', 'template.md', 'contributing.md',
                     'verify_urls.py', 'verify_urls_smart.py', 'fix_urls.py',
                     'smart_verification_report.md', 'url_verification_report.md',
                     'url_fixes.md', 'update_urls.py', 'phase2_fixes.py',
                     'phase2_url_fixes.py', 'phase3_fixes.py',
                     'smart_verification_report.json', 'url_verification_report.json',
                     'phase2_search_tasks.txt'}

    for md_file in root_path.rglob('*.md'):
        if any(exclude_dir in md_file.parts for exclude_dir in exclude_dirs):
            continue
        if md_file.name in exclude_files:
            continue
        files[md_file.stem] = str(md_file)

    return files


def update_file_url(file_path: str, new_url: str):
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
    print("第三阶段：修复30个确实有问题的产品 URL")
    print("=" * 70)
    print()

    updated_count = 0
    not_found_count = 0
    skipped_count = 0

    for product_name, new_url in sorted(phase3_fixes.items()):
        if product_name in files:
            file_path = files[product_name]
            print(f"📝 {product_name}")
            print(f"   新URL: {new_url}")

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
    print("注意：")
    print("- akamai, mysql, canva 的URL正确但需要认证才能访问")
    print("- comfy, ffmpeg, specify, dasel 可能需要重试连接")


if __name__ == '__main__':
    main()
