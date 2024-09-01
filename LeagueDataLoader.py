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