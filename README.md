1. Bu proje, zar atmayı simüle eden bir program oluşturmayı içerir. Kullanıcı, atmak istediği zar sayısını seçebilir ve program sonuçları çıktı olarak verir. (This project involves creating a program that simulates rolling dice. The user can select the number of dice they want to roll and the program will output the results.)

```python
import random

def roll_dice(number):
    for i in range(number):
        print("Dice",i+1,":",random.randint(1,6))

user_input = int(input("How many dice would you like to roll? "))
roll_dice(user_input)
```

2. Bu proje, kullanıcının belirli bir aralıkta rastgele oluşturulan bir sayıyı tahmin etmesi gereken bir oyun oluşturmayı içerir. Program, kullanıcının tahminlerini daraltmalarına yardımcı olacak geri bildirimler sağlar. (This project involves creating a game where the user has to guess a randomly generated number within a certain range. The program will provide feedback to the user to help them narrow down their guesses.)

```python
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
```

3. Bu proje, belirli bir metindeki kelime ve karakter sayısını sayan bir program oluşturmayı içerir. (This project involves creating a program that counts the number of words and characters in a given text.)

```python
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
```

4. Bu proje, bir cümleyi veya kelime öbeğini alıp her kelimenin ilk harfinden bir akronim oluşturan bir program oluşturmayı içerir. (This project involves creating a program that takes a phrase or sentence and generates an acronym from the first letter of each word.)

```python
def create_acronym(user_text):
    words = user_text.split()
    acronym = ''.join(word[0].upper() for word in words)
    return acronym

user_text = input("Please enter a sentence or phrase: ")
print(create_acronym(user_text))
```

5. Bu proje, kullanıcının bilgisayara karşı taş-kağıt-makas oyunu oynayabileceği bir oyun oluşturmayı içerir. (This project involves creating a game where the user can play against the computer in a game of rock-paper-scissors.)

```python
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
```

6. Bu proje, belirli bir uzunluk ve karmaşıklıkta rastgele bir şifre oluşturan bir program oluşturmayı içerir. (This project involves creating a program that generates a random password with a specified length and complexity.)

```python
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
```

7. Bu proje, sıralanmış bir listede bir öğeyi aramak için ikili arama algoritmasını uygulayan bir program oluşturmayı içerir. (This project involves creating a program that implements the binary search algorithm to search for an item in a sorted list.)

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid

    return -1


arr = [int(target) for target in input("Enter a sorted list of numbers separated by commas: ").split(",")]
target = int(input("Enter the target value: "))

result = binary_search(arr, target)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")
```

8. Bu proje, rastgele seçilen kelimeler ve ifadeler kullanarak bir hikaye oluşturan bir program oluşturmayı içerir. (This project involves creating a program that generates a story using randomly selected words and phrases.)

```python
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
```

9. Bu proje, kullanıcının bilgisayarından e-posta (Outlook) göndermesine izin veren bir program oluşturmayı içerir. (This project involves creating a program that allows the user to send emails (Outlook) from their computer.)

```python
#Python'da Outlook kullanarak mail göndermek için bilgisayarınızda Outlook'un kurulu olması gerekiyor.
#In order to send emails using Outlook in Python, you need to have Outlook installed on your computer.

import win32com.client as client

# Start Outlook
outlook = client.Dispatch('Outlook.Application')

# Create a new email
email = outlook.CreateItem(0)

# Set the recipients
email.To = 'receiver_mail_address'

# Set the subject
email.Subject = 'Test Email'

# Set the body
email.Body = 'Hello,\n\nThis is a test message.'

# Add attachment (optional)
email.Attachments.Add('C:/...')

# Send the email
email.Send()
```

10. Bu proje, kullanıcının alarm kurmasına ve alarm çaldığında bildirim almasına olanak tanıyan bir program oluşturmayı içerir. (This project involves creating a program that acts as an alarm clock, allowing the user to set alarms and receive notifications when the alarm goes off.)

```python
import datetime
import time
import wave
import pyaudio

alarm_time = input("Enter the alarm time in 'hh:mm:ss' format: ")

alarm_hour = int(alarm_time[0:2])
alarm_minute = int(alarm_time[3:5])
alarm_second = int(alarm_time[6:8])

print("Alarm set for " + alarm_time)

wave_file = wave.open("wake_up.wav", 'rb')
chunk = 1024

p = pyaudio.PyAudio()

def play_sound(wave_file, chunk, p):
    stream = p.open(format=p.get_format_from_width(wave_file.getsampwidth()),
                channels=wave_file.getnchannels(),
                rate=wave_file.getframerate(),
                output=True)

    data = wave_file.readframes(chunk)

    while data:
        stream.write(data)
        data = wave_file.readframes(chunk)

    stream.stop_stream()
    stream.close()

    p.terminate()

