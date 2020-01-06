@echo off
set /p begin=Hit ENTER to INSTALL REQUIREMENTS...
pip3 install -r requirements.txt && cls && (echo pip3: Successfully Installed Discord.py!) || (pip install -r requirements.txt && cls && echo pip: Successfully Installed Discord.py!)
set /p begin=Hit ENTER to CONTINUE...
cls
set /p begin=Hit ENTER to START BOT!
cls
python bot.py
