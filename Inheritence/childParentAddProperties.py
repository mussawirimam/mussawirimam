class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019 #Add a property called graduationyear to the Student class:
    self.three = 3
    self.four = 4
    self.five = 5
x = Student("Mike", "Olsen")
print(x.graduationyear)
print(x.three)
print(x.four)
print(x.five)