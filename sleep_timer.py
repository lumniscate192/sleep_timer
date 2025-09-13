import os
import time

print("sleep_timer_v1 by lumi192\n\n")
print("Welcome to the sleep timer-!\n")

while True:
    try:
        sleep_minutes = int(input("How many mins before bro sleeps?\n"))
    except ValueError:
        print("That aint no number bro\n")
        continue

    if sleep_minutes in list(range(1, 121)): break
    print("That number aint in my list-\n")

print(f"Aight I gotchu, I'll close the pc after {sleep_minutes} mins, sleep tight-")

split = 5
timer = sleep_minutes
while timer > 0:
    time.sleep(60)
    timer -= 1

    if (sleep_minutes - timer) % split == 0:
        print(f"{timer} mins left!")
    
print("Time over- cya blud-")
os.system("shutdown /s /t 0")

