from ytmusicapi import YTMusic

# import pafy
import yt_dlp
from PIL import Image
import requests


def get_link(name: str) -> tuple:
    """Returns music link of the closesnt searched keyword"""
    yt = YTMusic()
    data = yt.search(query=name, filter="songs")
    print(data)
    top_name, video_id = data[0]["title"], data[0]["videoId"]
    return (video_id, top_name)


def get_thumbnail(thumbnail, name):
    "downloads a thumbnail of the song"
    # Cropping the thumbnail to square
    thumbnail = "https://i.ytimg.com/vi/" + thumbnail + "/maxresdefault.jpg"
    a = requests.get(thumbnail, timeout=10)
    with open(name + ".jpg", "wb") as file:
        file.write(a.content)
    #  im = Image.open(name+".jpg")
    # width, height = im.size   # Get dimensions

    # left = (width - height)/2
    # top = (height - height)/2
    # right = (width + height)/2
    # bottom = (height + height)/2

    # # Crop the center of the image
    # im = im.crop((left, top, right, bottom))
    # im.save(name+".jpg")


def get_audio(urls: tuple, name, download=True) -> str:
    "downloads audio of the song"
    ydl_opts = {
        "outtmpl": "/home/Sk7/Documents/python/YT_APP/" + name + ".%(ext)s",
        "format": "mp3/bestaudio/best",
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        return str(ydl.prepare_filename(ydl.extract_info(urls, download)))

if __name__ == "__main__":
    from Player import AudioPlayer

    A = AudioPlayer()
    print(get_audio("https://music.youtube.com/watch?v=G1ej5up7JG0", "a", A))
