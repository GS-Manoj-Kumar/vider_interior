@echo off
start "Tailwind Watcher" cmd /k ".\tailwindcss.exe -i ./static/css/input.css -o ./static/css/output.css --watch"
start "Django Server" cmd /k "venv\Scripts\activate && python manage.py runserver"


@REM Then run it:
@REM ```
@REM .\start.bat

@REM ssh -i "copy and paste path of your ssh.key file here " ubuntu@140.238.249.156
@REM /home/ubuntu/deploy.sh