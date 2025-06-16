import random  # Mengimpor modul random untuk memilih opsi komputer secara acak

opsi = ("batu", "kertas", "gunting")  # Menyimpan pilihan permainan dalam tuple
running = True  # Menentukan kondisi untuk menjalankan permainan

print("------gunting kertas batu------")  # Menampilkan judul permainan

while running:  # Selama permainan masih berjalan
    pemain = None  # Menyimpan input pemain
    komputer = random.choice(opsi)  # Memilih secara acak antara batu, kertas, atau gunting untuk komputer

    while pemain not in opsi:  # Memastikan pemain memilih salah satu dari batu, kertas, atau gunting
        pemain = input("pilih apa: ")  # Minta pemain untuk memilih

    print(f"Pemain: {pemain}")  # Menampilkan pilihan pemain
    print(f"komputer: {komputer}")  # Menampilkan pilihan komputer

    # Kondisi jika pilihan pemain dan komputer sama
    if pemain == komputer:
        print("imbang")  # Jika sama, hasilnya imbang
    # Kondisi jika pemain menang
    elif pemain == "gunting" and komputer == "kertas":
        print("pemain menang")  # Gunting mengalahkan kertas
    elif pemain == "batu" and komputer == "gunting":
        print("pemain menang")  # Batu mengalahkan gunting
    elif pemain == "kertas" and komputer == "batu":
        print("pemain menang")  # Kertas mengalahkan batu
    else:
        print("komputer menang")  # Jika tidak ada kondisi menang pemain, maka komputer menang

    # Menanyakan apakah pemain ingin bermain lagi
    if not input("main lagi? (y/n)\n").lower() == "y":
        running = False  # Jika input bukan 'y', permainan akan berhenti

print("terima kasih sudah bermain")  # Menampilkan pesan terima kasih setelah permainan selesai    