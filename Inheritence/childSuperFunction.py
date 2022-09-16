
class Person:
  def __init__(self, fname, lname, tname):
    self.firstname = fname
    self.lastname = lname
    self.thirdname = tname

  def printname(self):
    print(self.firstname, self.lastname, self.thirdname)

#Python also has a super() function that will make the child class
# inherit all the methods and properties from its parent:
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname, tname)

x = Person("Mike", "Olsen", "robert")
#x = Student("Mike", "Olsen", "robert")
x.printname()
