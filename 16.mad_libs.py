# Bu proje, eksik kelimelerle bir hikaye oluşturan bir program oluşturmayı içerir ve kullanıcıların kendi kelimelerini girerek benzersiz bir hikaye oluşturmasına izin verir.
# (This project involves creating a program that generates a story with missing words, allowing the user to fill in the blanks with their own words to create a unique story.)

print("Welcome! Please answer the following questions to start playing Mad Libs:\n")

name = input("Enter a name: ")
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adverb = input("Enter an adverb: ")

story = f"{name} was a {adjective} {noun} who loved to {verb} {adverb}. One day, while {verb}ing in the park, {name} met a {adjective} {noun} who was also {verb}ing {adverb}. They quickly became friends and decided to {verb} together every day."

print("\nHere's your completed story:\n")
print(story)
