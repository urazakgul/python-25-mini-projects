# Bu proje, zar atmayı simüle eden bir program oluşturmayı içerir. Kullanıcı, atmak istediği zar sayısını seçebilir ve program sonuçları çıktı olarak verir.
# (This project involves creating a program that simulates rolling dice. The user can select the number of dice they want to roll and the program will output the results.)

import random

def roll_dice(number):
    for i in range(number):
        print("Dice",i+1,":",random.randint(1,6))

user_input = int(input("How many dice would you like to roll? "))
roll_dice(user_input)