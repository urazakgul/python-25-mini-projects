# Bu proje, kullanıcıların okumak için Wikipedia'dan rastgele bir makale seçebilecekleri bir program oluşturmayı içerir.
# (This project involves creating a program that randomly selects an article from Wikipedia for the user to read.)

import wikipedia

while True:
    input_str = input("Do you want to read a random Wikipedia article? (Y/N): ")
    if input_str.upper() == "N":
        break
    elif input_str.upper() == "Y":
        try:
            page = wikipedia.random(pages=1)
            print("Selected article: ", page)
            content = wikipedia.page(page).content
            print(content)
        except wikipedia.exceptions.DisambiguationError as e:
            print("A disambiguation error occurred. Please try again.")
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")