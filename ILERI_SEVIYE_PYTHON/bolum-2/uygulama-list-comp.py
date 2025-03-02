# (1-100) arasındaki sayılardan 12'e tam bölünebilen sayı listesini oluştur.
result=[i for i in range(1,101) if i % 3==0 if i % 4 ==0]


# Verilen text içerisindeki rakamları içeren bir liste oluşturunuz.
#text="Hello 123456 World"----->[1,2,3,4,5,6]

text="Hello 123456 World"
result= [i for i in text if i.isdigit()]

# Sıcaklıklar listesinde bulunan her hava sıcaklık bilgisine göre 4 derecenin altında buzlanma tehlikesi yazınız.
# sicakliklar=[20,15,0,-5,-2]------>[20,15,"Buzlanma Tehlikesi","Buzlanma Tehlikesi","Buzlanma Tehlikesi"]

sicakliklar=[20,15,0,-5,-2]
result=[i if i>= 4 else "Buzlanma Tehlihesi" for i in sicakliklar]

#oğrenciler ve notlar listelerinedeki notu 50 den fazla olan kişileri ekrana dict verisinde yazdırınız.
# "{'Nazlı':70, 'Canan':80}"

students=["Nazli","Ali","Canan"]
grades=[ 70,50,80]

#[("Nazli":70),("Ali":50),("Canan":80)]
liste=[(students[i],grades[i]) for i in range(0,len(students))]
liste_dic={ key:value for (key,value) in liste if value > 50}
print(liste_dic)

# For döngüsüyle yazılan uygulamıyı list comprehension ile yazınız.
for x in range(3):
    for y in range(3):
        result.append((x,y))

result=[(x,y) for x in range(3) for y in range(3)]
print(result)