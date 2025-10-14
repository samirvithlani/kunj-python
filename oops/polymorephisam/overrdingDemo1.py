class Parent:
    
    def __init__(self):
        print("parent class const called..")
    
    def add(self):
        print("add from parent called...")    



class Child(Parent):
    
    def __init__(self):
        print("child called...")        
    
    
    # def add(self):
    #     print("add from child called...")    


c =Child()
c.add()