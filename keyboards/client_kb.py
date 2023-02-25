from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb_start = InlineKeyboardMarkup().add(InlineKeyboardButton(text="Here goes!", callback_data='go'))
kb_download = InlineKeyboardMarkup().add(InlineKeyboardButton(text="Download", callback_data='download'))
