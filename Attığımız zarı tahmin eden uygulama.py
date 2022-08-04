import random

zar1 = int(input("İstediğiniz ilk zar değerini giriniz: "))
zar2 = int(input("İstediğiniz ikinci zar değerini giriniz: "))

sayac = 0

while "x" != "y":
    sayac = sayac + 1
    a = random.randint(1,6)
    b = random.randint(1,6)
    print(str(sayac)+". deneme",a,b)
    if zar1 == a and zar2 == b:
        print("İstediğiniz 2 zar değeri de ",sayac,".denemede bulundu")
        break