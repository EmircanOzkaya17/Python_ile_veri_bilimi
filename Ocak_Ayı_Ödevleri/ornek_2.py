#Soru: Kullanıcıdan bir sayı alarak, bu sayının çift mi tek mi olduğunu ekrana yazdıran
# bir Python programı yazın. Eğer sayı negatifse, ekrana "Negatif sayı girdiniz!" mesajı versin.

num = int(input("Sayı giriniz: "))
if num<0:
    print("Negatif sayı girdiniz")
elif num%2==0:
    print("Girdiğiniz sayı çift.")
else:
    print("Girdiğiniz sayı tek.")




