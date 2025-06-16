import random

low = 1
high = 100
opsi = ("batu", "kertas", "gunting")
kartu = ["1", "2", "3", "4", "5", "6", "7"]

'''
number = random.randint(low, high)
number = random.random()
'''
random.shuffle(kartu)

opsi = random.choice(opsi)
print(opsi)

