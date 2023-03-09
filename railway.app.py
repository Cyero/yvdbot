import os
from start import on_shutdown
from aiogram import executor
from bot_init import bot, dp, db
from handlers import client, admin


async def on_startup(dp) -> None:
    await bot.set_webhook({os.getenv('RAILWAY_STATIC_URL')})
    admin.admin_handlers_register(dp)
    client.client_handlers_register(dp)
    db.check_table_existing()


if __name__ == "__main__":
    executor.start_webhook(
        dispatcher=dp,
        webhook_path="",
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=os.getenv('HOST', '0.0.0.0'),
        port=int(os.getenv('PORT', "5000"))
    )
