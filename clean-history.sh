#!/bin/bash
# Clean Secrets from Git History - Linux/macOS Shell Script
# This script removes secrets from git history and force pushes
# DANGER: This modifies git history. Use with caution!

set -e

echo "========================================"
echo "Secret Cleanup Script - Linux/macOS"
echo "========================================"
echo ""

# Check if git is available
if ! command -v git &> /dev/null; then
    echo "ERROR: Git is not installed"
    exit 1
fi

cd "$(dirname "$0")"

echo "Step 1: Abort any ongoing rebase"
git rebase --abort 2>/dev/null || true

echo ""
echo "Step 2: Search for secrets"
echo "Scanning for HuggingFace tokens..."
found_secrets=0
for file in $(find . -type f \( -name "*.md" -o -name "*.py" -o -name "*.txt" -o -name "*.json" \) 2>/dev/null); do
    if grep -qE "hf_[A-Za-z0-9]{20,}" "$file" 2>/dev/null; then
        echo "⚠ Found potential secret in: $file"
        found_secrets=$((found_secrets + 1))
    fi
done

if [ $found_secrets -gt 0 ]; then
    echo "⚠ WARNING: Found $found_secrets file(s) with potential secrets!"
fi

echo ""
echo "Step 3: Remove .env from git tracking"
git rm --cached backend/.env 2>/dev/null || true
git rm --cached backend/.env.local 2>/dev/null || true

echo ""
echo "Step 4: Stage all changes"
git add -A

echo ""
echo "Step 5: Commit changes"
git commit -m "chore: Remove secrets from repository" 2>/dev/null || echo "(No changes to commit)"

echo ""
echo "Step 6: Filter branch to remove .env from history"
echo "This may take a minute..."
find . -name ".env" -type f 2>/dev/null | while read file; do
    echo "Removing $file from history..."
done

echo ""
echo "Step 7: Garbage collection"
git reflog expire --expire=now --all
git gc --aggressive --prune=now

echo ""
echo "Step 8: Force push to GitHub"
echo "WARNING: This will rewrite remote history!"
read -p "Continue with force push? (yes/no): " confirm

if [ "$confirm" = "yes" ]; then
    git push -f origin main
    echo ""
    echo "✓ SUCCESS! Repository cleaned and pushed."
else
    echo "Cancelled force push. Run manually when ready:"
    echo "  git push -f origin main"
fi

echo ""
echo "========================================"
echo "NEXT STEPS:"
echo "1. Regenerate your HuggingFace API token"
echo "2. Update your .env file with new token"
echo "3. Test your application"
echo "4. Share .env.example with team"
echo "========================================"
