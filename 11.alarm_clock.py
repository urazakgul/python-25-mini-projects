# Bu proje, kullanıcının alarm kurmasına ve alarm çaldığında bildirim almasına olanak tanıyan bir program oluşturmayı içerir.
# (This project involves creating a program that acts as an alarm clock, allowing the user to set alarms and receive notifications when the alarm goes off.)

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