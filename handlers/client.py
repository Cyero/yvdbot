import os
from aiogram import types, Dispatcher
from modules import downloader as dw
from modules import fsworker as fw
from bot_init import db
from keyboards import kb_start, kb_download


async def cmd_menu(message: types.Message) -> None:
    await message.answer("In order to download the video - send a URL to me. After that, it will be added to the "
                         "download queue. Press the 'Download' button when your greed reaches the limit. "
                         "I hope this is clear?", reply_markup=kb_start)


async def get_single_url(call: types.CallbackQuery) -> None:
    db.user_existing(call.from_user.id)
    fw.mkdir(call.from_user.id)
    await call.message.answer("Now I have all your personal data! Come on, just kidding,"
                              "now I'm only ready to accept a bit of URLs from you")


async def get_url(msg: types.Message) -> None:
    if os.path.isfile(f'./users/{msg.from_user.id}/tasks.txt'):
        prefix = "youtu", "/playlist", "/@"
        if any(p in msg.text for p in prefix):
            fw.tasks_append(msg.text, msg.from_user.id)
            await msg.reply("Ok, this video is already in the queue. When you want me to start stealing "
                            "from YouTube - click the button below under any of the videos",
                            reply_markup=kb_download)
        else:
            await msg.answer("Sorry, but its not a YouTube URL. Dont try to fight with me!")
    else:
        await msg.answer("Looks like something went wrong! Restart me using the /start command")


async def download_video(call: types.CallbackQuery) -> None:
    await call.message.answer("I start downloading videos. Looks like you'll have to wait... But I don't "
                              "know how long, let's see how many videos you want. When I'm ready to send them "
                              "to you, I'll let you know.")
    dw.start_download(call.from_user.id)
    fw.get_mp4(call.from_user.id)
    if os.path.isfile(f'./users/{call.from_user.id}/errors.txt'):
        await call.message.answer("It seems that some of your videos will remain on YouTube. What I managed to steal,"
                                  " of course, I will send you (already sending them), but for now, look at the list"
                                  " of failures below:")
        with open(f'./users/{call.from_user.id}/errors.txt', 'r') as file:
            errors = file.read()
            await call.message.answer(f'{errors}')
    else:
        await call.message.answer("Wow, I managed to steal something from YouTube. I'm starting to send them to you,"
                                  " but keep in mind it will take some time, because my Internet speed is not the "
                                  "same as yours")
    videos = fw.send_mp4(call.from_user.id)
    for video in videos:
        video_to_send = open(f'./users/{call.from_user.id}/{video}', 'rb')
        await call.message.answer_video(video_to_send)
    await call.message.answer("Well, that's all, now you can (or not) save your videos to "
                              "your device. I hope you're happy? Bye, leather!")
    fw.rmdir(call.from_user.id)
    db.set_activity(call.from_user.id, '0')


def client_handlers_register(dp: Dispatcher) -> None:
    dp.register_message_handler(cmd_menu, commands='start')
    dp.register_callback_query_handler(get_single_url, text='go')
    dp.register_callback_query_handler(download_video, text='download')
    dp.register_message_handler(
        get_url,
        lambda message: message.text and "youtube.com" or "youtu.be" in message.text.lower()
    )
