# customers = ["sadikturan","ahmetyilmaz","cinarturan","yigitbilgi"]
# order_totals = [12000,13000,5000,15000]

# 1- 'sadikturan' kullanıcı adıyla yapılan 5000 liralık siparişi listeye ekleyiniz.
# customers.append("sadikturan")
# order_totals.append(5000)

# 2- Son eklenen siparişi siliniz.
# customers.pop()
# order_totals.pop()


# 3- Tüm müşteriler için aşağıdaki özet cümleyi yazdırınız.
# '<username>' isimli müşterinin sipariş toplamı '<10000>' liradır.
# elemanSayisi = len(customers)
# for i in range(elemanSayisi):
#     mesaj = f"{customers[i]} isimli müşterinin sipariş toplamı {order_totals[i]} liradır"
#     print(mesaj)


# 4- Müşterileri alfabetik olarak sıralayınız.
# customers.sort()
# print(customers)


# 5- Sipariş toplamlarını azalan şekilde sıralayınız.
# order_totals.sort(reverse=True)
# print(order_totals)



# 6- En düşük sipariş hangisidir?
# minSiparis = min(order_totals)
# print(minSiparis)


# 7- 'sadikturan' isimli kullanıcının kaç tane siparişi vardır?
# elemanSayisi = customers.count("sadikturan")
# mesaj = f"Sadik Turan isimli kullanıcnın {elemanSayisi} tane siparişi vardır."
# print(mesaj)


# 8- Customers listesinden 'ahmetyilmaz' isimli kullanıcıyı siliniz.
# customers.remove("ahmetyilmaz")
# print(customers)



# 9- Listelerdeki tüm içerikleri siliniz.
# customers.clear()
# order_totals.clear()

# print(customers)
# print(order_totals)

# 10- Kullanıcıdan aldığınız kullanıcı adı ve sipariş toplamlarını listeye ekleyiniz.
# username = input("kullanıcı adı giriniz: ")
# order_total = int(input("sipariş toplamını giriniz: "))
# customers.append(username)
# order_totals.append(order_total)

# print(customers)
# print(order_totals)