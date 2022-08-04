from os import system, name

def clear():
      if name == 'nt':
            _ = system('cls')

def menu():
    print("MENÜ")
    print("======================")
    print("1- Uzunluk birimleri\n"
          "2- Ağırlık birimleri\n"
          "3- Hacim birimleri\n"
          "4- Data birimleri\n"
          "5- Sıcaklık birimleri\n")

def menu_secim(birim_sınıfı):
    if birim_sınıfı == 1:
        uzunluk_birimleri()
    elif birim_sınıfı == 2:
        ağırlık_birimleri()
    elif birim_sınıfı == 3:
        hacim_birimleri()
    elif birim_sınıfı == 4:
        data_birimleri()
    elif birim_sınıfı == 5:
        sıcaklık_birimleri()
    elif birim_sınıfı == 6:
        çıkış()
    else:
        "Yanlış rakamı tuşladınız"

while True:
    def ana_menu_don():
        clear()
        print("                          BİRİM ÇEVİRME UYGULAMASINA HOŞ GELDİNİZ")
        print("--------------------------------------------------------------------------------------")
        print("")
        menu()
        birim_sınıfı = int(input("Çevirmek istediğiniz sınıfı seçiniz: "))
        menu_secim(birim_sınıfı)

    def uzunluk_birimleri():
        print("1- Kilometre\n""2- Hektometre\n""3- Dekametre\n""4- Metre\n""5- Desimetre\n""6- Santimetre\n""7- Milimetre\n""8- Ana menüye dön")
        uzunluk_seçimi = int(input("Hangi birimden işlem yapmak istersiniz: "))
        if(uzunluk_seçimi == 8):
            ana_menu_don()
        clear()
        menualt_uzunluk(uzunluk_seçimi)

    def seçim_yap_uzunluk(uzunluk_seçimi):
        if uzunluk_seçimi == 1 :
            secim = "Kilometre"
        elif uzunluk_seçimi == 2:
            secim = "Hektometre"
        elif uzunluk_seçimi == 3:
            secim = "Dekametre"
        elif uzunluk_seçimi == 4:
            secim = "Metre"
        elif uzunluk_seçimi == 5:
            secim = "Desimetre"
        elif uzunluk_seçimi == 6:
            secim = "Santimetre"
        elif uzunluk_seçimi == 7:
            secim = "Milimetre"
        return secim

    def menualt_uzunluk(uzunluk_seçimi):
        ilkbirim_isim = seçim_yap_uzunluk(uzunluk_seçimi)
        ilkbirim_miktar = float(input("Hesaplamak istediğiniz "+ilkbirim_isim+" değerini giriniz: "))
        if uzunluk_seçimi == 1:
            ikincibirim = int(input("\n""2- Hektometre\n""3- Dekametre\n""4- Metre\n""5- Desimetre\n""6- Santimetre\n""7- Milimetre\n""8- Ana menüye döner\n""çevirmek istediğiniz birimi seçiniz: "))
        elif uzunluk_seçimi == 2:
            ikincibirim = int(input("1- Kilometre\n""\n""3- Dekametre\n""4- Metre\n""5- Desimetre\n""6- Santimetre\n""7- Milimetre\n""8- Ana menüye döner\n""çevirmek istediğiniz birimi seçiniz: "))
        elif uzunluk_seçimi == 3:
            ikincibirim = int(input("1- Kilometre\n""2- Hektometre\n""\n""4- Metre\n""5- Desimetre\n""6- Santimetre\n""7- Milimetre\n""8- Ana menüye döner\n""çevirmek istediğiniz birimi seçiniz: "))
        elif uzunluk_seçimi == 4:
            ikincibirim = int(input("1- Kilometre\n""2- Hektometre\n""3- Dekametre\n""\n""5- Desimetre\n""6- Santimetre\n""7- Milimetre\n""8- Ana menüye döner\n""çevirmek istediğiniz birimi seçiniz: "))
        elif uzunluk_seçimi == 5:
            ikincibirim = int(input("1- Kilometre\n""2- Hektometre\n""3- Dekametre\n""4- Metre\n""\n""6- Santimetre\n""7- Milimetre\n""8- Ana menüye döner\n""çevirmek istediğiniz birimi seçiniz: "))
        elif uzunluk_seçimi == 6:
            ikincibirim = int(input("1- Kilometre\n""2- Hektometre\n""3- Dekametre\n""4- Metre\n""5- Desimetre\n""\n""7- Milimetre\n""8- Ana menüye döner\n""çevirmek istediğiniz birimi seçiniz: "))
        elif uzunluk_seçimi == 7:
            ikincibirim = int(input("1- Kilometre\n""2- Hektometre\n""3- Dekametre\n""4- Metre\n""5- Desimetre\n""6- Santimetre\n""\n""8- Ana menüye döner\n""çevirmek istediğiniz birimi seçiniz: "))
        if ikincibirim == 8:
            ana_menu_don()
        ikincibirim_isim = seçim_yap_uzunluk(ikincibirim)
        if(uzunluk_seçimi < ikincibirim):
            sonuc = ilkbirim_miktar * 10**(ikincibirim-uzunluk_seçimi)
        else:
            sonuc = ilkbirim_miktar / (10**(uzunluk_seçimi-ikincibirim))
        print(sonuc,ikincibirim_isim)

    def ağırlık_birimleri():
        print("1- Kilogram\n""2- Hektogram\n""3- Dekagram\n""4- Gram\n""5- Desigram\n""6- Santigram\n""7- Miligram\n""8- Ana menüye dön")
        ağırlık_seçimi = int(input("Hangi birimden işlem yapmak istersiniz: "))
        if(ağırlık_seçimi == 8):
            ana_menu_don()
        clear()
        menualt_ağırlık(ağırlık_seçimi)

    def seçim_yap_ağırlık(ağırlık_seçimi):
        if ağırlık_seçimi == 1:
            secim = "Kilogram"
        elif ağırlık_seçimi == 2:
            secim = "Hektogram"
        elif ağırlık_seçimi ==3:
            secim = "Dekagram"
        elif ağırlık_seçimi == 4:
            secim = "Gram"
        elif ağırlık_seçimi == 5:
            secim = "Desigram"
        elif ağırlık_seçimi == 6:
            secim = "Santigram"
        elif ağırlık_seçimi == 7:
            secim = "Miligram"
        return secim

    def menualt_ağırlık(ağırlık_seçimi):
        ilkbirim_isim = seçim_yap_ağırlık(ağırlık_seçimi)
        ilkbirim_miktar = float(input("Hesaplamak istediğiniz "+ilkbirim_isim+" değerini giriniz: "))
        if ağırlık_seçimi == 1:
            ikincibirim = int(input("\n""2- Hektogram\n""3- Dekagram\n""4- Gram\n""5- Desigram\n""6- Santigram\n""7- Miligram\n""8- Ana menüye dön\n""çevirmek istediğiniz birimi seçiniz :"))
        elif ağırlık_seçimi == 2:
            ikincibirim = int(input("1- Kilogram\n""\n""3- Dekagram\n""4- Gram\n""5- Desigram\n""6- Santigram\n""7- Miligram\n""8- Ana menüye dön\n""çevirmek istediğiniz birimi seçiniz :"))
        elif ağırlık_seçimi == 3:
            ikincibirim = int(input("1- Kilogram\n""2- Hektogram\n""\n""4- Gram\n""5- Desigram\n""6- Santigram\n""7- Miligram\n""8- Ana menüye dön\n""çevirmek istediğiniz birimi seçiniz :"))
        elif ağırlık_seçimi == 4:
            ikincibirim = int(input("1- Kilogram\n""2- Hektogram\n""3- Dekagram\n""\n""5- Desigram\n""6- Santigram\n""7- Miligram\n""8- Ana menüye dön\n""çevirmek istediğiniz birimi seçiniz :"))
        elif ağırlık_seçimi == 5:
            ikincibirim = int(input("1- Kilogram\n""2- Hektogram\n""3- Dekagram\n""4- Gram\n""\n""6- Santigram\n""7- Miligram\n""8- Ana menüye dön\n""çevirmek istediğiniz birimi seçiniz :"))
        elif ağırlık_seçimi == 6:
            ikincibirim = int(input("1- Kilogram\n""2- Hektogram\n""3- Dekagram\n""4- Gram\n""5- Desigram\n""\n""7- Miligram\n""8- Ana menüye dön\n""çevirmek istediğiniz birimi seçiniz :"))
        elif ağırlık_seçimi == 7:
            ikincibirim = int(input("1- Kilogram\n""2- Hektogram\n""3- Dekagram\n""4- Gram\n""5- Desigram\n""6- Santigram\n""\n""8- Ana menüye dön\n""çevirmek istediğiniz birimi seçiniz :"))
        if ikincibirim == 8:
            ana_menu_don()
        ikincibirim_isim = seçim_yap_ağırlık(ikincibirim)
        if ağırlık_seçimi < ikincibirim:
            sonuc = ilkbirim_miktar * (10**(ikincibirim-ağırlık_seçimi))
        else:
            sonuc =  ilkbirim_miktar / (10**(ağırlık_seçimi-ikincibirim))
        print(sonuc,ikincibirim_isim)

    def data_birimleri():
        print("1- Exabyte\n""2- Petabyte\n""3- Terabyte\n""4- Gigabyte\n""5- Megabyte\n""6- Kilobyte\n""7- Byte\n""8- Ana menüye dön")
        data_seçimi = int(input("Hangi birimden işlem yapmak istersiniz: "))
        if(data_seçimi == 8):
            ana_menu_don()
        clear()
        menualt_data(data_seçimi)

    def seçim_yap_data(data_seçimi):
        if data_seçimi == 1:
            secim = "Exabyte"
        elif data_seçimi == 2:
            secim = "Petabyte"
        elif data_seçimi == 3:
            secim = "Terabyte"
        elif data_seçimi == 4:
            secim = "Gigabyte"
        elif data_seçimi == 5:
            secim = "Megabyte"
        elif data_seçimi == 6:
            secim = "Kilobyte"
        elif data_seçimi == 7:
            secim = "Byte"
        return secim

    def menualt_data(data_seçimi):
        ilkbirim_isim = seçim_yap_data(data_seçimi)
        ilkbirim_miktar = float(input("Hesaplamak istediğiniz "+ilkbirim_isim+" değerini giriniz: "))
        if data_seçimi == 1:
            ikincibirim = int(input("\n""2- Petabyte\n""3- Terabyte\n""4- Gigabyte\n""5- Megabyte\n""6- Kilobyte\n""7- Byte\n""8- Ana menüye döner\n""çevirmek istediğiniz birimi seçiniz: "))
        elif data_seçimi == 2:
            ikincibirim = int(input("1- Exabyte\n""\n""3- Terabyte\n""4- Gigabyte\n""5- Megabyte\n""6- Kilobyte\n""7- Byte\n""8- Ana menüye döner\n""çevirmek istediğiniz birimi seçiniz: "))
        elif data_seçimi == 3:
            ikincibirim = int(input("1- Exabyte\n""2- Petabyte\n""\n""4- Gigabyte\n""5- Megabyte\n""6- Kilobyte\n""7- Byte\n""8- Ana menüye döner\n""çevirmek istediğiniz birimi seçiniz: "))
        elif data_seçimi == 4:
            ikincibirim = int(input("1- Exabyte\n""2- Petabyte\n""3- Terabyte\n""\n""5- Megabyte\n""6- Kilobyte\n""7-Byte\n""8- Ana menüye döner\n""çevirmek istediğiniz birimi seçiniz: "))
        elif data_seçimi == 5:
            ikincibirim = int(input("1- Exabyte\n""2- Petabyte\n""3- Terabyte\n""4- Gigabyte\n""\n""6- Kilobyte\n""7- Byte\n""8- Ana menüye döner\n""çevirmek istediğiniz birimi seçiniz: "))
        elif data_seçimi == 6:
            ikincibirim = int(input("1- Exabyte\n""2- Petabyte\n""3- Terabyte\n""4- Gigabyte\n""5- Megabyte\n""\n""7- Byte\n""8- Ana menüye döner\n""çevirmek istediğiniz birimi seçiniz: "))
        elif data_seçimi == 7:
            ikincibirim = int(input("1- Exabyte\n""2- Petabyte\n""3- Terabyte\n""4- Gigabyte\n""5- Megabyte\n""6- Kilobyte\n""\n""8- Ana menüye döner\n""çevirmek istediğiniz birimi seçiniz: "))
        if ikincibirim == 8:
            ana_menu_don()
        ikincibirim_isim = seçim_yap_data(ikincibirim)
        if data_seçimi < ikincibirim:
            sonuc = (ilkbirim_miktar * 1024*(ikincibirim-data_seçimi))
        else:
            sonuc = (ilkbirim_miktar / 1024*(data_seçimi-ikincibirim))
        print(sonuc,ikincibirim_isim)

    def hacim_birimleri():
        print("1- Kilometreküp\n""2- Hektometreküp\n""3- Dekametreküp\n""4- Metreküp\n""5- Desimetreküp\n""6- Santimetreküp\n""7- Milimetreküp\n""8- Ana menüye dön")
        hacim_seçimi = int(input("Hangi birimden işlem yapmak istersiniz: "))
        if(hacim_seçimi == 8):
            ana_menu_don()
        clear()
        menualt_hacim(hacim_seçimi)

    def seçim_yap_hacim(hacim_seçimi):
        if hacim_seçimi == 1 :
            secim = "Kilometreküp"
        elif hacim_seçimi == 2:
            secim = "Hektometreküp"
        elif hacim_seçimi == 3:
            secim = "Dekametreküp"
        elif hacim_seçimi == 4:
            secim = "Metreküp"
        elif hacim_seçimi == 5:
            secim = "Desimetreküp"
        elif hacim_seçimi == 6:
            secim = "Santimetreküp"
        elif hacim_seçimi == 7:
            secim = "Milimetreküp"
        return secim

    def menualt_hacim(hacim_seçimi):
        ilkbirim_isim = seçim_yap_hacim(hacim_seçimi)
        ilkbirim_miktar = float(input("Hesaplamak istediğiniz "+ilkbirim_isim+" değerini giriniz: "))
        if hacim_seçimi == 1:
            ikincibirim = int(input("\n""2- Hektometreküp\n""3- Dekametreküp\n""4- Metreküp\n""5- Desimetreküp\n""6- Santimetreküp\n""7- Milimetreküp\n""8- Ana menüye döner\n""çevirmek istediğiniz birimi seçiniz: "))
        elif hacim_seçimi == 2:
            ikincibirim = int(input("1- Kilometreküp\n""\n""3- Dekametreküp\n""4- Metreküp\n""5- Desimetreküp\n""6- Santimetreküp\n""7- Milimetreküp\n""8- Ana menüye döner\n""çevirmek istediğiniz birimi seçiniz: "))
        elif hacim_seçimi == 3:
            ikincibirim = int(input("1- Kilometreküp\n""2- Hektometreküp\n""\n""4- Metreküp\n""5- Desimetreküp\n""6- Santimetreküp\n""7- Milimetreküp\n""8- Ana menüye döner\n""çevirmek istediğiniz birimi seçiniz: "))
        elif hacim_seçimi == 4:
            ikincibirim = int(input("1- Kilometreküp\n""2- Hektometreküp\n""3- Dekametreküp\n""\n""5- Desimetreküp\n""6- Santimetreküp\n""7- Milimetreküp\n""8- Ana menüye döner\n""çevirmek istediğiniz birimi seçiniz: "))
        elif hacim_seçimi == 5:
            ikincibirim = int(input("1- Kilometreküp\n""2- Hektometreküp\n""3- Dekametreküp\n""4- Metreküp\n""\n""6- Santimetreküp\n""7- Milimetreküp\n""8- Ana menüye döner\n""çevirmek istediğiniz birimi seçiniz: "))
        elif hacim_seçimi == 6:
            ikincibirim = int(input("1- Kilometreküp\n""2- Hektometreküp\n""3- Dekametreküp\n""4- Metreküp\n""5- Desimetreküp\n""\n""7- Milimetreküp\n""8- Ana menüye döner\n""çevirmek istediğiniz birimi seçiniz: "))
        elif hacim_seçimi == 7:
            ikincibirim = int(input("1- Kilometreküp\n""2- Hektometreküp\n""3- Dekametreküp\n""4- Metreküp\n""5- Desimetreküp\n""6- Santimetreküp\n""\n""8- Ana menüye döner\n""çevirmek istediğiniz birimi seçiniz: "))
        if ikincibirim == 8:
            ana_menu_don()
        ikincibirim_isim = seçim_yap_hacim(ikincibirim)
        if(hacim_seçimi < ikincibirim):
            sonuc = ilkbirim_miktar * ((10**(ikincibirim-hacim_seçimi))**3)
        else:
            sonuc = ilkbirim_miktar / ((10**(hacim_seçimi-ikincibirim))**3)
        print(sonuc,ikincibirim_isim)

    def  sıcaklık_birimleri():
        print("1- Celcius\n""2- Kelvin\n""3- Fahreneit\n""4- Ana menüye dön")
        sıcaklık_seçimi = int(input("Hangi birimden işlem yapmak istersiniz: "))
        if sıcaklık_seçimi == 8:
            ana_menu_don()
        clear()
        menualt_sıcaklık(sıcaklık_seçimi)

    def seçim_yap_sıcaklık(sıcaklık_seçimi):
        if sıcaklık_seçimi == 1:
            secim = "Celcius"
        elif sıcaklık_seçimi == 2:
            secim = "Kelvin"
        elif sıcaklık_seçimi == 3:
            secim = "Fahreneit"
        return secim

    def menualt_sıcaklık(sıcaklık_seçimi):
        ilkbirim_isim = seçim_yap_sıcaklık(sıcaklık_seçimi)
        ilkbirim_miktar = float(input("Hesaplamak istediğiniz "+ilkbirim_isim+" değerini giriniz: "))
        if sıcaklık_seçimi == 1:
            ikincibirim = int(input("\n""2- Kelvin\n""3- Fahreneit\n""4- Ana menüye dön\n""çevirmek istediğiniz birimi seçiniz: "))
            if ikincibirim == 2:
                sonuc = ilkbirim_miktar + 273.15
                print(sonuc,"Kelvin")
            elif ikincibirim == 3:
                sonuc = ilkbirim_miktar * 1.8 + 32
                print(sonuc,"Fahreneit")
        if sıcaklık_seçimi == 2:
            ikincibirim = int(input("1- Celcius\n""\n""3- Fahreneit\n""4- Ana menüye dön\n""çevirmek istediğiniz birimi seçiniz: "))
            if ikincibirim == 1:
                sonuc = ilkbirim_miktar - 273.15
                print(sonuc,"Celcius")
            elif ikincibirim == 3:
                sonuc = ilkbirim_miktar * 1.8 - 459.67
                print(sonuc,"Fahreneit")
        if sıcaklık_seçimi == 3:
            ikincibirim = int(input("1- Celcius\n""2- Kelvin\n""\n""4- Ana menüye dön\n""çevirmek istediğiniz birimi seçiniz: "))
            if ikincibirim == 1:
                sonuc = (ilkbirim_miktar-32) * 5/9
                print(sonuc,"Celcius")
            elif ikincibirim == 2:
                sonuc = (ilkbirim_miktar + 459.67) * 5/9
                print(sonuc,"Kelvin")
        if sıcaklık_seçimi == 4:
            ana_menu_don()

    def  sıcaklık_birimleri():
        print("1- Celcius\n""2- Kelvin\n""3- Fahreneit\n""4- Ana menüye dön")
        sıcaklık_seçimi = int(input("Hangi birimden işlem yapmak istersiniz: "))
        if sıcaklık_seçimi == 4:
            ana_menu_don()
        clear()
        menualt_sıcaklık(sıcaklık_seçimi)

    def seçim_yap_sıcaklık(sıcaklık_seçimi):
        if sıcaklık_seçimi == 1:
            secim = "Celcius"
        elif sıcaklık_seçimi == 2:
            secim = "Kelvin"
        elif sıcaklık_seçimi == 3:
            secim = "Fahreneit"
        return secim

    def menualt_sıcaklık(sıcaklık_seçimi):
        ilkbirim_isim = seçim_yap_sıcaklık(sıcaklık_seçimi)
        ilkbirim_miktar = float(input("Hesaplamak istediğiniz "+ilkbirim_isim+" değerini giriniz: "))
        if sıcaklık_seçimi == 1:
            ikincibirim = int(input("\n""2- Kelvin\n""3- Fahreneit\n""4- Ana menüye dön\n""çevirmek istediğiniz birimi seçiniz: "))
            if ikincibirim == 2:
                sonuc = ilkbirim_miktar + 273.15
                print(sonuc,"Kelvin")
            elif ikincibirim == 3:
                sonuc = ilkbirim_miktar * 1.8 + 32
                print(sonuc,"Fahreneit")
        if sıcaklık_seçimi == 2:
            ikincibirim = int(input("1- Celcius\n""\n""3- Fahreneit\n""4- Ana menüye dön\n""çevirmek istediğiniz birimi seçiniz: "))
            if ikincibirim == 1:
                sonuc = ilkbirim_miktar - 273.15
                print(sonuc,"Celcius")
            elif ikincibirim == 3:
                sonuc = ilkbirim_miktar * 1.8 - 459.67
                print(sonuc,"Fahreneit")
        if sıcaklık_seçimi == 3:
            ikincibirim = int(input("1- Celcius\n""2- Kelvin\n""\n""4- Ana menüye dön\n""çevirmek istediğiniz birimi seçiniz: "))
            if ikincibirim == 1:
                sonuc = (ilkbirim_miktar-32) * 5/9
                print(sonuc,"Celcius")
            elif ikincibirim == 2:
                sonuc = (ilkbirim_miktar + 459.67) * 5/9
                print(sonuc,"Kelvin")
        if ikincibirim == 4:
            ana_menu_don()

    ana_menu_don()

    dongu_kapa = str(input("programı sonlandırmak istiyor musunuz (e/h): "))

    if dongu_kapa == "e":
        break
    else:
        continue