#string indexing untuk mengelola sebuah string

#name = input("enter name : ")
#phone_number = input("enter phone number: ")

#menghitung jumlah karakter
#result = len(name)

#untuk menemukan awal sebuah karakter ingat mesin menghitung dari 0 bukan 1
#result = name.find("a")

#untuk menemukan akhir dari karakter yang dicari
#result = name.rfind("t")

#untuk membuat huruf pertama menjadi kapital
#name = name.capitalize()

#untuk membuat sebuah huruf menjadi kapital semua
#name = name.upper()

#untuk membuat huruf menjadi huruf kecil semua
#name = name.lower()

#haya untuk string angka ketika di print menjadi boolean
#result = name.isdigit()

#hanya untuk string alpanumerik atau huruf
#result = name.isalpha()

#unutk memhintung string yang dipilih
#result = phone_number.count("-")

#untuk mengganti string yang diplih
#result = phone_number.replace("-", "")

#untuk meminta pertolongan
#print(help(str))

#latihan string method

"""
membuat username dengan ketentuan berikut
1. username tidak boleh lebih dari 12 karakter
2. username tidak boleh mengandung spasi dan angka
"""

username = input("masukan username: ")

if len(username) > 12:
    print("username tidak boleh lebih 12 karakter")
elif not username.find(" ") == -1:
    print("username tidak boleh mengandung spasi")
elif not username.isalpha():
    print("username tidak boleh mengandung angka")
else:
    print(f"selamat datang {username}")
