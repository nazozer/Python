# for item in liste:
#     if(kosul):
#         expression

#[expression for item in liste if kosul]

numbers=[3,5,7,8,12,56,33]
result=[]

for i in numbers:
    if(i % 2 ==0):
        result.append(i)

result=[i for i in numbers if(i % 2==0)]
result=[i if i % 2 ==0 else "odd number" for i in numbers]
print(result)

product_prices=[3000,1000,0,4000,500]
taxes=[]

for price in product_prices:
    if(price > 0):
        taxes.append(price *1.18)


taxes= [price *1.18 for price in product_prices if price > 0]
taxes= [price*1.18 if price>0 else "taxes not calculated" for price in product_prices ]
print(taxes)

