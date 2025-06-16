# nestedloop = loop inside loop
#             outer :
#                     inner:
'''
for y in range(3):
    for x in range(1, 10):
        print(x, end="")
    print()
'''

counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

