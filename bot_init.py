import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from modules import Database, get_db_env

# Configure logging
logging.basicConfig(filename='./src/log.txt', level=logging.WARN)

# Initialize bot and dispatcher
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())
db = Database(get_db_env())
