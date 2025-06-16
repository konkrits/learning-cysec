#exercise

principle = 0
time = 0
rate = 0

"""
while principle <= 0 :
    principle = float(input("enter the principle amount: "))
    if principle <= 0 :
        print("principle can't be less than zero")

while rate <= 0 :
    rate = float(input("enter the rate: "))
    if rate <= 0 :
        print("principle can't be less than zero")

while time <= 0 :
    time = float(input("enter the time years: "))
    if time <= 0 :
        print("principle can't be less than zero")
"""

while True:
    principle = float(input("enter the principle amount: "))
    if principle <= 0 :
        print("principle can't be less than zero")
    else:
        break

while True:
    rate = float(input("enter the rate: "))
    if rate <= 0 :
        print("principle can't be less than zero")
    else:
        break

while True:
    time = float(input("enter the time years: "))
    if time <= 0 :
        print("principle can't be less than zero")
    else:
        break
        
total = principle * pow((1 + rate / 100), time)
print(f"balance after {time} year/s: ${total:.2f}")







