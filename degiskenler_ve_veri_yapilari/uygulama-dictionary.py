# Aşağıdaki öğrenci bilgilerini dictionary listesinde saklayınız.
    # 101 Yiğit Bilgi 2010 (40,80,90)
    # 102 Ada Bilgi   2012 (80,80,80)
    # 103 Çınar Turan 2017 (70,70,70)

# dict_1 = {
#     "101": ["Yiğit", "Bilgi", "2010", (40,80,90)],
#     "102": ["Ada", "Bilgi", "2012", (80,80,80)],
#     "103": ["Çınar", "Turan", "2017", (70,70,70)]
# }

# # print(type(dict_1))
# print(dict_1["101"])



# # Klavyeden girilen öğrenci numarasına göre aşağıdaki cümleyi yazdırınız.
#     # 101 numaralı Yiğit Bilgi ismindeki öğrencinin yaşı 14 ve not ortalaması 70.

# girilenNumara = input("öğrenci numarası giriniz: ")

# mesaj = f"{girilenNumara} numaralı {dict_1[girilenNumara][0]} {dict_1[girilenNumara][1]} ismindeki öğrencinin yaşı {2024 - int((dict_1[girilenNumara][2]))} ve not ortalaması {(dict_1[girilenNumara][3][0] + dict_1[girilenNumara][3][1] + dict_1[girilenNumara][3][2]) / 3}"

# print(mesaj)