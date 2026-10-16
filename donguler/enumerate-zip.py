# markalar = ["opel", "bmw", "togg"]

# index = 1
# for marka in markalar:
#     print(f"{index}-{marka}")
#     index += 1

# enumerate = index numrasını sağlar.

# obj1 = enumerate(markalar)
# print(type(obj1))
# print(list(obj1))

# for marka in enumerate(markalar):
#     print(marka)

# for index, marka in enumerate(markalar):   # bu şekilde yazınca index = indexi tutar, marka ise marka ismini tutar.
#     print(f"{index}-{marka}")



# ZIP = birden fazla listeyi birleştirmeye yarar.
# numara = [100, 200, 300]
# ogrenci = ["Ali", "Ayşe", "Canan"]

# print(list(zip(numara, ogrenci)))  # eğer for döngüsü dışında kullanılıyorsa list komutu ile listeye çevrilmelidir. yukarıdaki enumerate de aynı şekilde. ama for ile kullanılıyorlarsa list komutunu kullanmaya gerek yoktur.

# for ogr in zip(numara, ogrenci):
#     print(ogr)

# for no, isim in zip(numara, ogrenci):
#     print(f"{no} - {isim}")


