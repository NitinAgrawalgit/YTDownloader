import yt_dlp

url = input("Enter URL: ")

ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': '/Downloads/%(title)s.%(ext)s'  # Output template
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

#If you want ffmpeg to convert the final format to .mp4, add the following code to the ydl_opts dictionary:
#'postprocessors': [{
#        'key': 'FFmpegVideoConvertor',
#        'preferedformat': 'mp4'
#        }]