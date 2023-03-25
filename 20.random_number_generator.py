# Bu proje, belirli bir aralıkta rastgele sayılar üreten bir program oluşturmayı içerir.
# (This project involves creating a program that generates random numbers within a specified range.)

import random

user_min_num = int(input("Enter the minimum number: "))
user_max_num = int(input("Enter the maximum number: "))
user_nums = int(input("How many numbers do you want to generate? "))

numbers = random.sample(range(user_min_num, user_max_num+1), user_nums)
numbers.sort()
print("The generated numbers are:", numbers)