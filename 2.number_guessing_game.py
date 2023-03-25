# Bu proje, kullanıcının belirli bir aralıkta rastgele oluşturulan bir sayıyı tahmin etmesi gereken bir oyun oluşturmayı içerir. Program, kullanıcının tahminlerini daraltmalarına yardımcı olacak geri bildirimler sağlar.
# (This project involves creating a game where the user has to guess a randomly generated number within a certain range. The program will provide feedback to the user to help them narrow down their guesses.)

import random
import time

user_input_min = int(input("Enter the minimum number of the range: "))
user_input_max = int(input("Enter the maximum number of the range: "))

random_number = random.randint(user_input_min, user_input_max)

count = 0
user_numbers = []

while True:
    user_guess = int(input("Guess the number between {} and {}: ".format(user_input_min, user_input_max)))

    if user_guess == random_number:
        count += 1
        user_numbers = []
        if count == 1:
            print("You rock! You guessed the number in {} try ^_^ The number was: {}".format(count, random_number))
        else:
            print("You rock! You guessed the number in {} tries ^_^ The number was: {}".format(count, random_number))
        time.sleep(1)
        play_again = input("Do you want to play again? (Y/N): ")
        if play_again.lower() == "y":
            user_input_min = int(input("Enter the minimum number of the range: "))
            user_input_max = int(input("Enter the maximum number of the range: "))
            random_number = random.randint(user_input_min, user_input_max)
            count = 0
            user_numbers = []
            continue
        else:
            time.sleep(1)
            print("Okay, have a nice day!")
            break
    elif user_guess < random_number:
        user_numbers.append(user_guess)
        user_numbers.sort()
        count += 1
        print("The number is higher than your guess.")
        print("Your previous guesses: {}".format(user_numbers))
        time.sleep(1)
    elif user_guess > random_number:
        user_numbers.append(user_guess)
        user_numbers.sort()
        count += 1
        print("The number is lower than your guess.")
        print("Your previous guesses: {}".format(user_numbers))
        time.sleep(1)