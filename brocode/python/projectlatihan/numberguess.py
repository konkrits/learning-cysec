import random

# Mengatur batas nomor rendah dan tinggi
nomor_rendah = 1
nomor_tinggi = 100
# Menguji angka acak
jawaban = random.randint(nomor_rendah, nomor_tinggi)

# Mengatur variabel untuk menghitung tebakan yang salah
tebakan = 0

# Membuat header game
print("-------python number guessing game-------")
print(f"tebak angka antara {nomor_rendah} dan {nomor_tinggi}")

# Membuat loop berjalan sampai jawaban benar
while True:
    # Mengambil input dari pengguna
    tebak = input("tebak angka: ")
    
    # Memeriksa apakah input pengguna hanya angka
    if tebak.isdigit():
        # Mengubah input menjadi integer
        tebakan = int(tebak)
        
        # Meningkatkan tebakan yang telah ditebak sebelumnya
        tebakan += 1
        
        # Mencegah input yang tidak valid
        if tebak < 1 or tebak > 100:
            print("nomor tidak valid")
            print(f"tebak angka antara {nomor_rendah} dan {nomor_tinggi}")
        
        elif tebak < jawaban:
            # Memberi petunjuk apakah nomor terlalu kecil
            print("angka terlalu kecil")
        
        elif tebak > jawaban:
            # Memberi petunjuk apakah nomor terlalu besar
            print("angka terlalu besar")
        
        else:
            # Memberitahukan kepada pengguna bahwa tebakan benar dan menghitung jumlah tebakan yang salah
            print(f"Benar! angka yang benar: {jawaban}")
            print(f"percobaan menebak {tebakan}")
            break
        
    else:
        # Memberi pesan kepada pengguna bahwa hanya angka saja yang dapat diterima
        print("hanya angka saja")
        print(f"tebak angka antara {nomor_rendah} dan {nomor_tinggi}")

'''
Mengatur batas nomor rendah dan tinggi: Menentukan batasan untuk permainan, dalam hal ini adalah 1 sampai 100. Batasan ini dapat diubah sesuai kebutuhan.

Menguji angka acak: Menggunakan fungsi random.randint() untuk menghasilkan angka yang benar dan tidak dapat diperoleh dengan cara lain. Angka ini akan digunakan 
sebagai jawaban akhir permainan.

Fungsi random adalah sebuah modul Python yang membantu dalam menciptakan algoritma pengenalan acak, permutasi, sampel, dan elemen lainnya.
Membuat header game: Menampilkan pesan di atas layar agar pemain menyadari bahwa permainan sedang berlangsung. Keterangan ini akan memberitahukan kepada pengguna 
tentang batasan untuk permainan.

Header atau pesan dapat digunakan sebagai bagian dari antarmuka pengguna untuk mempermudah pengguna dalam memahami apa yang harus dilakukan.
Loop Berjalan: Mengatur perulangan untuk memastikan bahwa pengguna dapat terus mencoba sampai mendapatkan jawaban yang benar. Perulangan ini akan berhenti 
ketika jawaban telah ditemukan.

Loop dapat digunakan untuk membuat program tetap berjalan dan melakukan tindakan sampai kondisi tertentu terpenuhi.
Mengambil input dari pengguna: Menawarkan pengguna untuk memasukkan nomor. Pengguna akan diminta untuk masukkan angka dalam rentang yang telah ditentukan.

Input adalah cara untuk meminta data kepada pengguna melalui console atau layar.
Periksa input: Mengecek apakah input tersebut hanya angka dengan menggunakan isdigit(). Fungsi isdigit() dapat digunakan untuk mengecek apakah sebuah string terdiri dari 
karakter digit saja.

Fungsi isdigit dapat digunakan untuk memeriksa apakah semua karakter dalam suatu string merupakan digit.
Meningkatkan tebakan yang telah ditebak sebelumnya: Menghitung jumlah tebakan yang salah untuk menentukan ketika jawaban benar. 
Jumlah ini akan memberitahu kepada pengguna bahwa permainan sudah selesai.

Perulangan dapat digunakan dalam program untuk menghitung sebanyak itu sebanyak.
Memberi petunjuk: Memberikan kesempatan kepada pemain untuk memahami apakah jawaban yang ditebak terlalu kecil, terlalu besar, atau tepat. 
Petunjuk ini akan membantu pemain dalam mencoba kembali sampai jawabannya benar.

Kondisi perulangan dapat digunakan untuk memberikan petunjuk kepada pengguna mengenai jawaban yang mereka masukkan.
Memberitahukan bahwa tebakan benar: Memberitahu kepada pemain bahwa jawaban akhir adalah nomor yang telah ditebak. Permainan akan berakhir ketika jawabannya tepat.

Kondisi dapat digunakan untuk memberitahu kepada pemain bahwa jawaban mereka tepat atau tidak tepat.

'''







