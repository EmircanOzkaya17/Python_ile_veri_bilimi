"""
print("İki sayı giriniz")
num1=int(input("birinci sayı  : "))
num2=int(input("İkinci sayı:"))

# print içerisnde '+' kullanmak yerine ',' kullanmamızın sebebi programlama dilleri arasında bulunan bazı
# ufak farklılıklardan kaynaklanıyor, Python da int bir değer ile string (str) değer arasında '+'
# koyduğumuzda  hata alıyoruz.
print("Sayıların toplamı =", num2+num1)
print("Sayıların çarpımı =", num2*num1)
if num1>num2:
    print("Sayıların farkı =", num1-num2)
else:
    print("Sayıların farkı=",num2-num1)
print("İlk sayının ikinici sayıya olası küsüratlı bölümü =", num1/num2)
print("İlk sayının ikinici sayıya tam bölümü =", num1//num2)

print("İlk sayını ikinci sayıyya bölümden kalan =", num1%num2)
print("İlk sayını taban ikinci sayını üs olması =", num1**num2)
"""
"""
#Kullanıcıdan bir sayı alarak 1’den o sayıya kadar olan sayıların toplamını hesaplayan
# bir Python programı yazın.

last_Number=int(input("Toplanacak son sayıyı giriniz : "))

# while döngüsü ile yapımı
sum=0
k=1
while k<=last_Number:
    sum=sum+k
    k+=1
print("Toplam =", sum)

# for döngüsü ile çözüm
sum1=0
# Alt satırda +1 yapmamızın sebebi range  fonksiyonu [1,x) aralığında çalışmasından ötürü
for i in range(1,last_Number+1):
    sum1+=i
print("Toplam =", sum1)


#1 ile 100 arasındaki çift sayıları ekrana yazdıran bir Python programı yazın.
for i in range(1,101):
    print(i)
"""
# Kullanıcıdan alınan bir metni ters çeviren ve ekrana yazdıran bir Python
# programı yazın. (Döngü kullanarak yapın.)
metin =input("Metin giriniz: ")
metin_lenght=len(metin)
index=metin_lenght-1
ters_metin=""
while index>=0:
    ters_metin=ters_metin+metin[index]
    index=index-1
print(ters_metin)


print("      ")

