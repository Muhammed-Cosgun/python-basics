"""
    Uygulama 1: Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız.
    Alan: πr²
    Çevre: 2πr

    Uygulama 2: Klavyeden girilen km bilgisini mil cinsinden hesaplayınız.
    mil = km / 1.609344
"""

# 1. UYGULAMA
yaricap = float(input("yaricapi giriniz: "))
pi = 3.14

alan = pi * (yaricap ** 2)
cevre = 2 * pi * yaricap
print(f"Alan: {alan:.2f} Çevre: {cevre:.2f}")

# 2. UYGULAMA
km = float(input("kilometreyi gir: "))
mil = km / 1.609344
print(f"mil: {mil:.2f}")