@echo off
set /p begin=Hit ENTER to COMPILE SOURCE...
pip3 install -r requirements.txt && cls && (echo pip3: Successfully Installed Discord.py!) || (pip install -r requirements.txt && cls && echo pip: Successfully Installed Discord.py!)
cls
pip3 install pyinstaller && cls || (pip install pyinstaller)
pyinstaller -F bot.py -i discord-canary.ico

