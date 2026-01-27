@echo off
echo Starting Vegapunk Discord Bots...
echo.

REM Activate virtual environment
call venv\Scripts\activate

REM Run the bots
python vegapunk_bots.py

REM Deactivate when done (Ctrl+C)
deactivate
