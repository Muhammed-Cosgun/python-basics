# with open("markalar.txt", "a") as file:
#     file.write("6-Bmw")

# append = sadece sonuna ekler.
# r+ = seek ile belirlediğimiz konuma ekleme yapabilir.




# en başa eklemek:
# with open("markalar.txt", "r+", encoding="utf-8") as file:
#     markalar = file.read()
#     markalar = "1-Toyota\n" + markalar
#     file.seek(0)  # bu şekilde yapıldığında imleç en başa gelir ama en baştaki verinün üzerine yazar, öteleme yapmaz.
#     file.write(markalar)



# ortaya eklemek
# with open("markalar.txt", "r+", encoding="utf-8") as file:
#     markalar = file.readlines() # okuduğu satırları liste halinde tutar.
#     markalar.insert(2, "3-Renault\n")
#     file.seek(0)
#     # for marka in markalar:
#     #     file.write(marka)
#     file.writelines(markalar)

# with open("markalar.txt", "r", encoding="utf-8") as file:
#     print(file.read())