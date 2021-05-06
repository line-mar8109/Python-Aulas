from pytube import YouTube
import animation
from time import sleep

 # C:\Users\aline\Videos\DownloaderdoYouTube
link = str(input("Link do video: "))
yt = YouTube(link)

print('*'*50)
print('Video Title: ', yt.title)
print('Views: ', yt.views)
print('Duration: ', yt.length, 'seconds')
print('Assessment: ', yt.rating)
print('*'*50)

def progress(percent=0, width=30):
    hashes = width * percent // 100
    blanks = width - hashes
    print('\r[', hashes*'#', blanks*' ', ']', f' {percent:.0f}%', sep='',
        end='', flush=True)

yt.streams.get_highest_resolution().download('C://Users//aline//Videos//DownloaderdoYouTube')

print('Fazendo Download')
for i in range(101):
    progress(i)
    sleep(0.1)

print()
print('Download completo!!!')
