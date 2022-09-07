import youtube_dl

def download_as_mp3(vid_url):
    vid_info = youtube_dl.YoutubeDL().extract_info(url = vid_url, download=False)
    filename = f"{vid_info['title']}.mp3"
    options = {
        'format' : 'bestaudio/best',
        'keepvideo' : False,
        'outtmpl' : filename
    }

    with youtube_dl.YoutubeDL(options) as downloader:
        downloader.download([vid_info['webpage_url']])
    return filename

