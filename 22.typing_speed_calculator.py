# Bu proje, kullanıcının yazma hızını ve doğruluğunu ölçen bir program oluşturmayı içerir.
# (This project involves creating a program that measures the user's typing speed and accuracy.)

import time

input("Press Enter to begin.")

start_time = time.time()
user_text = "I’ve never found it hard to hack most people. If you listen to them, watch them, their vulnerabilities are like a neon sign." # Mr. Robot
print(user_text)
typed_text = input()
end_time = time.time()
time_taken = end_time - start_time
text_length = len(user_text)
typed_length = len(typed_text)
correct_chars = 0
for i in range(min(text_length, typed_length)):
    if user_text[i] == typed_text[i]:
        correct_chars += 1

accuracy = correct_chars / text_length * 100

print("Typing time:", round(time_taken, 2), "seconds")
print("Typing accuracy:", round(accuracy, 2), "%")
print("Typing speed:", round(typed_length / time_taken * 60), "words per minute")