import random  # Mengimpor modul random untuk menghasilkan angka acak

# ● ┌ ─ ┐ │ └ ┘
# Ini adalah representasi seni dari dadu yang akan digunakan dalam output

# Dictionary seni_dadu berisi representasi seni dadu untuk setiap angka (1 hingga 6)
seni_dadu = {
    1: ("┌─────────┐", 
        "│         │", 
        "│    ●    │", 
        "│         │", 
        "└─────────┘"),

    2: ("┌─────────┐", 
        "│  ●      │", 
        "│         │", 
        "│      ●  │", 
        "└─────────┘"),

    3: ("┌─────────┐", 
        "│ ●       │", 
        "│    ●    │", 
        "│       ● │", 
        "└─────────┘"),

    4: ("┌─────────┐", 
        "│ ●     ● │", 
        "│         │", 
        "│ ●     ● │", 
        "└─────────┘"),

    5: ("┌─────────┐", 
        "│ ●     ● │", 
        "│    ●    │", 
        "│ ●     ● │", 
        "└─────────┘"),

    6: ("┌─────────┐", 
        "│ ●     ● │", 
        "│ ●     ● │", 
        "│ ●     ● │", 
        "└─────────┘")
}

# Inisialisasi list 'dadu' untuk menyimpan nilai-nilai acak dari dadu yang dilempar
dadu = []
total = 0  # Variabel untuk menyimpan total nilai dadu yang dilempar

# Meminta input dari pengguna untuk menentukan jumlah dadu yang akan dilempar
nomor_dadu = int(input("berapa dadu?: "))

# Menghasilkan angka acak untuk setiap dadu yang dilempar
for dad in range(nomor_dadu):
    dadu.append(random.randint(1, 6))  # Menambahkan nilai acak antara 1 hingga 6 ke list dadu

# Mencetak hasil lemparan dadu dalam format seni
for garis in range(5):  # Ada 5 baris untuk setiap seni dadu
    for dad in dadu:
        print(seni_dadu.get(dad)[garis], end="")  # Mencetak baris sesuai dengan nilai dadu
    print()  # Menambahkan baris baru setelah mencetak setiap baris

# Menghitung total nilai dari dadu yang dilempar dan mencetaknya
for dad in dadu:
    total += dad  # Menambahkan nilai setiap dadu ke total
print(f"total: {total}")  # Mencetak total nilai dadu yang dilempar

'''
Penjelasan Kode:
Modul random: Digunakan untuk menghasilkan angka acak antara 1 dan 6 yang akan mewakili nilai dadu yang dilempar.

Dictionary seni_dadu:

Ini berisi representasi visual dari dadu dengan angka 1 hingga 6 dalam bentuk seni menggunakan karakter teks (seperti ┌ ─ ┐, │, dll.).
Setiap angka (1 sampai 6) memiliki bentuk visual yang berbeda berdasarkan jumlah titik (●) di dalam dadu.
Input Pengguna:

Pengguna diminta untuk memasukkan jumlah dadu yang ingin dilempar.
Nilai input tersebut disimpan dalam variabel nomor_dadu.
Melempar Dadu:

Program menghasilkan angka acak antara 1 dan 6 sebanyak nomor_dadu kali menggunakan random.randint(1, 6).
Nilai-nilai acak ini disimpan dalam list dadu.
Mencetak Hasil Lemparan Dadu:

Dengan menggunakan dua loop (for garis in range(5) dan for dad in dadu), program mencetak representasi visual dari dadu yang dilempar dalam format seni.
Setiap garis dari seni dadu dicetak satu per satu untuk setiap nilai dadu yang ada di list dadu.
Menghitung Total:

Setelah mencetak hasil lemparan dadu, program menghitung total nilai dari semua dadu yang dilempar dengan menambahkan nilai-nilai dadu yang ada dalam list dadu.
Hasil total ditampilkan pada akhir output.

'''