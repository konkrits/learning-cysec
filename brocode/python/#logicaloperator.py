#logicaloperator

umur = int(input("berapa usia kamu?\n"))
gen = input("Pria, Wanita? \n").lower()

if umur <= 0 or (gen != "pria" and gen != "wanita"):
    print("tidak valid")
elif umur >= 18:
    if gen == "pria":
        print("Hidupmu berat")
    else:  # Jika gen adalah "wanita"
        print("hidupmu sedikit susah")
else:
    print("persiapkan masa depan")
