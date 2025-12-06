@echo off
REM Script to clean .env from git history using filter-branch

cd "c:\Users\hp\Downloads\Real Estate"

echo Cleaning .env from git history...
FOR /F "delims=" %%i IN ('git rev-list --all --objects ^| findstr "backend/.env" ^| cut -d" " -f2') DO (
    echo Found secret file: %%i
)

echo.
echo Using git-filter-branch to remove backend/.env from all commits...
SET FILTER_BRANCH_SQUELCH_WARNING=1

REM Remove the file from all commits
git filter-branch -f --tree-filter "if [ -f backend/.env ]; then rm backend/.env; fi" -- --all

echo.
echo Cleaning up git reflog...
git reflog expire --expire=now --all
git gc --aggressive --prune=now

echo.
echo Force pushing to GitHub...
git push -f origin main

echo.
echo Done! Secret removed from history.
