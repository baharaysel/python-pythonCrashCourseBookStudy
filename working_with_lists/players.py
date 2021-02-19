##Working with Part of a List
#Slicing a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
#['charles', 'martina', 'michael']
print(players[:1])
#['charles']
print(players[3:])
#['florence', 'eli']
print(players[-3:])         ## this is cool it prints last 3 players only
#['michael', 'flroence', 'eli']


##Looping Through a Slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())
'''Here are the first three players on my team:
Charles
Martina
Michael'''

