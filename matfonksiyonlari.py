import math
#math kütüphanesindeki ifadeleri türkçe de kullanmak için
#sin,tan gibi komutlarda math.radians(x) olarak kullandığımız için radyan değil direkt açı girerek hesaplayacağımız biçimde yazdım
#math.radians(x) dereceyi radyana çevirir

def kareal(x):
    return x ** 2

def kupal(x):
    return x ** 3

def usal(x, us):
    return x ** us

def faktoriyel(x):
    if x < 0:
        return("Faktoriyel bulmak için 0 veya pozitif sayı giriniz")
    faktoriyel = 1
    for i in range(1, x + 1):
        faktoriyel *= i
    return faktoriyel

def mutlakdeger(x):
    return abs(x)

def karekok(x):
    if x < 0:
        return("Pozitif sayı giriniz")
    else:
        return x ** 0.5

def kalan(x, y):
    return x % y

def logaritma(x, altdeger=10):
    return math.log(x, altdeger)

def sinal(x):
    return math.sin(math.radians(x))

def cosal(x):
    return math.cos(math.radians(x))

def tanal(x):
    return math.tan(math.radians(x))

