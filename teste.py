import pytube
from pytube import Youtube
url = input ('URL do vídeo: ')
yt = pytube.Youtube(url)
print ('Baixando', yt.title)
res = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
res.download()
print ('Download concluído !')
