from pytube import YouTube
import animation
import time

 # C:\Users\aline\Videos\DownloaderdoYouTube
link = str(input("Link do video: "))
yt = YouTube(link)

print('*'*29)
print('Video Title: ', yt.title)
print('Views: ', yt.views)
print('Duration: ', yt.length, 'seconds')
print('Assessment: ', yt.rating)
print('*'*29)

elipses = (
    '....                 ', '...........              ', '...........          ',
    '........             ', '..............           ', '...............      ',
    '............         ', '...................      ', '..................   ',
    '...................  ', '........................ ', '.....................'
)
@animation.wait(elipses, color='red')
def long_running_function():
    time.sleep(3)
    return
print('Baixando ', end='')
long_running_function()

yt.streams.get_highest_resolution().download('C://Users//aline//Videos//DownloaderdoYouTube')
print('Download completo!!!')
