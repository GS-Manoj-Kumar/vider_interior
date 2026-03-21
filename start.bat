@echo off
start "Tailwind Watcher" cmd /k ".\tailwindcss.exe -i ./static/css/input.css -o ./static/css/output.css --watch"
start "Django Server" cmd /k "venv\Scripts\activate && python manage.py runserver"


@REM Then run it:
@REM ```
@REM .\start.bat


@REM /home/ubuntu/deploy.sh