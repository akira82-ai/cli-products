#!/usr/bin/env python3
"""
分类优化方案A - 激进优化
合并相关分类，创建更清晰的结构
"""

import os
import shutil
from pathlib import Path
from collections import defaultdict

# 定义新的分类结构
category_merges = {
    'ai-tools': {
        'name': 'AI工具',
        'sources': ['ai-agent', 'ai-platform'],
        'description': 'AI编程代理和模型平台'
    },
    'communication': {
        'name': '通讯工具',
        'sources': ['email-marketing', 'messaging'],
        'description': '邮件营销和即时通讯工具'
    },
    'content-creation': {
        'name': '内容创建',
        'sources': ['docs-tool', 'static-site'],
        'description': '文档工具和静态站点生成器'
    },
    'dev-tools': {
        'name': '开发工具',
        'sources': ['testing', 'project-management'],
        'description': '测试和项目管理工具'
    },
}

# 重新定义的分类
category_renames = {
    'big-tech': 'general-tools',
}

# 新分类说明
NEW_CATEGORY_DESCRIPTIONS = {
    'ai-tools': 'AI工具',
    'communication': '通讯工具',
    'content-creation': '内容创建',
    'dev-tools': '开发工具',
    'general-tools': '通用工具',
    'dev-utility': '开发者实用工具',
    'package-manager': '包管理器/运行时',
    'container': '容器/编排',
    'security': '安全/密钥',
    'cicd': 'CI/CD',
    'dev-platform': '开发者平台',
    'database': '数据库',
    'hashicorp': 'HashiCorp套件',
    'iac': '基础设施即代码',
    'cloud': '云服务商',
    'data-analytics': '数据分析',
    'version-control': '版本控制',
    'design-media': '设计/媒体',
    'monitoring': '监控/可观测',
    'payment': '支付/电商',
}

def create_new_categories():
    """创建新的分类目录"""
    print("创建新分类目录...")

    # 创建合并后的新目录
    for new_cat, info in category_merges.items():
        new_dir = Path(new_cat)
        if not new_dir.exists():
            new_dir.mkdir()
            print(f"  ✅ 创建 {new_cat}/ ({info['name']})")

    # 重命名 big-tech 为 general-tools
    old_dir = Path('big-tech')
    new_dir = Path('general-tools')
    if old_dir.exists() and not new_dir.exists():
        shutil.move(str(old_dir), str(new_dir))
        print(f"  ✅ 重命名 big-tech/ → general-tools/")

def move_products_to_new_categories():
    """移动产品文件到新分类"""
    print("\n移动产品文件...")

    for new_cat, info in category_merges.items():
        for source_cat in info['sources']:
            source_dir = Path(source_cat)
            if not source_dir.exists():
                continue

            # 移动所有 .md 文件（除了 README.md）
            for md_file in source_dir.glob('*.md'):
                if md_file.name == 'README.md':
                    continue

                dest_file = Path(new_cat) / md_file.name
                shutil.move(str(md_file), str(dest_file))
                print(f"  📝 {md_file.name} → {new_cat}/")

            # 删除旧目录（如果为空）
            if source_dir.exists():
                try:
                    source_dir.rmdir()
                    print(f"  🗑️  删除空目录 {source_cat}/")
                except:
                    print(f"  ⚠️  {source_cat}/ 不为空，保留")

def update_product_file_categories():
    """更新产品文件中的分类路径（如果需要）"""
    print("\n产品文件不需要修改（保持原有内容）")

def scan_new_structure():
    """扫描新的分类结构"""
    print("\n扫描新结构...")

    products_by_category = defaultdict(list)
    exclude_dirs = {'.git', '.claude', 'node_modules'}
    exclude_files = {'README.md', 'template.md', 'contributing.md',
                     'verify_urls.py', 'verify_urls_smart.py', 'verify_urls_smart_v2.py',
                     'fix_urls.py', 'smart_verification_report.md', 'smart_verification_report_v2.md',
                     'url_verification_report.md', 'url_fixes.md', 'update_urls.py',
                     'phase2_fixes.py', 'phase2_url_fixes.py', 'phase3_fixes.py', 'phase4_fixes.py',
                     'smart_verification_report.json', 'smart_verification_report_v2.json', 'url_verification_report.json',
                     'phase2_search_tasks.txt', 'update_readme.py', 'reorganize_categories.py'}

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

def update_all_readmes(products_by_category):
    """更新所有 README 文件"""
    print("\n更新 README 文件...")

    # 更新主 README
    update_main_readme(products_by_category)

    # 更新每个分类的 README
    for category, products in sorted(products_by_category.items()):
        description = NEW_CATEGORY_DESCRIPTIONS.get(category, category)
        update_category_readme(category, products, description)
        print(f"  ✅ {category:20} | {len(products):3} 个产品")

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

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)

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
        desc = NEW_CATEGORY_DESCRIPTIONS.get(category, category)
        content += f"| {desc} | [{category}/]({category}/) | {len(products)} | |\n"

    content += "\n## 贡献指南\n\n"
    content += "欢迎贡献新的 CLI 工具！请阅读 [contributing.md](contributing.md) 了解如何参与。\n\n"
    content += "## License\n\n"
    content += "MIT License\n"

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)

def get_product_info(md_file):
    """从产品文件中提取信息"""
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        name_match = re.search(r'^# (.+?)\s*\(`', content, re.MULTILINE)
        product_name = name_match.group(1).strip() if name_match else md_file.stem

        cmd_match = re.search(r'\(`(.+?)`\)', content[:200])
        command = cmd_match.group(1).strip() if cmd_match else ''

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
    except:
        return {
            'name': md_file.stem,
            'command': '',
            'file': md_file.name,
            'description': ''
        }

def main():
    import re
    print("=" * 70)
    print("分类优化方案A - 激进优化")
    print("=" * 70)
    print()

    # 1. 创建新分类目录
    create_new_categories()

    # 2. 移动产品文件
    move_products_to_new_categories()

    # 3. 扫描新结构
    products_by_category = scan_new_structure()

    # 4. 更新所有 README
    update_all_readmes(products_by_category)

    print()
    print("=" * 70)
    print("优化完成！")
    print("=" * 70)
    print(f"新分类数: {len(products_by_category)}")
    print(f"总产品数: {sum(len(p) for p in products_by_category.values())}")

if __name__ == '__main__':
    main()
