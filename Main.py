import xml.etree.ElementTree as ET
from League import *

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
    print("-"*30)
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
        else:
            league.teams[name].displayTeamInfo()
    elif choice == 5:
        league.resetStats()
        print("League stats heve been reset.")
    elif choice == 6:
        break
    else:
        print("\nInvalid choice. Please enter a number between 1 and 6.")