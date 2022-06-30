from pytube import YouTube
import ffmpy
import os


def download_mp4(link, destination):
    title = None
    if ',' in link:
        title = link[link.index(',') + 1:].strip() + '.mp4'
        link = link[:link.index(',')]

    try:
        yt = YouTube(link)
        if title is None:
            title = yt.title + '.mp4'

        video = yt.streams.get_highest_resolution()
        if not os.path.exists(title):
            out = video.download(output_path=destination, filename=title)
            print('Downloaded: ', title)
        else:
            print(f'\'{title}\' already exists. Delete or rename the original file and try again.')
    except:
        print('Error Downloading: ', link)


def download_mp3(link, destination):
    title = None
    if ',' in link:
        title = link[link.index(',') + 1:].strip() + '.mp4'
        link = link[:link.index(',')]

    try:
        yt = YouTube(link)
        if title is None:
            title = yt.title + '.mp4'

        video = yt.streams.get_audio_only()
        if not os.path.exists(title):
            out = video.download(output_path=destination, filename=title)
        else:
            out = video.download(output_path=destination, filename='hadiuf729108349yhjksd.mp4')
            # this is a randomly generated name for a temporary file that the user is unlikely to have in their computer

        title = title[:-4] + '.mp3'
        if convert_to_mp3(out, title, destination , True):
            print('Downloaded: ', title)
    except:
        print('Error Downloading: ', link)


def convert_to_mp3(input_file, output_file, destination = '.', delete_original=False):
    is_converted_successfully = False
    if not os.path.exists(output_file):
        ff = ffmpy.FFmpeg(
            inputs={input_file: None},
            outputs={destination + '/' + output_file: None}
        )
        ff.run()
        is_converted_successfully = True
    else:
        print(f'\'{output_file}\' already exists. Delete or rename the original file and try again.')

    if delete_original:
        os.remove(input_file)

    return is_converted_successfully


def main():
    mp3_links_file = open("mp3.txt", "r")
    destination = mp3_links_file.readline().strip()

    for line in mp3_links_file:
        download_mp3(line.strip(), destination)

    mp4_links_file = open("mp4.txt", "r")
    destination = mp4_links_file.readline().strip()

    for line in mp4_links_file:
        download_mp4(line.strip(), destination)


main()
