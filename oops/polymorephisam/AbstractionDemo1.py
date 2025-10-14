
from abc import ABC,abstractmethod

#ABSTRACT CLAS
class RBI(ABC):
    
    def __init__(self):
        print("const called...")
    
    
    @abstractmethod
    def upi(self,sender,reciver,amount):
        pass

class SBI(RBI):
    
    def __init__(self):
        print("sbi called...")    
    
    def upi(self, sender, reciver, amount):
        print("sbi upi logic...")    

s = SBI()        
            
    