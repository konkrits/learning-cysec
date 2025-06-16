
#format specifier = {value:flags} memformat sebuah value berdasarkan bendera yang diinginkan

# .(number)f = round to that many decimal places (fixes point)
#:(number) = allocate that many spaces
#:03 = allocate and xero pad that many spaces
#:< = left justify
#:> = right justify
#:^ = center align 
#:+ = use aplus sign to indicate positive value
#:= = place sign to leftmost position 
#:  = insert a space before positive numbers
#:, = comma separator

price1 = 3.14519
price2 = -987.65
price3 = 12.34

print(f"Price 1 is {price1:.2f}")
print(f"Price 2 is {price2:,}")
print(f"Price 3 is {price3: }")