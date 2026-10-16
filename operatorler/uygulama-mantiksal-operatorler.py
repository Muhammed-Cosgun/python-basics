# 1- Yaşı 18' den büyük ya da veli izni varsa bir işte çalışabilir durumunu kontrol ediniz.

# yas = int(input("yasini gir: "))
# veliIzniVarMi = input("veli izni var mi (var/yok): ")
# if yas >= 18 or veliIzniVarMi == "var":
#     print("bir işte çalışabilir.")
# else:
#     print("bir işte çalışamaz.")


# # 2- Ders notu 50-100 arasındaysa geçti değilse kalsın bilgisini yazdırınız.
# dersNotu = 82
# if dersNotu >= 50:
#     print("geçti")
# else:
#     print("kaldi")



# # 3- Not ortalaması en az 70 puan ve zayıfı yoksa teşekkür belgesi alabilme durumunu kontrol ediniz.
# point_average = 75
# zayifiVarMi = False
# if point_average >= 70 and not zayifiVarMi:
#     print("teşekkür alabilirsin.")
# else:
#     print("teşekkür alamazsın.")



# # 4- İşe girmek için en az önlisans ya da lisans mezunu olma durumunu kontrol ediniz. Sigara kullanmama koşulu.
# lisansMezunu = True
# onLisansMezunu = False
# sigaraKullanma = False
# if (lisansMezunu or onLisansMezunu) and not sigaraKullanma:
#     print("işe girebilirsiniz")
# else:
#     print("işe giremezsiniz")

# # 5- Uygulamaya giriş kontrolünü "username yada email" ve "parola" için yapalım.
# username = "muhammedcsgn"
# email = "muhammed99@gmail.com"
# password = "1905"

# kullaniciGirisUsername = input("kullanici adini giriniz: ")
# KullaniciGirisPassword = input("parolanızı giriniz: ")

# user1, pas1 = kullaniciGirisUsername == username, KullaniciGirisPassword == password

# if user1 and pas1:
#     print("Giriş başarılı")
# else:
#     print("Giriş başarısız")


# IDENTITY VE MEMBERSHIP
# == opatatörü = sadece değerlerin eşitliğine bakarken, is operatörü nesnelerin kimliklerin yani adreslerinin aynı olup olmadığına bakar. eğer referans ile atama yapıldıysa ikisi se aynı nesne olmuş oluyordu bunu daha önceki konularda öğrenmiştim. is operatörü de işte tam olarak bunu kontrol eder.

# x = [2, 4, 6]
# y = [2, 4, 6]

# print(x == y) # bu true döndürür. çünkü x ve y listelerinin içindeki elemanlar eşittir. (ama adresleri eşit değil!)

# z = y # bu şekilde yapıldığında sadece liste kopayalanmaz, liste adresi de kopyalanır. z veya y üzerinde yapılan bir değişkilik diğer liste üzerinde de yapılmış olur.

# print(z is y) # z, y midir? yani z elemanı y ile aynı adreste midir? nesnelerin aynı olup olmamasına bakar. iki nesne yukarıda referans yoluyla atama yapıldığından dolayı iki nesne ne aynıdır.

# print(x is y) # elemanları aynı olmasına rağmen false döndürür. çünkü adresleri farklıdır ve farklı nesnelerdir.

# m = y.copy()
# print(m is y)  # bu da false döndürür. çünkü copy metot ile listenin içindekiler kopyalanmıştır. listenin adresi kopyalanmaz.

# print(x is not y) # bu ise x, y değil midir der. yani yukarıda yaptığımız işlemi tersten kontrol eder.




# membership ise bir elemanın bir listede vs bulunup bulunmadığını kontrol etmeye yarar.
# list_1 = [1,2,3,4]
# print(3 in list_1) # 3 sayısı list_1'in içinde var mı?
# print(5 not in list_1) # 5 sayısı list_1'içinde yok mu?