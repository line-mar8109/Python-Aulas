from pytube import YouTube

 # C:\Users\aline\Videos\Downloader do YouTube
link = input("Link do video: ")
path = 'C://Users//aline//Videos//DownloaderdoYouTube'
yt = YouTube(link)

print('*'*29)
print('Video Title: ', yt.title)
print('Views: ', yt.views)
print('Duration: ', yt.length, 'seconds')
print('Assessment: ', yt.rating)
print('*'*29)

ys = yt.streams.get_highest_resolution()

print('Baixando....................')
ys.download(path)
print('Download completo!!!')
