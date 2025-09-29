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
    
def printData(batchsize, totaldata):
    #1 ,101,10
    for i in range(1, totaldata + 1, batchsize):
        # 1,(10)
        batch = list(range(i, min(i + batchsize, totaldata + 1)))
        yield batch
    


for batch in printData(10, 100):
    print(batch)
    
    
    
    