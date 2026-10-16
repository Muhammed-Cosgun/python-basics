# urunler = [
#     {"urunAdi":"Hp Victus", "fiyat": 32999},
#     {"urunAdi":"Lenovo ThinkPad", "fiyat": 25499},
#     {"urunAdi":"Apple Macbook", "fiyat": 49999},
#     {"urunAdi":"Huawei Matebook", "fiyat": 26999},
#     {"urunAdi":"Casper Nirvana", "fiyat": 20000}
# ]

# 1- Aşağıdaki örnek cümleyi tüm ürünlere uygulayınız.
#    "Hp Victus marka ürünün fiyatı 32999 Türk Lirası."
# for x in urunler:
#     message = f"{x['urunAdi']} marka ürünün fiyatı {x['fiyat']} Türk Lirası"
#     print(message)

# 2- Ürünlerin fiyatları toplamı nedir?
# toplam = 0
# for x in urunler:
#     toplam += x["fiyat"]
# print(f"Ürünlerin fiyatları toplamı: {toplam}")




# 3- 25000 ile 40000 arasındaki ürünleri listeleyiniz.
# for x in urunler:
#     if 25000 < x["fiyat"] < 40000:
#         print(x)



# 4- Kullanıcıdan alınan anahtar kelimeye göre ürünleri listeleyiniz.
# userInput = input("bir anahtar kelime giriniz (Hp, Lenovo, Apple, Huawei, Casper): ").lower()
# for x in urunler:
#     if userInput in x["urunAdi"].lower():
#         print(x)