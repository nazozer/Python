# sort(): Yerinde (In-place) siralama.Orijinal liste değişir.Sadece listeler 

numbers=[17,5,98,12,0]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

# sorted(): Yeni bir sıralı liste döndürür,orijinal veri değişmez.Tüm iterable'lar (list, tuple, set, dict keys, vb.)

result=sorted(numbers)
print(result)


users=[
    {"username":"nazliözer","posts":["post1","post2"],"email":"info@abc.com","phone":"12345678"},
    {"username":"aliözer","posts":["post1"],"email":"info@abcd.com"},
    {"username":"sevdaözer","posts":["post1","post2","post3"]}
]

#key bilgilerinin sayısına göre filtreler
result_user=sorted(users, key=len)
print(result_user)
result_user=sorted(users, key=len, reverse=True)
print(result_user)

result_user=sorted(users, key=lambda user: user["username"])
print(result_user)

result_user=sorted (users, key=lambda user: len(user["posts"]))
print=(result_user)

#en az post atan kişiyi filtreleme
result_user1=list(map(lambda user: user["username"], sorted(users, key=lambda user: len(user["posts"]))))

print(result_user1)
