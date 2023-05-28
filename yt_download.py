from pytube import YouTube
from sys import argv

link = input("Paste link here: ")
yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)

res = int(input("Choose the resolution (0-lowest, 1-highest): "))

yd = yt.streams.get_highest_resolution()

yd.download("/Users/user/Downloads/YouTube")