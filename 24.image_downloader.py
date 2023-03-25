# Bu proje, kullanıcının internetten resim indirebileceği bir program oluşturmayı içerir.
# (This project involves creating a program that allows the user to download images from the internet.)

import requests
import os

url = input("Enter a URL: ")
filename = input("Enter a file name: ")
file_extension = input("Enter a file extension (e.g. jpg, png): ")
response = requests.get(url)

if response.status_code == 200:
    download_dir = "downloads"
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    filepath = os.path.join(download_dir, filename + "." + file_extension)
    with open(filepath, "wb") as f:
        f.write(response.content)
    print("Image successfully downloaded.")
else:
    print("Image could not be downloaded.")