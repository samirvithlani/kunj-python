data = {}

while True:
    name = input("enter name :")
    if name == "exit":
        break
    age = int(input("enter age :"))
    
    data.update({name:age})

print(data)    
        