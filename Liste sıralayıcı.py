import logging

logging.basicConfig(
    filename="proje4ün.txt",
    format="%(asctime)s - %(levelname)s - %(message)s ",
    filemode="a",
    level=logging.DEBUG)

def bksırala(a):
    list.sort(a,reverse=True)
    print(liste1)

def kbsırala(a):
    list.sort(a)
    print(liste1)

while True:
    liste1 = []
    s = 0
    sayı = int(input("Kaç tane sayı girmek istediğinizi giriniz: "))
    while s != sayı:
        d = int(input("Girmek istediğiniz sayıları giriniz: "))
        liste1.append(d)
        s += 1
        if s == sayı:
            break

    soru1 = str(input("Girdiğiniz sayıları büyükten küçüğe sıralamak için (b)' yi küçükten büyüğe sıralamak için (k)' yı seçiniz: "))

    if soru1 == "b":
        bksırala(liste1)
        logger = logging.getLogger()
        logger.info(liste1)

    elif soru1 == "k":
        logger = logging.getLogger()
        kbsırala(liste1)

    else:
        print("Yanlış harfi tuşladınız")

    if soru1 == "b":
        soru2 = str(input("Büyükten küçüğe sıraladınız küçükten büyüğe de sıralamak ister misiniz (e/h):"))

        if soru2 == "e":
            kbsırala(liste1)
            logger.info(liste1)

        else:
            pass

    if soru1 == "k":
        soru3 = str(input("Küçükten büyüğe sıraladınız büyükten küçüğe de sıralamak ister misiniz (e/h): "))

        if soru3 == "e":
            bksırala(liste1)
            logger.info(liste1)

        else:
            pass

    dongu_kapa = str(input("programı sonlandırmak istiyor musunuz (e/h): "))

    if dongu_kapa == "e":
        break
    else:
        continue