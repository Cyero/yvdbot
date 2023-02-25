import pytube.exceptions
from pytube import YouTube, Playlist, Channel


def start_download(chat_id: str = "call.from_user.id", file: str = "tasks.txt", ) -> None:

    def errors_logger(error: str) -> None:
        with open(f'./users/{chat_id}/errors.txt', 'a') as log:
            log.write(f'{error}\n')
            pass

    path = f'./users/{chat_id}'
    queue = []
    with open(f'{path}/{file}', 'r') as file:
        for link in file:
            if "/playlist" in link:
                yt = Playlist(link)
                for url in yt.video_urls:
                    queue.append(url)
            elif "/@" in link:
                yt = Channel(link)
                for url in yt.video_urls:
                    queue.append(url)
            else:
                queue.append(link)
    for task in queue:
        yt = YouTube(task)
        try:
            yt.streams.filter(file_extension='mp4').get_highest_resolution().download(
                        output_path=path)
        except pytube.exceptions.LiveStreamError as exc:
            errors_logger(f"{yt.title} -> {exc}")
        except pytube.exceptions.AgeRestrictedError as exc:
            errors_logger(f"{yt.title} -> {exc}")
        except pytube.exceptions.RecordingUnavailable as exc:
            errors_logger(f"{yt.title} -> {exc}")
        except pytube.exceptions.MembersOnly as exc:
            errors_logger(f"{yt.title} -> {exc}")
        except pytube.exceptions.VideoUnavailable as exc:
            errors_logger(f"{yt.title} -> {exc}")
        except pytube.exceptions.PytubeError:
            errors_logger(f"{yt.title} -> Internal error")
        except pytube.exceptions.RegexMatchError:
            errors_logger("Invalid URL error")
