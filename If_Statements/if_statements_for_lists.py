##page 91

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


###Using Multiple Lists
'''it covers all nonsense topping sutiation and compare with available toppings.'''
available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
'''this could be tuple if the pizzeria has a stable selection of toppins''' 
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, we don't have " + requested_topping + ".")		
print("\nFinished making your pizza!.")
#Adding mushrooms.
#Sorry, we don't have french fries.
#Adding extra cheese.

#Finished making your pizza!.

'''ALWAYS think about next step, like price of toppings and how much would it cost to customer'''
'''Maybe customer details to save print a message how much it would cost with option to home delivery or store collection'''
'''date: 11/01/2020 '''

###TRY IT YOURSELF Page93
##5.8 Hello Admin

'''it is in different file to make it easier for me to find check hello_admin.py'''
