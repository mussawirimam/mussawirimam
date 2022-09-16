#Create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printName(self):
        print("My first and last name: " + self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:        
x = Person("John", "Hero")
x.printName()

#To create a class that inherits the functionality from another class,
# send the parent class as a parameter when creating the child class:
class Student(Person):
    pass 

x = Student("student", "class") #creating or defining object through parent Class
x.printName() #parent class method
    




