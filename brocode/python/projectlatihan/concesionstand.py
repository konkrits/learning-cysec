#latihan

#dictionary
menu = {"latte": 24.000,
        "cappucino": 15.000,
        "milk": 20.000,
        "red velvet": 25.000}

keranjang = []
total = 0

print("-------------menu----------------")

#menampilkan kunci dan nilai di menu
for key, value in menu.items():
    print(f"{key:20} Rp.{value:.3f}")

print("---------------------------------")

#jika kondisi ini benar dan ini memang benar
while True:
    beli = input("pilih item (q untuk keluar)").lower() #input user 
    if beli == "q" or beli == "quit":                       #jika user mengetik q dan quit maka akan putus
        break
    elif menu.get(beli) is not None:                        #jika user memesan yang tidak ada di menu maka akan diabaikan
        keranjang.append(beli)

for beli in keranjang:
    total = total + menu.get(beli)
    print(beli, end=" ")
print()
print("-------------pesananmu--------------")
print(f"total pesanan: Rp.{total:.3f}")