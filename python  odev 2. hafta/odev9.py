cumle = input("Bir cümle giriniz: ")

kelimeler = cumle.split()            # boşluklara göre ayır
kelimeler_buyuk = [kelime.capitalize() for kelime in kelimeler]  # baş harfleri büyük yap
yeni_cumle = " ".join(kelimeler_buyuk)  # kelimeleri tekrar birleştir

print("Düzeltilmiş cümle: ", yeni_cumle)
