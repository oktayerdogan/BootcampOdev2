yorumlar = []

while True:
    yorum = input("Film yorumunuz nedir? (Eğer yorum bittiyse 0'a basın): ")
    if yorum == "0":
        break
    yorumlar.append(yorum)

print("Toplam yorum sayısı:", len(yorumlar))

iyiSayisi = 0

if yorumlar:
    enUzun = yorumlar[0]
    enKısa = yorumlar[0]
else:
    enUzun = ""
    enKısa = ""

toplam_karakter = 0  # ortalama için karakter toplamı

for yorum in yorumlar:
    toplam_karakter += len(yorum)  # karakterleri topla
    if "iyi" in yorum.lower():
        iyiSayisi += 1
    if len(yorum) > len(enUzun):
        enUzun = yorum
    if len(yorum) < len(enKısa):
        enKısa = yorum

# Ortalama karakter sayısı
ortalama_karakter = toplam_karakter / len(yorumlar) if yorumlar else 0

print("İçinde 'iyi' geçen yorum sayısı:", iyiSayisi)
print("En uzun yorum:", enUzun)
print("En kısa yorum:", enKısa)
print("Yorumların ortalama karakter sayısı:", ortalama_karakter)
