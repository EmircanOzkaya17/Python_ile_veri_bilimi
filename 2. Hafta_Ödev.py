ogrenciler =dict()

def ogrenci_Ekle():
    #öğrencinin  bilgilerini alıyoruz, bunları bir sözlüğe atıyoruz
    numara = int(input("öğrencinin numarasını giriniz: "))
    if numara not in ogrenciler:
        # girilen nuamranın bir başka bir öğrenciye ait olup olmadağını kontrol ediyoruz
        # girilen numaraya sahip başka bir öğrenci yoksa diğer bilgileri istiyoruz
        ad = input("Öğrencinin adını giriniz: ")
        soyad = input("öğrencinin soyadını giriniz: ")
        ortalama = float(input("öğrencinin ortalamasını giriniz: "))
        bolum = input("Öğrencinin bölümünü giriniz: ")
        ogrenciler[numara] ={"Adı: ":ad ,
                      "Soyadı: ":soyad ,
                      "Numarası: ":numara,
                      "Bölümü: ":bolum,
                      "Ortalaması: ":ortalama}


    else:
        print("Aynı numaraya sahip başka bir öğrenci var !!")

    # silme değiştirme güncelleme için öğrenci sorgusu yaparken öğrenci numarası kullanacağımızdan
    # key olarak öğrenci nuamrsı kullanıyoruz.

def ogrenciyi_gosterme():
    # bu fonksiyon sayesinde numarsı mevcut olan bir öğrencinin bilgileri görülebilir
    no=int(input("Bulmak istediğinz öğrencinin numarasını giriniz: "))

    if no in ogrenciler: # bu numaraya sahip bir öğrenci var mı
        print(ogrenciler)
    else:
        print("Böyle bir öğrenci yok")


def ogrencinin_bilgilerini_guncelleme():
    # öğrencinin biliglerinin güncellemek için kullanacağımız fonksiyon
    no=int(input("Öğrencinin numarsını giriniz"))
    if no in ogrenciler:
        print("Seçtiğiniz öğrencinin bilgileri şu şekilde:")
        print(ogrenciler[no])
        while True:
            print("1 - Öğrencinin numarsını güncellemek istiyorsanız \n"
                  "2 -  Öğrencinin adını güncellemek istiyorsanız \n"
                  "3 -  Öğrencinin soyadını güncellemek istiyorsanız \n"
                  "4 -  Öğrencinin bölümünü güncellemek istiyorsanız \n"
                  "5 -  Öğrencinin ortalamasını güncellemek istiyorsanız \n"
                  "6 -  Güncelleme işlemlerinizi bittiyse ")
            sec = int(input("Yapmak istediğinz işlemin numarasını girin"))
            if sec == 1:
                yeni_numara = int(input("Yeni nuamrayı giriniz"))
                # öğrenciinn yeni numarasını aldık
                ogrenciler[no]["Numarası: "] = yeni_numara
                # eski numarası ile erişerek önce içerikdeki   numarayı güncelledik
                ogrenciler[yeni_numara] = ogrenciler[no]
                # burada ise yeni nuamrayı key yaparak eski bilgileri
                # yeni nuamranını key olduğu birime atadık
                del ogrenciler[no]
                # burada ise sözlükten eski key'i sildik
                no = yeni_numara
                # başka bir işlem yapmak istedeğimzde no değişkeni üzerindeki nuamradan
                # öğrenciye erişeceğimiz için burada no değişkeninin içeriğini güncelliyoruz
            elif sec == 2:
                ad = input("Öğrencinin adını giriniziz: ")  # Ad güncelleniyor
                ogrenciler[no]["Adı: "] = ad
            elif sec == 3:
                soyad = input("Öğrencinin soyadını giriniziz: ")  # Soyad güncelleniyor
                ogrenciler[no]["Soyadı: "] = soyad
            elif sec == 4:
                bolum = input("Öğrencinin yeni bölümünü giriniz: ")  # Bölüm güncelleniyor
                ogrenciler[no]["Bölümü: "] = bolum
            elif sec == 5:
                ortalama = float(input("Öğrencinin ortalamasını giriniziz: "))  # Ortalama güncelleniyor
                ogrenciler[no]["Ortalaması: "] = ortalama
            else:
                break  # Güncelleme işlemi tamamlandığı için döngüden çıkılıyor


def ogrencil_silme():
    no=int(input("Silmek istedğiniz öğrencinin numarasını giriniz: "))
    print("Sildiğniiz öğrencinin bilgileri: \n",
          ogrenciler[no]) # Silinmesi istenilen  öğrencinin biligleri ekrana yazırılıyor
    del ogrenciler[no]  #



def tum_ogrenciler():
    print(ogrenciler.values()) # tüm öğrencilerin bilgileri gözükür


while True:
    print("1 - Öğrenci Ekleme \n"
          "2 - Öğrencilerin Hepsini Bilgilerini Listeleme \n"
          "3 - Seçilen Öğrencinin Bilgilerini Listeleme \n"
          "4 - Seçilen Öğrencinin Bilgilerini Güncelleme \n"
          "5 - Seçilen Öğrenciyi Silme \n"
          "6 - Çıkış ")
    sec= int (input("Yapmak istediğiniz işlemi giriniz: "))
    if sec==1:
        ogrenci_Ekle()
    elif sec==2:
        tum_ogrenciler()
    elif sec==3:
        ogrenciyi_gosterme()
    elif sec==4:
        ogrencinin_bilgilerini_guncelleme()
    elif sec==5:
        ogrencil_silme()
    elif sec==6:
        break












