#!/usr/bin/env python3
"""
自动更新所有分类的 README 和主 README
"""

import os
import re
from pathlib import Path
from collections import defaultdict

# 分类说明
CATEGORY_DESCRIPTIONS = {
    'ai-agent': 'AI 编程代理',
    'ai-platform': 'AI 模型平台',
    'big-tech': '大厂工具套件',
    'cdn-network': 'CDN/网络',
    'cicd': 'CI/CD',
    'cloud': '云服务商',
    'container': '容器/编排',
    'data-analytics': '数据分析',
    'database': '数据库',
    'design-media': '设计/媒体',
    'dev-platform': '开发者平台',
    'dev-utility': '开发者实用工具',
    'docs-tool': '文档工具',
    'email-marketing': '邮件/营销',
    'hashicorp': 'HashiCorp 套件',
    'iac': '基础设施即代码',
    'messaging': '即时通讯',
    'monitoring': '监控/可观测',
    'package-manager': '包管理器/运行时',
    'payment': '支付/电商',
    'project-management': '项目管理',
    'security': '安全/密钥',
    'static-site': '静态站点/框架',
    'testing': '测试工具',
    'version-control': '版本控制',
}

def scan_products():
    """扫描所有产品文件"""
    products_by_category = defaultdict(list)

    exclude_dirs = {'.git', '.claude', 'node_modules'}
    exclude_files = {'README.md', 'template.md', 'contributing.md',
                     'verify_urls.py', 'verify_urls_smart.py', 'verify_urls_smart_v2.py',
                     'fix_urls.py', 'smart_verification_report.md', 'smart_verification_report_v2.md',
                     'url_verification_report.md', 'url_fixes.md', 'update_urls.py',
                     'phase2_fixes.py', 'phase2_url_fixes.py', 'phase3_fixes.py', 'phase4_fixes.py',
                     'smart_verification_report.json', 'smart_verification_report_v2.json', 'url_verification_report.json',
                     'phase2_search_tasks.txt', 'update_readme.py'}

    root_path = Path('.')
    for md_file in root_path.rglob('*.md'):
        if any(exclude_dir in md_file.parts for exclude_dir in exclude_dirs):
            continue
        if md_file.name in exclude_files:
            continue
        if md_file.parent == root_path:
            continue

        category = md_file.parts[-2]
        products_by_category[category].append(md_file)

    return products_by_category

def get_product_info(md_file):
    """从产品文件中提取信息"""
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 提取产品名称
        name_match = re.search(r'^# (.+?)\s*\(`', content, re.MULTILINE)
        product_name = name_match.group(1).strip() if name_match else md_file.stem

        # 提取命令
        cmd_match = re.search(r'\(`(.+?)`\)', content[:200])
        command = cmd_match.group(1).strip() if cmd_match else ''

        # 提取简短说明（从"适用场景"中提取第一项）
        desc_match = re.search(r'## 适用场景\s*\n-\s*(.+)', content)
        if desc_match:
            description = desc_match.group(1).strip()[:60]
        else:
            description = ''

        return {
            'name': product_name,
            'command': command,
            'file': md_file.name,
            'description': description
        }
    except Exception as e:
        return {
            'name': md_file.stem,
            'command': '',
            'file': md_file.name,
            'description': ''
        }

def update_category_readme(category, products, description):
    """更新分类 README"""
    readme_path = Path(category) / 'README.md'

    # 按文件名排序
    sorted_products = sorted(products, key=lambda x: x.name)

    content = f"# {description}\n\n"
    content += f"共收录 {len(sorted_products)} 个 CLI 工具。\n\n"
    content += "## 工具列表\n\n"
    content += "| 工具 | 命令 | 说明 |\n"
    content += "|------|------|------|\n"

    for product in sorted_products:
        info = get_product_info(product)
        cmd = info['command'] if info['command'] else ''
        desc = info['description'] if info['description'] else ''
        content += f"| [{info['name']}]({info['file']}) | `{cmd}` | {desc} |\n"

    # 写入文件
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return len(sorted_products)

def update_main_readme(products_by_category):
    """更新主 README"""
    readme_path = Path('README.md')

    content = "# CLI Products Collection\n\n"
    content += f"> 全面收集国内外提供 CLI 能力的产品工具，涵盖 {len(products_by_category)} 个分类、{sum(len(p) for p in products_by_category.values())}+ 个工具。\n\n"
    content += "## 分类目录\n\n"
    content += "| 分类 | 目录 | 工具数 | 说明 |\n"
    content += "|------|------|--------|------|\n"

    # 按工具数量排序
    sorted_categories = sorted(products_by_category.items(), key=lambda x: -len(x[1]))

    for category, products in sorted_categories:
        desc = CATEGORY_DESCRIPTIONS.get(category, category)
        content += f"| {desc} | [{category}/]({category}/) | {len(products)} | |\n"

    content += "\n## 贡献指南\n\n"
    content += "欢迎贡献新的 CLI 工具！请阅读 [contributing.md](contributing.md) 了解如何参与。\n\n"
    content += "## License\n\n"
    content += "MIT License\n"

    # 写入文件
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    print("=" * 70)
    print("更新所有分类 README 和主 README")
    print("=" * 70)
    print()

    # 扫描所有产品
    products_by_category = scan_products()

    # 更新每个分类的 README
    updated_count = 0
    for category, products in sorted(products_by_category.items()):
        description = CATEGORY_DESCRIPTIONS.get(category, category)
        count = update_category_readme(category, products, description)
        print(f"✅ {category:25} | {count:3} 个产品")
        updated_count += 1

    print()
    print(f"已更新 {updated_count} 个分类的 README")

    # 更新主 README
    update_main_readme(products_by_category)
    print(f"✅ 已更新主 README")

    print()
    print("=" * 70)
    print("更新完成！")
    print("=" * 70)
    print(f"总产品数: {sum(len(p) for p in products_by_category.values())}")
    print(f"分类数: {len(products_by_category)}")

if __name__ == '__main__':
    main()
