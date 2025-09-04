sayi =int(input("Lütfen bir sayı giriniz :"))
print("girdiğiniz sayı : ",sayi)

if sayi==0:
    print("girdiğiniz sayı sıfıra eşit")

elif sayi<0 :
    if sayi % 2 == 1:
        print("negatif tek")
    elif sayi % 2 == 0:
        print("negatif çift")
        
elif sayi>0:
    if sayi % 2 == 1:
        print("pozitif tek")
    elif sayi % 2 == 0:
        print("pozitif çift")
else:
    print("yanlış bir değer girdiniz.")
