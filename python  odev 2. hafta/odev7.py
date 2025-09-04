kelime = input("Bir kelime giriniz: ").lower()  # küçük harfe çevir

if kelime == kelime[::-1]:  # stringi ters çevir ve karşılaştır
    print("Palindrom")
else:
    print("Palindrom değil")
