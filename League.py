from Player import *
from Manager import *
from Team import *
from Match import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
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
    
    def simulateRounds(self,logWidget):
        self.makeRounds()
        for round_number, round_matches in enumerate(self.rounds, 1):
            logWidget.append(f"Round number: {round_number}")
            for match in round_matches:
                match.simulateMatch()
                logWidget.append(str(match))
                if match.HomeGoals > 0:
                    scorers = []
                    for player , goals in match.HomeScorers.items():
                        if goals >= 2:
                            scorers.append(f"{player} {goals}")
                        else:
                            scorers.append(player)
                    logWidget.append(f"  Scorers for {match.HomeTeam.name}: {', '.join(scorers)}")
                if match.AwayGoals > 0:
                    scorers = []
                    for player , goals in match.AwayScorers.items():
                        if goals >= 2:
                            scorers.append(f"{player} {goals}")
                        else:
                            scorers.append(player)
                    logWidget.append(f"  Scorers for {match.AwayTeam.name}: {', '.join(scorers)}")
                logWidget.append("\\\\\\\\\\\\\\\\\\")
            logWidget.append("-----------------")
        
    def resetStats(self) -> None:
        for team in self.teams.values():
            team.resetStats()
    
    def displayTopScorers(self,topN,logWidget):
        topScorers = []
        for team in self.teams.values():
           for player in team.players:
               if player.getGoals() > 0:
                   topScorers.append((player.name,team.name,player.getGoals())) 
        topScorers.sort(key = lambda x:-x[2])
        for idx,player in enumerate(topScorers[:topN]):
            logWidget.append(f"{idx+1}. {player[0]:<15} | {player[1]:<15} | {player[2]:<2} goals")
        
    
    def displayTable(self,tableWidget) -> None:
        
        standings = sorted(self.teams.values(), key = lambda x: (-x.points, -(x.goalsFor - x.goalsAgainst)))
        row=0
        tableWidget.setRowCount(len(standings))
        for team in standings:
            tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(team.name))
            tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(team.gamesPlayed)))
            tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(team.wins)))
            tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(team.draws)))
            tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(team.loses)))
            tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(team.goalsFor)))
            tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(team.goalsAgainst)))
            tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(str(team.points)))
            row += 1
