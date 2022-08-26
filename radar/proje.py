import numpy as np
import fuzzPy as fuzz
import matplotlib.pyplot as plt

#input değerleri tanımlı olduğu aralıkalr
xR=np.arange(0,91,1)#0-90 hız tanım aralığı 
xW=np.arange(0,11,1)#0-10 hava tanım aralığı
xS=np.arange(0,151,1)#0-150 ortalma hız tanım aralığı 
xE=np.arange(0,21,1)#0-20 kullanıcı deneyimi tanım aralığı

#output değerleri tanımlı olduğu aralık
xO=np.arange(0,101,1)#0-100 çıkış değerleri tanım aralığı

#yolun yapısı üyelik fonksiyonları
Rkotu=fuzz.trapez(xR,"sol",[30,45])
Rnormal=fuzz.ucgen(xR,[30,45,60])
Riyi=fuzz.trapez(xR,"sag",[45,60])

#hava durumu üyelik fonksiyonları
Wkotu=fuzz.ucgen(xW,[0,0,5])
Wnormal=fuzz.ucgen(xW,[0,5,10])
Wiyi=fuzz.ucgen(xW,[5,10,10])

#ortalama hız üyelik fonksiyonları
Saz=fuzz.ucgen(xS,[0,0,70])
Sort=fuzz.ucgen(xS,[0,70,130])
Scok=fuzz.trapez(xS,"sag",[70,130])

#kullanıcı tecrübesi üyelik fonksiyonları
Eaz=fuzz.ucgen(xE,[0,0,10])
Eort=fuzz.ucgen(xE,[0,10,20])
Ecok=fuzz.ucgen(xE,[10,20,20])

#çıkış hız sınırı için üyelik fonksiyonları
Oaz=fuzz.trapez(xO,"sol",[25,50])
Oort=fuzz.ucgen(xO,[25,50,85])
Ocok=fuzz.trapez(xO,"sag",[50,85])

# <--buradan hata ayıklama modunda çalıştırmaya başlarsanız
#grafik cizimini satır satır işleyişini görebilirsiniz 

#ınput grafiklerini pylotlib ile render et
# 5 adet alt alta grafik oluşturmak için
fig,(ax0,ax1,ax2,ax3,ax4)=plt.subplots(nrows=5,figsize=(6,10))

#yol viraj ve eğim için grafik (r:kırmzı- g:yeşil- b:mavi)
ax0.plot(xR,Rkotu,'r',linewidth=2,label="kötü")
#Rkotu dizisinin
#0-30 arası 1 
# 30-44 arası sıfır ile bir arası
# 44-90 arası 0
ax0.plot(xR,Rnormal,"g",linewidth=2,label="normal")
#Rnormal dizisinin
#0-31 arası 0 
# 31-59 arası sıfır ile bir arası
# 59-90 arası 0
ax0.plot(xR,Riyi,"b",linewidth=2,label="iyi")
#Riyi dizisinin
#0-90 arası 0
ax0.set_title("Yol Viraj ve Eğimi")#grafiğe başlık ekler
ax0.legend()#çıktıya işlenir

#hava şartları için grafik
ax1.plot(xW,Wkotu,"r",linewidth=2,label="kötü")
#Wkotu dizisinin
#0-4 arası sıfır ile bir arası 
# 4-10 0
ax1.plot(xW,Wnormal,"g",linewidth=2,label="normal")
#Wnormal dizisinin
#0-5 arası ve 5-10 sıfır ile bir arası 
#5 de 1 değerini alır
ax1.plot(xW,Wiyi,"b",linewidth=2,label="iyi")
#Wiyi dizisinin
#0-6 arası 0 
#6-9 arasında sıfır ile bir arsı değer alır
ax1.set_title("Hava Şartları")#grafiğe başlık ekler
ax1.legend()#çıktıya işlenir

