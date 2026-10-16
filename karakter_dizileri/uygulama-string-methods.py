# kursAdi = "BtkAkademi Python ile Programlama Dersleri çalışmaları"
# website = "https://www.btkakademi.gov.tr/"

# 1- ' Btk Akademi ' karakter dizisinin baş ve sondaki boşluk karakterlerini siliniz. (strip)
# sonuc = kursAdi.strip()


# 2- kursAdi değişkenindeki tüm karakterleri küçük harfe çeviriniz.
# sonuc = kursAdi.lower()


# 3- website değişkeninde kaç tane '.' karakteri vardır?
# sonuc = website.count(".")

# 4- website değişkeni 'https' ile mi başlıyor?
# sonuc = website.startswith("https")

# 5- website 'tr' ile mi bitiyor?
# sonuc = website.endswith("tr")

# 6- kursAdi içerisindeki tüm karakterler harflerden mi oluşuyor
# sonuc = kursAdi.isalpha() # tüm karakterler harf mi diye kontrol eder. eğer stringte boşluk, nokta gibi işaretler varsa False döndürür.

# 7- kursAdi değişkenindeki tüm boşlukları '-' ile değiştiriniz.
# sonuc = kursAdi.replace(" ", "-")


# 8- kursAdi değişkenindeki Python kelimesini ReactJs ile değiştiriniz.
# sonuc = kursAdi.replace("Python", "ReactJs")

# 9- website değişkeni 'www' içeriyor mu?
# sonuc = website.find("www") # eğer geçiyorsa www'nun başladığı indexi döner. eğer geçmiyorsa -1 döner.
# sonuc = "www" in website # bu daha paratiktir. direkt var mı diye kontrol edip true veya false döndürür.

# 10- kursAdi değişkenini listeye çeviriniz.
# sonuc = kursAdi.split()

# print(sonuc[2])
# print(sonuc)