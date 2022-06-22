from pytube import YouTube
import ffmpy
import os


def download(link, destination):
    try:
        yt = YouTube(link)

        video = yt.streams.get_audio_only()
        out = video.download(output_path=destination)

        base, ext = os.path.splitext(out)
        if convert_to_mp3(out, base + '.mp3', yt.title, True):
            print('Downloaded: ', yt.title)
    except:
        print('Error Downloading: ', link)


def convert_to_mp3(input_file, output_file, filename="The file", delete_original=False):
    is_converted_successfully = False
    if not os.path.exists(output_file):
        ff = ffmpy.FFmpeg(
            inputs={input_file: None},
            outputs={output_file: None}
        )
        ff.run()
        is_converted_successfully = True
    else:
        print(f'{filename} already exists. Delete the original and try again.')

    if delete_original:
        os.remove(input_file)

    return is_converted_successfully


def main():
    file = open("links.txt", "r")
    destination = file.readline().strip()

    for line in file:
        download(line.strip(), destination)


main()
