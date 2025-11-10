#public:

class Bank:
    
    __balance=1000
    def __init__(self):
        self. __name="ram"
        print("bank class const called..")
    
    def checkBal(self):
        print("this si publc method...")        
    
    def __loan(self):
        print("private method..")    
    
    def getLoadnData(self):
        print(self.__balance)
        print(self.__name)
        self.__loan()    


b = Bank()
b.checkBal()        
#b.__loan() #error....
b.getLoadnData()
#b.__balance