@echo off
echo ========================================
echo Running All API Tests
echo ========================================
echo.
echo Make sure your FastAPI server is running on http://127.0.0.1:8003
echo Press any key to continue or Ctrl+C to cancel...
pause > nul
echo.

echo ========================================
echo Story 1: API Verification Tests
echo ========================================
python test_api_verification.py
echo.

echo ========================================
echo Story 2: Validation Tests  
echo ========================================
python test_validation.py
echo.

echo ========================================
echo Story 4: Integration Tests
echo ========================================
python test_integration.py
echo.

echo ========================================
echo All Tests Completed!
echo ========================================
echo.
echo If all tests passed, your API is ready for production use.
echo You can now connect your React frontend to the backend.
echo.
pause