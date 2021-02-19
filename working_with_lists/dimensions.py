
##Defining a Tuple ()
#tuples value doesnt change

dimensions = (200, 50)
print(dimensions[0])
#200
print(dimensions[1])
#50
# dimensions[0] = 20  ## we cant change dimensions/tuple it gives error

###Looping Through All Values in a Tuple
dimensions = (200,50)
for dimension in dimensions:
	print(dimension)
#200
#50

###Writin over a Tuple # see tuple as one variable and change together
dimensions = (400, 100)
print(dimensions)
#(400, 100)
for dimension in dimensions:
	print(dimension)
#400
#100


###TRY IT YOURSELF Page71
##4.13 Buffet
buffet_food = ('pasta', 'pizza', 'carrot cake', 'noodles', 'drinks')
for food in buffet_food:
	print(food.title())


# buffet_food[0] = 'cant change the tuple you need to change whole tuple'

####couldnt solve this one

buffet_food = ('pasta', 'pizza', 'carrot cake', 'noodles', 'drinks')  ## try to add 2 more food to a tuple by writing a code
buffet_food_2 = []
for food in buffet_food:
	buffet_food_2.append(food)
buffet_food_2.append('wine')   ####i have created new list instead of tuple with 2more items. this is not what they are exactly asking
buffet_food_2.append('shrimps')
print(buffet_food_2)






