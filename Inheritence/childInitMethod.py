class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname): #When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
    Person.__init__(self, fname, lname) #To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

x = Student("Mike", "Olsen")
x.printname()

#Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.