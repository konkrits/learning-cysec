import time

mytime = int(input("enter the time: "))

for x in reversed(range(mytime)):
    second = x % 60
    minute = int(x / 60) % 60
    hour = int(x / 3600)
    print(f"{hour:02}:{minute:02}:{second:02}")
    time.sleep(1)

print("BAngun!")