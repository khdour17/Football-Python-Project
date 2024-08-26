from Player import *
from Manager import *
from Team import *
from Match import *
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
        self.rounds.clear()
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
