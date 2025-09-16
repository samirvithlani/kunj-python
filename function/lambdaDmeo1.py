def test():
    print("test called...")

test()    

x = lambda :print("test called...")
x()

# def add(a,b):
#     print(a+b)

x1 = lambda a,b : print(a+b)
x1(10,20)


# def add(a,b,c):
#     return a + b+ c

x2 = lambda a,b,c : a+b+c
ans = x2(1,2,3)
print(f"ans = {ans}")
print(f"{x2(10,20,30)}")


x3 = lambda fname,lname : f"{fname} {lname}"
print(x3("ram","sharma"))


findmax = lambda a,b :a if a>b else b
print(findmax(10,0))

findmax2 = lambda a,b,c : a if a>b else(b if b>c else c)
print(findmax2(10,100,20))

