class Match:
    
    players =20 #static varible --> instance variable..
    
    def printPLayers(self):
        print("players = ",self.players)
        print("players = ",Match.players)


m =Match()
m.printPLayers()        