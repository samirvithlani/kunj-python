#default
#param
#copy
#to initil instance variable of class
#const is a special funciton which has same name as class name
#cosnt will call auto when class object is created..
#in python const can be create using __init__(self):

class Bank:
    
    def __init__(self):
        self.name = "ICICI"
        print("default const of classs")
        
    def getDetail(self):
        print(self.name)    


b=Bank()        
b.getDetail()

