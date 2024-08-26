class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    
    def getName(self) -> str:
        return self.name
    def getAge(self) -> str:
        return self.age