# with open("demo1.txt","r") as file:
#     #data = file.read()
#     data = file.read(2)
#     print(data)


# count=0
# with open("th.txt","r") as file2:
#     for i in file2:
#         count+=1
#         print(i,end=" ")

# print("count = ",count)        

file3 = open("files/ram.txt","r")
while True:
    x = file3.readline()
    print(x,end=" ")
    if not x:
        break
# x = file3.readline()
# print(x)

        