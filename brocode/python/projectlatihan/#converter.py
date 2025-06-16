#converter

weight = float(input("what is your weight: "))
unit = input("Kilogram or Pounds? (K or L) : ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"your weight is {weight} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kg."
    print(f"your weight is {weight} {unit}")
else:
    print(f"unit {unit} is not valid")
    exit()
