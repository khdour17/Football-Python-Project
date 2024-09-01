from Team import *
import random
class Match:
    def __init__(self,HomeTeam:Team,AwayTeam:Team) -> None:
        self.HomeTeam = HomeTeam
        self.AwayTeam = AwayTeam
        self.HomeGoals = 0
        self.AwayGoals = 0
        self.HomeScorers = {}
        self.AwayScorers = {}
        
    def simulateMatch(self) -> str:
        self.HomeGoals = random.randint(0, 5)
        self.AwayGoals = random.randint(0, 5)
        
        self.HomeTeam.UpdateStats(self.HomeGoals,self.AwayGoals)
        self.AwayTeam.UpdateStats(self.AwayGoals,self.HomeGoals)

        for _ in range(self.HomeGoals):
            player = self.HomeTeam.players[random.randint(1,3)]
            player.addGoal()
            if player.name not in self.HomeScorers:
                self.HomeScorers[player.name] = 1
            else:
                self.HomeScorers[player.name] += 1
        for _ in range(self.AwayGoals):
            player = self.AwayTeam.players[random.randint(1,3)]
            player.addGoal()
            if player.name not in self.AwayScorers:
                self.AwayScorers[player.name] = 1
            else:
                self.AwayScorers[player.name] += 1            
        
    def __str__(self):
        return (f"{self.HomeTeam.name} {self.HomeGoals} - {self.AwayGoals} {self.AwayTeam.name}" )
 