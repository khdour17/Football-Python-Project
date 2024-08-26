from Person import *
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
