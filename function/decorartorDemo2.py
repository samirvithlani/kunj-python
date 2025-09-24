
#deco is a pure pyth function which will accept anothrt func as argument
#and return inner funciton object
#it denoed by @

def purchase_pass(func): #3 func == go_for_garba()
    
    def inner(person): #6
        print("purchasing passes...",person) #7
        func(person) #8
        
    
    return inner    #4



@purchase_pass #2 #5
def go_for_garba(pers):#9
    print("print going for garba...",pers) #10


go_for_garba(10)    #1