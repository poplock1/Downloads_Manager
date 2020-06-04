import os
import settings
import shutil


language = os.getenv('LANG')

if language[:2] == 'pl':

    downloads_directory = os.path.expanduser('~/Pobrane')
    documents_directory = os.path.expanduser('~/Dokumenty')
    movies_directory = os.path.expanduser('~/Wideo')
    pictures_direcotry = os.path.expanduser('~/Obrazy')
    music_directory = os.path.expanduser('~/Muzyka')
    archive_directory = os.path.expanduser('~/Archiwa')

if language[:2] == 'en':

    downloads_directory = os.path.expanduser('~/Downloads')
    documents_directory = os.path.expanduser('~/Documents')
    movies_directory = os.path.expanduser('~/Video')
    pictures_direcotry = os.path.expanduser('~/Pictures')
    music_directory = os.path.expanduser('~/Music')
    archive_directory = os.path.expanduser('~/Archives')

for filename in os.listdir(downloads_directory):
    for extension in settings.document_file_extensions_list:
        if filename.endswith(extension):
            shutil.move(f"{downloads_directory}/{filename}",
                        f"{documents_directory}/{filename}")
for filename in os.listdir(downloads_directory):
    for extension in settings.movie_file_extensions_list:
        if filename.endswith(extension):
            shutil.move(f"{downloads_directory}/{filename}",
                        f"{movies_directory}/{filename}")
for filename in os.listdir(downloads_directory):
    for extension in settings.music_file_extensions_list:
        if filename.endswith(extension):
            shutil.move(f"{downloads_directory}/{filename}",
                        f"{music_directory}/{filename}")
for filename in os.listdir(downloads_directory):
    for extension in settings.pictures_file_extensions_list:
        if filename.endswith(extension):
            shutil.move(f"{downloads_directory}/{filename}",
                        f"{pictures_direcotry}/{filename}")
for filename in os.listdir(downloads_directory):
    for extension in settings.archive_file_extensions_list:
        if filename.endswith(extension):
            shutil.move(f"{downloads_directory}/{filename}",
                        f"{archive_directory}/{filename}")
