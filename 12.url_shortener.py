# Bu proje, uzun URL'leri paylaşması ve hatırlaması daha kolay hale getiren kısa URL'ler oluşturan bir program oluşturmayı içerir.
# (This project involves creating a program that shortens long URLs into shorter ones that are easier to share and remember.)

import random
import string

url_database = {}

def shorten_url(long_url):
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choices(characters, k=6))
    url_database[short_url] = long_url
    return short_url

def get_long_url(short_url):
    return url_database.get(short_url)

long_url = input("Enter a long URL: ")
short_url = shorten_url(long_url)

print("Short URL:", short_url)
print("To retrieve the original long URL, enter the short URL below:")
user_input = input()
print("Long URL:", get_long_url(user_input))