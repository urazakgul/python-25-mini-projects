# Bu proje, kullanıcının bilgisayara karşı taş-kağıt-makas oyunu oynayabileceği bir oyun oluşturmayı içerir.
# (This project involves creating a game where the user can play against the computer in a game of rock-paper-scissors.)

import random
import time

def get_user_choice():
    user_choice = input("Rock (R), Paper (P), or Scissors (S)? Press Q to Quit. ").lower()
    while user_choice not in ["r","p","s","q"]:
        user_choice = input("Please enter a valid choice (R, P, or S) or press Q to Quit. ").lower()
    return user_choice

def get_computer_choice():
    computer_choice = random.choice(["r","p","s"])
    return computer_choice

def who_is_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif user_choice == "r" and computer_choice == "s":
        return "user"
    elif user_choice == "p" and computer_choice == "r":
        return "user"
    elif user_choice == "s" and computer_choice == "p":
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        if user_choice == "q":
            break
        computer_choice = get_computer_choice()
        winner = who_is_winner(user_choice,computer_choice)
        if winner == "user":
            user_score += 1
            print("You won!")
        elif winner == "computer":
            computer_score += 1
            print("You lost!")
        else:
            print("It's a tie!")
        time.sleep(1)
        print(f"User: {user_score} - Computer: {computer_score}")

play_game()