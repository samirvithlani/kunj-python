# def test():
#     return 1
#     return 2

# x = test()
# print(x)

def test():
    print("test called...")
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

# x = test()
# print(x)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

for i in test():
    print(i)
    
    
    