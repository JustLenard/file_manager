import os

home_path = "/home/len/"
downloads_path = home_path + "Downloads/"

music_path = home_path + "Music/"
docs_path = home_path + "Docs/"
video_path = home_path + "Video/"
pictures_path = home_path + "Pictures/"

to_delete = ["torrent"]
music = ["mp3", "mp4"]
docs = ["pdf"]
video = ["mvc"]
pictures = ["png", "jpg", "jpeg"]


def get_ending(string: str):
    return string.split(".")[-1]


with os.scandir(downloads_path) as entries:
    # os.mkdir(downloads_path + "/trash")
    for entry in entries:
        fname = entry.name
        print(get_ending(fname))
        if get_ending(fname) in to_delete:
            os.remove(downloads_path + fname)
        if get_ending(fname) in music:
            os.rename(downloads_path + fname, music_path + fname)
        if get_ending(fname) in docs:
            os.rename(downloads_path + fname, docs_path + fname)
        if get_ending(fname) in video:
            os.rename(downloads_path + fname, video_path + fname)
        if get_ending(fname) in pictures:
            os.rename(downloads_path + fname, pictures_path + fname)
