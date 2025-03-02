numbers=[]

for i in range(5):
    numbers.append(i)
print(numbers)

numbers2=[i*2 for i in range(5)]
print(numbers2)

kurum="BTK Akademi"
sonuc=[x.upper() for x in kurum]
print(sonuc)
