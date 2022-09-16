class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print("this is the first name: " + self.firstname, self.lastname)

x = Person("John", "Hero")
x.printname()

x2 = Person("Mussawir", "Imam")
x2.printname()