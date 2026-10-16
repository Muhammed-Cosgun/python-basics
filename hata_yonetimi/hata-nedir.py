# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x / y)
# except:
#     print("hata oluştu")

# ZeroDivisionError = 0'a bölme hatası
# ValueError = 
# SyntaxError = yazım yanlışı
# NameError = tanımlanmayan bir şeyin kullanılmaya çalışılması
# TypeError = hatalı parametre kullanımından dolayı
# IndexError = yanlış index kullanımından dolayı
# KeyError = olmayan bir keye erişilmeye çalışılması
# AttributeError = olmayan bir özelliğe ulaşmak istediğimizde gelen hata.


# x = int(input("x: "))
# y = int(input("y: "))
# print(x / y)

# print(len(10)) # typeError
# print(10 + 'a') #typeError
# while True:
#     try: 
#         x = int(input("x: "))
#         y = int(input("y: "))
#         print(x/y)

    # except (ZeroDivisionError, ValueError) as e: # bu şekilde 2 hataya aynı anda aynı mesajı da verebiliriz.
    #     print("x ve y sayı olmalıdır. Sıfır olamaz.")
    #     print(e)
    # except ZeroDivisionError: # sadece bu hata geldiğinde çalışır.
    #     print("y sıfır olamaz")
    # except ValueError: # yine burada sadece bu hata geldiğinde çalışır.
        # print("x ve y sayı olmalıdır.")
    # except Exception as e: # diğer tüm hatalarda ise burası çalışır.
    #     print("bilinmeyen bir hata oluştu")
    #     print(e)
    # else:
    #     print("her şey yolunda") # herhangi bir except bloğu çalışılmazsa burası çalışır.
    #     break
    # finally:
    #     print("finally bloğu çalıştı.")  # burası ise her zaman çalışır.