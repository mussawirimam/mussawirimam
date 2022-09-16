class Name:
    def __init__(self, name):
        self.name = name 
        
        # print (name)
        # return name


    def my_function(self):
        print("My name is " + self.name)

p1 = Name("John")
p1.my_function()

p2 = Name("Hero")
p2.my_function()