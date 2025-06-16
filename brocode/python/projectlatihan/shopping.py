#shopping cart

foods = []
prices = []
total = 0

while True:
    food = input("enter a food you buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"enter a price of {food}: $"))
        foods.append(food)
        prices.append(price)
print("-----Your cart-----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price
    
print(f"your total is ${total}")
    