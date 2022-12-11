from pytube import *

def downloader(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution() # gets highest quailty it can get

    try: 
        youtubeObject.download() # downloads the videos  
    except: 
        print("An error was caused while downloading")
    print("Download is down enjoy!")

link = input("Youtube link you wish to download: ")
downloader(link)
