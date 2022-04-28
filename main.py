import os

route = './'
l_archive = sorted([archive.name for archive in os.scandir(route) if archive.is_file()])


def edit_media_data():
    for f in range(0, len(l_archive[:-1])):
        os.system(f"c:/users/baron/desktop/ffmpeg/bin/ffmpeg.exe -i '{l_archive[f]}' -codec copy -metadata title='' '{l_archive[f]}.new'")
        os.system(f"rename '{l_archive[f]}.new' '{l_archive[f]}")