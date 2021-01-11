from pytube import YouTube  # pip install pytube

import os

'''This function will make you download the video
It has two parameters :-
1)link of the video you want to download
2)location you want to store your file'''


def downloadYoutube(vid_url, store_path):
    yt = YouTube(vid_url)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    print(yt)
    if not os.path.exists(store_path):
        os.makedirs(store_path)

    yt.download(store_path)


url = input('Input url:\n')
store_path = input('Path to store file:\n')

downloadYoutube(url, store_path)
print("video Downloaded")
