class Parent:
    
    car="BMW"
    
    def __init__(self):
        self.amount = 20000
        print("parent class default const..")


class Child(Parent):
    
    # def __init__(self):
    #     print("child const called...")
    #     super().__init__()
    
    
    def display(self):
        print("display called...")  
        print(self.car)
        print("amount from parent",self.amount)  


c = Child()        
c.display()
    
            
    