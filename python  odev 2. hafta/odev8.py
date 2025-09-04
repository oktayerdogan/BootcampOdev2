sayilar=[]

for sayi in range(1, 101): 
    if(sayi%3==0 and sayi%5==0 ):
        sayi=sayi*sayi
        sayilar.append(sayi)
        
print(sayilar)