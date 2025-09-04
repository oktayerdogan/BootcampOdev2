
sayilar = []
toplam=0
while True:
    sayi =int(input("bir sayı giriniz : "))
    if sayi == 0:
        break
    sayilar.append(sayi)
    toplam+=sayi
    
ortalama = toplam/len(sayilar)
    
print("girilen tüm sayıların toplamı : ",toplam)
print("Girilen tüm sayıların ortalaması : ",ortalama)