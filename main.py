import matfonksiyonlari as mf
import fonks as f

sayilar = [1, 2, 3, 4, 5]

print("Liste Toplam:", f.listetoplam(sayilar))
print("Liste en büyük sayı:", f.enbuyuksayi(sayilar))
print("Liste Ortalama:", f.listeortalama(sayilar))
print("Sesli Harfler:", f.sesliharfleribul("Taha Toprak Yurttutan"))
print("Sessiz Harfler:", f.sessizharfleribul("Taha Toprak Yurttutan"))
print("10 derecenin radyanı:", f.derecedenradyan(10))
print("Metnin Ters Hali:", f.metinterscevir("Taha"))


print(f.resitlikkontrol(30,10,2004))
print(f.resitlikkontrol(30,10,2011))
print("Yaşınız:",f.yashesapla(30,10,2004))
print(f.gencyaslihesapla(30,10,2004))
print(f.gencyaslihesapla(30,10,2011))
print(f.gencyaslihesapla(30,10,1950))
print(f.gencyaslihesapla(30,10,1920))


print("5'in karesi:",mf.kareal(5))
print("5'in küpü:",mf.kupal(5))
print("5'in 7 üssü:",mf.usal(5,7))

print("-1'in faktöriyeli:", mf.faktoriyel(-1))
print("5'in faktöriyeli:", mf.faktoriyel(5))
print("-1'in mutlakdegeri:", mf.mutlakdeger(-1))
print("-1'in karekökü:", mf.karekok(-1))
print("100'ün karekökü:", mf.karekok(100))
print("100ün 3e bölümünden kalan:", mf.kalan(100,3))
print("100ün logoritması",mf.logaritma(100))

print("5 derecenin cos değeri:", mf.cosal(5))
print("5 derecenin sin değeri:", mf.sinal(5))
print("5 derecenin tan değeri:", mf.tanal(5))


