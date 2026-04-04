#!/usr/bin/env python3
"""
搜索正确的 CLI 文档 URL
"""

import json
import subprocess
from pathlib import Path

# 读取验证报告
with open('smart_verification_report.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 筛选需要修复的产品
invalid_products = [
    r for r in data['results']
    if r['status'] in ['invalid', 'error']
]

print(f"需要修复的产品数量: {len(invalid_products)}\n")

# 生成搜索任务
print("=" * 80)
print("需要搜索正确 URL 的产品列表:")
print("=" * 80)

for i, product in enumerate(invalid_products, 1):
    print(f"{i:3}. {product['product']:30} | 当前: {product['url'][:60]}...")

# 输出到文件供批量搜索
with open('search_queries.txt', 'w', encoding='utf-8') as f:
    for product in invalid_products:
        query = f"{product['product']} CLI documentation official site"
        f.write(f"{product['product']}|{query}\n")

print(f"\n搜索查询已保存到: search_queries.txt")
