class User:
    
    def __init__(self,name):
        self.name = name

    def getUser(self):
        print("userName = ",self.name)        

kunj = User("kunj")        
kunj.getUser()
ram = User("ram")        
ram.getUser()