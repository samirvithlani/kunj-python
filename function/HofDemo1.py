def calling():
    print("calling....")

def test(a):
    print(a) #calling()
    a()

# test(10)
# test("java")
# test(False)
# test({})
# test([])    
test(calling)