import datetime
# x = dir(datetime)
x = datetime.datetime.fromisoformat()

print(x)
print(x.year)
print(x.hour)
print(x.strftime("%A"))
