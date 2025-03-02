# any(iterable), iterable içindeki en az bir eleman True ise True döndürür. Eğer tüm elemanlar False ise False döner.
# all(iterable), iterable içindeki tüm elemanlar True ise True döndürür. Eğer en az bir eleman False ise False döner.

numbers1=[1,3,5,7,6,53]
result1= all([bool(num) for num in numbers1])

print(result1)

numbers2=[12,0,9,8,45]
result2=all([bool(num) for num in numbers2])
result3=any([bool(num) for num in numbers2])

even_result=all([num % 2 == 0 for num in numbers2])

print(result2)
print(result3)
print(even_result)

users=["ali","ahmet","fatma","ece"]
user_result=all([user[0] == "a" for user in users])

print(user_result)