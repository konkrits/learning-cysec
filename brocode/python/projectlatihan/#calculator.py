#calculator
#exercise from brocode

operator = input("Enter operator ( + - * /): ")

num = float(input("enter the number1: "))

num2 = float(input("enter the number2: "))

if operator == "+":
    result = num + num2
    print(result, 3)
    exit()
elif operator == "-":
    result = num - num2
    print(result, 3)
    exit()
elif operator == "*":
    result = num * num2
    print(result, 3)
    exit()
elif operator == "/":
    result = num / num2
    print(result, 3)
    exit()
else:
    print(f"that's not valid")
    exit()