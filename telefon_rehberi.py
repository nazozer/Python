tel_rehberi= dict()

def numara_ekle(x):
    print("****NUMARA EKLEME EKRANINA HOŞGELDİNİZ****")
    isim_al= input("Kayıt edilecek kişinin adını yazınız : ")
    tel_no=input("Telefon numarasını girin :")

    x= tel_rehberi.setdefault(isim_al,tel_no)
    print(f"{isim_al} adlı kişi telefon rehberine eklendi..")


def tel_rehberi_göster(x):
    kişi_sayısı=len(x)
    print(f"Rehberinizdeki Kişi sayısı:{kişi_sayısı}")
    print("Rehbere Hoşgeldiniz")

    for i,j in x.items():
        print(i,":",j)
    input("Devam edilsin mi??")

def no_sil(x):
    print("Kişi Silme Ekranına Hoşgeldiniz")
    silinecek_kişi= input("Silinecek kişiyi yazınız : ")
    x=tel_rehberi.pop(silinecek_kişi)
    input("Devam edilsin mi??")


while True:
    print("*****Hoşgeldiniz*****")
    print("**Seçim yapınız**")
    seçim=int(input("1-Ekle\n2-Rehberi Gör\n3-Sil\n"))

    if seçim==1:
        numara_ekle(tel_rehberi)
    elif seçim==2:
        tel_rehberi_göster(tel_rehberi)
    elif seçim==3:
        no_sil(tel_rehberi)
    else:
        print("Lütfen uygun tuşlara basınız")

    
    


