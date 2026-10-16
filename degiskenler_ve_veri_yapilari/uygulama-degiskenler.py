# """
# Aşağıdaki müşterinin bilgilerini ve satın aldığı ürün bilgilerini değişkenler içerisinde saklayınız.
# Toplam ödenen ücret nedir?
# Ödenen miktarın kdv oranı nedir? (%18)

# Sadık Turan
# 05321234567
# info@sadikturan.com
# Kocaeli

# Satın Alınan Ürünler

# Ürün adı: Kablosuz Mouse
# Fiyatı: 550 TL

# Ürün adı: Kablosuz Klavye
# Fiyatı: 650 TL

# Ürün adı: Dizüstü Bilgisayar
# Fiyatı: 55.000 TL

# """

musteriAd = "Sadık Turan"
musteriTelNo = "05321234567"
musteriMail = "info@sadikturan.com"
musteriSehir = "Kocaeli"

urunMouse = 550
urunKlavye = 650
urunBilgisayar = 55000
urunToplamTutar = urunMouse + urunKlavye + urunBilgisayar
print("Toplam ödenen ücret = ", urunToplamTutar)


kdvOrani = 0.18
odenenKdvTutari = urunToplamTutar * kdvOrani
print("Toplam ödenene Kdv Miktarı: ", odenenKdvTutari)