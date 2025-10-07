@echo off
REM Installation script for Desktop Pet on Windows

echo =echo Pet Features:
echo ^• Lives in a small container in the corner of your desktop
echo ^• Click and drag to move the pet within its container
echo ^• Double-click to make it play
echo ^• The pet will follow your cursor and wander randomly
echo ^• It will sleep, play, and be idle randomly
echo ^• Only visible when all apps are minimized to desktopktop Pet Installation for Windows ===
echo.

REM Get current directory
set CURRENT_DIR=%cd%

REM Check if we're in the right directory
if not exist "desktop_pet.py" (
    echo Error: Please run this script from the directory containing desktop_pet.py
    pause
    exit /b 1
)

echo Installing Desktop Pet...

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python not found. Please install Python 3 from python.org
    pause
    exit /b 1
)

echo ✓ Python found

REM Try to install pywin32 for better Windows integration
echo Installing Windows integration package...
pip install pywin32 >nul 2>&1
if %errorlevel% equ 0 (
    echo ✓ Windows integration package installed
) else (
    echo ! Optional Windows integration package installation failed (pet will still work)
)

REM Create startup shortcut
set STARTUP_DIR=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
set SHORTCUT_PATH=%STARTUP_DIR%\Desktop Pet.lnk

REM Create a VBS script to create the shortcut
echo Set WshShell = WScript.CreateObject("WScript.Shell") > create_shortcut.vbs
echo Set Shortcut = WshShell.CreateShortcut("%SHORTCUT_PATH%") >> create_shortcut.vbs
echo Shortcut.TargetPath = "%CURRENT_DIR%\start_pet.bat" >> create_shortcut.vbs
echo Shortcut.WorkingDirectory = "%CURRENT_DIR%" >> create_shortcut.vbs
echo Shortcut.Description = "Desktop Pet - Cute desktop companion" >> create_shortcut.vbs
echo Shortcut.Save >> create_shortcut.vbs

cscript //nologo create_shortcut.vbs
del create_shortcut.vbs

if exist "%SHORTCUT_PATH%" (
    echo ✓ Created startup shortcut
) else (
    echo ! Failed to create startup shortcut - you can manually run start_pet.bat
)

echo.
echo === Installation Complete! ===
echo.
echo Your desktop pet is now installed and will start automatically when you log in.
echo.
echo Manual Controls:
echo • To start the pet manually: start_pet.bat
echo • To stop the pet: Close using Task Manager or system tray
echo • To uninstall: uninstall_windows.bat
echo.
echo Pet Features:
echo • Click and drag to move the pet around
echo • Double-click to make it play
echo • The pet will follow your cursor when you're nearby
echo • It will sleep, play, and be idle randomly
echo • Only visible when all apps are minimized to desktop
echo.
echo Starting the pet now...
call start_pet.bat

echo.
echo Enjoy your new desktop companion! 🐱
pause