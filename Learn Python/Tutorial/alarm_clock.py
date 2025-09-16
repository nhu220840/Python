# Python alarm clock

import time
import datetime
import pygame
import os

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "./Learn python/Tutorial/lofi-alarm-clock-243766.mp3"

    # isExist = os.path.exists(sound_file)
    # print(isExist)

    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP!!! ⏰")

            # Khoi tao sound
            pygame.mixer.init()
            # Load sound
            pygame.mixer.music.load(sound_file)
            # Play sound
            pygame.mixer.music.play()

            # Khi nao sound van chua het thi chuong trinh van chua ket thuc, se ket thuc khi phat het sound
            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False

        time.sleep(1)

if __name__ == '__main__':
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
    