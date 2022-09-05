fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

while x in fruits:
    print(x,y,z)
    break #if you dont have this break here you while loop will keep on replicating
print(x)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

for x in fruits:
    print(x,y,z)
    break
print(x)