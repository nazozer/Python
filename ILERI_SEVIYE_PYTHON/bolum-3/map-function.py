#Bir fonksiyonda listenin tüm elemanlarını map fonksiyonu aracılığıyla sırasıyla gönderilip liste de istenilen yapılandırmalar yapılır.
numbers=[1,2,3,4,5]
# squares=[]
numbers_str=["1","2","3"]
names=["ali","mehmet","ayşe"]
users=[
    {"ad":"barış","soyad":"yılmaz"},

    {"ad":"ahmet","soyad":"demir"}
]

# for number in numbers:
#     squares.append(number**2)
# print(squares)

def kareAl(number):
    return number**2

results=list(map(kareAl, numbers))
print(results)

result= list(map(lambda sayi: sayi**2,numbers))
print(result)

convert= list(map(int,numbers_str))
print(convert)

letter=list(map(str.capitalize,names))
print(letter)

result_user=list(map(lambda user:user["ad"],users))
print(result_user)