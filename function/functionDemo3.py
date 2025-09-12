# #tuple
# def getNames(*args):
#     print(args)


# #getNames("ram","shyam","amit","sumit")    
# #getNames()    

#tuple
def getNames(*args,x,y):
    print(args)
    print(x)
    print(y)


#getNames("ram","shyam","amit","sumit")    #error
#getNames("ram","shyam","amit","sumit",x="raja","ok") #compile time error
getNames("ram","shyam","amit","sumit",x="raja",y="ok") 

#getNames()    


def getNames1(x,*args):
    print(x)
    print(args)

getNames1(100,299,20,30)