@echo off

echo =============================
echo        GIT AUTO PUSH
echo =============================

echo.
echo Adding files...
git add .

echo.
echo Committing...
git commit -m "update"

echo.
echo Pushing to remote...
git push origin main

echo.
echo ✅ DONE!
pause
