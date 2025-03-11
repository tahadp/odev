import math
from datetime import date

sesliharfler = 'aeiouAEIOU'


def derecedenradyan(x):
    return math.radians(x)

def metinterscevir(metin):
    return metin[::-1]

def resitlikkontrol(gun, ay, yil):
    bugun = date.today()
    #date içi yıl ay gün olmalıymış hata ondan
    dogumgunu = date(yil, ay, gun)

    # Yaş hesaplama: Yıl farkından ay/gün kontrolü yap
    yas = bugun.year - dogumgunu.year

    return "Reşit" if yas >= 18 else "Reşit değil"

def yashesapla(gun, ay, yil):
    bugun = date.today()
    dogum_tarihi = date(yil, ay, gun)  # Yıl, ay, gün sırasıyla olmalı

    yas = bugun.year - dogum_tarihi.year

    #doğum günü bu yıl henüz gelmediyse yaşı bir azaltıyor (çözemediğim için internetten buldum)
    if (bugun.month, bugun.day) < (dogum_tarihi.month, dogum_tarihi.day):
        yas -= 1

    return yas

def gencyaslihesapla(gun, ay, yil):
#0-18 yaş arası: ergen,18-65 yaş arası: genç,65-74 yaş arası: genç-yaşlı,74-84 yaş arası: yaşlı,85 yaş ve üzeri: çok yaşlı kabul edilmektedir.
#https://www.uplifers.com/dunya-saglik-orgutu-18-65-yas-arasini-genc-kabul-ediyor-o-zaman-omurgamiz-icin-dans/

    bugun = date.today()
    dogum_tarihi = date(yil, ay, gun)  # Yıl, ay, gün sırasıyla olmalı

    yas = bugun.year - dogum_tarihi.year

    #doğum günü bu yıl henüz gelmediyse yaşı bir azaltıyor (çözemediğim için internetten buldum)
    if (bugun.month, bugun.day) < (dogum_tarihi.month, dogum_tarihi.day):
        yas -= 1

    if yas < 0:
        return "0'dan küçük yaş olamaz."
    elif yas <= 18:
        return "Ergen"
    elif yas <= 65:
        return "Genç"
    elif yas <= 74:
        return "Genç-yaşlı"
    elif yas <= 84:
        return "Yaşlı"
    else:
        return "Çok yaşlı"

def listetoplam(liste):
    return sum(liste)

def enbuyuksayi(liste):
    enbuyuk = liste[0]

    for sayi in liste:
        if sayi > enbuyuk:
            enbuyuk = sayi

    return enbuyuk

def listeortalama(liste):
    ortalama = sum(liste) / len(liste)
    return ortalama

def sesliharfleribul(metin):
    sesliler = [harf for harf in metin if harf in sesliharfler]
    return sesliler


def sessizharfleribul(metin):
    sessizharfler = [harf for harf in metin if harf.isalpha() and harf not in sesliharfler]
    return sessizharfler
