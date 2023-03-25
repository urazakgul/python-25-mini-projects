# Bu proje, kullanıcının doğum tarihine ve mevcut tarihe dayanarak yaşını hesaplayan bir program oluşturmayı içerir.
# (This project involves creating a program that calculates the user's age based on their birthdate and the current date.)

import datetime

birthdate = input("Enter your birthdate (DD/MM/YYYY): ")
birthdate = datetime.datetime.strptime(birthdate, "%d/%m/%Y").date()
today = datetime.date.today()
age_delta = today - birthdate
years = age_delta.days // 365
months_remaining = age_delta.days % 365
months = months_remaining // 30
days = months_remaining % 30
print("Your age is: {} years, {} months, and {} days".format(years, months, days))