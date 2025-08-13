#string stores data in array ---> index [0,...]
#string is immutable

data = "royal techno"
print(data)
# print(data[0])
# print(data[1])
# print(data[2])
# print(data[3])

#len find..

l = len(data)
print(f"len = {l}")

# for i in range(0,l):
#     print(data[i],end=" ")

# for i in range(len(data)):
#     print(data[i],end="")

for i in data:
    print(i,end="")


#data[0] = "X" error