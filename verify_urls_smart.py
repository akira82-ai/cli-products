#!/usr/bin/env python3
"""
CLI 产品网址智能验证脚本
不仅检查 URL 可访问性，还验证页面内容是否真的对应 CLI 产品
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
    """智能网址验证器"""

    def __init__(self, timeout: int = 15, max_workers: int = 4):
        self.timeout = timeout
        self.max_workers = max_workers
        self.results = []

        # CLI 相关关键词
        self.cli_keywords = [
            'cli', 'command line', 'command-line', 'cmd', 'shell',
            'terminal', 'console', '命令行', '命令', 'documentation',
            'docs', 'reference', 'guide', 'tutorial', 'api'
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
                # 提取产品名称 - 修复：使用贪婪匹配
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
                title = re.sub(r'<[^>]+>', '', title)  # 移除残留的 HTML 标签
                title = ' '.join(title.split())  # 规范化空格
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
        计算置信度和判断理由
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

        # 1. 检查页面标题中是否包含产品名称（最重要的指标）
        title_product_overlap = len(product_words & title_words)
        if title_product_overlap > 0:
            match_ratio = title_product_overlap / len(product_words)
            confidence += min(match_ratio * 0.4, 0.4)  # 最多贡献 0.4
            if match_ratio > 0.5:
                reasons.append(f"标题包含产品关键词")
            else:
                reasons.append(f"标题部分匹配 ({title_product_overlap} 个关键词)")

        # 2. 检查 URL 中是否包含产品名称
        if product_normalized.replace(' ', '-') in url_path or \
           product_normalized.replace(' ', '') in url_path or \
           any(word in url_path for word in product_words if len(word) > 3):
            confidence += 0.2
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
        }

        for popular_domain, products in popular_domains.items():
            if popular_domain in domain and any(p in product_normalized for p in products):
                confidence += 0.15
                reasons.append(f"官方域名匹配 ({popular_domain})")
                break

        # 4. 检查是否包含 CLI 相关关键词
        combined_text = (page_title + ' ' + url).lower()
        cli_matches = sum(1 for kw in self.cli_keywords if kw in combined_text)
        if cli_matches >= 2:
            confidence += 0.1
            reasons.append(f"页面包含 CLI 相关内容")

        # 5. 检查是否是可疑页面（扣分）
        for pattern in self.suspicious_patterns:
            if re.search(pattern, combined_text, re.IGNORECASE):
                confidence -= 0.3
                reasons.append(f"⚠️ 页面可能不是文档页")
                break

        # 6. 检查状态码
        # 这里在调用方已经处理，所以不在这里扣分

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
            if confidence >= 0.5:
                status = 'valid'
                message = f'有效 (置信度: {confidence:.1%})'
            elif confidence >= 0.3:
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
            if md_file.name in ['README.md', 'template.md', 'contributing.md']:
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
        report_path = os.path.join(output_dir, 'smart_verification_report.md')
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"# CLI 产品网址智能验证报告\n\n")
            f.write(f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            f.write("## 汇总\n\n")
            f.write(f"| 指标 | 数量 | 占比 |\n")
            f.write(f"|------|------|------|\n")
            f.write(f"| 总产品数 | {len(results)} | 100% |\n")
            f.write(f"| 有效且匹配 | {len(valid)} | {len(valid)*100//len(results)}% |\n")
            f.write(f"| 需要人工确认 | {len(suspicious)} | {len(suspicious)*100//len(results)}% |\n")
            f.write(f"| 无效/不匹配 | {len(invalid)} | {len(invalid)*100//len(results)}% |\n")
            f.write(f"| 连接错误 | {len(errors)} | {len(errors)*100//len(results)}% |\n\n")

            # 需要人工确认的
            if suspicious:
                f.write("## 需要人工确认\n\n")
                f.write("这些页面可以访问，但内容可能不是对应的 CLI 文档：\n\n")
                f.write("| 产品 | 页面标题 | 置信度 | 理由 | URL |\n")
                f.write("|------|----------|--------|------|-----|\n")
                for r in sorted(suspicious, key=lambda x: x.confidence):
                    rel_path = os.path.relpath(r.file_path, output_dir)
                    reasons_str = '; '.join(r.reasons[:3])
                    f.write(f"| {r.product_name} | {r.page_title} | {r.confidence:.0%} | {reasons_str} | {r.url} |\n")
                f.write("\n")

            # 无效/不匹配的
            if invalid:
                f.write("## 无效或内容不匹配\n\n")
                f.write("| 产品 | 文件 | 状态 | 页面标题 | URL |\n")
                f.write("|------|------|------|----------|-----|\n")
                for r in sorted(invalid, key=lambda x: x.product_name):
                    rel_path = os.path.relpath(r.file_path, output_dir)
                    f.write(f"| {r.product_name} | `{rel_path}` | {r.message} | {r.page_title[:50]} | {r.url} |\n")
                f.write("\n")

            # 连接错误
            if errors:
                f.write("## 连接错误\n\n")
                f.write("| 产品 | 错误信息 | URL |\n")
                f.write("|------|----------|-----|\n")
                for r in sorted(errors, key=lambda x: x.product_name):
                    f.write(f"| {r.product_name} | {r.message} | {r.url} |\n")
                f.write("\n")

            # 有效列表（按置信度排序）
            f.write("## 有效且匹配（按置信度排序，前 30 个）\n\n")
            f.write("| 产品 | 页面标题 | 置信度 | URL |\n")
            f.write("|------|----------|--------|-----|\n")
            for r in sorted(valid, key=lambda x: -x.confidence)[:30]:
                f.write(f"| {r.product_name} | {r.page_title} | {r.confidence:.0%} | {r.url} |\n")

        print(f"\n报告已生成: {report_path}")

        # JSON 报告
        json_path = os.path.join(output_dir, 'smart_verification_report.json')
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump({
                'generated_at': datetime.now().isoformat(),
                'summary': {
                    'total': len(results),
                    'valid': len(valid),
                    'suspicious': len(suspicious),
                    'invalid': len(invalid),
                    'errors': len(errors)
                },
                'results': [
                    {
                        'product': r.product_name,
                        'file': r.file_path,
                        'url': r.url,
                        'status': r.status,
                        'status_code': r.status_code,
                        'message': r.message,
                        'page_title': r.page_title,
                        'confidence': round(r.confidence, 2),
                        'reasons': r.reasons
                    }
                    for r in results
                ]
            }, f, indent=2, ensure_ascii=False)

        print(f"JSON 报告已生成: {json_path}")


def main():
    """主函数"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = script_dir

    print("=" * 60)
    print("CLI 产品网址智能验证工具")
    print("=" * 60)
    print(f"工作目录: {root_dir}\n")

    validator = SmartURLValidator(timeout=15, max_workers=4)
    results = validator.run_validation(root_dir)

    # 生成报告
    validator.generate_smart_report(results, root_dir)

    print("\n" + "=" * 60)
    print("验证完成！")
    print("=" * 60)


if __name__ == '__main__':
    main()
