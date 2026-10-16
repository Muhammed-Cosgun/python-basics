# """
# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.

# Kullanımı           : open(dosya_adi,dosya_erişme_modu)
# dosya_erişme_modu   : dosyayı hangi amaçla açtığımızı belirtir.
# "r" okuma modu      : okuma modu. belirtilen konumda dosya olmalıdır.
# seek                : cursor konumu
# """

# var olan bir dosyayı okumak için ya da yeni bir dosya açmak için open metotu kullanılabilir.
# dosya = open("log.txt", "w")
# dosya.write("ilk satır log yazısı")
# dosya.close()



# file = open("log.txt", encoding = 'utf-8') # read = okuma modu. aynı dizindeyse okur. r yazmasan da defaultu read modudur. yazmaya gerek yoktur.

# print(file.read())
# file.close()


# with open("log.txt", encoding='utf-8') as file:
#     print(file.read(10))
#     print(file.tell())
# # bu şekilde yapıldığında dosyayı close ile kapatmaya gerek kalmaz. with bu işlemleri kendisi yapar.

# tell = o an hangi karakterdeyse onu alır.

# try:
#     with open("log2.txt", encoding='utf-8') as file:
#         for i in file:
#             print(i, end="")
# except FileNotFoundError as e:
#     print("dosya okuma hatası")