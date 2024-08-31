from Player import *
from Manager import *
class Team:
    def __init__(self,name) -> None:
        self.name = name
        self.players = []
        self.manager = None
        self.points = 0
        self.gamesPlayed = 0
        self.wins = 0
        self.draws = 0
        self.loses = 0
        self.goalsFor = 0
        self.goalsAgainst = 0
    def addPlayer(self,name,age,position) -> None:
        self.players.append(Player(name,age,position))
    
    def setManager(self,name,age,tactics):
        self.manager = Manager(name,age,tactics)
    
    def UpdateStats(self,goalsFor,goalsAgainst):
        if goalsFor > goalsAgainst:
            self.points += 3
            self.wins += 1
            self.goalsFor += goalsFor
            self.goalsAgainst += goalsAgainst
        elif goalsFor == goalsAgainst:
            self.points += 1
            self.draws += 1
            self.goalsFor += goalsFor
            self.goalsAgainst += goalsAgainst
        else:
            self.loses += 1
            self.goalsFor += goalsFor
            self.goalsAgainst += goalsAgainst
        self.gamesPlayed += 1
    
    def resetStats(self):
        self.points = 0
        self.gamesPlayed = 0
        self.wins = 0
        self.draws = 0
        self.loses = 0
        self.goalsFor = 0
        self.goalsAgainst = 0
        for player in self.players:
            player.resetGoals()
    
    def displayTeamInfo(self):
        print("*"*15)
        print(f"Team name: {self.name}")
        print(f"Team manager: {self.manager}")
        print("Players:")
        for player in self.players:
            print(f"    {player}")
        print("*"*15)
    
    def __str__(self) -> str:
        return f"{self.name:<15} | {self.gamesPlayed:<2} | {self.wins:<2} | {self.draws:<2} | {self.loses:<2} | {self.goalsFor:<2} | {self.goalsAgainst:<2} | {self.points:<2}"
 