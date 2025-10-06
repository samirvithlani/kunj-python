class Team:
    
    teamName = "CSK" #static
    
    def getTeamData(self):
        coachName = "amitabh"
        self.players = 11 #instance variable..
        print("coachName = ",coachName)
        print("players =",self.players)
    
    def printTeam(self):
        print("team players",self.players)    


t1 = Team()
t1.getTeamData()
t1.printTeam()        

t2 = Team()
t2.printTeam()