sifre = input("Lütfen şifrenizi giriniz : ")

if len(sifre)<8:
    print("şifreniz 8 karakterden küçük olamaz!")
elif not sifre[0].isupper():
    print("Şifreniz büyük harfle başlamalı!")
elif not any(ch.isdigit() for ch in sifre):
    print("şifre en az bir rakam içermeli")
else:
    print("şifreniz geçerli.")