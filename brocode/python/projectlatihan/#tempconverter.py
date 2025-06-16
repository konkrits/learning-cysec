#tempconverter

unit = input("Celcius or Farenheit (C or F)? ")
temp = float(input("what is the temperature? "))

if unit == "C" or unit == "c":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"the temperature in Farenheit is {temp} F")
elif unit == "F" or unit == "f":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"the temperature in celcius is : {temp}")
else:
    print(f"unit {unit} is not valid")
    exit()