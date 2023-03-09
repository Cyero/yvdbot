import os
from aiogram import executor
from bot_init import bot, dp, db
from handlers import client, admin


async def on_startup(dp) -> None:
    await bot.set_webhook(f"{os.getenv('SITEURL')}/{os.getenv('TOKEN')}")
    admin.admin_handlers_register(dp)
    client.client_handlers_register(dp)
    db.check_table_existing()


async def on_shutdown(dp) -> None:
    db.close_db()
    await bot.delete_webhook()


if __name__ == "__main__":
    executor.start_webhook(
        dispatcher=dp,
        webhook_path=f"/{os.getenv('TOKEN')}",
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=os.getenv('APPHOST', '127.0.0.1'),
        port=int(os.getenv('APPPORT', "5000"))
    )
