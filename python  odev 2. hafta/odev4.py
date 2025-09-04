sayilar=[12,4,9,25,30,7,18]
sayilar2=[]
toplam = sum(sayilar)
ortalama = toplam/len(sayilar)
print("ortalama : ",ortalama)

for sayi in sayilar[:]:
    if sayi>ortalama:
        sayilar.remove(sayi)
        sayilar2.append(sayi)
        
print(sayilar)
print(sayilar2)