import pafy
from pafy import new

print("powered by SASKE Company")
print("0 = exit program")
print("1 = download video from youtube")
print("2 = download audio from youtube")
print("enter your choise ")
x = int(input()) 
if(x==1):
    print("enter your video's link: ")
    video = new(str(input()))
    stream =  video.streams
    for i in stream:
        print(i)
    print("enter your value of streams start by zero number: ")
    value=int(input())
    print("enter location of downloaded videos")
    path=str(input())
    stream[value].download(filepath=path)
elif(x==2):
    print("enter your audio's link: ")
    audio = new(str(input()))
    stream = audio.getbestaudio()
    print("enter location of downloaded songs")
    path=str(input())
    stream.download(filepath=path)
elif(x==0):
    print("the program closed !! visit us agine.")
    exit()
else:
    print("not!!")