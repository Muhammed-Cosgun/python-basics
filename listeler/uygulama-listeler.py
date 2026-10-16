# 1- "Toyota, Bmw, Renault, Mercedes" elemanlarına sahip markalar isimli bir liste oluşturunuz.
# markalar = ["Toyota", "Bmw", "Renault", "Mercedes"]


# 2- Liste kaç elemanlıdır?
# elemanSayisi = len(markalar)
# print(f"liste {elemanSayisi} elemanlıdır.")


# 3- Listenin ilk ve son elemanı nedir?
# ilkEleman = markalar[0]
# sonEleman = markalar[len(markalar)-1]
# print(f"Liste ilk elemanı = {ilkEleman}, son elemanı = {sonEleman}")


# 4- "Renault" markasını "Togg" ile güncelleyiniz.
# renaultIndexi = markalar.index("Renault")
# markalar[renaultIndexi] = "Togg"
# print(markalar)



# 5- "Togg" listenin bir elemanı mıdır?
# if "Togg" in markalar:
#     print("Togg listenin bir elemanıdır.")
# else: 
#     print("Togg listenin bir elemanı değildir.")



# 6- Listenin ilk 2 elemanını alınız.
# ilkIkiEleman = markalar[:2]
# for item in ilkIkiEleman:
#     print(item)


# 7- Listenin sonuna "Ford" ve "Citroen" markalarını ekleyiniz.
# markalar.append("Ford")
# markalar.append("Citroen")
# for item in markalar:
#     print(item)


# 8- Listenin son elemanını siliniz.
# del markalar[-1]
# for item in markalar:
#     print(item)



# 9- Aşağıdaki verileri liste içerisinde saklayınız.

    # öğrenci1: Yiğit Bilgi 2010 [70,80,90]
    # öğrenci2: Ada Bilgi   2011 [70,70,80]
    # öğrenci3: Çınar Turan 2017 [60,60,90]

# ogrenci1 = [
#     "Yigit", "Bilgi", 2010, [70,80,90]
# ]

# ogrenci2 = [
#     "Ada", "Bilgi", 2011, [70,70,80]
# ]

# ogrenci3 = [
#     "Çınar", "Turan", 2017, [60,60,90]
# ]

# ogrenciler = [ogrenci1, ogrenci2, ogrenci3]

# 10- Öğrencilerin yaşlarını hesaplayınız.
# ogrenci_1_yasi = 2024 - ogrenci1[2]
# ogrenci_2_yasi = 2024 - ogrenci2[2]
# ogrenci_3_yasi = 2024 - ogrenci3[2]

# mesaj = f"yiğitin yaşı: {ogrenci_1_yasi}, adanın yaşı: {ogrenci_2_yasi}  çınarın yaşı: {ogrenci_3_yasi}"
# print(mesaj)


# 11- Öğrencilerin not ortalamalarını hesaplayınız.
# ogr1_ortalama = (ogrenci1[3][0] + ogrenci1[3][1] + ogrenci1[3][2]) / 3
# ogr2_ortalama = (ogrenci2[3][0] + ogrenci2[3][1] + ogrenci2[3][2]) / 3
# ogr3_ortalama = (ogrenci3[3][0] + ogrenci3[3][1] + ogrenci3[3][2]) / 3

# mesaj = f"yiğitin ortalamasi: {ogr1_ortalama:.2f}, adanın ortalamasi: {ogr2_ortalama:.2f}  çınarın ortalamasi: {ogr3_ortalama:.2f}" 
# print(mesaj)





