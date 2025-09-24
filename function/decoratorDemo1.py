
#deco is a pure pyth function which will accept anothrt func as argument
#and return inner funciton object
#it denoed by @

def purchase_pass(func): #3 func == go_for_garba()
    
    def inner(): #6
        print("purchasing passes...") #7
        func() #8
        
    
    return inner    #4



@purchase_pass #2 #5
def go_for_garba():#9
    print("print going for garba...") #10


go_for_garba()    #1