
import random

def tas_kagıt_makas_GIZEM_BOCEK():
    print("Taş, Kağıt, Makas Oyununa Hoş Geldiniz :)")
    print("Kurallar : Taş makası, makas kağıdı, Kağıt taşı yener.")
    print("İlk iki turu kazanan oyunun galibi olur.")
    print("çıkmak için '0' tuşlayınız")
def bsyr_secimi():
    x = random.randint(1,3)
    if x == 1:
        return "Taş"
    elif x == 2:
        return "Kağıt"
    else:
        return "Makas"

skor_kullanici = 0
skor_bilgisayar = 0
tur_sayisi= 0

while skor_kullanici < 2 and skor_bilgisayar <2 :
    kullanici_secimi = input(" Birini Seçiniz: Taş ?, Kağıt ? , Makas ? ").capitalize()
    if kullanici_secimi == "0":
        print("Oyundan çıkılıyor...")
        break
    bilgisayar_secimi = bsyr_secimi()
    tur_sayisi += 1

    print(f"Bilgisayar seçimi : {bilgisayar_secimi}")

    if kullanici_secimi == bilgisayar_secimi:
        print("Berabere")
    elif (kullanici_secimi == "Taş" and bilgisayar_secimi == "Makas") or (kullanici_secimi == "Kağıt" and bilgisayar_secimi == "Taş") or (kullanici_secimi == "Makas" and bilgisayar_secimi == "Kağıt"):

        print("KAZANDINIZ :)")
        skor_kullanici += 1
    else:
        print("KAYBETTİNİZ :(")
        skor_bilgisayar += 1
        print(f"Siz:{skor_kullanici} VS Bilgisayar: {skor_bilgisayar}")

if skor_kullanici == 2:
    print("TEBRİKLER KAZANDINIZ :)")
elif skor_bilgisayar == 2:
    print("MAALESEF KAYBETTİNİZ :(")

print(f"Toplam oynanan tur sayısı: {tur_sayisi}")