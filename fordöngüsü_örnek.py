for i in range(3):
    sifre = input ("Lütfen şifre belirleyin:" )
    if not sifre:
        print("Bu alan boş bırakılamaz...!")
    elif len(sifre) in range(3,8):
        print("Yeni şifreniz :",sifre)
        break

    elif i==2:
        print("Şifreyi 3 kere yanlış girdiniz, lütfen 10 dakika bekleyiniz.")

    else:
        print("Şifreniz 8 karakterden uzun ya da 3 karakterden kısa.")
        


