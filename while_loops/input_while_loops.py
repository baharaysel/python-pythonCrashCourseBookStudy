
#message = input("Tell me something, and I will repeat it back to you: ")
#print(message)
'''x = input()
print(x)'''
'''name = input("Please enter your name: ")
print("Hello, " + name.title() + "!")
	
# For pompt is longer than one line
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt +="\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")'''

#python assumes all inputs are string eveb numbers are returned as strings
age = input("How old are you? ")
age = int(age)
age >= 18

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36 :
	print("\nYou're tall enough to ride!")
else:
	print("\nYou'll be able to ride when you're a little older.")


#The Modulo Operator % it tells remainder
#to check if the numers are even or divisible with certain numbers
number = input("Enter a number, and I'lltell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
	print("\nThe number " + str(number) + " is even.")
else:
	print("\nThe number " + str(number) + " is odd.")
	

##TRY IT YOURSELF page 121
#7.1 Rental Car
rental_car = input("What kind of rental car would you like to have?")
print("Let me see if i can find you a " + rental_car + ".")

#7.2 Restaurant Seating
number_guests = input("How many people are in the group?")
number_guests = int(number_guests)
if number_guests <= 8:
	print("Table is ready")
elif number_guests > 8:
	print("You have to wait for a table")

#7.3 Multiples of Ten
number_10 = input("Type an integer number except zero: ")
number_10 = int(number_10)
if number_10 % 10 == 0:
	print("The number  " + str(number_10) + " is multiple of 10.")
elif number_10 % 10 != 0:
	print("The number" + str(number_10) + " is not multiple of 10.")



##Introducing while Loops

current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1

##Letting the User Choose When to Quit
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
	message = input(prompt)
	if message != 'quit':
		print(message)

##Using a Flag

	












