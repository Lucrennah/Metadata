import os

if True:
    route = r"C:\Users\baron\desktop\dossier"
    l_archive = sorted([archive.name for archive in os.scandir(route) if archive.is_file()])

    base_command_string = r"c:\ffmpeg\bin\ffmpeg.exe -i"
    end_command_string = r'-codec copy -metadata title="" '


    for file in l_archive:
        new_file_name = str(file) + ".new.mkv"
        os.system(base_command_string + " " + str(file) + " "+ end_command_string + new_file_name)