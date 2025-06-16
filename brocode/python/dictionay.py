#dictionary

#print(help(ibukota))

ibukota = {"indonesia": "jakarta",
           "malaysa": "kuala",
           "australia": "sidney"}

if ibukota.get("indonesia"):
    print("itu ada")
else:
    print("tidak ada")

for key, value in ibukota.items():
    print(f"{key}: {value}")

print("----------------------------")

for values in ibukota.values():
    print(values)

print("----------------------------")

for key in ibukota.keys():
    print(key)

print("----------------------------")

#menambahkan
ibukota.update({"jerman": "berlin"})

#menghapus
ibukota.pop("indonesia")

print(ibukota)