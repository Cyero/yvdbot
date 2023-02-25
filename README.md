![](https://img.shields.io/badge/python-3.11-green) ![](https://img.shields.io/badge/platform-macos%20%7C%20linux%20%7C%20windows-lightgrey) ![](https://img.shields.io/badge/required-PostgreSQL%20%7C%20Telegram_Bot_API_Server%20%7C%20ngrok-blue)

# YouTube Video Downloader Bot
Telegram bot for downloading video from YouTube

## Environment Variables
To run this project, you will need to add the following environment variables to your .env file

`TOKEN`- Telegram BOT Token

`URL` - Hosting\ngrok URL 

`WHPATH` - Optional Webhook path (defaults '' if not provided)

`HOST` - IP for listening (defaults to '0.0.0.0' if not provided) For local use - "localhost"

`PORT` - Port for listening. For deploy it`s taken auto from host provider (defaults to 3001 if not provided)

`PWD_ADMIN`- Password for the administrator menu. You need to generate your own. To launch the admin panel, 
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
  export HOST='localhost'
  export PWD_ADMIN='YOUR_PASSWORD'
  
#PowerShell
  $env:TOKEN='YOUR_TOKEN_HERE'
  $env:HOST='localhost'
  $env:PWD_ADMIN='YOUR_PASSWORD'
```

Start the ngrok server at new terminal

```bash
  ngrok http 3001
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
