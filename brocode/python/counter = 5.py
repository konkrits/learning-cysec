largest_number = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to end the program: "))

if counter:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")

'''
count = 0

while count < 100:
    count += 1
print(count)





counter = 5
while counter:
    print("inside the loop", counter)
    counter -= 1
print("outside the loop", counter)


secret = 1515
hitung = 0

user = int(input("enter secret number : "))

while user != secret:
    print("infinite loop")
    user = int(input("enter secret number : "))
    hitung += 1 
print("good job bro")
print("hitungan salahmu : ", hitung)
'''

