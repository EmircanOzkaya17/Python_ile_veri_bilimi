#Soru: Kullanıcıdan 5 adet tam sayı alarak bir listeye ekleyen
# Ve ardından bu sayıların en büyüğünü ve en küçüğünü bulan bir Python programı yazın.
# Bu işlemi gerçekleştiren bir fonksiyon tanımlayın ve çağırarak sonucu ekrana yazdırın.

def enBuyukBulma():
    sayilar=[] # sayıları içine koyacağımız listeyi oluşturudk
    print("Lütfen listeye eklemek istedğiniz 5 sayıyı giriniz")
    for i in range(5): # 5 elemanlı bir liste istediğimiz için indexler [0,4] olmalı o yüzden range 5 yazdık
        sayilar.append(int(input("{}. sayıyı giriniz: ".format(i+1))))

    enbuyuk=sayilar[0] # 0 atasaydım ve listedeki tüm sayılar negatif olsaydı doğru sonucu elde edemezdik
    for x in range(1,len(sayilar)):
        # 1. index'den başlatmamızın sebebi başlarken 0'dakini en büyük kabul etmemiz
        if enbuyuk<sayilar[x]: # anlık olarak en büyük kabul edilen sayı ile sıradaki sayıyı karşılaştırdık
            enbuyuk=sayilar[x]

    return enbuyuk # en büyük sayıyı return ettik


print("Girdiğiniz sayılardan en büyüğü: ",enBuyukBulma())











