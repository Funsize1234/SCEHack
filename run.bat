@echo off
REM SCE Question App Runner Script for Windows

REM Change to script directory
cd /d "%~dp0"

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    msg * "Error: Python is required but not installed"
    exit /b 1
)

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    python -m venv venv >nul 2>&1
    if %errorlevel% neq 0 (
        msg * "Error: Failed to create virtual environment"
        exit /b 1
    )
)

REM Activate virtual environment and install dependencies silently
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo Failed to activate virtual environment
    exit /b 1
)

pip install -r requirements.txt >nul 2>&1
if %errorlevel% neq 0 (
    msg * "Error: Failed to install dependencies"
    exit /b 1
)

REM Run the GUI application
python src/gui_app.py

REM Script ends here - no terminal window was ever