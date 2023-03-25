# Bu proje, rastgele seçilen kelimeler ve ifadeler kullanarak bir hikaye oluşturan bir program oluşturmayı içerir.
# (This project involves creating a program that generates a story using randomly selected words and phrases.)

import random
import time

subjects = input("Please enter a list of subjects seperated by commas: ").split(", ")
verbs = input("Please enter a list of verbs seperated by commas: ").split(", ")
objects = input("Please enter a list of objects seperated by commas: ").split(", ")

print("Welcome to the Random Story Generator!")

while True:
    user_input = input("Press enter to continue or Q to quit...").lower()
    if user_input == "q":
        print("Exiting the Random Story Generator...")
        time.sleep(1)
        break

    subject = random.choice(subjects)
    verb = random.choice(verbs)
    object = random.choice(objects)

    story = f"{subject} {verb} {object}."

    time.sleep(1)
    print(story)

time.sleep(1)
print("Thank you for using the Random Story Generator!")