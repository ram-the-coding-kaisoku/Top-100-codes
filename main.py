class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def talk(self):
        print(f"{self.name} is talking")
        
    def getData(self):
        return f"{self.name} is {self.age} years old"
    
    
class Student(Human):
    def __init__(self, name, age,year):
        super().__init__(name, age)
        self.year = year
    
    def getYear(self):
        print(f"{self.name} is graduated in the year of {self.year}")

h1=Human("Luffy",21)
h2=Human("sanji",23)
h3=Human("zoro",23)

h4=Student("Nami",21,2024)

h1.getYear()