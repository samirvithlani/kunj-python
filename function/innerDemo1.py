# def outer():
#     print("outer called...")
#     def inner():
#         print("inner function called...")
#     inner()

# outer()        

def outer():
    print("outer called...")
    def inner():
        print("inner function called...")
        return 100
    return inner

x = outer()
print(x())