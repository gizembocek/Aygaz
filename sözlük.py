"""
from sys import argv

sözlük = {"kitap"      : "book",
          "bilgisayar" : "computer",
          "programlama": "programming"}

def ara(sözcük):
    hata = "{} kelimesi sözlükte yok!"
    return sözlük.get(sözcük, hata.format(sözcük))

if __name__ == "__main__":
	print(ara(argv[1]))
	print(ara(argv[2]))


def ekle(sözcük, anlam):
    mesaj = "{} kelimesi sözlüğe eklendi!"
    sözlük[sözcük] = anlam
    print(mesaj.format(sözcük))
"""
