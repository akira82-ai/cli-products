#!/usr/bin/env python3
"""
第二阶段 URL 修复 - 基于 68 个无效/不匹配的产品
"""

import json
from pathlib import Path

# 读取最新验证报告
with open('smart_verification_report.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 筛选需要修复的产品
invalid_products = [r for r in data['results'] if r['status'] in ['invalid', 'error']]

print(f"需要修复的产品: {len(invalid_products)}\n")
print("=" * 80)

# 按分类整理
products_by_category = {}
for product in invalid_products:
    if product['product'] in ['smart_verification_report', 'url_fixes', 'url_verification_report']:
        continue

    # 从文件路径推断分类
    file_path = product.get('file', '')
    if '/' in file_path:
        category = file_path.split('/')[0]
    else:
        category = 'other'

    if category not in products_by_category:
        products_by_category[category] = []

    products_by_category[category].append({
        'name': product['product'],
        'current_url': product['url'],
        'status': product['message'],
        'file': file_path
    })

# 输出分类列表
for category, products in sorted(products_by_category.items()):
    print(f"\n## {category.upper()} ({len(products)} 个)")
    for p in products:
        print(f"  - {p['name']:30} | {p['status']}")

# 生成搜索任务文件
with open('phase2_search_tasks.txt', 'w', encoding='utf-8') as f:
    f.write("# 第二阶段 URL 搜索任务\n\n")
    for category, products in sorted(products_by_category.items()):
        f.write(f"## {category}\n\n")
        for p in products:
            f.write(f"- [{p['name']}]({p['current_url']}) - {p['status']}\n")
        f.write("\n")

print(f"\n\n搜索任务已保存到: phase2_search_tasks.txt")
