@echo off
REM SCE Question App Runner Script for Windows (Alternative Version)
REM This version handles more Python installation scenarios

echo ==================================================
echo SCE Question App Setup ^& Runner (Windows)
echo ==================================================

REM Change to script directory
cd /d "%~dp0"

REM Try different Python commands to find a working one
set PYTHON_CMD=
python --version >nul 2>&1
if %errorlevel% equ 0 (
    set PYTHON_CMD=python
    goto :python_found
)

python3 --version >nul 2>&1
if %errorlevel% equ 0 (
    set PYTHON_CMD=python3
    goto :python_found
)

py --version >nul 2>&1
if %errorlevel% equ 0 (
    set PYTHON_CMD=py
    goto :python_found
)

echo Error: Python is required but not found
echo Please install Python from https://python.org
echo Make sure to check "Add Python to PATH" during installation
pause
exit /b 1

:python_found
echo ✓ Python detected (%PYTHON_CMD%)

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating virtual environment...
    %PYTHON_CMD% -m venv venv
    if %errorlevel% neq 0 (
        echo Error: Failed to create virtual environment
        echo Make sure you have the full Python installation (not just from Microsoft Store)
        pause
        exit /b 1
    )
    echo ✓ Virtual environment created
) else (
    echo ✓ Virtual environment found
)

REM Check if venv was created properly
if not exist "venv\Scripts\python.exe" (
    echo Error: Virtual environment is incomplete
    echo Removing and recreating...
    rmdir /s /q venv
    %PYTHON_CMD% -m venv venv
    if %errorlevel% neq 0 (
        echo Error: Still failed to create virtual environment
        pause
        exit /b 1
    )
)

REM Install dependencies using the virtual environment's pip
echo Installing dependencies...
venv\Scripts\python.exe -m pip install --upgrade pip
venv\Scripts\python.exe -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error: Failed to install dependencies
    echo This might be due to missing build tools or incompatible packages
    pause
    exit /b 1
)
echo ✓ Dependencies installed successfully

echo.
echo ==================================================
echo Setup complete! Starting application...
echo ==================================================

REM Run the application using the virtual environment's Python
venv\Scripts\python.exe src\gui_app.py
if %errorlevel% neq 0 (
    echo Error: Application failed to start
    echo Check the error messages above for details
)

echo.
echo Application finished. Press any key to close this window.
pause
