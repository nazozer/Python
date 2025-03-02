names=["ahmet","ali","sena","melisa","yasemin"]
result= max([len(name) for name in names])

result=min(names, key= lambda name: len(name))
print(result)

urunler= [
    {"title": "samsung s23", "price" : 70000},
    {"title": "samsung s24", "price": 80000},
    {"title": "samsung s25", "price": 90000}

]
resultt= min(urunler, key= lambda urun: urun["price"])
resultt_1=max(urunler, key=lambda urun: urun ["price"])["title"]
print(resultt)
print(resultt_1)

