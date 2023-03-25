# Bu proje, belirli bir metindeki kelime ve karakter sayısını sayan bir program oluşturmayı içerir.
# (This project involves creating a program that counts the number of words and characters in a given text.)

user_text = input("Please enter some text: ")
count_type = input("Do you want to count words (W) or characters (C)? (W/C): ")

if count_type.lower() == "w":
    word_count = len(user_text.split())
    print("Number of words in the text: {}".format(word_count))
elif count_type.lower() == "c":
    char_count = len(user_text)
    print("Number of characters in the text: {}".format(char_count))
else:
    print("Please choose either 'W' or 'C' as the counting type.")