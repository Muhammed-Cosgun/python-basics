# local scope
# global scope

# x = "global scope" # global scope

# def my_func():
#     x = "local scope" # yerel scope
#     print(x)

# my_func()
# print(x)

# name = "Çınar"
# def change_name(new_name):
#     name = new_name
#     print(name)

# change_name("ada")
# print(name)
# bu iki name birbirinden farklı değişkenlerdir. ikisi de farklı adreslerde tutulur.




# name = "Çınar"
# def change_name(new_name):
#     global name
#     name = new_name
#     print(name)

# change_name("ada")
# print(name)
# burada ise 2 name de aynı değişkendir ve aynı adreslerde tutulurlar.


# name = "Çınar"
# def change_name(new_name):
#     global name
#     name = new_name
#     print(name)

# change_name("ada")
# print(name)


# name = "global string"
# def greeting():
#     # name = "Çınar"

#     def hello():
#         # name = "Ada"
#         print("Hello ", name) 
#     hello()

# greeting()
# bu konuda mantık şudur: en içte en yerelde aynı isimde değişken varsa bu değişken farklı bir değişkendir. değeri de adresi de farklıdır. ama yerelde herhangi bir şekidle ayı isimle tanımlama yoksa ise globaldeki değişken aynen kullanılır.




# x = 50
# def test(x):
#     print(f"x: {x}")
#     x = 100
#     print(f"changed x to {x}")

# test(x)
# print(x)
# yukarıdaki gibi kullanımda x yerel ve global olarak 2 farklı değişken olarak ramde tutulur.




# x = 50
# def test():
#     global x  
#     print(f"x: {x}")

#     x = 100
#     print(f"changed x to {x}")

# test()
# print(x) 
# yukarıdaki gibi kullanımda ise x hep aynı değişkendir.