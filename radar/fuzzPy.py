#bulanık mantığı oluşturmak için kullandığımız 
# Uyelik, durulastir adlı fonksiyonlar bu dosya içinde bulunur


import numpy as np
import fuzzPy as fuzz
import matplotlib.pyplot as plt

#grafikte ucgensellesen 
def ucgen(x,abc):#x --> değişken tanım aralığı
    #a<=b<=c     #abc --> tanım aralığı içindeki 1. min ve 2.min
    assert len(abc)==3,"başlangıc,tepe ve bits değerleri verilmeli"#hata ayıklama için
    a,b,c=np.r_[abc]#a b ve c içine abc dizisinin değerlerini sırayla verir [0]=a gibi..
    assert a <= b and b<=c,"uye fonksiyonları değerleri basşangoc <=tepe<=bitis"#hata ayıklama için
    y=np.zeros(len(x))# x in eleman sayısı kadar(3) 0 dan oluşan yeni bir dizi oluşturu ve bunu y değişkenine atar

    #sol

    if a !=b:#eğer a b ye eşit değilse 
        idx =np.nonzero(np.logical_and(a <x ,x<b))[0]#dizide a<x ve x<b aralığında olan bölümü alır 
        y[idx]=(x[idx]-a)/float(b-a)#y nin içeriğini bu doğrultuda değiştirir

    #sağ (sol ile aynı mantık )
    if b !=c:
        idx=np.nonzero(np.logical_and(b<x ,x<c))[0]
        y[idx]=(c-x[idx])/float(c-b)
    
    
    idx=np.nonzero(x==b)#tek elamanlı x=b olan değeri döndürür
    y[idx]=1
    return y
#Grafikte azalış ya da artış 
def trapez(x,rota,abc):
    y= np.zeros(len(x))# x in eleman sayısı uzunluğunda 0 lardan oluşan yeni bir dizi oluşturuluyor
    if (rota=="orta"):
        assert len(abc)==3,"başlangıc,tepe ve bits değerleri verilmeli"
        a,b,c=np.r_[abc]
        assert a <= b and b<=c,"uye fonksiyonları değerleri basşangoc <=tepe<=bitis"
        idx=np.nonzero(np.logical_and(x>=0 , x<a))[0]
        y[idx]=(x[idx])/float(a)
        idx=np.nonzero(np.logical_and(x>=a,x<b))[0]
        y[idx]=1
        idx=np.nonzero(np.logical_and(x>=b,x<c))[0]
        y[idx]=(c-x[idx])/float(c-b)
        return y
    else:
        assert len(abc)==2,"başlangıc,tepe ve bits değerleri verilmeli"#hata ayıklamam
        a,b=np.r_[abc]#abc sayısı basamaklarına ayrılır ve atananır
        if(rota=="sol"):
            assert a <= b ,"uye fonksiyonları değerleri basşangoc <=tepe<=bitis"
            idx=np.nonzero(x<a)[0]#a değerinin x dizisinden büyük olan elamalarından oluşan yeni bir diziz oluşturur
            y[idx]=1#y nin idx elamanlarını 1 yapar
            idx=np.nonzero(np.logical_and(x>=a,x<b))[0]#verilen tanım aralığına uygun olan elemanlardan oluşan bir dizi
            y[idx]=(x[idx]-b)/float(a-b)
        return y
        if(rot=="sag"):
            assert a <= b and b<=c,"uye fonksiyonları değerleri basşangoc <=tepe<=bitis"
            idx=np.nonzero(x>a)[0]
            y[idx]=1
            idx=np.nonzero(np.logical_and(x>a,x<=b))[0]
            y[idx]=(x[idx]-a)/float(b-a)
        return y         



#gercek bir değerin üyelik fonksiyonuna olan üyelik değerini hesaplayan fonksiyon
#x:tanım aralığı 
#xmf:üyelik fonksiyonu(bulanık değeri)
#xx:sayısal giriş verisi 
def Uyelik(x,xmf,xx,zero_outside_x=True):
    if not zero_outside_x: #değilse
        kwargs=(None,None) #anahtarları 
    else:
        kwargs=(0.0,0.0)
        #numpyinin interpolasyon fonksiyonu
    return np.interp(xx,x,xmf,left=kwargs[0],right=kwargs[1])


def durulastir(x,LFX,model):
    model=model.lower()#model dizisini küçük harflerle dönüştürüyor
    x=x.ravel()#diziyi düzleştirmek için 
    LFX=LFX.ravel()
    n=len(x)
    if n!=len(LFX):
        print("Bulanık küme üyeliği ve değer sayısı eşit olmalıdır")
        return
    if 'agirlik_merkezi' in model:
        if 'agirlik_merkezi' in model:
            return agirlik_merkezi(x,LFX)

def agirlik_merkezi(x,LFX):
    sum_moment_area=0.0
    sum_area=0.0
    if len(x)==1:
        return x[0]*LFX[0]/np.fmax(LFX[0],np.finfo(float).eps).astype(float)
    for i in range(1,len(x)):
        x1=x[i-1]
        x2=x[i]
        y1=LFX[i-1]
        y2=LFX[i]
        if not (y1==y2==0.0 or x1==x2):
            if y1==y2:
                moment=0.5*(x1+x2)
                area=(x2-x1)*y1
            elif y1==0.0 and y2 != 0.0:
                moment=2.0/3.0*(x2-x1)+x1
                area=0.5*(x2-x1)*y2
            elif y2==0.0 and y1 !=0.0:
                moment=1.0/3.0*(x2-x1)+x1
                area=0.5*(x2-x1)*y1
            else:
                 moment=(2.0/3.0*(x2-x1)*(y2+0.5*y1))/(y1+y2)+x1
                 area=0.5*(x2-x1)*(y1+y2)
            sum_moment_area+=moment*area
            sum_area+=area
    return sum_moment_area/ np.fmax(sum_area,np.finfo(float).eps).astype(float)

