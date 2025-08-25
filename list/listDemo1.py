# data = [] #empty list
# print(data)
# print(type(data))

data = ["ram","shyam","amit","radha","seeta","ajay"]
print(data)
print(data[0])

#list mutable
data[0]="RAM"
print(data)

# for i in range(0,len(data)):
#     print(data[i])

# for i in data:
#     print(i)


data.append("lakshman") #none
print(data)

data.extend(["arjun","sahdev"])
print(data)

data.insert(2,"bhim")
print(data)


#remove
#data.clear()
#remvoedElm = data.pop() #last index remove...
remvoedElm = data.pop(2) #last index remove...
print(f"removing... {remvoedElm}")
print(data)

if "shyama" in data:
    data.remove("shyama") #none
print(data)


