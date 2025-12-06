#!/usr/bin/env python3
"""
Secret Scanner - Finds and reports potential secrets in repository
Usage: python3 clean_secret.py
"""

import os
import re
from pathlib import Path

# Patterns for common secrets
PATTERNS = {
    'huggingface': r'hf_[A-Za-z0-9]{20,}',
    'api_key': r'api[_-]?key["\']?\s*[:=]\s*["\']?[A-Za-z0-9]{20,}',
    'secret': r'secret["\']?\s*[:=]\s*["\']?[A-Za-z0-9]{20,}',
    'token': r'token["\']?\s*[:=]\s*["\']?[A-Za-z0-9]{20,}',
    'password': r'password["\']?\s*[:=]\s*["\']?[^\s"\']+',
}

def scan_file(filepath):
    """Scan a single file for secrets"""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        results = []
        for secret_type, pattern in PATTERNS.items():
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                line_num = content[:match.start()].count('\n') + 1
                results.append({
                    'type': secret_type,
                    'match': match.group(),
                    'line': line_num
                })
        return results
    except Exception as e:
        return []

def scan_repo(root_dir='.'):
    """Scan entire repository"""
    excluded_dirs = {'.git', '__pycache__', 'node_modules', '.venv', 'venv', 'env'}
    excluded_files = {'.pyc', '.pyo', '.lock', '.yarn', '.jpg', '.png', '.zip'}
    
    all_findings = {}
    
    for filepath in Path(root_dir).rglob('*'):
        # Skip excluded directories
        if any(part in excluded_dirs for part in filepath.parts):
            continue
        
        # Skip excluded file types
        if any(str(filepath).endswith(ext) for ext in excluded_files):
            continue
        
        # Only scan files
        if not filepath.is_file():
            continue
        
        findings = scan_file(filepath)
        if findings:
            all_findings[str(filepath)] = findings
    
    return all_findings

def main():
    print("=" * 60)
    print("SECRET SCANNER - Repository Secret Detection")
    print("=" * 60)
    
    findings = scan_repo()
    
    if not findings:
        print("✓ No secrets detected!")
        return 0
    
    print(f"\n⚠ Found {sum(len(f) for f in findings.values())} potential secrets:\n")
    
    for filepath, results in findings.items():
        print(f"\n📄 {filepath}")
        for result in results:
            print(f"   Line {result['line']}: [{result['type'].upper()}] {result['match'][:50]}")
    
    print("\n" + "=" * 60)
    print("ACTION REQUIRED:")
    print("1. Review findings above")
    print("2. Remove secrets from files")
    print("3. Regenerate compromised tokens")
    print("4. Run: git add -A && git commit")
    print("5. Run: git push -f origin main")
    print("=" * 60)
    
    return 1

if __name__ == '__main__':
    exit(main())
