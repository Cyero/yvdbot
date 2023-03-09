from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

users_button = InlineKeyboardButton(text="Users online", callback_data='users')
alert_button = InlineKeyboardButton(text="Send restart alert to active users", callback_data='sendall')
clear_button = InlineKeyboardButton(text="Clear users dir", callback_data='clean')
wipe_button = InlineKeyboardButton(text="Wipe database", callback_data='wipe')
kb_admin = InlineKeyboardMarkup().add(users_button).add(alert_button).add(clear_button).add(wipe_button)
