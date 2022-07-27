from pytube import YouTube
import ffmpy
import os
from datetime import datetime


now = datetime.now()


def download(link, destination='.', mime_type='mp4'):
    title = None
    if ',' in link:
        title = link[link.index(',') + 1:].strip() + '.mp4'
        link = link[:link.index(',')]

    try:
        yt = YouTube(link)
        if title is None:
            title = yt.title + '.mp4'

        video = yt.streams.get_highest_resolution()
        if not os.path.exists(destination + '/' + title):
            out = video.download(output_path=destination, filename=title)
            if mime_type == 'mp4':
                write_to_file(f'{link}, {title[:-4]}\n',
                              f'{destination}/mp4_download_list_{now}.txt')
                # print('Downloaded: ', title)
        elif mime_type == 'mp3':
            out = video.download(output_path=destination, filename='hadiuf729108349yhjksd.mp4')
            # this is a randomly generated name for a temporary file that the user is unlikely to have in their computer
        else:
            write_to_file(f'\'{title}\' already exists. Delete or rename the original file and try again.\n',
                          f'{destination}/error_log_{now}.txt')
            # print(f'\'{title}\' already exists. Delete or rename the original file and try again.')

        if mime_type == 'mp3':
            title = title[:-4] + '.mp3'
            if convert_to_mp3(out, title, destination, True):
                write_to_file(f'{link}, {title[:-4]}\n',
                              f'{destination}/mp3_download_list_{now}.txt')
                # print('Downloaded: ', title)
    except:
        # print('Error Downloading: ', link)
        write_to_file(f'Error Downloading: {title}\n',
                      f'{destination}/error_log_{now}.txt')


def convert_to_mp3(input_file, output_file, destination='.', delete_original=False):
    is_converted_successfully = False
    if not os.path.exists(destination + '/' + output_file):
        print('Downloading: ' + output_file)
        ff = ffmpy.FFmpeg(
            inputs={input_file: None},
            outputs={destination + '/' + output_file: None}
        )
        ff.run()
        is_converted_successfully = True
    else:
        # print(f'\'{output_file}\' already exists. Delete or rename the original file and try again.')
        print('I AM ERROR')
        write_to_file(f'\'{output_file}\' already exists. Delete or rename the original file and try again.\n',
                      f'{destination}/error_log_{now}.txt')

    if delete_original:
        os.remove(input_file)

    return is_converted_successfully


def write_to_file(message, file):
    (open(file, 'a')).write(message)


def main():
    mp3_links_file = open("mp3.txt", "r")
    destination = mp3_links_file.readline().strip()

    for line in mp3_links_file:
        download(line.strip(), destination, 'mp3')

    mp4_links_file = open("mp4.txt", "r")
    destination = mp4_links_file.readline().strip()

    for line in mp4_links_file:
        download(line.strip(), destination, 'mp4')


main()
