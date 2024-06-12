from pytube import YouTube
from sys import argv

link = argv[0]
yt = YouTube(link)

print("title", yt.title)

print("views",yt.views)
print("likes",yt.likes)

yd = yt.streams.get_highest_resolution()

yd.download()