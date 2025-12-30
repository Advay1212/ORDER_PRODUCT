@echo off
echo Starting FastAPI Backend and React Frontend...
echo.

echo Stopping any existing servers...
taskkill /f /im python.exe 2>nul
taskkill /f /im node.exe 2>nul
echo.

echo Starting FastAPI server...
start "FastAPI Backend" cmd /k "cd /d c:\Users\Advay\Desktop\Advay\fastapi\models && python server.py"

echo Waiting 5 seconds for backend to start...
timeout /t 5 /nobreak > nul

echo Starting React frontend...
start "React Frontend" cmd /k "cd /d c:\Users\Advay\Desktop\Advay\react-products-app && npm start"

echo.
echo Both services are starting...
echo FastAPI Backend: http://127.0.0.1:8003
echo React Frontend: http://localhost:3000
echo.
echo Press any key to close this window (services will keep running)
pause > nul