import random
import time

user_skor,com_skor = 0,0

print("Zar atma oyununa Hoş Geldiniz\nKurallar:Her 2 tarafta 2 tane zar atar yüksek sayıyı atan tarafa 2 puan eklenir kaybeden tarafa puan eklenmez eğer sayılar eşit gelirse her 2 tarafa da 1 puan eklenir")
bitis = int(input("Oyunun kaç puanda sonlanacağını seçiniz: ")) #4
print("Oyun başlasın...")
print("Bilgisayar: Size karşı centilmen olacağım izniniz olursa zarı atma önceliğini size vermek istiyorum...")
time.sleep(3)
oncelik = str(input("Teklifi kabul etmek için (e) yi reddetmek için (h) yi seçin: "))
i = 0
while i < bitis: #4
    if oncelik == "e":
        zar1 = random.randint(1,6)
        zar2 = random.randint(1,6)
        user_puan = zar1 + zar2
        print(user_puan,"attınız")
        print("Bilgisayar: Sıra bende")
        zar1 = random.randint(1,6)
        zar2 = random.randint(1,6)
        com_puan = zar1 + zar2
        time.sleep(3)
        print(com_puan,"geldi")
    elif oncelik == "h":
        print("Bilgisayar: Ben başlıyorum")
        zar1 = random.randint(1,6)
        zar2 = random.randint(1,6)
        com_puan = zar1 + zar2
        time.sleep(3)
        print(com_puan,"geldi")
        print("Sıra sizde zarlarınız atılıyor...")
        zar1 = random.randint(1,6)
        zar2 = random.randint(1,6)
        user_puan = zar1 + zar2
        time.sleep(3)
        print(user_puan,"geldi")
    time.sleep(3)
    if user_puan > com_puan:
        user_skor = user_skor + 2
        print("İki puan kazandınız")
    elif com_puan > user_puan:
        com_skor = com_skor + 2
        print("Bilgisayar iki puan kazandı")
    else:
        print("Berabere...")
        user_skor = user_skor + 1
        com_skor = com_skor + 1
        print("Her iki tarafta bir puan kazandı")
    if user_skor < com_skor:
        i = com_skor
    else:
        i = user_skor
    time.sleep(3)
    print("\nSet puan durumları:\nSiz: "+str(user_skor)+"\nBilgisayar: "+str(com_skor)+"\n")
print ("Oyun sona erdi")
print("Puanlar şunlar...")
print("Siz: "+str(user_skor)+"\nBilgisayar: "+str(com_skor))
if user_skor > com_skor:
    print("Tebrikler siz kazandınız!!!")
elif com_skor > user_skor:
    print("Kaybettiniz bir dahaki sefere")