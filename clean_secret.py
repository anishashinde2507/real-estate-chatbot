#!/usr/bin/env python3
"""
Clean secret from git history and push to GitHub.
This removes .env files from all commits without rebuilding the entire repo.
"""

import subprocess
import sys
import os

def run_command(cmd, check=True):
    """Run a shell command and return output"""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"ERROR: {result.stderr}")
        sys.exit(1)
    return result.stdout + result.stderr

def main():
    os.chdir(r"c:\Users\hp\Downloads\Real Estate")
    
    print("="*60)
    print("Cleaning .env from git history")
    print("="*60)
    
    # Set environment variable to suppress warning
    os.environ['FILTER_BRANCH_SQUELCH_WARNING'] = '1'
    
    # Remove .env from history using filter-branch
    print("\n1. Removing backend/.env from all commits...")
    run_command('git filter-branch -f --tree-filter "del /q backend\\.env 2>nul" -- --all')
    
    # Clean up reflog
    print("\n2. Cleaning reflog...")
    run_command('git reflog expire --expire=now --all', check=False)
    
    # Aggressive garbage collection
    print("\n3. Running garbage collection...")
    run_command('git gc --aggressive --prune=now', check=False)
    
    # Verify the secret is gone
    print("\n4. Verifying secret is removed...")
    output = subprocess.run(
        'git log -p --all -- backend/.env',
        shell=True,
        capture_output=True,
        text=True
    ).stdout
    
    if 'HUGGINGFACE_API_KEY' in output:
        print("ERROR: Secret still found in history!")
        sys.exit(1)
    else:
        print("✓ Secret successfully removed from history")
    
    # Force push
    print("\n5. Force pushing to GitHub...")
    run_command('git push -f origin main')
    
    print("\n" + "="*60)
    print("✓ SUCCESS! Secret removed and pushed to GitHub")
    print("="*60)

if __name__ == '__main__':
    main()
