###for loop

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)
#alice
#david
#carolina

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician.title() + ", that was a great trick!")
#Alice, that was a great trick!
#David, that was a great trick!
#Carolina, that was a great trick!

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")  # \n provide line space
#Alice, that was a great trick!
#I can't wait to see your next trick, Alice.

#David, that was a great trick!
#I can't wait to see your next trick, David.

#Carolina, that was a great trick!
#I can't wait to see your next trick, Carolina.


### 2loop in one print message amazing:)
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician.title() + ", that was a great trick!" + "\nI can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!") #this print after the loop be careful indentation is different.
#Alice, that was a great trick!
#I can't wait to see your next trick, Alice.

#David, that was a great trick!
#I can't wait to see your next trick, David.

#Carolina, that was a great trick!
#I can't wait to see your next trick, Carolina.

#Thank you, everyone. That was a great magic show!


###TRY IT YOURSELF page60
##4.1 Pizzas
pizza_names = ['margarita', 'hawaian', 'pepperoni', 'seafood']
for pizza_name in pizza_names:
	print(pizza_name)

pizza_names = ['margarita', 'hawaian', 'pepperoni', 'seafood']
for pizza_name in pizza_names:
	print("I like " + pizza_name.upper() + " pizza")
print("I really love pizza!")


##4.2 Animals
animals = ['bird', 'lion', 'goat', 'mouse']
for animal in animals:
	print(animal.title() + " can fly.")
print("No idiot! Only "+ animals[0] + " can fly.")


  
	
	
	
	
	

