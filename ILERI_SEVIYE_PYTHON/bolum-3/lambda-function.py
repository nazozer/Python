#lambda arguments: expression  
# fonk isim verilir ama lambda fonk isim verilmez ve return yazılmaz

def kareAl(a):
    return a**2
sonuc= kareAl(5)

sonuc= (lambda a: a**2) (3)
# y= lambda a: a**2
# sonuc= y(4)  bu şekilde değişkene atılabilir

toplama= lambda a,b,c: a+b+c
sonuc= toplama(1,2,3)

sonuc =(lambda a,b,c: a+b+c) (1,2,3)
print(sonuc)