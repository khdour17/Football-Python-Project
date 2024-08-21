class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    
    def getName(self) -> str:
        return self.name
    def getAge(self) -> str:
        return self.age


class Player(Person):
    def __init__(self,name,age,position) -> None:
        self.position = position
        self.goals = 0
        super().__init__(name,age)
    
    def getPos(self) -> str:
        return self.position
    def getGoals(self) -> int:
        return self.goals
    def addGoal(self) -> None:
        self.goals += 1
    def __str__(self):
        return f"{self.name} | {self.age} | {self.position} | goals scored: {self.goals}"


class Manager(Person):
    def __init__(self,name,age,tactics) -> None:
        self.tactics = tactics
        super().__init__(name,age)
    
    def getTactics(self) -> str:
        return self.tactics

    def __str__(self) -> str:
        return f"{self.name} | {self.age} | tactics: {self.tactics}"


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
    
    def DisplayTeamInfo(self):
        print(self.name)
        print(self.manager)
        for player in self.players:
            print(player)
    
    def __str__(self) -> str:
        return f"{self.name:<15} | {self.gamesPlayed:<2} | {self.wins:<2} | {self.draws:<2} | {self.loses:<2} | {self.goalsFor:<2} | {self.goalsAgainst:<2} | {self.points:<2}"
            


import random
class Match:
    def __init__(self,HomeTeam:Team,AwayTeam:Team) -> None:
        self.HomeTeam = HomeTeam
        self.AwayTeam = AwayTeam
        self.HomeGoals = 0
        self.AwayGoals = 0
        self.HomeScorers = []
        self.AwayScorers = []
        
    def simulateMatch(self) -> str:
        self.HomeGoals = random.randint(0, 5)
        self.AwayGoals = random.randint(0, 5)
        
        self.HomeTeam.UpdateStats(self.HomeGoals,self.AwayGoals)
        self.AwayTeam.UpdateStats(self.AwayGoals,self.HomeGoals)

        for _ in range(self.HomeGoals):
            player = self.HomeTeam.players[random.randint(1,3)]
            player.addGoal()
            self.HomeScorers.append(player.name)
        for _ in range(self.AwayGoals):
            player = self.AwayTeam.players[random.randint(1,3)]
            player.addGoal()
            self.AwayScorers.append(player.name)            
        
    def __str__(self):
        return (f"{self.HomeTeam.name} {self.HomeGoals} - {self.AwayGoals} {self.AwayTeam.name}" )


class League:
    def __init__(self,name) -> None:
        self.name = name
        self.teams = {}
        self.rounds = []
    
    def addTeam(self,team: Team)->str:
        if team.name in self.teams:
            return "This team is allready in the league!"
        self.teams[team.name] = team
        return "This team has been added to the league!"
    
    def removeTeam(self,teamName)->str:
        if teamName not in self.teams:
            return "This team is not in the league!"
        self.teams.pop(teamName)
        return "This team has been removed form the league!"
    
    def makeRounds(self):
        teams = list(self.teams.values())
        n = len(teams)
        for i in range(n-1):
            roundMatches = []
            for j in range(n//2):
                home = teams[j]
                away = teams[n-j-1]
                roundMatches.append(Match(home,away))
            self.rounds.append(roundMatches)
        teams = teams[::-1]
        secondHalf = []
        for roundMatches in self.rounds:
            newRound = [Match(match.AwayTeam,match.HomeTeam) for match in roundMatches]
            secondHalf.append(newRound)
        self.rounds.extend(secondHalf)
    
    def simulateRounds(self):
        self.makeRounds()
        for round_number, round_matches in enumerate(self.rounds, 1):
            print(f"Round number: {round_number}")
            for match in round_matches:
                match.simulateMatch()
                print(match)
                if match.HomeGoals > 0:
                    print(f"  Scorers for {match.HomeTeam.name}: {', '.join(match.HomeScorers)}")
                if match.AwayGoals > 0:
                    print(f"  Scorers for {match.AwayTeam.name}: {', '.join(match.AwayScorers)}")
                print("|||||||||||")
            print("-----------------")
        
    def resetStats(self) -> None:
        for team in self.teams.values():
            team.resetStats()
    
    def displayTopScorers(self):
        pass
    
    def displayTable(self) -> None:
        print("\nLeague Standings:")
        print(f"{'Team':<15} | {'P':<2} | {'W':<2} | {'D':<2} | {'L':<2} | {'GF':<2} | {'GA':<2} | {'Pts':<2}")
        print("-" * 51)
        standings = sorted(self.teams.values(), key = lambda x: (-x.points, x.goalsFor - x.goalsAgainst))
        for team in standings:
            print(team)

import xml.etree.ElementTree as ET

def Main():
    league = League("Champions League")
    tree = ET.parse('data.xml')
    root = tree.getroot()
    for child in root:
        team = Team(child[0].text)
        league.addTeam(team)
        for player in child[1]:
            team.addPlayer(player[0].text,player[1].text,player[2].text)
        team.setManager(child[2][0].text,child[2][1].text,child[2][2].text)
    league.simulateRounds()
    league.displayTable()
    league.resetStats()
    
Main()