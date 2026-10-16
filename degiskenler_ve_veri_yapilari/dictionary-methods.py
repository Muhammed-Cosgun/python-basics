# yemekTarifi = {
#     "yemekAdi": "Musakka",
#     "yemekTarifi": "tarif açıklaması",
#     "resim": "1.jpeg"
# }

# access items
# sonuc = yemekTarifi["yemekTarifi"] # value değerlerine ulaşabilmek için 1. yol bu.
# sonuc = yemekTarifi.get("yemekAdi")  # bu şekilde de value değerlerine ulaşanbilriz.
# sonuc = yemekTarifi.keys() # sözlükteki bütün key bilgileri gelir.
# sonuc = yemekTarifi.values()
# sonuc = yemekTarifi.items() # sözlük yapısı liste şeklinde düzenlenir.



# update items
# yemekTarifi["yemekAdi"] = "Mantı"   # bu şekilde güncelleme yapılabilir.
# yemekTarifi.update({"yemekAdi": "Cacık"}) # bu şekilde metotla birlikte de güncelleme yapılabilir.

# yemekTarifi.update({"yemekAdi2": "Gilik"}) # bu şekilde olmayan bir anahtar ismi girilerek de ekleme işlemi yapılabilir. yani güncelleme komutuyla ekleme işlemi de yapılabilir.




# delete items
# yemekTarifi.pop("yemekAdi") # istenen eleman listeden silinebilir.
# yemekTarifi.popitem() # vardayılan olarak dictionary'deki son key-value çiftini siler.
# yemekTarifi.clear() # liste içerisindeki bütün elemanlar bu şekilde silinebilir.

# sonuc = yemekTarifi
# print(sonuc)







