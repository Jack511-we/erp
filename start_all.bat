@echo off
REM 激活虚拟环境
call D:\erp\.venv\Scripts\activate

REM 启动 Flask 后端（后台运行）
start /min cmd /c "cd /d D:\erp\backend && python app.py"

REM 启动前端静态服务器（后台运行）
start /min cmd /c "cd /d D:\erp\erp-frontend\lowcode-engine-demo\deploy-space\static && npx http-server . -p 8080"

echo 前后端服务已启动！
pause
