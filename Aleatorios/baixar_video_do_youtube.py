from pytube import YouTube

# C:\Userd\aline\Downloads
link = input("Link do video: ")
path = input("Path aqui: ")
yt = YouTube(link)

print('*'*29)
print('titulo: ', yt.title)
print('Views: ', yt.views)
print('Tempo de duração: ', yt.length, 'segundos')
print('Avaliação: ', yt.rating)
print('*'*29)

ys = yt.streams.get_highest_resolution()

print('Baixando........................')
ys.download(path)
print('Download completo!!!')
