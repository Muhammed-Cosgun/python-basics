# Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız.

# def goster(kelime, adet):
#     for i in range(adet):
#         print(kelime + " ")

# gonderilecekKelime = input("Kelimeyi Gir: ")
# adet = int(input("ekranda kaç kez gösterilsin? "))
# goster(gonderilecekKelime, adet)



# Dikdörtgenin alan ve çevresini hesaplayan fonksiyonu yazınız.
# def hesapla(kisaKenar, uzunKenar):
#     alan = kisaKenar * uzunKenar
#     cevre = (kisaKenar + uzunKenar)*2
#     return f"alan = {alan}, cevre = {cevre}"

# kisa = int(input("kısa kenar? "))
# uzun = int(input("uzun kenar? "))
# print(hesapla(kisa, uzun))




# Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)
# def yaziTura(kullaniciSecimi):
#     import random
#     randomSayi = random.randint(0,1)
#     if randomSayi == int(kullaniciSecimi):
#         print(f"Bilgisayar seçimi: {randomSayi}. Tebrikler doğru bildiniz.")
#     else:
#         print(f"Bilgisayar seçimi: {randomSayi}. Bilemediniz.")
    

# kullaniciSecimi = input("Yazı mı Tura mı tahmin et? (Yazı için 0, Tura için 1 giriniz): ")
# yaziTura(kullaniciSecimi)




# Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.
# def asal_sayilari_bul(baslangic, bitis):
#     asallar = []
#     for sayi in range(baslangic, bitis + 1):
#         if sayi>1:
#             for i in range(2, sayi):
#                 if sayi % i == 0:
#                     break
#             else:
#                 asallar.append(sayi)
#     return asallar

# Python'da for ... else yapısı, döngü break ifadesiyle erkenden kesilmeden normal bir şekilde tamamlandığında else bloğunun çalıştırılmasını sağlar.
# Eğer döngü içinde break ifadesi çalışırsa, döngü anında sonlandırılır ve else bloğu çalıştırılmaz; program döngünün altındaki kodlardan akışına devam eder.


# print(asal_sayilari_bul(10, 30))


# Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.
# def tamBolenBulma(sayi):
#     list_1 = []
#     i = 1
#     while i <= sayi:
#         if sayi % i == 0:
#             list_1.append(i)
#         i += 1
#     print(f"{sayi} sayısının tam bölenleri: {list_1}")

# sayi = int(input("sayi gir: "))

# tamBolenBulma(sayi)