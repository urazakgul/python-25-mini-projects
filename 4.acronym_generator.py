# Bu proje, bir cümleyi veya kelime öbeğini alıp her kelimenin ilk harfinden bir akronim oluşturan bir program oluşturmayı içerir.
# (This project involves creating a program that takes a phrase or sentence and generates an acronym from the first letter of each word.)

def create_acronym(user_text):
    words = user_text.split()
    acronym = ''.join(word[0].upper() for word in words)
    return acronym

user_text = input("Please enter a sentence or phrase: ")
print(create_acronym(user_text))