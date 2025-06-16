'''
"Argumen default adalah nilai yang diberikan untuk parameter tertentu dalam sebuah fungsi. Nilai default ini akan digunakan jika argumen tersebut tidak diberikan saat fungsi dipanggil. Ini membuat fungsi Anda lebih fleksibel karena memungkinkan Anda untuk mengurangi jumlah argumen yang perlu disebutkan saat memanggil fungsi. Ada beberapa jenis argumen dalam fungsi:

Argumen Posisi: Argumen yang diberikan berdasarkan urutan posisinya saat fungsi dipanggil.
Argumen Default: Argumen yang memiliki nilai bawaan yang digunakan jika argumen tersebut tidak diberikan saat pemanggilan.
Argumen Kata Kunci: Argumen yang dipanggil menggunakan nama parameter secara eksplisit.
Argumen Sewenang-wenang: Argumen yang dapat menerima jumlah parameter yang tidak terbatas (menggunakan tanda *args atau **kwargs)."
Penjelasan ini memberikan gambaran yang lebih jelas tentang bagaimana setiap jenis argumen bekerja dan bagaimana argumen default meningkatkan fleksibilitas fungsi.

#default argumen
def harga(daftar_harga, diskon=0, pajak=0.07):
    return daftar_harga * (1 - diskon) * (1 + pajak)

print(harga(200))
print(harga(200, 0.11))
print(harga(200, 0.11, 0))

note jika ingin menggunakan default argumenr pastikan di akhir

import time

def hitung(akhir, awal=0):
    for i in range(awal, akhir+1):
        print(i)
        time.sleep(1)
    print("Sudah!!")

hitung(10)
'''
import time

def tidur(awal, akhir=0):
    for waktu in range(akhir, awal+1):
        print(waktu)
        time.sleep(1)
    print("sudah")

tidur(10)













