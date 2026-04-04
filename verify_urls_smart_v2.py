#!/usr/bin/env python3
"""
CLI 产品网址智能验证脚本 V2
改进：在页面内容中搜索完整的 "command line interface" 等关键词
"""

import os
import re
import html
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional
import json

@dataclass
class SmartValidationResult:
    """智能验证结果"""
    file_path: str
    product_name: str
    url: str
    status: str  # 'valid', 'invalid', 'error', 'suspicious'
    status_code: Optional[int]
    message: str
    page_title: Optional[str] = None
    confidence: float = 0.0  # 0-1 之间的置信度
    reasons: list = None  # 判断理由列表


class SmartURLValidator:
    """智能网址验证器 V2"""

    def __init__(self, timeout: int = 15, max_workers: int = 4):
        self.timeout = timeout
        self.max_workers = max_workers
        self.results = []

        # 扩展的 CLI 相关关键词 - 包含完整拼写
        self.cli_keywords = [
            # 常见缩写
            'cli', 'CLI',

            # 完整拼写
            'command line interface',
            'command-line interface',
            'command line',
            'command-line',

            # 其他变体
            'cmd', 'CMD',
            'shell', 'terminal', 'console',

            # 中文
            '命令行', '命令', '命令行工具', '命令行界面',

            # 文档相关
            'documentation', 'docs', 'reference', 'guide', 'tutorial', 'api',

            # 常见命令相关
            'commands', 'command reference', 'command syntax',
            'usage', 'options', 'flags', 'arguments', 'parameters',
        ]

        # 不相关页面特征（可能是登录页、首页等）
        self.suspicious_patterns = [
            r'login', r'sign in', r'404', r'not found', r'page not found',
            r'access denied', r'forbidden', r'登录', r'sign.up',
            r'welcome', r'home\s*page', r'landing', r'首页'
        ]

    def extract_url_from_file(self, file_path: str) -> tuple[str, str]:
        """从 Markdown 文件中提取官方文档 URL"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # 提取产品名称
                name_match = re.search(r'^# (.+?)\s*\(`', content, re.MULTILINE)
                product_name = name_match.group(1).strip() if name_match else Path(file_path).stem

                # 提取 URL
                url_match = re.search(r'- 官方文档：(https?://[^\s\]]+)', content)
                if url_match:
                    return product_name, url_match.group(1)
        except Exception as e:
            print(f"读取文件失败 {file_path}: {e}")
        return None, None

    def fetch_page_content(self, url: str) -> tuple[int, str, str]:
        """
        获取页面内容
        返回: (状态码, 响应内容, 最终URL)
        """
        try:
            req = urllib.request.Request(
                url,
                method='GET',
                headers={
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
                }
            )

            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                content = response.read().decode('utf-8', errors='ignore')
                return response.status, content, response.url

        except urllib.error.HTTPError as e:
            error_content = ''
            try:
                if e.fp:
                    error_content = e.fp.read().decode('utf-8', errors='ignore')
            except:
                pass
            return e.code, error_content, url
        except urllib.error.URLError as e:
            return 0, '', url
        except Exception as e:
            return 0, '', url

    def extract_title(self, html_content: str) -> str:
        """从 HTML 中提取标题"""
        # 尝试多种方式提取标题
        patterns = [
            r'<title[^>]*>(.*?)</title>',
            r'<h1[^>]*>(.*?)</h1>',
            r'meta\s+property="og:title"\s+content="([^"]*)"',
            r'meta\s+name="title"\s+content="([^"]*)"',
        ]

        for pattern in patterns:
            match = re.search(pattern, html_content, re.IGNORECASE | re.DOTALL)
            if match:
                title = match.group(1).strip()
                # 解码 HTML 实体并清理
                title = html.unescape(title)
                title = re.sub(r'<[^>]+>', '', title)
                title = ' '.join(title.split())
                if len(title) > 3:
                    return title[:200]

        return "无标题"

    def normalize_text(self, text: str) -> str:
        """规范化文本用于比较"""
        text = text.lower()
        text = re.sub(r'[^\w\s\-]', ' ', text)
        text = ' '.join(text.split())
        return text

    def calculate_confidence(self, product_name: str, page_title: str, page_content: str, url: str) -> tuple[float, list]:
        """
        计算置信度和判断理由 - V2 改进版
        返回: (置信度分数, 理由列表)
        """
        confidence = 0.0
        reasons = []

        # 规范化产品名称
        product_normalized = self.normalize_text(product_name)
        product_words = set(product_normalized.split())

        # 规范化页面标题
        title_normalized = self.normalize_text(page_title)
        title_words = set(title_normalized.split())

        # 规范化 URL
        url_normalized = url.lower()
        url_path = urllib.request.urlparse(url).path.lower()

        # 清理页面内容（移除HTML标签）
        content_text = re.sub(r'<[^>]+>', ' ', page_content)
        content_text = self.normalize_text(content_text[:5000])  # 只取前5000字符

        # 1. 检查页面标题中是否包含产品名称
        title_product_overlap = len(product_words & title_words)
        if title_product_overlap > 0:
            match_ratio = title_product_overlap / len(product_words)
            confidence += min(match_ratio * 0.35, 0.35)
            if match_ratio > 0.5:
                reasons.append(f"标题包含产品关键词")
            else:
                reasons.append(f"标题部分匹配 ({title_product_overlap} 个关键词)")

        # 2. 检查 URL 中是否包含产品名称
        if product_normalized.replace(' ', '-') in url_path or \
           product_normalized.replace(' ', '') in url_path or \
           any(word in url_path for word in product_words if len(word) > 3):
            confidence += 0.15
            reasons.append("URL 路径包含产品名称")

        # 3. 检查域名是否匹配
        domain = urllib.request.urlparse(url).netloc.lower()
        popular_domains = {
            'docs.github.com': ['github', 'copilot'],
            'docs.aws.amazon.com': ['aws', 'amazon'],
            'cloud.google.com': ['google', 'gcp', 'gcloud'],
            'learn.microsoft.com': ['azure', 'microsoft'],
            'redis.io': ['redis'],
            'mongodb.com': ['mongodb', 'mongo'],
            'postgres': ['postgresql', 'postgres'],
            'docker.com': ['docker'],
            'kubernetes.io': ['kubernetes', 'kubectl'],
            'nodejs.org': ['node', 'npm'],
            'python.org': ['python', 'pip'],
            'go.dev': ['go'],
            'rust-lang.org': ['rust', 'cargo'],
            'deno.land': ['deno'],
            'brew.sh': ['brew', 'homebrew'],
            'ffmpeg.org': ['ffmpeg'],
            'bun.sh': ['bun'],
        }

        for popular_domain, products in popular_domains.items():
            if popular_domain in domain and any(p in product_normalized for p in products):
                confidence += 0.15
                reasons.append(f"官方域名匹配 ({popular_domain})")
                break

        # 4. 检查页面内容是否包含 CLI 相关关键词（改进：使用完整内容）
        # 检查标题、URL和页面内容
        combined_text = (page_title + ' ' + url + ' ' + content_text).lower()

        # 统计不同类型的关键词匹配
        cli_full_matches = sum(1 for kw in ['command line interface', 'command-line interface', 'command line', 'command-line']
                               if kw in combined_text)
        cli_abbr_matches = 1 if 'cli' in combined_text else 0
        cmd_matches = sum(1 for kw in ['commands', 'command reference', 'command syntax']
                          if kw in combined_text)
        doc_matches = sum(1 for kw in ['documentation', 'docs', 'reference', 'guide']
                          if kw in combined_text)

        # 根据不同类型的关键词给予不同的权重
        if cli_full_matches > 0:
            confidence += 0.15
            reasons.append(f"页面包含 'command line interface' 相关内容")
        elif cli_abbr_matches > 0:
            confidence += 0.1
            reasons.append(f"页面包含 'CLI' 关键词")
        elif cmd_matches > 0:
            confidence += 0.08
            reasons.append(f"页面包含命令参考内容")

        if doc_matches >= 2:
            confidence += 0.05
            reasons.append(f"页面包含文档相关内容")

        # 5. 检查页面内容中是否直接提到产品名称（额外加分）
        if product_normalized in content_text:
            confidence += 0.1
            reasons.append(f"页面内容中提到产品名称")

        # 6. 检查是否是可疑页面（扣分）- 改进：更智能的判断
        # 只有当页面标题明确显示为登录/错误页面时才扣分
        title_lower = page_title.lower()
        is_suspicious = False
        for pattern in ['login', 'sign in', '404', 'not found', 'page not found', 'access denied', 'forbidden']:
            if pattern in title_lower and 'command' not in title_lower:
                is_suspicious = True
                break

        if is_suspicious:
            confidence -= 0.3
            reasons.append(f"⚠️ 页面可能不是文档页")

        # 确保置信度在 0-1 之间
        confidence = max(0.0, min(1.0, confidence))

        return confidence, reasons

    def smart_validate(self, file_path: str) -> SmartValidationResult:
        """智能验证单个文件"""
        product_name, url = self.extract_url_from_file(file_path)

        if not url:
            return SmartValidationResult(
                file_path=file_path,
                product_name=Path(file_path).stem,
                url='未找到',
                status='error',
                status_code=None,
                message='无法提取 URL',
                confidence=0.0,
                reasons=['无法从文件中提取 URL']
            )

        # 获取页面内容
        status_code, page_content, final_url = self.fetch_page_content(url)

        # 提取标题
        page_title = self.extract_title(page_content) if page_content else "无法获取内容"

        # 计算置信度
        confidence, reasons = self.calculate_confidence(product_name, page_title, page_content, final_url)

        # 判断状态
        if status_code >= 200 and status_code < 400:
            if confidence >= 0.4:  # 降低阈值从0.5到0.4
                status = 'valid'
                message = f'有效 (置信度: {confidence:.1%})'
            elif confidence >= 0.25:
                status = 'suspicious'
                message = f'需要确认 (置信度: {confidence:.1%})'
            else:
                status = 'invalid'
                message = f'内容不匹配 (置信度: {confidence:.1%})'
        elif status_code == 0:
            status = 'error'
            message = '连接失败'
            confidence = 0.0
        else:
            status = 'invalid'
            message = f'HTTP {status_code}'
            confidence = 0.0

        return SmartValidationResult(
            file_path=file_path,
            product_name=product_name,
            url=url,
            status=status,
            status_code=status_code,
            message=message,
            page_title=page_title[:100],
            confidence=confidence,
            reasons=reasons
        )

    def find_all_markdown_files(self, root_dir: str) -> list[str]:
        """递归查找所有产品 Markdown 文件"""
        md_files = []
        root_path = Path(root_dir)

        exclude_dirs = {'.git', 'node_modules', '.claude'}

        for md_file in root_path.rglob('*.md'):
            if md_file.name in ['README.md', 'template.md', 'contributing.md',
                               'verify_urls.py', 'verify_urls_smart.py', 'verify_urls_smart_v2.py',
                               'fix_urls.py', 'smart_verification_report.md', 'url_verification_report.md',
                               'url_fixes.md', 'update_urls.py', 'phase2_fixes.py',
                               'phase2_url_fixes.py', 'phase3_fixes.py', 'phase4_fixes.py',
                               'phase2_search_tasks.txt']:
                continue
            if any(exclude_dir in md_file.parts for exclude_dir in exclude_dirs):
                continue
            md_files.append(str(md_file))

        return sorted(md_files)

    def run_validation(self, root_dir: str) -> list[SmartValidationResult]:
        """运行所有文件的智能验证"""
        md_files = self.find_all_markdown_files(root_dir)
        print(f"找到 {len(md_files)} 个产品文件\n")

        results = []

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_file = {
                executor.submit(self.smart_validate, f): f
                for f in md_files
            }

            completed = 0
            for future in as_completed(future_to_file):
                completed += 1
                result = future.result()
                results.append(result)

                # 显示进度
                status_icon = {
                    'valid': '✅',
                    'invalid': '❌',
                    'error': '⚠️',
                    'suspicious': '❓'
                }.get(result.status, '❓')

                confidence_str = f" ({result.confidence:.0%})" if result.status in ['valid', 'suspicious'] else ""
                print(f"[{completed}/{len(md_files)}] {status_icon} {result.product_name}: {result.message}{confidence_str}")

        return results

    def generate_smart_report(self, results: list[SmartValidationResult], output_dir: str):
        """生成智能验证报告"""
        valid = [r for r in results if r.status == 'valid']
        suspicious = [r for r in results if r.status == 'suspicious']
        invalid = [r for r in results if r.status == 'invalid']
        errors = [r for r in results if r.status == 'error']

        # Markdown 报告
        report_path = os.path.join(output_dir, 'smart_verification_report_v2.md')
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"# CLI 产品网址智能验证报告 V2\n\n")
            f.write(f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("**改进**: 在页面内容中搜索完整的 'command line interface' 等关键词\n\n")

            f.write("## 汇总\n\n")
            f.write(f"| 指标 | 数量 | 占比 |\n")
            f.write(f"|------|------|------|\n")
            total = len(results)
            f.write(f"| ✅ 有效 | {len(valid)} | {len(valid)/total*100:.1f}% |\n")
            f.write(f"| ❓ 需要确认 | {len(suspicious)} | {len(suspicious)/total*100:.1f}% |\n")
            f.write(f"| ❌ 无效 | {len(invalid)} | {len(invalid)/total*100:.1f}% |\n")
            f.write(f"| ⚠️ 错误 | {len(errors)} | {len(errors)/total*100:.1f}% |\n")
            f.write(f"| 📊 总计 | {total} | 100% |\n\n")

            # 详细结果
            f.write("## 详细结果\n\n")

            f.write("### ✅ 有效产品\n\n")
            for r in sorted(valid, key=lambda x: -x.confidence):
                f.write(f"#### {r.product_name}\n\n")
                f.write(f"- **URL**: {r.url}\n")
                f.write(f"- **置信度**: {r.confidence:.1%}\n")
                if r.page_title:
                    f.write(f"- **页面标题**: {r.page_title}\n")
                if r.reasons:
                    f.write(f"- **判断理由**: {', '.join(r.reasons)}\n")
                f.write("\n")

            f.write("### ❓ 需要确认的产品\n\n")
            for r in sorted(suspicious, key=lambda x: -x.confidence):
                f.write(f"#### {r.product_name}\n\n")
                f.write(f"- **URL**: {r.url}\n")
                f.write(f"- **置信度**: {r.confidence:.1%}\n")
                if r.page_title:
                    f.write(f"- **页面标题**: {r.page_title}\n")
                if r.reasons:
                    f.write(f"- **判断理由**: {', '.join(r.reasons)}\n")
                f.write("\n")

            f.write("### ❌ 无效产品\n\n")
            for r in sorted(invalid, key=lambda x: x.message):
                f.write(f"#### {r.product_name}\n\n")
                f.write(f"- **URL**: {r.url}\n")
                f.write(f"- **状态**: {r.message}\n")
                if r.page_title and r.page_title != "无标题":
                    f.write(f"- **页面标题**: {r.page_title}\n")
                f.write("\n")

        # JSON 报告
        json_path = os.path.join(output_dir, 'smart_verification_report_v2.json')
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump({
                'timestamp': datetime.now().isoformat(),
                'total': len(results),
                'valid': len(valid),
                'suspicious': len(suspicious),
                'invalid': len(invalid),
                'errors': len(errors),
                'results': [
                    {
                        'product': r.product_name,
                        'url': r.url,
                        'status': r.status,
                        'message': r.message,
                        'confidence': r.confidence,
                        'page_title': r.page_title,
                        'reasons': r.reasons,
                        'file': r.file_path
                    }
                    for r in results
                ]
            }, f, ensure_ascii=False, indent=2)

        print(f"\n报告已生成: {report_path}")
        print(f"JSON 报告已生成: {json_path}")


def main():
    validator = SmartURLValidator(timeout=15, max_workers=4)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    results = validator.run_validation(script_dir)

    print()
    print("=" * 70)
    print("验证完成！")
    print("=" * 70)

    validator.generate_smart_report(results, script_dir)


if __name__ == '__main__':
    main()
