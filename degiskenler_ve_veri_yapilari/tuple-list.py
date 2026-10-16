# tuplenin listeden farkı; tuple'ye eleman ekleme, elemen silme gibi işlemler yapılamaz.
# listede ise listeye eleman ekleme, silme gibi işlemler yapılabilir.

# my_list = [1, 2, 3]
# my_tuple = (1,2,3) # değiştirilemezler. performans olarak tupleler, listelerden daha performanslıdır. mesela veri tabanından veri alınacaksa ve bu alınacak verilerle ilgili ekleme, silme veya güncelleme yapılmayacaksa tuple kullanılması mantıklıdır. çünkü tuple daha performanslı ve hızlıdır. 
# ya da mesela elimizdeki verinin güvenliği ve değiştirilemezliği isteniyorsa yine tuple kullanılması mantıklıdır.


# my_list[0] = 2 # bunda problem yoktur.

# my_tuple[0] = 2 # bunda hata verir. çünkü tuple'de eleman ekleme veya silme veya güncelleme işlemi yapılamaz.

# my_tuple.append(3) # bunda da hata verir. tuple'ye ekleme işlemi yapılamaz.

# sonuc = my_tuple.count(1) 

# my_list2 = [2, 3, 4]

# my_tuple2 = tuple(my_list2) # bu şekilde listeler, tuplelere dönüştürülebilir.

# my_list3 = list(my_tuple2) # bu şekilde de tupleler, listelere dönüştürülebilir.
# print(type(my_list3))

# sonuc = my_list

# print(type(my_tuple2))