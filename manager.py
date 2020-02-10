import os
import shutil

downloads_directory = '/home/poplock/Pobrane/'
documents_directory = '/home/poplock/Dokumenty'
movies_directory = '/home/poplock/Wideo'
pictures_direcotry = '/home/poplock/Obrazy'
music_directory = '/home/poplock/Muzyka'
archive_directory = '/home/poplock/Archiwa'

document_file_extensions_list = ['.doc', '.docx', '.txt', '.pdf', '.odt']
movie_file_extensions_list = ['.mp4', '.mov', '.avi', '.flv', '.mkv']
music_file_extensions_list = ['.mp3', '.wav', '.flac']
pictures_file_extensions_list = ['.jpg', '.gif', '.png']
archive_file_extensions_list = ['.7z', '.zip', '.rar']

for filename in os.listdir(downloads_directory):
    for extension in document_file_extensions_list:
        if filename.endswith(extension):
            shutil.move(f"{downloads_directory}/{filename}", f"{documents_directory}/{filename}")
for filename in os.listdir(downloads_directory):
    for extension in movie_file_extensions_list:
        if filename.endswith(extension):
            shutil.move(f"{downloads_directory}/{filename}", f"{movies_directory}/{filename}")
for filename in os.listdir(downloads_directory):
    for extension in music_file_extensions_list:
        if filename.endswith(extension):
            shutil.move(f"{downloads_directory}/{filename}", f"{music_directory}/{filename}")
for filename in os.listdir(downloads_directory):
    for extension in pictures_file_extensions_list:
        if filename.endswith(extension):
            shutil.move(f"{downloads_directory}/{filename}", f"{pictures_direcotry}/{filename}")
for filename in os.listdir(downloads_directory):
    for extension in archive_file_extensions_list:
        if filename.endswith(extension):
            shutil.move(f"{downloads_directory}/{filename}", f"{archive_directory}/{filename}")
