#to install , type : 
# pip install yt-dlp
import yt_dlp
url = input("ENTER URL :")
ydl_opts = {
    'outtmpl': r'C:\\Users\\khoul\\Downloads\\hazymoon.%(ext)s',
} #to save the video
with yt_dlp.YoutubeDL(ydl_opts) as yt:
    yt.download([url])