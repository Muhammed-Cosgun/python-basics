# file = open("dosya.txt", "w", encoding="utf-8")
# file.write("Emre Coşgun\n")
# file.write("Muhammed Coşgun\n")

# file.close()
# w modu ile metin yazdırdığımız dosyaya ekleme yapılmaz, eski içerikler tamamen silinir ve yeni yazdığımız metinler dosyaya aktarılır.


# # dosya yazma veya oluşturma işlemi
# with open("dosya.txt", "w", encoding="utf-8") as file:
#     file.write("Muhammed Coşgun\n")
#     file.write("Emre Coşgun\n")



# dosya okuma işlemi
# with open("dosya.txt", "r", encoding="utf-8") as file:
#     for i in file:
#         print(i, end="")
    


# yazma modunda açılır, dosya o konumda yoksa o konumda oluşturulur. varsa dosyadaki eski içerikler silinir, yeni içerikler yazılır.


