# Klavyeden girilen n sayıdaki öğrenci bilgisini liste içerisinde saklayınız.
## dictionary liste yapısı (ogrenciNo, ogrenciAdi, ogrenciSoyad) şeklinde olsun.
# ürün ekleme işlemi bittiğinde öğrencileri lsiteleyiniz.


# 1. ÇÖZÜM
# studentCount = int(input("kaç öğrenci ekleyeceksiniz? "))

# i = 1
# ogrencilerSozlugu = {}
# while i <= studentCount:
#     ogr_no = input(f"{i}. öğrencinin nosunu gir: ")
#     ogr_isim = input(f"{i}. öğrencinin ismini gir: ")
#     ogr_soyad = input(f"{i}. öğrencinin soyadını gir: ")
#     ogrencilerSozlugu[ogr_no] = ogr_isim + " " + ogr_soyad
#     i += 1


# for x in ogrencilerSozlugu.items():
#     print(x)




# 2. ÇÖZÜM
# studentCount = int(input("kaç öğrenci ekleyeceksiniz? "))
# i = 1
# students = []
# while i <= studentCount:
#     ogr_no = input(f"{i}. öğrencinin nosunu gir: ")
#     ogr_isim = input(f"{i}. öğrencinin ismini gir: ")
#     ogr_soyad = input(f"{i}. öğrencinin soyadını gir: ")

#     ogrenci = {
#         "ogr_no": ogr_no,
#         "ogr_isim": ogr_isim,
#         "ogr_soyad": ogr_soyad 
#     }
#     students.append(ogrenci)
#     i += 1

# for x in students:
#     print(x)




