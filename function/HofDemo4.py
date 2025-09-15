
def science(stuname):
    print(f"admission of {stuname} in science confirmed!!")
    return f"Hello {stuname} welome to science"

def comm(stuname):
    print(f"admission of {stuname} in com confirmed!!")
    return f"Hello {stuname} welome to comm"

def arts(stuname):
    print(f"admission of {stuname} in arts confirmed!!")    
    return f"Hello {stuname} welome to arts"

def addmission(cb,name):
    #cb("ram")
    message = cb(name)
    #print(message)
    return f"{message} Hello {name} admission process done"
    


msg = None
name  = input("enter name :")
pers = float(input("enter pers :"))    

if pers>80:
    msg = addmission(science,name)
elif pers>70:
    msg = addmission(comm,name)    
else:
    msg = addmission(arts,name)    

print(msg)    
