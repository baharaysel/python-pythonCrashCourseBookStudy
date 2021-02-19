
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
#['trek', 'cannondale', 'redline', 'specialized']

print(bicycles[0])
#trek
print(bicycles[0].title())
#Trek
print(bicycles[1])
#cannondale
print(bicycles[-1])
#specialzed

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
#My first bicycle was a Trek.


##TRY IT YOURSELF 3.1 names, greetings and your own list page40

names = ['Hatice', 'Figen', 'Dilshan','Vimla', 'Nazli']
print(names[0])
#Hatice
print(names[-1])
#Nazli
print(names[0],names[2])
#Hatice Dilshan
print(names[1:3])
#['Figen', 'Dilshan']


message = " is my best friend."
print(names[0] + message)
#Hatice is my best friend.


favorite_food = ['pasta', 'pizza', 'mutton curry']
message = 'I would like to eat '
print(message + favorite_food[2] + '.')
#I would like to eat mutton curry.





