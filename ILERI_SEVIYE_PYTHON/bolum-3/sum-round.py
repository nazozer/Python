numbers=[1,3,9,7,6,90,123]
result= sum(numbers)
result= sum(numbers, 30)
print(result)

products=[
    {"title":"iphone 15", "price": 60000},
    {"title":"iphone 16", "price": 70000},
    {"title":"iphone 17", "price": 80000},
    {"title":"iphone 5", "price": 0}

]

toplamFiyat= sum(product["price"] for product in products)
urunAdedi=len([product for product in products if product["price"]> 0 ])
avrg_price= toplamFiyat/ urunAdedi
print(toplamFiyat)
print(avrg_price)


result= round(5.3)
result=round(10.8)
result=round(124.589, 2)
print(result)