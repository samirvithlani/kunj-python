#builtin , udf
#with retun type with argument
#with retun type without argument
#without retun type with argument
#without retun type without argument

#def keyword

def test():
    print("this is test function")
    #wo return type wo argument
test()    

def greet(name):
    print(f"Hello {name}")

greet("MS")    

# def add(a,b):
#     print("add called...")
#     return a + b

# ans = add(10,20)
# print(f"ans  = {ans}")

def add(a,b)->int:
    print("add called...")
    return a + b

#ans = add(10,20)
ans = add("ram","shyam")
print(f"ans  = {ans}")

