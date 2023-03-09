import os
import subprocess
import time


def tasks_append(url: str = "message.text", chat_id: str = "call.from_user.id", file: str = "tasks.txt") -> None:
    try:
        with open(f'./users/{chat_id}/{file}', 'a') as file:
            file.write(f'{url}\n')
    except FileNotFoundError:
        pass


def get_mp4(chat_id: str = "call.from_user.id", extension: str = ".mp4") -> None:
    files = [file for file in os.listdir(f'./users/{chat_id}') if file.endswith(extension)]
    with open(f'./users/{chat_id}/to_send.txt', 'w') as file:
        for filename in files:
            file.write(f'{filename}\n')


def send_mp4(chat_id: str = "call.from_user.id", file: str = "to_send.txt") -> list | None:
    try:
        files_to_send = []
        with open(f'./users/{chat_id}/{file}', 'r') as file:
            urls = file.readlines()
            for url in urls:
                files_to_send.append(url.strip())
        return files_to_send
    except FileNotFoundError:
        pass


def mkdir(chat_id: str = "call.from_user.id") -> None:
    if os.name == 'nt':
        subprocess.Popen(f'powershell.exe mkdir ./users/{chat_id}', shell=True)
        time.sleep(1)
        subprocess.Popen(f'powershell.exe "New-Item ./users/{chat_id}/tasks.txt"', shell=True)
    else:
        subprocess.run(f'mkdir -p ./users/{chat_id} && touch ./users/{chat_id}/tasks.txt', shell=True)


def rmdir(chat_id: str = "call.from_user.id") -> None:
    if os.name == 'nt':
        subprocess.Popen(f'powershell.exe rm -R ./users/{chat_id}', shell=True)
    else:
        subprocess.run(f'rm -rf ./users/{chat_id}', shell=True)
