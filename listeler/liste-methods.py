# sayilar = [4,6,8,2,56,78,90,4,4]
# isimler = ['ahmet', 'abi', 'ali','canan', 'zeynep', 'gökhan', 'canan']

# LİSTE MİN-MAX BULMA
# sonuc = min(sayilar)
# sonuc = min(isimler)
# sonuc = max(sayilar)
# sonuc = max(isimler)

# LİSTE ELEMAN EKLEME
# sayilar.append(12)
# isimler.append('Meral')

# herhangi bir yere eleman ekleme. bu şekilde eleman eklemedeki mantık şudur: eklemek istediğimiz eleman yani 2. parametre, ilk parametredeki index numarasının listedeki yerine geçer. yerine geçilen eleman ise sağa kayar.
# sayilar.insert(0, 100)
# sayilar.insert(-1,100)
# sayilar.insert(-3, 100)
# sayilar.insert(2, 100)
# sayilar.insert(1, 100)
# sayilar.insert(len(sayilar), 100)  # listenin sonuna eleman ekler.




# LİSTEDE ELEMAN SİLME
# sayilar.pop() # varsayılan olarak son indexteki eleman silinir.
# sayilar.pop(0) # kendi istediğimiz indexteki elemanı da sildirebiliriz.

# isimler.remove("abi")  # index olarak değil de değer üzerinden silme işlemi yapılmak istenirse remove kullanılmalıdır.



# LİSTEDE SIRALAMA
# küçükten büyüğe ya da a dan z'ye sıralama
# sayilar.sort()
# isimler.sort()

# listeyi tersten sıralama
# sayilar.reverse()
# isimler.reverse()




# LİSTEDE ELEMAN SAYMA
# sonuc = sayilar.count(4) # herhangi bir elemanın listede kaç defa geçtiği sayılabilir. burada sayilar listesinde 4 kaç defa geçtiği bulundu.

# sonuc = isimler.count("canan")



# LİSTEDE ARAMA
# sonuc = sayilar.index(4) # 4 elemanı kaçıncı indextedir? bulduğu ilk 4 değerinin index numarasını verir.





# sonuc = sayilar
# sonuc = isimler

# print(sonuc)