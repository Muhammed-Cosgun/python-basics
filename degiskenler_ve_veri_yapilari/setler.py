# eğer indeksleme ile uğraşılmayacaksa liste yerine set kullanılabilir. 
# set elemanları güncellenemez,
# set elemanları indexslenemezler, sırasızlardır.
# eleman silinip eklenebilir ama güncellenemezler.
# süslü parantez ile tanımlanır. 

# meyveler = {"elma", "armut", 10}
# meyveler2 = {"elma", "armut", "kiraz", "kavun"}
# sonuc = meyveler[0] # herhangi bir şekilde indexle erişilemez.

# aynı eleman yalnızca bir kere bulunabilir.

# elemanların sırası yoktur, program her çalıştırıldığında yeniden rastgele oluşur.

# liste elemanlarına erişebilmek için döngüler kullanılabilir. herhangi bir şekilde index ile erişilemezler.
# for x in meyveler:
    # print(x)


# bir elemanın olup olmadığı da şu şekilde kontrol edilebilir.
# sonuc = "elma" in meyveler
# if sonuc == True:
#     sonuc = "Elma, meyveler listesinde bulunuyor"
# else:
#     sonuc = "Elma, meyveler listesinde bulunmuyor."


# metotlar
# meyveler.add("karpuz") # herhangi bir index belirtilemez.

# meyvelerde bulunup meyveler2'de bulunmayan nesneler
# meyveFarkMeyve2 = meyveler - meyveler2

# iki seti birleştirme işlemi
# meyveler.update(meyveler2)


# setten eleman silme
# meyveler.remove("vişne") # hata verir
# meyveler.discard("vişne") # hata vermez.
# bu ikisi de eleman silmeye yarar. remove, silinmek istenen eleman sette yoksa hata verir. discard ise sette bulunmayan bir eleman silinmek bile istense herhangi bir şekilde hata vermez.


# listede rastgele bir eleman siler. çünkü indexleme yok sette.
# meyveler.pop()



# liste elemanlarını tamamen silme
# meyveler.clear()

# sonuc = meyveler
# print(sonuc)