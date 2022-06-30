# YouTube-Downloader
Simple downloader for YouTube videos (Currently only mp3)

**Requirements**
1. pytube
2. ability to run .py files
3. ffmpy
4. FFmpeg
5. Make sure mp3.txt, mp4.txt and main.py are in the same folder

**Note**
- All videos you want downloaded as mp3 (audio only) will use mp3.txt. If you are not downloading any mp3 files, make sure mp3.txt is blank. 
- All videos you want downloaded as mp4 (audio and video) will use mp4.txt. If you are not downloading any mp4 files, make sure mp4.txt is blank.

**How to Use**
1. Make the very first line of the text file(s) the directory to which you want to install the songs to
2. Place the links you want to convert on separate lines after the first line
- If you want the downloaded video to have a specific name, put a comma after the link and then write the name you want (Example: https://www.youtube.com/watch?v=dQw4w9WgXcQ, Test Video)
- If you do not want a custom name, make sure the link is the only thing on each line
3. Run main.py
