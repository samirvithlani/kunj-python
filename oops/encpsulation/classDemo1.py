#class name must starts with cap
class Demo:
    
    #self is current object of class
    def test(self):
        print("test function called...")
        #print(self)
    def sum(self,a,b):
        print(a+b)    

#class ref 
d = Demo()  
d.test()  
#print(d)    
#d.test(d) 
d.sum(10,20)