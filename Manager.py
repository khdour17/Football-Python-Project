from Person import *
class Manager(Person):
    def __init__(self,name,age,tactics) -> None:
        self.tactics = tactics
        super().__init__(name,age)
    
    def getTactics(self) -> str:
        return self.tactics

    def __str__(self) -> str:
        return f"{self.name} | {self.age} | tactics: {self.tactics}"
