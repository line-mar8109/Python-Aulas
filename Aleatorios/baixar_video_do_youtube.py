from pytube import YouTube

 # C:\Users\aline\Videos\DownloaderdoYouTube
link = input("Link do video: ")
yt = YouTube(link)

print('*'*29)
print('Video Title: ', yt.title)
print('Views: ', yt.views)
print('Duration: ', yt.length, 'seconds')
print('Assessment: ', yt.rating)
print('*'*29)


print('Baixando.....................')
yt.streams.get_highest_resolution().download('C://Users//aline//Videos//DownloaderdoYouTube')
print('Download completo!!!')
