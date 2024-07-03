from pytube import YouTube

# Example YouTube video URL
video_url = 'https://youtu.be/ajGo94h0JxE?si=WgOpE_radClZxeZM'

yt = YouTube(video_url)
stream = yt.streams.first()

# Download the video
stream.download(output_path='downloads')

print("Download completed successfully.")
