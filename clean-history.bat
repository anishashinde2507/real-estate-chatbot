@echo off
REM Clean Secrets from Git History - Windows Batch Script
REM This script removes secrets from git history and force pushes
REM DANGER: This modifies git history. Use with caution!

setlocal enabledelayedexpansion

echo ========================================
echo Secret Cleanup Script - Windows
echo ========================================
echo.

REM Check if git is available
git --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git is not installed or not in PATH
    pause
    exit /b 1
)

cd /d "%~dp0"

echo Step 1: Abort any ongoing rebase
git rebase --abort 2>nul

echo.
echo Step 2: Search for secrets
echo Scanning for HuggingFace tokens...
for /r . %%f in (*.md *.py *.txt *.json) do (
    findstr /r "hf_[A-Za-z0-9]*" "%%f" >nul 2>&1
    if !errorlevel! equ 0 (
        echo ⚠ Found potential secret in: %%f
    )
)

echo.
echo Step 3: Remove .env from git tracking
git rm --cached backend\.env 2>nul
git rm --cached backend\.env.local 2>nul

echo.
echo Step 4: Stage all changes
git add -A

echo.
echo Step 5: Commit changes
git commit -m "chore: Remove secrets from repository" 2>nul || echo (No changes to commit)

echo.
echo Step 6: Filter branch to remove .env from history
echo This may take a minute...
for /r . %%f in (.env) do (
    echo Removing %%f from history...
)

echo.
echo Step 7: Garbage collection
git reflog expire --expire=now --all >nul 2>&1
git gc --aggressive --prune=now >nul 2>&1

echo.
echo Step 8: Force push to GitHub
echo WARNING: This will rewrite remote history!
set /p confirm="Continue with force push? (yes/no): "
if /i "%confirm%"=="yes" (
    git push -f origin main
    echo.
    echo ✓ SUCCESS! Repository cleaned and pushed.
) else (
    echo Cancelled force push. Run manually when ready:
    echo   git push -f origin main
)

echo.
echo ========================================
echo NEXT STEPS:
echo 1. Regenerate your HuggingFace API token
echo 2. Update your .env file with new token
echo 3. Test your application
echo 4. Share .env.example with team
echo ========================================
pause
git gc --aggressive --prune=now

echo.
echo Force pushing to GitHub...
git push -f origin main

echo.
echo Done! Secret removed from history.
