class Java:
    
    compiler = "JDK"
    x =100
    def __init__(self):
        self.concept = "oops"
        print("java class const called..")

class C:
    compiler = "GCC"        
    y=200
    def __init__(self):
        self.concept="POPS"
        self.a =100
        print("c lang const called...")


class Python(Java,C):        
    
    def __init__(self):
        print("python class const called...")
        super().__init__()
    
    def coding(self):
        print("x = ",self.x)
        print("y = ",self.y)
        #print("y = ",self.a) error..
        print("using compiler ..",self.compiler)    
        print("using concept ...",self.concept)
        


p = Python()
p.coding()        