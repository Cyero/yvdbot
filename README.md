![](https://img.shields.io/badge/python-3.11-green) ![](https://img.shields.io/badge/platform-macos%20%7C%20linux%20%7C%20windows-lightgrey) ![](https://img.shields.io/badge/required-PostgreSQL%20%7C%20Telegram_Bot_API_Server%20%7C%20ngrok-blue)

# YouTube Video Downloader Bot
Telegram bot for downloading video from YouTube

## Environment Variables
To run this project, you will need to add the following environment variables to your .env file

`TOKEN`- Telegram BOT Token

`SITEURL` - Hosting\ngrok URL 

`APPHOST` - IP for listening (defaults to '127.0.0.1' if not provided)

`APPPORT` - Port for listening. For deploy it`s taken auto from host provider (defaults to 5000 if not provided)

`PWDADMIN`- Password for the administrator menu. You need to generate your own. To launch the admin panel, 
send a message ".admin YOUR_PASS" to the bot, and after a warning that something went wrong, enter your password. 
In the admin panel, you can: view the number of active users, warn users about a scheduled restart of the bot,
clear the directory with user files, clear the database 

`PGDATABASE` - The database name

`PGUSER` - Username used to authenticate to database

`PGPASSWORD` - Password used to authenticate to database

`PGHOST` - Database host address (defaults to UNIX socket if not provided)

`PGPORT` - Database connection port number (defaults to 5432 if not provided)

## Run Locally
If you are using PostgreSQL, specify the connection data in environment variables, if you do not have a valid 
PostgreSQL database, the local database sqlite3 will be used

Clone the project

```bash
  git clone https://github.com/Cyero/yvdbot.git
```

Go to the project directory

```bash
  cd yvdbot
```

Install dependencies

```bash
  poetry install
```

Install environment variables

```bash
#UNIX
  export TOKEN='YOUR_TOKEN_HERE'
  export APPHOST='localhost'
  export PWDADMIN='YOUR_PASSWORD'
  
#PowerShell
  $env:TOKEN='YOUR_TOKEN_HERE'
  $env:APPHOST='localhost'
  $env:PWDADMIN='YOUR_PASSWORD'
```

Start the ngrok server at new terminal

```bash
  ngrok http 5000
```

Run a bot

```bash
#UNIX
  URL=YOUR_NGROK_FORWARDING_URL python3 start.py
  
#PowerShell
  $env:URL=YOUR_NGROK_FORWARDING_URL 
  python3.exe ./start.py
```
Attention! When specifying the "URL" variable, remove the " \ " at the end of the address


## Deployment
Clone the project
```bash
git clone https://github.com/Cyero/yvdbot.git
```
Go to the project directory
```bash
cd yvdbot
```
Create a virtual environment
```bash
python3 -m venv env
```
Activate virtual environment
```bash
source env/bin/Activate
```
Install dependencies
```bash
poetry install
```
Deactivate virtual environment
```bash
deactivate
```
Add rule in firewall
```bash
sudo ufw allow 443
```
Add route to your nging configuration
```bash
location /$TOKEN {
      proxy_set_header Host $http_host;
      proxy_redirect off;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Scheme $scheme;
      proxy_pass http://127.0.0.1:5000/$TOKEN;
  }
```
Make script for runnig bot as service
```bash
sudo nano /etc/systemd/system/yvdbot.service
```
Paste next code to file. If you're using PostgreSQL - add 'Environment="KEY=VALUE"' for every variable
```bash
[Unit]
Description=YVDBot
After=multi-user.target

[Service]
User=USERNAME
Environment="SITEURL=YOUR_SITE_URL"
Environment="TOKEN=YOUR_BOT_TOKEN"
Environment="PWDADMIN=YOUR_ADMIN_PASS"
Type=simple
Restart=always
WorkingDirectory=/home/USERNAME/yvdbot
ExecStart=/bin/bash -c 'cd /home/USERNAME/yvdbot/ && source env/bin/activate && python start.py'

[Install]
WantedBy=multi-user.target
```
Reload systemctl
```bash
sudo systemctl daemon-reload
```
Enable autorun
```bash
sudo systemctl enable yvdbot.service
```
Start service
```bash
sudo systemctl start yvdbot.service
``````

## Appendix
The bot can work both on the local and on the public [Telegram BOT API](https://github.com/tdlib/telegram-bot-api) server.
In the local mode the Bot API server allows to:

    1. Download files without a size limit.
    2. Upload files up to 2000 MB. (50MB limit for public server)
    3. Upload files using their local path and the file URI scheme.
    4. Use an HTTP URL for the webhook.
    5. Use any local IP address for the webhook.
    6. Use any port for the webhook.
    7. Set max_webhook_connections up to 100000.
    8. Receive the absolute local path as a value of the file_path  
    field without the need to download the file after 
    a getFile request.
