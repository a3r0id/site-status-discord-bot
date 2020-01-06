# discord-uptime-client
A simple bot for periodically checking your websites stats including port used on http request, http request latency, http status code and more from almost any remote machine using Python3 requests module.

-------------------------------------------------

## Deployment
* Windows 10/8/7
  * [Setup](https://github.com/aerobotpro/site-status-discord-bot#windows-1087)
* Linux
  * [Setup](https://github.com/aerobotpro/site-status-discord-bot#linux)
-------------------------------------------------
## Some Pics

### Public Updates
![](https://cdn.discordapp.com/attachments/662110077955604481/663853562643742760/public.png)

### Admin Updates
![](https://media.discordapp.net/attachments/662110077955604481/663853599989825556/admin.png?width=609&height=474)

### Error Notifications
![](https://cdn.discordapp.com/attachments/662110077955604481/663853585045651477/admin_notification.png)

-------------------------------------------------

### Windows 10/8/7

* Install Python3 (3.6+) - [Latest: Install Python3 on Windows 10](https://www.youtube.com/watch?v=V_ACbv4329E)
* Important: *Be sure to add Python3 to your PATH upon installation!!!*
* Extract contents of `discord-uptime-client` to the folder of your choice but remember that folder.
* Extract contents of `windows` to the folder thats contains our bot files. Should be `start_bot.bat` & and install_requirements.bat`
* Open `config.py` and change the contents to your bot's information.
* Make sure that the channels can be accessed by your bot on Discord (Valid Permissions)
* Double-click or run `install_requirements.bat`. You will be prompted to start your bot from there if you please.
* Start Bot by double-clicking `start_bot.py`.
* Important: *You need to be sure all files remain in the same folder at all times.*
* Important: *Emojis/Special Fonts in your channel names may cause issues! You will be prompted if so.*

-------------------------------------------------

### Linux

* `git clone https://github.com/aerobotpro/site-status-discord-bot.git`
* Edit Your `config.py`
* Start bot.py
* Done!
* ALSO, you can run `build.sh` to create a python3 executable if you please, it will work.
 
------------------------------------------------- 
 
## Enjoy!