#sürücü ortalama hızı için grafik
ax2.plot(xS,Saz,"r",linewidth=2,label="az")
#Saz dizisinin
#0-70 arası sıfır ile bir arası 
#70-150 arasında 0
ax2.plot(xS,Sort,"g",linewidth=2,label="orta")
#Sort dizisinin
#0-70 arası sıfır ile bir arası 
#70 de 1 değerini alıe
#70-130 arası sıfır ile bir değerlerini alır
# 130-150 arası 0 
ax2.plot(xS,Scok,"b",linewidth=2,label="cok")
#Scok dizisinin
10 #0-150 arası 0 
ax2.set_title("Sürürcü ortalama hızı")#grafiğe başlık ekler
ax2.legend()#çıktıya işlenir

#kullanıcı tecrübesi için grafik
ax3.plot(xE,Eaz,"r",linewidth=2,label="kötü")
#Eaz dizisinin
#0-10 arası sıfır ile bir arası
#10-20 arası 0
ax3.plot(xE,Eort,"g",linewidth=2,label="normal")
#Eort dizisinin
#0-10 arası sıfır ile bir 
#10 da 1 değerini alır
#10-20 arası sıfır ile bir arası
ax3.plot(xE,Ecok,"b",linewidth=2,label="iyi")
#Ecok dizisinin
#0-11 arası 0 
#11-20 arasında sıfır ile bir arasında 
ax3.set_title("Kullanıcı Tecrübesi")#grafiğe başlık ekler
ax3.legend()#çıktıya işlenir

#çıkış hız için grafik
ax4.plot(xO,Oaz,"r",linewidth=2,label="kötü")
#0-26 arası 1 
#26-50 arası sıfır ile bir arası 
#50-100 arası 0
ax4.plot(xO,Oort,"g",linewidth=2,label="normal")
#Oort dizisinin
#0-25 arası sıfır
#25-50 arası sıfır ile bir arası 
#50 de 1 değerini alır 
#50-85 arasında sıfır ile bir 
# 85-100 arası sıfır 
ax4.plot(xO,Ocok,"b",linewidth=2,label="iyi")
#0-100 arası sıfır değerirni alır
ax4.set_title("Çıkış Hız Sınırı")#grafiğe başlık ekler
ax4.legend()#çıktıya işlenir
plt.tight_layout()
plt.savefig('uyelik fonksiyonları.png')#grafiği png dosyası olarak kaydeder



#Inputları al
print("yol viraj düzeyini girin (0-90)")
input_R=input()

print("hava durumu girin(0-10)")
input_W=input()

print("sürücü ortalma hızını girin(30-150)")
input_S=input()

print("Sürücü deneyim yılını girin(0-20)")
input_E=input()

# Input değerlerinin uyelik degerlerini hesaplama

#yolun bulanık değeri hesaplanır
R_fit_kotu=fuzz.Uyelik(xR,Rkotu,input_R)
R_fit_normal=fuzz.Uyelik(xR,Rnormal,input_R)
R_fit_iyi=fuzz.Uyelik(xR,Riyi,input_R)
#hava durumunun bulanık değeri hesaplanır
W_fit_kotu=fuzz.Uyelik(xW,Wkotu,input_W)
W_fit_normal=fuzz.Uyelik(xW,Wnormal,input_W)
W_fit_iyi=fuzz.Uyelik(xW,Wiyi,input_W)
#ortalama hız bulanık değeri hesaplanır
S_fit_az=fuzz.Uyelik(xS,Saz,input_S)
S_fit_ortalama=fuzz.Uyelik(xS,Sort,input_S)
S_fit_cok=fuzz.Uyelik(xS,Scok,input_S)
#sürücü deneyimi bulanık değeri hesaplanır
E_fit_az=fuzz.Uyelik(xE,Eaz,input_E)
E_fit_ortalama=fuzz.Uyelik(xE,Eort,input_E)
E_fit_cok=fuzz.Uyelik(xE,Ecok,input_E)

