from pytube import YouTube

# C:\Userd\aline\Downloads
link = 'https://www.youtube.com/watch?v=_ysomCGaZLw'
path = input("Path aqui: ")
yt = YouTube(link)


print('titulo: ', yt.title)
print('Views: ', yt.views)
print('Tempo de duração: ', yt.length, 'segundos')
print('Avaliação: ', yt.rating)

ys = yt.streams.get_highest_resolution()

print('Baixando...')
ys.download(path)
print('Download completo!!!')
