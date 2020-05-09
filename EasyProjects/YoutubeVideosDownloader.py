from Lib.bcolors import bcolors
from pytube import YouTube

def YoutubeVideosDownloader():
    print(bcolors.HEADER + "Welcome to Youtube Videos Downloader" + bcolors.ENDC)

    link = input("enter link of youtube video: ")
    print("downloading video.... please wait while pytube downloads the video for you...")
    yt = YouTube(link)
    # videos = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1] .download()

    yt.streams.get_lowest_resolution().download()
