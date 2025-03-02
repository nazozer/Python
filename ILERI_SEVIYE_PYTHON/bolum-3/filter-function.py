numbers=[1,3,5,-4,-3]

# def negativeNumbers(x):
#     if x < 0:
#         return True
#     else:
#         return False

# result= list(filter(negativeNumbers, numbers))
# print(result)

result=list(filter(lambda x: x < 0 , numbers))
result=list(filter(lambda y: y % 2 == 1,numbers ))


names=["çınar","ada","ali","sena"]
filteredResult=list(filter(lambda x: x[0]=="a", names))

# result=list(map(lambda i: i.upper(),filter(lambda i: i[0]=="a", names)))
result=list(map(lambda i: i.upper(),filteredResult))


users=[
    {"username":"nazliözer", "posts":["post1","post2"]},
    {"username":"ömerözer","posts":[]},
    {"username":"hiranur","posts":["post1","post2","post3"]}
]

filteredUsers=list(filter(lambda u: len(u["posts"])>2 , users))
# result=list(map(lambda u: u["username"] ,filter(lambda u: len(u["posts"])>2 , users)))
result=list(map(lambda u: u["username"], filteredUsers))

#list-comp
result=[user["username"].upper() for user in users if len(user["posts"]) >0]
print(result)