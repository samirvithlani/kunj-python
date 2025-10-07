from multipledispatch import dispatch


class Shape:
    
    @dispatch()
    def area(self):
        print("area called...")
    
    @dispatch(int,int)
    def area(self,h,w):
        print("recangle = ",h,w)
    
    @dispatch(int)
    def area(self,h):
        print("square area called...")        


s = Shape()
s.area()
s.area(10,20)        
s.area(100)
    