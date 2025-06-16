#function = satu blok kode yang dapat digunakan kembali 
# place() setelah nama fungsi untuk memanggilnya

# Fungsi 'menyapa' menerima dua parameter: 'nama' dan 'umur'.
# Fungsi ini menampilkan sapaan kepada pengguna berdasarkan nama dan umur yang diberikan.
def menyapa(nama, umur):
    print(f"halo {nama}")  # Menampilkan sapaan "halo" diikuti dengan nama
    print(f"kamu {umur} tahun!")  # Menampilkan informasi umur pengguna
    print("halo kamu")  # Menampilkan sapaan umum lagi
    print()  # Menambahkan baris kosong setelah setiap pemanggilan fungsi

# Memanggil fungsi 'menyapa' dengan beberapa nama dan umur sebagai argumen
menyapa("kidong", 18)  # Output: "halo kidong", "kamu 18 tahun!", "halo kamu"
menyapa("rois", 19)  # Output: "halo rois", "kamu 19 tahun!", "halo kamu"
menyapa("eda", 18)  # Output: "halo eda", "kamu 18 tahun!", "halo kamu"

# Fungsi 'tagihan' menerima tiga parameter: 'tagiha' (jumlah tagihan), 'gal' (tanggal bayar), dan 'nam' (nama pengguna).
# Fungsi ini menampilkan informasi mengenai tagihan yang harus dibayar, tanggal pembayaran, dan nama pengguna.
def tagihan(tagiha, gal, nam):
    print(f"tagihan kamu {tagiha}")  # Menampilkan informasi tagihan pengguna
    print(f"bayar lah tgl {gal}")  # Menampilkan tanggal yang harus dibayar
    print(f"atas nama {nam}")  # Menampilkan nama pengguna yang tertera pada tagihan
    print()  # Menambahkan baris kosong setelah setiap pemanggilan fungsi

# Memanggil fungsi 'tagihan' dengan jumlah tagihan, tanggal bayar, dan nama pengguna sebagai argumen
tagihan(150.000, 29, "kidong")  # Output: "tagihan kamu 150000", "bayar lah tgl 29", "atas nama kidong"
tagihan(170.000, 2, "rois")  # Output: "tagihan kamu 170000", "bayar lah tgl 2", "atas nama rois"
tagihan(120.000, 18, "eda")  # Output: "tagihan kamu 120000", "bayar lah tgl 18", "atas nama eda"

'''
Penjelasan Kode:
Fungsi menyapa:

Fungsi ini digunakan untuk menyapa pengguna berdasarkan nama dan umur yang diberikan.
Parameter yang diterima adalah nama (nama pengguna) dan umur (umur pengguna).
Fungsi ini mencetak sapaan seperti "halo [nama]" dan informasi umur seperti "kamu [umur] tahun!".
Setelah itu, fungsi ini juga mencetak "halo kamu" dan memberikan baris kosong setelah setiap pemanggilan fungsi.
Fungsi tagihan:

Fungsi ini digunakan untuk menampilkan informasi terkait tagihan pengguna, tanggal bayar, dan nama pengguna.
Parameter yang diterima adalah tagiha (jumlah tagihan), gal (tanggal pembayaran), dan nam (nama pengguna).
Fungsi ini mencetak informasi tentang tagihan yang harus dibayar, tanggal pembayaran yang harus dilakukan, dan nama pengguna yang tertera pada tagihan.
Setelah setiap pemanggilan, ada baris kosong yang ditambahkan.
Pemanggilan Fungsi:

Fungsi menyapa dipanggil beberapa kali dengan nama dan umur yang berbeda untuk memberikan sapaan yang berbeda.
Fungsi tagihan dipanggil dengan tagihan, tanggal bayar, dan nama yang berbeda untuk memberikan informasi tagihan yang sesuai.

'''


#return = pernyataan yang digunakan untuk mengakhiri suatu fungsi dan mengirimkan hasilnya kembali ke pemanggil

# Fungsi 'bagi' menerima dua parameter 'x' dan 'y', kemudian membagi 'x' dengan 'y' dan mengembalikan hasilnya.
def bagi(x, y):
    z = x / y  # Membagi x dengan y
    return z  # Mengembalikan hasil pembagian

# Fungsi 'kali' menerima dua parameter 'x' dan 'y', kemudian mengalikan 'x' dengan 'y' dan mengembalikan hasilnya.
def kali(x, y):
    z = x * y  # Mengalikan x dengan y
    return z  # Mengembalikan hasil perkalian

# Fungsi 'tambah' menerima dua parameter 'x' dan 'y', kemudian menjumlahkan keduanya dan mengembalikan hasilnya.
def tambah(x, y):
    z = x + y  # Menjumlahkan x dan y
    return z  # Mengembalikan hasil penjumlahan

# Fungsi 'kurang' menerima dua parameter 'x' dan 'y', kemudian mengurangi 'x' dengan 'y' dan mengembalikan hasilnya.
def kurang(x, y):
    z = x - y  # Mengurangi x dengan y
    return z  # Mengembalikan hasil pengurangan

# Mencetak hasil dari fungsi 'kali', 'bagi', 'tambah', dan 'kurang' dengan contoh nilai input.
print(kali(2, 4))  # Output: 8, hasil perkalian 2 * 4
print(bagi(6, 2))  # Output: 3.0, hasil pembagian 6 / 2
print(tambah(2, 3))  # Output: 5, hasil penjumlahan 2 + 3
print(kurang(90, 80))  # Output: 10, hasil pengurangan 90 - 80

# Fungsi 'buat_nama' menerima dua parameter 'awal' dan 'akhir', lalu mengkapitalisasi kedua kata tersebut 
# dan menggabungkannya dengan spasi di antara keduanya.
def buat_nama(awal, akhir):
    awal = awal.capitalize()  # Mengkapitalisasi huruf pertama dari 'awal'
    akhir = akhir.capitalize()  # Mengkapitalisasi huruf pertama dari 'akhir'
    return awal + ' ' + akhir  # Mengembalikan gabungan nama dengan spasi di antara keduanya

# Menyimpan hasil dari fungsi 'buat_nama' yang menggabungkan dua string "patruk" dan "star"
f_name = buat_nama("patruk", "star")  
print(f_name)  # Output: "Patruk Star", hasil gabungan nama yang telah dikapitalisasi

'''
Penjelasan:
Fungsi bagi, kali, tambah, dan kurang masing-masing melakukan operasi aritmatika sederhana dan mengembalikan hasilnya.
Fungsi buat_nama digunakan untuk menggabungkan dua string dengan memodifikasi huruf pertama masing-masing agar menjadi kapital, dan hasil akhirnya adalah penggabungan dua kata tersebut dengan spasi di antaranya.
Setiap kali fungsi tersebut dipanggil, hasilnya akan dicetak melalui perintah print.

'''