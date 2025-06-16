'''
List adalah struktur data yang digunakan untuk menyimpan kumpulan item yang terurut dan dapat diubah (mutable). List bisa berisi berbagai jenis data, seperti angka, string, atau bahkan list lainnya.

Ciri-ciri List: []
Terurut (ordered): Urutan elemen dalam list akan tetap sama.
Dapat diubah (mutable): Elemen di dalam list dapat diubah setelah list dibuat.
Dapat berisi elemen dengan tipe data yang berbeda

Set adalah struktur data yang digunakan untuk menyimpan kumpulan item yang tidak terurut dan tidak dapat memiliki elemen yang duplikat. Set juga bersifat mutable.

Ciri-ciri Set: {}
Tidak terurut (unordered): Urutan elemen dalam set tidak dijamin.
Tidak ada elemen duplikat: Set hanya menyimpan elemen yang unik.
Dapat diubah (mutable): Elemen dalam set dapat ditambahkan atau dihapus.

Tuple adalah struktur data yang mirip dengan list, tetapi bersifat immutable (tidak dapat diubah setelah dibuat). Tuple digunakan ketika Anda membutuhkan kumpulan data yang tidak boleh diubah, misalnya koordinat atau data tetap.


Ciri-ciri Tuple:()
Terurut (ordered): Urutan elemen dalam tuple tetap.
Tidak dapat diubah (immutable): Setelah tuple dibuat, elemen-elemen di dalamnya tidak bisa diubah.
Dapat berisi elemen dengan tipe data yang berbeda.

'''

#buah = ["apel", "jeruk", "pisang", "melon"]


# print(dir, (buah))
# print(help(buah))
# print(len(buah))
# print("apple" in buah)
#print(buah[0])

#buah[0] = "kelapa"
#buah.append("kelapa")
#buah.remove("apel")
#buah.insert(0, "kadu")
#buah.reverse()
#buah.clear()
#print(buah.count("apel"))
#print(buah.index("apel"))

'''
buah = {"apel", "jeruk", "pisang", "melon"}

buah.add("hab")
buah.remove("hab")
buah.pop()
buah.clear()

print(buah)
'''
buah = ("apel", "jeruk", "pisang", "melon")

print(buah.count("apel"))
print(buah.index("apel"))




for bua in buah:
   print(bua)




