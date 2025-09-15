
def science(stuname):
    print(f"admission of {stuname} in science confirmed!!")

def comm(stuname):
    print(f"admission of {stuname} in com confirmed!!")

def arts(stuname):
    print(f"admission of {stuname} in arts confirmed!!")    

def addmission(cb,name):
    #cb("ram")
    cb(name)
    


name  = input("enter name :")
pers = float(input("enter pers :"))    

if pers>80:
    addmission(science,name)
elif pers>70:
    addmission(comm,name)    
else:
    addmission(arts,name)    
