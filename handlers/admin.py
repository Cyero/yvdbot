import os
from aiogram import types, Dispatcher
from bot_init import bot, db
from modules import fsworker as fw
from keyboards import kb_admin


async def admin_panel(message: types.Message) -> None:
    await message.answer("Hello creator, what would you like to do?", reply_markup=kb_admin)


async def clean_dir(call: types.CallbackQuery) -> None:
    fw.rmdir('*')
    await call.message.answer("Killed!")


async def send_all(call: types.CallbackQuery) -> None:
    user_list = db.get_user()
    for user in user_list:
        await bot.send_message(user[0], "--- Warning! Bot will be restarted at 5 minutes ---")
    await call.answer()


async def users_online(call: types.CallbackQuery) -> None:
    await call.message.answer(f"Now online: {len(db.get_user())} user(s)")
    await call.answer()


async def wipe_db(call: types.CallbackQuery) -> None:
    db.drop_db()
    await call.message.answer("Wiped! Database was recreated")


def admin_handlers_register(dp: Dispatcher) -> None:
    admin_pass = os.getenv('PWD_ADMIN')
    dp.register_message_handler(admin_panel, lambda message: message.text and ".admin" and admin_pass in message.text)
    dp.register_callback_query_handler(clean_dir, text='clean')
    dp.register_callback_query_handler(send_all, text='sendall')
    dp.register_callback_query_handler(users_online, text='users')
    dp.register_callback_query_handler(wipe_db, text='wipe')
