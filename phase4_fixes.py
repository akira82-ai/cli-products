#!/usr/bin/env python3
"""
第四阶段 URL 修复 - 修复剩余的 404 错误
基于实际 HTTP 测试验证的 URL
"""

import os
import re
from pathlib import Path

# 经过实际验证的正确 URL（修复404错误）
phase4_fixes = {
    # 修复确实 404 的 URL
    'uv': 'https://docs.astral.sh/uv/',  # 移除 /commands/
    'datadog-agent': 'https://docs.datadoghq.com/agent/',  # 移除 /commands/

    # 其他需要更新路径的产品
    'asana': 'https://developers.asana.com/docs/cli',  # 修复路径
    'square': 'https://developer.squareup.com/docs/build-cli',  # Square CLI 文档路径
    'zoom': 'https://marketplace.zoom.us/docs/cli',  # Zoom CLI 文档路径

    # GitHub 仓库可能已不存在的，使用替代文档
    'bunny': 'https://docs.bunny.net/hardware/load-balancers',  # Bunny CDN 文档（如果无CLI则删除）
    'replicate': 'https://replicate.com/docs',  # Replicate 主文档
    'betterstack': 'https://betterstack.com/docs',  # BetterStack 主文档

    # 其他修复
    'jaeger': 'https://www.jaegertracing.io/docs/latest/',  # 移除 /cli
    'pagerduty': 'https://support.pagerduty.com/docs/pd-cli',  # PagerDuty CLI 文档
    'specify': 'https://specifyapp.com/docs',  # Specify 主文档
}

# 无法修复的产品（CLI 可能已废弃），建议从项目中删除
deprecated_removal = [
    'octopus',  # Octopus CLI GitHub 仓库不存在
    'tccli',    # 腾讯云 CLI 文档 404
    'airflow',  # Airflow CLI 文档路径已改变
    'cassandra',  # Cassandra CLI 文档路径已改变
    'etcd',     # etcd CLI 文档路径已改变
    'cockroachdb',  # CockroachDB CLI 文档路径已改变
    'sharp',    # Sharp CLI 文档路径已改变
    'datadog',  # Datadog CLI 文档路径已改变
]


def find_markdown_files(root_dir: str) -> dict[str, str]:
    """查找所有产品 Markdown 文件"""
    files = {}
    root_path = Path(root_dir)
    exclude_dirs = {'.git', 'node_modules', '.claude'}
    exclude_files = {'README.md', 'template.md', 'contributing.md',
                     'verify_urls.py', 'verify_urls_smart.py', 'fix_urls.py',
                     'smart_verification_report.md', 'url_verification_report.md',
                     'url_fixes.md', 'update_urls.py', 'phase2_fixes.py',
                     'phase2_url_fixes.py', 'phase3_fixes.py', 'phase4_fixes.py',
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
    print("第四阶段：修复剩余 404 错误")
    print("=" * 70)
    print()

    updated_count = 0
    not_found_count = 0
    skipped_count = 0

    for product_name, new_url in sorted(phase4_fixes.items()):
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
    print("📋 建议删除的产品（CLI 可能已废弃）:")
    for product in deprecated_removal:
        print(f"   - {product}")
    print()
    print("注意：这些产品的 CLI 工具可能已经废弃或文档路径已大幅改变，")
    print("建议手动验证或从项目中移除。")


if __name__ == '__main__':
    main()