while True:
    now = datetime.datetime.now()
    current_hour = now.hour
    current_minute = now.minute
    current_second = now.second

    if(alarm_hour == current_hour and
       alarm_minute == current_minute and
       alarm_second == current_second):
        play_sound(wave_file, chunk, p)
        time.sleep(wave_file.getnframes() / wave_file.getframerate())
        break
    time.sleep(1)

wave_file.close()
```

11. Bu proje, uzun URL'leri paylaşması ve hatırlaması daha kolay hale getiren kısa URL'ler oluşturan bir program oluşturmayı içerir. (This project involves creating a program that shortens long URLs into shorter ones that are easier to share and remember.)

```python
import random
import string

url_database = {}

def shorten_url(long_url):
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choices(characters, k=6))
    url_database[short_url] = long_url
    return short_url

def get_long_url(short_url):
    return url_database.get(short_url)

long_url = input("Enter a long URL: ")
short_url = shorten_url(long_url)

print("Short URL:", short_url)
print("To retrieve the original long URL, enter the short URL below:")
user_input = input()
print("Long URL:", get_long_url(user_input))
```

12. Bu proje, belirli bir konum için mevcut hava koşullarını ve tahminleri gösteren bir program oluşturmayı içerir. (This project involves creating a program that displays the current weather conditions and forecast for a specified location.)

```python
# API Key: https://home.openweathermap.org/users/sign_up

import requests

api_key = input("Please enter your OpenWeatherMap API key: ")
city = input("Please enter a city: ")
city = city.capitalize()

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
response = requests.get(url)
data = response.json()

temp_kelvin = data["main"]["temp"]
humidity = data["main"]["humidity"]
temp_celsius = temp_kelvin - 273.15
weather = data["weather"][0]["description"].capitalize()

print(f"Current weather in {city}: {weather}.")
print(f"Temperature: {temp_celsius:.1f} Celsius")
print(f"Humidity: {humidity}%.")

num_forecasts = int(input("How many weather forecasts would you like to see? "))

forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
forecast_response = requests.get(forecast_url)
forecast_data = forecast_response.json()

for i in range(num_forecasts):
    date = forecast_data["list"][i]["dt_txt"]
    forecast_temp_kelvin = forecast_data["list"][i]["main"]["temp"]
    forecast_temp_celsius = forecast_temp_kelvin - 273.15
    forecast_weather = forecast_data["list"][i]["weather"][0]["description"].capitalize()
    print(f"Date: {date}. Weather forecast: {forecast_weather}. Temperature forecast: {forecast_temp_celsius:.1f} Celsius")
```

13. Bu proje, kullanıcının masaüstünde bildirimler gösteren bir program oluşturmayı içerir. (This project involves creating a program that displays notifications on the user's desktop.)

```python
import time
import datetime
from plyer import notification

while True:
    now = datetime.datetime.now()

    if now.minute % 5 == 0:
        notification.notify(
            title="Time to Drink Water!",
            message="Remember to drink water every 5 minutes.",
            # Tabi ki test için böyle yazdım.
            # Of course, I wrote it for testing purposes.
            app_name="Water Reminder",
            timeout=10
        )

    time.sleep(300)
```

14. Bu proje, kullanıcının yaptığı tüm klavye girdilerini kaydeden bir program oluşturmayı içerir. (This project involves creating a program that records all keyboard inputs made by the user.)

```python
from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener :
    listener.join()
```

15. Bu proje, eksik kelimelerle bir hikaye oluşturan bir program oluşturmayı içerir ve kullanıcıların kendi kelimelerini girerek benzersiz bir hikaye oluşturmasına izin verir. (This project involves creating a program that generates a story with missing words, allowing the user to fill in the blanks with their own words to create a unique story.)

```python
print("Welcome! Please answer the following questions to start playing Mad Libs:\n")

name = input("Enter a name: ")
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adverb = input("Enter an adverb: ")

story = f"{name} was a {adjective} {noun} who loved to {verb} {adverb}. One day, while {verb}ing in the park, {name} met a {adjective} {noun} who was also {verb}ing {adverb}. They quickly became friends and decided to {verb} together every day."

print("\nHere's your completed story:\n")
print(story)
```

16. Bu proje, kullanıcının Youtube platformundan videoları indirebileceği bir program oluşturmayı içerir. (This project involves creating a program that allows the user to download videos from the Youtube platform.)

```python
from pytube import YouTube

