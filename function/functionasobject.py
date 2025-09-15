def test():
    print(":test function called...")

# test() #calling part...    
# print(test())
# print(test) #address

x = test #x == test()
x()
# x = 100
# y = x


def add(a,b):
    return a+b

x1 = add
print(x1(10,20))