#kural tanimları
#fit olarak bulduğumuz değerlere 
# eğer yol cok virajlı ise ve hava kötü ise hız sınırı düşmeli
# eğer yol orta virajlı ve hava orta ise hız sınırı ortalama olmalıdır
# eğer yol az virajlı ve hava iyi ise hız sınırı yüksek olmalı
# eğer ortalama hız yüksek veya sürücü deneyimi düşük ise hız sınırı düşmeli
# eğer ortalama gız orta veya sürücü deneyimi orta ise hız sınırı orta olmalı
# eğer ortalam hız düşük veya sürücü deneyimi yüksek ise hız sınırı yüksel olmalı 

rule1=np.fmin(np.fmin(R_fit_kotu,W_fit_kotu),Oaz)
rule2=np.fmin(np.fmin(R_fit_normal,W_fit_normal),Oort)
rule3=np.fmin(np.fmin(R_fit_iyi,W_fit_iyi),Ocok)

rule4=np.fmin(np.fmin(S_fit_az,E_fit_az),Oaz)
rule5=np.fmin(np.fmin(S_fit_ortalama,E_fit_ortalama),Oort)
rule6=np.fmin(np.fmin(S_fit_cok,E_fit_cok),Ocok)

out_az=np.fmax(rule1,rule4)
out_ortalama=np.fmax(rule2,rule5)
out_cok=np.fmax(rule3,rule6)

#output grafikleini Pylotlib ile render etme
o_zeros=np.zeros_like(xO)
fig,grafik_output=plt.subplots(figsize=(7,4))
grafik_output.fill_between(xO,o_zeros,out_az,facecolor='r',alpha=0.7)
grafik_output.plot(xO,Oaz,'r',linestyle='--')
grafik_output.fill_between(xO,o_zeros,out_ortalama,facecolor='g',alpha=0.7)
grafik_output.plot(xO,Oaz,'g',linestyle='--')
grafik_output.fill_between(xO,o_zeros,out_cok,facecolor='b',alpha=0.7)
grafik_output.plot(xO,Ocok,'b',linestyle='--')
grafik_output.set_title("periyot cıktı:")
plt.tight_layout()
plt.savefig('cıkıs.png')

#output
print("-"*20)
#üç farklı bulanık çıkış var(out_az,out_ortalama,out_cok) durulama işleminden önce
#en çok etki eden np.fmax ile seçilir
mutlak_bulanık_sonuc=np.fmax(out_az,out_ortalama,out_cok)
#0-50 tanım aralığında sonuc üretir o yüzden sonucu 3/2 ile çarparız
#böylece 0-1 arası bir değer elde ederiz
durulastirilmis_sonuc=fuzz.durulastir(xO,mutlak_bulanık_sonuc,'agirlik_merkezi')
durulastirilmis_sonuc=durulastirilmis_sonuc*3/2
print("duru sonuc -->",durulastirilmis_sonuc)

#çıkış değerlerinin bulanık cıkış üyelik değerlerini buluruz
sonuc_az=fuzz.Uyelik(xO,Oaz,durulastirilmis_sonuc)
sonuc_ort=fuzz.Uyelik(xO,Oort,durulastirilmis_sonuc)
sonuc_cok=fuzz.Uyelik(xO,Ocok,durulastirilmis_sonuc)
print("Duru sonuc üyelik fonksiyonları ---->Az:",sonuc_az,"| orta:",sonuc_ort,"| çok:",sonuc_cok)

hizSiniri=100
hizSiniri_dusuk=hizSiniri-(sonuc_az*durulastirilmis_sonuc)
hizSiniri_yuksek=hizSiniri-(sonuc_cok*durulastirilmis_sonuc)
hizSiniri=(hizSiniri_dusuk+hizSiniri_yuksek)/2

if(sonuc_az>sonuc_cok):
    hizSiniri=hizSiniri+(sonuc_ort * durulastirilmis_sonuc)/3
else:
    hizSiniri=hizSiniri-(sonuc_ort * durulastirilmis_sonuc)/3
degisim=hizSiniri-100
print("Mevcut şartlar altında hız sınırı,",degisim," degiserek",hizSiniri," olamlıdır")
print("Değişim oranı: %",float(degisim/100))