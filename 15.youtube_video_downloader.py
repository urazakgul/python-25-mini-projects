# Bu proje, kullanıcının Youtube platformundan videoları indirebileceği bir program oluşturmayı içerir.
# (This project involves creating a program that allows the user to download videos from the Youtube platform.)

from pytube import YouTube

def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        print("Download completed successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

video_url = input("Enter the YouTube video URL: ")
download_video(video_url)