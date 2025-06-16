#indexing = mengakses elemen dalam sequence menggunakan [] (indexing operators)
#           [start : end : step]

nomor_bank = "1234-5678-9012-3456"

#akses ke awal string
#print(nomor_bank[0])

#akses ke sampai string yang dituju 
#print(nomor_bank[:4])

#akses dari ke samapi ke
#print(nomor_bank[5:9])

#print dari sampai seterusnya
#print(nomor_bank[5:])

#print dari akhir
#print(nomor_bank[-1])

#untuk mengeliminasi tiap angka atau baris ke 2
#print(nomor_bank[::2])

#untuk menghitung kebalikan
#nomor = nomor_bank[::-1]
#print(nomor)

#contoh penggunaan
#menyembunyikan semua nomor kecuali 4 digit terakhir

nomor_bank = nomor_bank[-4:]

print(f"XXXX-XXXX-XXXX-{nomor_bank}")

