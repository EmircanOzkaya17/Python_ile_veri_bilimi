#Soru: Kullanıcıdan bir sayı alarak 1’den bu sayıya kadar olan tüm sayıların toplamını hesaplayan
# bir Python programı yazın.
# Programda hem for hem de while döngüsü kullanarak iki farklı yöntemle sonucu ekrana yazdırın.

num=int(input("Lütfen bir sayı giriniiz: "))
sum_for=0

for i in range(1,num+1):
    sum_for+=i

sum_while=0
i=0
while i<=num:
    sum_while+=i
    i+=1

print("For döngüsü ile yapılan toplamanın sonuncu :",sum_for)

print("While döngüsü ile yapılan toplamanın sonuncu :",sum_while)








