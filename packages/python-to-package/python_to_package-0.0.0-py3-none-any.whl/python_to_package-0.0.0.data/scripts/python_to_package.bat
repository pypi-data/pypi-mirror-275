
@echo off
setlocal
cd /d "%~dp0"
python __init__.py %*
endlocal
