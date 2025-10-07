@echo off
REM Desktop Pet Startup Script for Windows

REM Get the directory where this script is located
set SCRIPT_DIR=%~dp0

REM Path to the desktop pet Python script
set PET_SCRIPT=%SCRIPT_DIR%desktop_pet.py

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python not found. Please install Python 3.
    pause
    exit /b 1
)

REM Check if the pet script exists
if not exist "%PET_SCRIPT%" (
    echo Error: desktop_pet.py not found in %SCRIPT_DIR%
    pause
    exit /b 1
)

REM Run the desktop pet
echo Starting Desktop Pet...
cd /d "%SCRIPT_DIR%"
start /min python "%PET_SCRIPT%"

echo Desktop Pet started! Check your desktop.
timeout /t 3 /nobreak >nul