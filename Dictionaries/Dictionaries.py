
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned" + str(new_points) + " points!")


##Addiny new key-value to dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0) 

##Starting with an Empty Dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)


##Modifying Values in a Dictionary
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print(alien_0)
print("The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3 # this must be a fast alien
#The new position is th eold position plus the incement.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))


##Removing Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

##A Dictionary of Similar Objects
favorite_languages = {
	'jen': 'python',
	'sarah': 'c', 
	'edward': 'ruby', 
	'phil': 'python',
	}
print(favorite_languages)
print(favorite_languages['sarah'].title()) # or print as below
print("Sarah's favorite language is " +
	favorite_languages['sarah'].title() +
	".")


##TRY IT YOURSELF Page102
#6.1 Person
person = {'first_name': 'Aysel', 'last_name': 'Isik', 'age': 36,
	'city': 'London',
	}
print(person)
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

#6.2 Favorite Numbers
favorite_numbers = {
	'aysel': 6, 
	'mehmetali': 17, 
	'ayhan': 43,
	'sermin': 26,
	'fatma': 79,
	}
print(favorite_numbers)

print("Aysel's favorite number: " + str(favorite_numbers['aysel']))
print("Mehmetali's favorite number: " + str(favorite_numbers['mehmetali']))
print("Ayhan's favorite number: " + str(favorite_numbers['ayhan']))
print("Sermin's favorite number: " + str(favorite_numbers['sermin']))
print("Fatma's favorite number: " + str(favorite_numbers['fatma']))
'''this is very long way to do it. Think about shorter way. how to bring first key value? and use loop'''
i=0
for favorite_number in favorite_numbers:
	x= list(favorite_numbers.keys())[i]
	print(x.title() + "'s favorite number is " + str(favorite_numbers[x])+ "\n")
	i= i+1
print("Well done Aysel.The loop is finished.")

	
#x= favorite_numbers.keys()
#print(favorite_numbers.keys())
copy= favorite_numbers.copy()
print(copy)
copy.clear()
print(copy)
#{}
copy = favorite_numbers.copy()
print(favorite_numbers['aysel'])
#6

print(list(favorite_numbers.keys())[0])
print(next(iter(favorite_numbers)))


##6.3 Glossary
glossary = {
	'class': ' A template for creating user-defined objects',
	'attribute': ' A value associated with an object which is referenced by name using dotting expressions.',
	'immutable': ' An object with a fixed value',
	}
print(list(glossary.keys())[0])
j=0
for gloss in glossary:
	x = list(glossary.keys())[j]
	print(x.title() + ": " + glossary[x]+ "\n")
	j= j+1
print("Aysel Well done! You did again. You're a star!")


###LOOPING THROUGH A DICTIONARY
user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
	}
for key,value in user_0.items():
	print("\nKey: " + key)
	print("\nValue: " + value)
'''or you can use any 2 variables instead of key and value pair like a and b'''
'''Let's try it'''
for a,b in user_0.items():
	print(a.title()+ ": " + b.title() + "\n")
	

favorite_languages = {
	'jen': 'python',
	'sarah': 'c', 
	'edward': 'ruby', 
	'phil': 'python',
	}
#   .items()
for name,language in favorite_languages.items():
	print(name.title() + "'s favorite language is " +
	language.title() + ".")
#  .keys()
for name in favorite_languages.keys():
	print(name.title())

for name in favorite_languages:  # it gives same result as above
	print(name.title())

#  for and if together
friends = ['phil', 'sarah']
for name in favorite_languages:
	#print(name.title()) # we dont really need this line
	if name in friends:
		print("Hi " + name.title() +
			", I see your favorite language is " +
			favorite_languages[name].title() + "!")
# Checking if it is in the dictionary
favorite_languages = {
	'jen': 'python',
	'sarah': 'c', 
	'edward': 'ruby', 
	'phil': 'python',
	}	
if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

###LOOPING THROUGH A DICTIONARY'S KEYS IN ORDER
for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking our poll.")

###Looping through all values in a dictionary
print("The following languages have been mentioned")
for language in favorite_languages.values(): # in this method we will see repetetive values
	print(language.title())
#to see only unique results use set
for language in set(favorite_languages.values()):
	print(language.title()) # python is not repeated now.


####TRY IT YOURSELF Page 108
#6.4 Glossary 2  (loop that runs through items, key and values (items=key,value))
glossary = {
	'class': ' A template for creating user-defined objects',
	'attribute': ' A value associated with an object which is referenced by name using dotting expressions.',
	'immutable': ' An object with a fixed value',
	}
