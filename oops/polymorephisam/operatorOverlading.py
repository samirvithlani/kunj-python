class Demo:
    
    def __init__(self,x):
        self.x = x
    
    def __add__(self,other):
        print("add called...")
        print(self.x)
        print(other.x)
        




d1 = Demo(100)
d2 = Demo(200)

d1 + d2 #__add__

        