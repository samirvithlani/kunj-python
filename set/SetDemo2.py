users1 = {"ram","shyam","amit","sumit"}
users2 = {"ram","shyam","amita","sumita"}


x = users1.union(users2)
print(x)

x = users1.difference(users2)
print(x)

x = users1 - users2
print(x)

x = users1.intersection(users2)
print(x)

x= users1 & users2
print(x)

x = users1.symmetric_difference(users2)
print(x)



flag = users1.issuperset(users2)
print(flag)

flag = users1.issubset(users2)
print(flag)


#{1,2,3,4}
#{1,2} -->
# users1.difference_update(users2)
# print(users1)