def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        print("Download completed successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

video_url = input("Enter the YouTube video URL: ")
download_video(video_url)
```

17. Bu proje, kullanıcıların okumak için Wikipedia'dan rastgele bir makale seçebilecekleri bir program oluşturmayı içerir. (This project involves creating a program that randomly selects an article from Wikipedia for the user to read.)

```python
import wikipedia

while True:
    input_str = input("Do you want to read a random Wikipedia article? (Y/N): ")
    if input_str.upper() == "N":
        break
    elif input_str.upper() == "Y":
        try:
            page = wikipedia.random(pages=1)
            print("Selected article: ", page)
            content = wikipedia.page(page).content
            print(content)
        except wikipedia.exceptions.DisambiguationError as e:
            print("A disambiguation error occurred. Please try again.")
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")
```

18. Bu proje, kullanıcıların paylaşmak ve tarayabilecekleri QR kodları oluşturabilecekleri bir program oluşturmayı içerir. (This project involves creating a program that generates QR codes for the user to share and scan.)

```python
import qrcode

data = "https://twitter.com/urazdev"
img = qrcode.make(data)
img.show()
```

19. Bu proje, sayıları Roma rakamlarına ve Roma rakamlarını sayılara dönüştüren bir program oluşturmayı içerir. (This project involves creating a program that converts numbers to Roman numerals and vice versa.)

```python
def roman_to_int(roman_numeral):
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0
    prev_value = 0
    for char in roman_numeral:
        current_value = roman_dict[char]
        if current_value > prev_value:
            total += current_value - 2 * prev_value
        else:
            total += current_value
        prev_value = current_value
    return total


roman_numeral = input("Please enter a Roman numeral: ")
if not all(char in "IVXLCDM" for char in roman_numeral):
    print("Please enter a valid Roman numeral.")
else:
    integer = roman_to_int(roman_numeral)
    print(f"{roman_numeral} = {integer}")
```

20. Bu proje, belirli bir aralıkta rastgele sayılar üreten bir program oluşturmayı içerir. (This project involves creating a program that generates random numbers within a specified range.)

```python
import random

user_min_num = int(input("Enter the minimum number: "))
user_max_num = int(input("Enter the maximum number: "))
user_nums = int(input("How many numbers do you want to generate? "))

numbers = random.sample(range(user_min_num, user_max_num+1), user_nums)
numbers.sort()
print("The generated numbers are:", numbers)
```

21. Bu proje, kullanıcının doğum tarihine ve mevcut tarihe dayanarak yaşını hesaplayan bir program oluşturmayı içerir. (This project involves creating a program that calculates the user's age based on their birthdate and the current date.)

```python
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
```

22. Bu proje, kullanıcının yazma hızını ve doğruluğunu ölçen bir program oluşturmayı içerir. (This project involves creating a program that measures the user's typing speed and accuracy.)

```python
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
```

23. Bu proje, Sudoku bulmacaları oluşturan ve çözen bir program oluşturmayı içerir. (This project involves creating a program that generates and solves Sudoku puzzles.)

```python
def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


def valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print_board(board)
solve(board)
print("\n\n")
print_board(board)
```

24. Bu proje, kullanıcının internetten resim indirebileceği bir program oluşturmayı içerir. (This project involves creating a program that allows the user to download images from the internet.)

```python
import requests
import os

url = input("Enter a URL: ")
filename = input("Enter a file name: ")
file_extension = input("Enter a file extension (e.g. jpg, png): ")
response = requests.get(url)

if response.status_code == 200:
    download_dir = "downloads"
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    filepath = os.path.join(download_dir, filename + "." + file_extension)
    with open(filepath, "wb") as f:
        f.write(response.content)
    print("Image successfully downloaded.")
else:
    print("Image could not be downloaded.")
```

25. Bu proje, bir şifrenin gücünü ve karmaşıklığını kontrol eden ve kullanıcıya geri bildirim sağlayan bir program oluşturmayı içerir. (This project involves creating a program that checks the strength and complexity of a password and provides feedback to the user.)

```python
import string

def check_password_strength(password):
    if len(password) < 8:
        return 'Password must be at least 8 characters long.'
    elif not any(char.isdigit() for char in password):
        return 'Password must contain at least one digit character.'
    elif not any(char.isupper() for char in password):
        return 'Password must contain at least one uppercase character.'
    elif not any(char.islower() for char in password):
        return 'Password must contain at least one lowercase character.'
    elif not any(char in string.punctuation for char in password):
        return 'Password must contain at least one special character.'
    else:
        return 'Password is strong and complex!'

password = input('Enter a password: ')
strength = check_password_strength(password)
print(strength)
```