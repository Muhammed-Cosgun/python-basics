# open(dosya_adi,dosya_erişim_modu)
# dosya_erişim_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "r": (Read) okuma. Dosya konumda yoksa hata verir.
# "w": (Write) yazma modu.
#    ** Dosyayı konumda oluşturur.
#    ** Dosya içeriğini siler ve yeniden ekleme yapar.
# "a": (Append) ekleme. Dosya konumda yoksa oluşturur.
# "r+": Hem okuma hem yazma modunda açılır. Dosya konumda yoksa hata verir.


# • "w" (Write - Yazma) modu bencildir: Dosyayı açtığı an içindeki her şeyi tamamen siler (sıfırlar) ve sadece senin o an verdiğin yeni metni yazar. Dosya yoksa sıfırdan oluşturur.
# • "a" (Append - Ekleme) modu vefakardır: Dosyanın içindeki eski bilgilere asla dokunmaz, imleci (cursor) dosyanın en sonuna götürür ve yeni metinleri oradan itibaren eklemeye başlar. Dosya yoksa o da sıfırdan oluşturur.

# with open("dosya.txt", "a", encoding="utf-8") as file:
#     # file.seek(0) # append modunda cursoru hareket ettiremeyiz. bu çalışmaz.
#     file.write("ikinci satır\n")


with open("dosya.txt", "r+", encoding="utf-8") as file:
    # r+ modu = dosya hem okuma modunda hem de yazma modunda açılır. dosya eğer ilgili konumda yoksa hata verir.
    # file.seek(40) # cursoru en başa getirir.
    print(file.read())
    file.write("yeni satır\n")