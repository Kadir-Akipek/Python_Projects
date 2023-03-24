print("Akrep ile Yelkovan Arasındaki Açıyı Bulan Program")

zaman = input("Lutfen Saati Giriniz: ")
time = zaman.split(":")

a = time[0]
b = time[1]

print("Saat:",a)
print("Dakika:",b)

akrep = int(a)%12
akrep_açı = akrep*30
yelkovan_açı = int(b)*6
ilerleme_payi = int(b)/2
açı = akrep_açı-yelkovan_açı
sonuç = abs(açı)

if akrep_açı > yelkovan_açı:
    sonuç += ilerleme_payi
elif yelkovan_açı > akrep_açı:
    sonuç -= ilerleme_payi
if sonuç > 180:
    yenisonuç = 360 - sonuç
    print("Akrep ve Yelkovan arasındaki açı: ",yenisonuç)
else:
    print("Akrep ve Yelkovan arasındaki açı: ", sonuç)
