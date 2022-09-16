class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name + abc.age)

p1 = Person(name="hero", age=36)
p1.myfunc()






#print(p1.name, p1.age)
    
#p1 = Person("John", 36)
#p1.myfunc()
