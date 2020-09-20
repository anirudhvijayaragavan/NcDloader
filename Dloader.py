from tkinter import filedialog

from pytube import YouTube as y

link = input("Enter the link:" )
vid = y(link)

def getVideos(stream):
    if (stream == 1):
        try:
            vdo = vid.streams.get_by_itag('137')
            return vdo
        except Exception:
            print("The video is not available in the selected quality.Please select another quality!")
            stream = int(input())
            getVideos(stream)
    elif (stream == 2):
        try:
            vdo = vid.streams.get_by_itag('22')
            return vdo
        except Exception:
            print("The video is not available in the selected quality.Please select another quality!")
            stream = int(input())
            getVideos()
    elif (stream == 3):
        try:
            vdo = vid.streams.get_by_itag('18')
            return vdo
        except Exception:
            print("The video is not available in the selected quality.Please select another quality!")
            stream = int(input())
            getVideos(stream)
    elif (stream == 4):
        try:
            vdo = vid.streams.get_by_itag('36')
            return vdo
        except Exception:
            print("The video is not available in the selected quality.Please select another quality!")
            stream = int(input())
            getVideos(stream)
    elif (stream == 5):
        try:
            vdo = vid.streams.get_by_itag('17')
            return vdo
        except Exception:
            print("The video is not available in the selected quality.Please select another quality!")
            stream = int(input())
            getVideos(stream)
    elif (stream == 6):
        try:
            vdo = vid.streams.get_by_itag('251')
            return vdo
        except Exception:
            print("The video is not available in the selected quality.Please select another quality!")
            stream = int(input())
            getVideos(stream)
    elif (stream == 7):
        try:
            vdo = vid.streams.get_by_itag('140')
            return vdo
        except Exception:
            print("The video is not available in the selected quality.Please select another quality!")
            stream = int(input())
            getVideos(stream)
    elif (stream == 8):
        try:
            vdo = vid.streams.get_by_itag('250')
            return vdo
        except Exception:
            print("The video is not available in the selected quality.Please select another quality!")
            stream = int(input())
            getVideos(stream)
    elif (stream == 9):
        try:
            vdo = vid.streams.get_by_itag('249')
            return vdo
        except Exception:
            print("The video is not available in the selected quality.Please select another quality!")
            stream = int(input())
            getVideos(stream)

def downPath():
    path = filedialog.askdirectory()
    return path

#print(vid.title)
print("Choose the video format:\n 1.1080p\n 2.720p\n 3.360p\n 4.240p\n 5.144p\n 6.Audio only(160 kbps)\n 7.Audio only(128 kbps)\n 8.Audio only(70 kbps)\n 9.Audio only(50 kbps)")
quality = int(input())
result = getVideos(quality)
path = downPath()
print("Downloading...")
result.download(path)
print("Download completed!")
