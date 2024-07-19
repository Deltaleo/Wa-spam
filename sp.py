from time import sleep
import os

t = ['doooooooooorrrrrrr', 'boooooooooom', 'Duarrrrrrrrrrrrr']

sleep(4)  # Tunggu 4 detik sebelum memulai
for i in range(30):
    message = t[i % len(t)]
    os.system(f'adb shell input text "{message}"')
    os.system('adb shell input keyevent 66')  # Keyevent 66 adalah tombol Enter
    sleep(0.3)