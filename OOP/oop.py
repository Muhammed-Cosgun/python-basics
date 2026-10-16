# OOP = Object Oriented Programming = nesne yönelimli programlama

# Instances = Nesne = Object

class Product:
    # method = sınıflar içerisindeki fonksiyonlara methot denir.
    # attribute, property


    # bu contructordur. nesne çalıştığı an otomatik olarak oluşur.
    def __init__(self, name, price, isActive):
        self.name = name
        self.price = price
        self.isActive = isActive


    # instance method
    def intro(self):
        return f"ürün adı: {self.name} ürün fiyat:{self.price}"

    
# bunlar instance, object diye geçer. kısacası nesne bunlar.
p1 = Product("IPhone 15", 50000, True) # sınıftan nesne türetme işlemi.
p2 = Product("IPhone 15 Pro", 40000, True)
p3 = Product("Samsung S24", 30000, False)

urunler = [p1, p2, p3]
for urun in urunler:
    if urun.isActive:
        print(urun.intro())
    

sonuc = p1.name
sonuc = p2.name
sonuc = p3.name
sonuc = p3.price

# print(sonuc)


