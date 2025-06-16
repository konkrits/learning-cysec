#foor loop = execute a block of code a fixed number of times
#            you can iterate range, string, sequence, etc

# for x in range(1, 11):
#    print(x)
# print("happy new year")
"""
bank = "1234-5678-9012-3456"

for x in bank:
    print(x)


for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)
"""

for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)