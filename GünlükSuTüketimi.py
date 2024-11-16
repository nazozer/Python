def su_tüketimihesapla(kilo):
    e_hesapla = kilo*0.04
    k_hesapla = kilo*0.03

    cinsiyet = input("Lütfen cinsiyetinizi giriniz(Kadın/Erkek:)").lower()

    if cinsiyet == "erkek":
        print("-"*30)
        print("Cinsiyetiniz:",cinsiyet)
        print(e_hesapla , "Litre su tüketmelisiniz..")
        print("-"*30)

    elif not cinsiyet:
        print("Lütfen cinsiyetinizi belirtin..")

    elif cinsiyet == "kadın":
        print("-"*30)
        print("Cinsiyetiniz", cinsiyet)
        print(k_hesapla, "Litre su içmelisiniz..")

kilo_al= int(input("Kilonuzu Giriniz: "))

su_tüketimihesapla(kilo_al)

