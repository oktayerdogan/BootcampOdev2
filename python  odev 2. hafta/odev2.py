kelime = input("bir kelime girin : ")

harf_sayilari={}

for harf in kelime:
    if harf in harf_sayilari:
        harf_sayilari[harf] +=1
    else :
        harf_sayilari[harf] = 1
        
print(harf_sayilari)
