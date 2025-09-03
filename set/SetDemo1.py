#set is dynamic
#set is unorders
#set stores data in hashtable
#set is unique element colelction
#set is not subscriptable
#set stores data  in {}

# data = set({})
# print(type(data))


data = {11,2,3,5,4,5,6,7,8,11,1,2,3,4,5}
print(data)

data.add(101)
print(data)

data.update([11,22,45,67,89])
print(data)


removedelm = data.pop()
print(f"removing... {removedelm}")


data.remove(89)
print(data)

# for  i in data:
#     print(i)


