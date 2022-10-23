import pytube
link=input("Enter YouTube video Link : ")
yt=pytube.YouTube(link)
yt.streams.first.download()
print('Downloaded',link)