data = (10,20,30,40,50)
print(data)

print(data[0])
#data[0] = 1000
print(data.count(30))
print(data.index(40))


datalist = list(data)
datalist.append(60)

data = tuple(datalist)

print(data)


a = (1,2,3)
b = (4,5,6)

x = a + b
print(x)

