# file = open("files/demo1.txt","w")
# file.write("Hi this is first line by python ")
# file.close()

# with open("files/demo2.txt","a") as file:
#     file.writelines(["java\n","python\n","cpp\n"])
#     #file close..



# with open("files/demo3.txt","a") as f:
#     print("Hi this is using print()",file=f)  

name = "ram"
age =23

with open("files/ram.txt","w") as file:
    print(f"name ={name} age = {age}",file=file) 
