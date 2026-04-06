---
name: python_scripts
description: Python utility scripts for maintenance and verification
type: reference
---

# Python Utility Scripts

**Location:** Root directory of project

**Available Scripts:**

1. **verify_urls.py** — URL verification for all tool links
   - Generates url_verification_report.json and url_verification_report.md
   - Checks HTTP status of all official documentation URLs

2. **verify_urls_smart.py / verify_urls_smart_v2.py** — Enhanced URL verification
   - Smarter detection with user-agent handling
   - Generates smart_verification_report.json/md
   - Improved error reporting

3. **fix_urls.py** — URL fixing utility
   - Corrects malformed or outdated URLs
   - Uses search_queries.txt for reference

4. **update_urls.py** — Batch URL updates
   - Updates URLs based on verification results

5. **update_readme.py** — README auto-update
   - Updates category README files
   - Extracts product info from markdown files
   - Maintains tool counts and descriptions

6. **reorganize_categories.py** — Category restructuring
   - Reorganizes tools into proper categories
   - Updates file paths and references

7. **phase2_fixes.py, phase3_fixes.py, phase4_fixes.py** — Incremental fix scripts
   - Applied fixes in phases during URL cleanup
   - Reference files: phase2_search_tasks.txt, phase2_url_fixes.py

**Usage:** These scripts are run during maintenance to verify URLs, fix broken links, and keep documentation up-to-date.
