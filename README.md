# Football League Simulation
This Python project simulates a football (soccer) league using PyQt5 for the graphical user interface (GUI). The program allows users to simulate rounds, track team standings, and display top goal scorers.

## Features
- League Management: Add, remove, and manage teams.
- Match Simulation: Simulate matches and update team statistics.
- League Table: View the league table with team standings.
- Top Scorers: Display the top goal scorers in the league.
- Reset Stats: Reset all league statistics.

## Installation
1. Clone the repository:
     `git clone https://github.com/khdour17/Football-Python-Project`
2. Install the required packages:
     `pip install -r requirements.txt`
3. Run the application:
     `python run Main.py`
   
## How to Use
1. Load the league data: The league data is loaded from an XML file (data.xml). Teams and players are automatically added to the league.
2. Simulate Rounds: Click on the Simulate button to simulate the league rounds. The results will be displayed in the logs, and the league table will be updated.
3. Reset League: Use the Reset button to clear all current league stats.
4. Search for a Team: Use the Search button to find a team and view detailed information about its players and manager.

## Screenshots
- Main Window Screen before simulation:  ![screenshot of the main window](https://github.com/khdour17/Football-Python-Project/blob/main/Screenshots/main%20window%20.png?raw=true)
- Main Window Screen after simulation:  ![screenshot of the main window after simulation](https://github.com/khdour17/Football-Python-Project/blob/main/Screenshots/main%20window%20simulated.png?raw=true)
- Search Screen: ![screenshot of the Search Screen](https://github.com/khdour17/Football-Python-Project/blob/main/Screenshots/Search%20Screen.png?raw=true)
- Search Screen after searching for PSG: ![screenshot of the Search Screen results](https://github.com/khdour17/Football-Python-Project/blob/main/Screenshots/Search%20Screen%20used.png?raw=true)

## Dependencies
- Python 3.x
- PyQt5
- xml.etree.ElementTree
- An XML file named data.xml containing the team, player, and manager information.
