
##Checking for Inequality !=
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
	print("Hold the anchovies!")
#Hold the anchovies!

##Numerical Comparisons
age = 18
age == 18
#True


requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings :
	print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")
#Adding mushrooms.
#Adding green peppers.
#Adding extra cheese.

#Finished making your pizza!.


requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']  
'''if the pizzeria runs out of 'green peppers'.'''
for requested_topping in requested_toppings :
	if requested_topping == 'green peppers' :
		print("Sorry, we are out of green peppers right now.")
	else:
		print("Adding " + requested_topping + ".")
		
print("\nFinished making your pizza!")
#Adding mushrooms.
#Sorry, we are out of green peppers right now.
#Adding extra cheese.

#Finished making your pizza!.



###Checking That a List Not Empty
requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + ".")
	print("Finished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")
#Are you sure you want a plain pizza?



