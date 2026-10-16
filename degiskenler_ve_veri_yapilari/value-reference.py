# x = 10
# y = 20

# x = y
# y = 30
# bu veri tipleri değer tipleridir. bir değişirse diğer değişmez.
# (value types)




# referans tipleri ise bellekte değer olarak değil de adres olarak saklanır.
# liste türleri referans yani adres türleridirler.
# a = ["portakal", "mandalina"]
# b = ["elma", "armut"]

# a = b # b'nin adresi a'ya atanır. yani a listesi de şu şekle dönüştü: ["elma", "armut"]
# mesela iki kap var diyelim(iki adres.). bir kabın değeri diğer kaba eşitlenince artık elimizde bir kap kalıyor.(yani elimizde bir adres kalıyor.)
# aynı kabın adresleri iki farklı değişkende tutulmuş olur.
# yani bu durumdan sonra a'da veya b'de yapılan herhangi bir değişiklik diğerine de yansır. çünkü adresleri aynıdır.
# yani kısacası listenin kendisi değil, adresi eşitlenir.
# bu şekilde kendisine adres kopyalanan değişken, diğer değişkene tamamen eşit olur.
#yani kısacası iki değişkenin her şeyleri eşit oluyor. birinde değişiklik yapınca diğerinde de değşiklik oluyor.

# b[0] = "Muhammed"
# print(a)





# eğer adresler eşitlenmek istenmiyorsa, sadece listedeki elemanlar başka bir adrese kopyalanmak istenebilir. bu durumda yukarıdaki işlem işimize yaramayacaktır. 
# bu durumda liste metotu kullanmak gerekir.

# listeA = [10, 20]
# listeB = listeA.copy() # bu şekilde listeB'nin adresi listeA'dan farklı olur. bu sayede bir listede yapılan güncelleme diğer listeye işlenmez.

# şu ikisi tamamen aynıdır ve sadece değeri kopyalarlar: listeB=listeA.copy()   =   listeB=list(listeA)



# listeB.append(30)


# print(f"Liste B: {listeB}")
# print(f"Liste A: {listeA}")


# print(x, y)