#default argument

def add(a=0,b=0):
    return a + b


print(add(10,20))
print(add(10))
print(add())


#named param function
def getUserData(name,age,salary,email,city):
    print(f"Name = {name}")
    print(f"Age = {age}")
    print(f"Salary = {salary}")
    print(f"Email = {email}")
    print(f"City = {city}")
    


#getUserData("ram",22,34500,"ram@seeta.com","ahmedbad")
#getUserData(22,34500,'ram',"ahmedabad","ram@seeta.com")
getUserData(name="ram",city="ahmedbad",age=23,salary=34500,email="ram@seeta.com")