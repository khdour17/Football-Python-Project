from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog
from League import *
from LeagueDataLoader import league

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
