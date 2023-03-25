# Bu proje, belirli bir uzunluk ve karmaşıklıkta rastgele bir şifre oluşturan bir program oluşturmayı içerir.
# (This project involves creating a program that generates a random password with a specified length and complexity.)

import random
import string
import time

def generate_password():
    lower = input("Use lowercase letters? (Y/N): ").lower()
    upper = input("Use uppercase letters? (Y/N): ").lower()
    numbers = input("Use numbers? (Y/N): ").lower()
    symbols = input("Use special characters? (Y/N): ").lower()

    if lower == "n" and upper == "n" and numbers == "n" and symbols == "n":
        print("You must select at least one character type!")
    else:
        selected_types = [lower, upper, numbers, symbols]
        selected_chars = [string.ascii_lowercase if lower == "y" else "",
                          string.ascii_uppercase if upper == "y" else "",
                          string.digits if numbers == "y" else "",
                          string.punctuation if symbols == "y" else ""]

        total_length = 0
        for chars in selected_chars:
            if chars:
                total_length += len(chars)

        print(f"Password length should be at most {total_length} characters long.")
        time.sleep(1)
        length = int(input("Enter the length of the password: "))

        if length > total_length:
            print("Password length is too long!")
            return

        all_chars = "".join(selected_chars)

        user_password = "".join(random.sample(all_chars, length))
        return user_password

user_password = generate_password()
print(user_password)