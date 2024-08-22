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
        return f"{self.name:<15} | {self.age:>2} | {self.position:>3} | goals scored: {self.goals:>2}"


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
                    scorers = []
                    for player , goals in match.HomeScorers.items():
                        if goals >= 2:
                            scorers.append(f"{player} {goals}")
                        else:
                            scorers.append(player)
                    print(f"  Scorers for {match.HomeTeam.name}: {', '.join(scorers)}")
                if match.AwayGoals > 0:
                    scorers = []
                    for player , goals in match.AwayScorers.items():
                        if goals >= 2:
                            scorers.append(f"{player} {goals}")
                        else:
                            scorers.append(player)
                    print(f"  Scorers for {match.AwayTeam.name}: {', '.join(scorers)}")
                print("\\\\\\\\\\\\\\\\\\")
            print("-----------------")
        
    def resetStats(self) -> None:
        for team in self.teams.values():
            team.resetStats()
    
    def displayTopScorers(self,topN):
        topScorers = []
        for team in self.teams.values():
           for player in team.players:
               if player.getGoals() > 0:
                   topScorers.append((player.name,team.name,player.getGoals())) 
        topScorers.sort(key = lambda x:-x[2])
        print("League Top Scoreres:")
        print(f"{'Player':<20} | {'Team':<15} | {'Goals':<5}")
        print("-" * 42)
        for scorer in topScorers[:topN]:
            print(f"{scorer[0]:<20} | {scorer[1]:<15} | {scorer[2]:<5}")
    
    def displayTable(self) -> None:
        print("\nLeague Standings:")
        print(f"{'Team':<15} | {'P':<2} | {'W':<2} | {'D':<2} | {'L':<2} | {'GF':<2} | {'GA':<2} | {'Pts':<2}")
        print("-" * 51)
        standings = sorted(self.teams.values(), key = lambda x: (-x.points, -(x.goalsFor - x.goalsAgainst)))
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
    
    while True:
        
        print("Welcome to the Champions League!")
        print("-"*20)
        print("Please choose one of the following options:")
        print("1- Simulate Round and show results")
        print("2- Show Standings Table")
        print("3- Show Top 5 Scorers")
        print("4- Show Info for a certain team")
        print("5- Reset Stats")
        print("6- Exit")
        
        choice = int(input("Enter a number between 1-6:"))
        
        if choice == 1:
            league.simulateRounds()
        elif choice == 2:
            league.displayTable()
        elif choice == 3:
            league.displayTopScorers(5)
        elif choice == 4:
            name = str(input("please enter the team name:")).strip()
            if name not in league.teams:
                print(f"{name} Team does not exist.")
            league.teams[name].displayTeamInfo()
        elif choice == 5:
            league.resetStats()
            print("League stats heve been reset.")
        elif choice == 6:
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")
Main()