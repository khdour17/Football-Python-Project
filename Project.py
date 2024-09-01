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
    
    def resetGoals(self) -> None:
        self.goals = 0
    
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
        for player in self.players:
            player.resetGoals()
    
    def displayTeamInfo(self, logWidget):
        
        logWidget.append(f"Team name: {str(self.name)}")
        logWidget.append(f"Team manager: {str(self.manager)}")
        logWidget.append("Players:")
        for player in self.players:
            logWidget.append(f"    {str(player)}")
        
    
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


import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("MainWindow.ui",self)
        self.tableWidget.setColumnWidth(0,158)
        self.tableWidget.setColumnWidth(1,50)
        self.tableWidget.setColumnWidth(2,50)
        self.tableWidget.setColumnWidth(3,50)
        self.tableWidget.setColumnWidth(4,50)
        self.tableWidget.setColumnWidth(5,50)
        self.tableWidget.setColumnWidth(6,50)
        self.tableWidget.setColumnWidth(7,50)
        self.tableWidget.setColumnWidth(8,50)
        self.LoadTableData()
        self.SimulateButton.clicked.connect(self.Simulation)
        self.ResetButton.clicked.connect(self.Reset)
        self.SearchButton.clicked.connect(self.openSearchWindow)
    
    def LoadTableData(self):
        league.displayTable(self.tableWidget)

    def Simulation(self):
        league.resetStats()
        self.RoundResultLog.clear() 
        self.GoalsScorersLog.clear()  
        self.tableWidget.clearContents()
        league.simulateRounds(self.RoundResultLog)
        league.displayTopScorers(5,self.GoalsScorersLog)
        self.LoadTableData()
    
    def Reset(self):
        league.resetStats()
        self.RoundResultLog.clear() 
        self.GoalsScorersLog.clear()  
        self.tableWidget.clearContents()
        self.LoadTableData()
    
    def openSearchWindow(self):
        self.window = SearchScreen()
        self.window.show()

class SearchScreen(QDialog):
    def __init__(self) -> None:
        super(SearchScreen, self).__init__()
        loadUi("SearchScreen.ui",self)
        self.SearchButton.clicked.connect(self.showTeamInfo)

    def showTeamInfo(self):
        self.TeamInfoLog.clear()
        name = self.SearchBar.text().strip()
        if name not in league.teams:
            self.TeamInfoLog.append("This team does not exsit!")
        else:
            league.teams[name].displayTeamInfo(self.TeamInfoLog)
        self.SearchBar.clear()



import xml.etree.ElementTree as ET

league = League("Champions League")
tree = ET.parse('data.xml')
root = tree.getroot()
for child in root:
    team = Team(child[0].text)
    league.addTeam(team)
    for player in child[1]:
        team.addPlayer(player[0].text,player[1].text,player[2].text)
    team.setManager(child[2][0].text,child[2][1].text,child[2][2].text)


app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(575)
widget.setFixedWidth(840)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")