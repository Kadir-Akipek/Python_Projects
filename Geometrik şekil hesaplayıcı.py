from os import system, name

π = 3.14

def clear():
      if name == 'nt':
            _ = system('cls')

def menu():
    print("MENÜ")
    print("======================")
    print("1- Kare\n"
          "2- Küp\n"
          "3- Çember\n"
          "4- Daire\n"
          "5- Eşkenar üçgen\n"
          "6- Dikdörtgen")

def cagır(seç):
    if seç == 1:
        kare()
    elif seç == 2:
        küp()
    elif seç == 3:
        çember()
    elif seç == 4:
        daire()
    elif seç == 5:
        eşkenar()
    elif seç == 6:
        dikdörtgen()

def kare():
    kare_uzunluk = int(input("Karenin bir kenarının uzunluğunu giriniz: "))
    print("Karenin çevresi:",str(kare_uzunluk*4)+" cm")
    print("Karenin alanı:",str(kare_uzunluk**2)+" cm²")

def küp():
    küp_uzunluk = int(input("Küpün bir kenarının uzunluğunu giriniz: "))
    print("Küpün alanı:",str(6*(küp_uzunluk**2))+" cm²")
    print("Küpün hacmi:",str(küp_uzunluk**3)+" cm³")
    print("küpün kenar uzunluları toplamı:",str(12*küp_uzunluk)+" cm")

def çember():
    r = int(input("Çemberin yarıçapını giriniz: "))
    ç = str(2*π*r)
    print("Çemberin çevresi:",ç[:5]," cm")

def daire():
    r = int(input("Dairenin yarıçapını giriniz: "))
    print("Dairenin çevresi:",str(2 * π * r)+" cm")
    print("Dairenin alanını:",str(π * (r**2))+" cm²")

def eşkenar():
    eşkenar_uzunluk = int(input("Eşkenar üçgenin bir kenarını uzunluğunu giriniz: "))
    print("Eşkenar üçgenin çevresi:",str(eşkenar_uzunluk*3)+" cm")
    e = (str(((eşkenar_uzunluk**2)*1.7) / 4))
    print("Eşkenar üçgenin alanı:",e[0:5]," cm")

def dikdörtgen():
    a = int(input("Dikdörtgenin kısa kenarının uzunluğunu giriniz: "))
    b = int(input("Dikdörtgenin uzun kenarının uzunluğunu giriniz: "))
    print("Dikdörtgenin çevresi:",str((a + b)*2)+" cm")
    print("Dikdörtgenin alanı:",str(a * b)+" cm²")

while True:
    print("                  GEOMETRİK ŞEKİL HESAPLAMA UYGULAMASINA HOŞ GELDİNİZ")
    print("--------------------------------------------------------------------------------------")
    print("")
    menu()
    seç = int(input("Hesaplamak istediğiniz geometrik şekli seçiniz: "))
    cagır(seç)
    dongu_kapa = str(input("programı sonlandırmak istiyor musunuz (e/h): "))

    if dongu_kapa == "e":
        break
    else:
        clear()