for words, meaning in glossary.items():  #words and meaning is treated as variable
	print(words.title() +": "+ meaning)
for words in glossary.keys():
	print(words.title())
for meaning in glossary.values():
	print(meaning.title())
	
glossary['1'] = 'a' # method to add 5 more items to dictionary
glossary['2'] = 'b'
glossary['3'] = 'c'
glossary['3'] = 'd'
glossary['5'] = 'e'

print(glossary)


#6.5 Rivers
rivers = {'nile': 'egypt', 'dicle': 'turkey', 'firat': 'turkey'}

for river, country in rivers.items():
	print("The " + river.title() + " runs through " + country.title() + ".")

for river in rivers:
	print(river.title())
#or method below gives same result
for river in rivers.keys():
	print(river.title())

for country in rivers.values():
	print(country.title())
	
#6.6 Polling
favorite_languages = {
	'jen': 'python',
	'sarah': 'c', 
	'edward': 'ruby', 
	'phil': 'python',
	}
list_of_people = ['aysel', 'sarah', 'nazli', 'phil']
for name in list_of_people:
	if name not in favorite_languages.keys():
		print(name.title() + ", please take the favorite language poll.")
	else:
		print(name.title()+ ", thank you for taking the poll")
''' you can do reverse way too'''
for name in list_of_people:
	if name in favorite_languages.keys():
		print(name.title() + ", thank you for taking the poll")
	else:
		print(name.title()+ ", please take the favorite language poll.")


#####NESTING  Nesting Nesting
##A list of Dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'green', 'points': 10} 
alien_2 = {'color': 'green', 'points': 15} 

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)

'''this is exciting! I am going to create a fleet of 30 aliens by using code range
#create empty list'''
aliens = []
#make 30 green aliens.
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)
print(aliens)
#Show the the first 5 aliens:
for alien in aliens[:5]:
	print(alien)
print("...")
#Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))

'''I have skipped the part in the book'''

###TRY IT YOURSELF
#6.7 People
person_1 = {'first_name': 'Aysel', 'last_name': 'Isik', 'age': 36,
	'city': 'Izmir',
	}
person_2 = {'first_name': 'Aysell', 'last_name': 'Isikk', 'age': 37,
	'city': 'London',
	}
person_3 = {'first_name': 'Ayselll', 'last_name': 'Isikkk', 'age': 38,
	'city': 'Canada',
	}
people = [person_1, person_2, person_3]
for person in people:
	for key,value in person.items():
		print(key + ": " + str(value))
	print("\n")
print("Well done!")


#6.8 Pets
Sally = {'cat':'Aysel'}
Petra = {'dog': 'Fatma'}
Lale = {'goat': 'Aysel'}
Badem = {'cat': 'Aysel'}
Ceylan = {'goat': 'Rabia'}
pets = [Sally, Petra, Lale, Badem, Ceylan]
for pet in pets:
	for pet_name, owner in pet.items():
		print(owner +" is owner of "+ pet_name + "\n")

#6.9 Favorite Places
favorite_places = {
	'aysel':['geneva', 'antalya', 'ibiza'], 
	'halise':['lisbon','denizli'], 
	'hatice':['gottenburg']
	}

for name, fav_places_list in favorite_places.items():
	print("\n"+ name.title()+ "'s favorite places are: ")
	for fav_places in fav_places_list:
		print(fav_places.title())

#6.10 Favorite Numbers
favorite_numbers = {
	'aysel': [6, 8, 0],
	'mehmetali': [17, 43, 54],
	'ayhan': [43, 0],
	'sermin': [26, 35],
	'fatma': [79, 46, 78],
	}
for name, fav_numbers in favorite_numbers.items():
	print("\n" + name.title() + "'s favorite numbers: ")
	for number in fav_numbers:
		print(number)
		
#6.11 Cities
cities = {
	'izmir':{'country':'turkey', 'population':'8000000', 'fact': 'not capital'},
	'london':{'country':'UK', 'population':'8000000', 'fact':'capital'},
	'geneva':{'country':'switzerland', 'population':'1000000', 'fact':'not capital'},
	}
for city, city_info in cities.items():
	print("\nThe city name is " + city.title())
	for country in city_info.values():
		print(country)
		
#6.12 Extensions
'''Learn how to add to dictionaries and change their values. now I am so tired'''
cities = {
	'izmir':['turkey','8000000','not capital'],
	'london':['UK', '8000000', 'capital'],
	'geneva':['switzerland', '1000000', 'not capital'],
	}
''' my brain stopped working:)
new_city = {'newyork':['usa', '15000000', 'capital']}
cities.append(new_city)
print(cities)
'''

