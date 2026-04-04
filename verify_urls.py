#!/usr/bin/env python3
"""
CLI 产品网址验证脚本
验证所有产品 Markdown 文件中的官方文档 URL 是否有效
"""

import os
import re
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional

@dataclass
class ValidationResult:
    """单个网址验证结果"""
    file_path: str
    product_name: str
    url: str
    status: str  # 'valid', 'invalid', 'error'
    status_code: Optional[int]
    message: str


class URLValidator:
    """网址验证器"""

    def __init__(self, timeout: int = 10, max_workers: int = 4):
        self.timeout = timeout
        self.max_workers = max_workers
        self.results = []

    def extract_url_from_file(self, file_path: str) -> tuple[str, str]:
        """从 Markdown 文件中提取官方文档 URL"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip().startswith('- 官方文档：'):
                        # 提取 URL
                        match = re.search(r'https?://[^\s\]]+', line)
                        if match:
                            url = match.group(0)
                            # 提取产品名称（文件第一行的 # 后面）
                            product_name = Path(file_path).stem
                            return product_name, url
        except Exception as e:
            print(f"读取文件失败 {file_path}: {e}")
        return None, None

    def check_url(self, url: str) -> tuple[int, str]:
        """
        检查单个 URL
        返回: (状态码, 消息)
        """
        try:
            # 使用 HEAD 请求，更轻量
            req = urllib.request.Request(
                url,
                method='HEAD',
                headers={'User-Agent': 'Mozilla/5.0 (CLI Products URL Checker)'}
            )
            req.add_header('Accept', '*/*')

            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                status_code = response.status

                # 2xx 和 3xx 都视为有效（跟随重定向）
                if 200 <= status_code < 400:
                    return status_code, '有效'
                else:
                    return status_code, f'HTTP {status_code}'

        except urllib.error.HTTPError as e:
            return e.code, f'HTTP {e.code}'
        except urllib.error.URLError as e:
            if hasattr(e, 'reason'):
                return 0, f'连接失败: {e.reason}'
            return 0, '连接失败'
        except Exception as e:
            return 0, f'错误: {str(e)}'

    def validate_file(self, file_path: str) -> ValidationResult:
        """验证单个文件中的 URL"""
        product_name, url = self.extract_url_from_file(file_path)

        if not url:
            return ValidationResult(
                file_path=file_path,
                product_name=Path(file_path).stem,
                url='未找到',
                status='error',
                status_code=None,
                message='无法提取 URL'
            )

        status_code, message = self.check_url(url)

        # 判断状态
        if status_code >= 200 and status_code < 400:
            status = 'valid'
        elif status_code == 0:
            status = 'error'
        else:
            status = 'invalid'

        return ValidationResult(
            file_path=file_path,
            product_name=product_name,
            url=url,
            status=status,
            status_code=status_code,
            message=message
        )

    def find_all_markdown_files(self, root_dir: str) -> list[str]:
        """递归查找所有产品 Markdown 文件"""
        md_files = []
        root_path = Path(root_dir)

        # 排除的目录
        exclude_dirs = {'.git', 'node_modules', '.claude'}

        for md_file in root_path.rglob('*.md'):
            # 跳过根目录的 README.md 和其他非产品文件
            if md_file.name in ['README.md', 'template.md', 'contributing.md']:
                continue

            # 跳过排除目录中的文件
            if any(exclude_dir in md_file.parts for exclude_dir in exclude_dirs):
                continue

            md_files.append(str(md_file))

        return sorted(md_files)

    def run_validation(self, root_dir: str) -> list[ValidationResult]:
        """运行所有文件的验证"""
        md_files = self.find_all_markdown_files(root_dir)
        print(f"找到 {len(md_files)} 个产品文件\n")

        results = []

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # 提交所有任务
            future_to_file = {
                executor.submit(self.validate_file, f): f
                for f in md_files
            }

            # 收集结果并显示进度
            completed = 0
            for future in as_completed(future_to_file):
                completed += 1
                result = future.result()
                results.append(result)

                # 显示进度
                status_icon = {'valid': '✅', 'invalid': '❌', 'error': '⚠️'}.get(result.status, '❓')
                print(f"[{completed}/{len(md_files)}] {status_icon} {result.product_name}: {result.message}")

        return results

    def generate_report(self, results: list[ValidationResult], output_dir: str):
        """生成验证报告"""
        valid = [r for r in results if r.status == 'valid']
        invalid = [r for r in results if r.status == 'invalid']
        errors = [r for r in results if r.status == 'error']

        # Markdown 报告
        report_path = os.path.join(output_dir, 'url_verification_report.md')
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"# CLI 产品网址验证报告\n\n")
            f.write(f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            f.write("## 汇总\n\n")
            f.write(f"| 指标 | 数量 |\n")
            f.write(f"|------|------|\n")
            f.write(f"| 总产品数 | {len(results)} |\n")
            f.write(f"| 有效网址 | {len(valid)} ({len(valid)*100//len(results)}%) |\n")
            f.write(f"| 无效网址 | {len(invalid)} ({len(invalid)*100//len(results)}%) |\n")
            f.write(f"| 验证错误 | {len(errors)} ({len(errors)*100//len(results)}%) |\n\n")

            if invalid:
                f.write("## 无效网址列表\n\n")
                f.write("| 产品 | 文件 | 状态码 | URL |\n")
                f.write("|------|------|--------|-----|\n")
                for r in sorted(invalid, key=lambda x: x.product_name):
                    rel_path = os.path.relpath(r.file_path, output_dir)
                    f.write(f"| {r.product_name} | `{rel_path}` | {r.status_code} | {r.url} |\n")
                f.write("\n")

            if errors:
                f.write("## 验证错误列表\n\n")
                f.write("| 产品 | 文件 | 错误信息 | URL |\n")
                f.write("|------|------|----------|-----|\n")
                for r in sorted(errors, key=lambda x: x.product_name):
                    rel_path = os.path.relpath(r.file_path, output_dir)
                    f.write(f"| {r.product_name} | `{rel_path}` | {r.message} | {r.url} |\n")
                f.write("\n")

            f.write("## 有效网址（前 50 个）\n\n")
            f.write("| 产品 | 状态码 | URL |\n")
            f.write("|------|--------|-----|\n")
            for r in sorted(valid, key=lambda x: x.product_name)[:50]:
                f.write(f"| {r.product_name} | {r.status_code} | {r.url} |\n")
            if len(valid) > 50:
                f.write(f"| ... | ... | ... (还有 {len(valid)-50} 个) |\n")

        print(f"\n报告已生成: {report_path}")

        # JSON 报告
        json_path = os.path.join(output_dir, 'url_verification_report.json')
        import json
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump({
                'generated_at': datetime.now().isoformat(),
                'summary': {
                    'total': len(results),
                    'valid': len(valid),
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
                        'message': r.message
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
    print("CLI 产品网址验证工具")
    print("=" * 60)
    print(f"工作目录: {root_dir}\n")

    validator = URLValidator(timeout=10, max_workers=4)
    results = validator.run_validation(root_dir)

    # 生成报告
    validator.generate_report(results, root_dir)

    print("\n" + "=" * 60)
    print("验证完成！")
    print("=" * 60)


if __name__ == '__main__':
    main()
