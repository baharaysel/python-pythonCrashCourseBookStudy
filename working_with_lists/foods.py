
## Copying a List using slice [:]
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]   # this way we create 2 different list instead friend_foods = my_foods

#print("My favorite foods are: " + my_foods) #it doesnt work as list is not a string
print("My favorite foods are:")
print(my_foods)
#My favorite foods are:
#['pizza', 'falafel', 'carrot cake']

print("\nMy friend's favorite foods are:")
print(friend_foods)
#My friend's favorite foods are:
#['pizza', 'falafel', 'carrot cake']

my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)


###TRY IT YOURSELF page 69
##4.10 Slices
clothes = ['jumpers', 'jeans', 'tshirts', 'dresses', 'skirts', 'coats']
print("The first three items in the list are:")
#"The first three items in the list are:
print(clothes[0:3])
#['jumpers', 'jeans', 'tshirts']


print(len(clothes)) # trying to find 3 middle items
#6
print(clothes[2:5])
#['tshirts', 'dresses', 'skirts']


print(clothes[-3:])  #last 3 items in the list
#['dresses', 'skirts', 'coats']



##4.11 My Pizzas, Your Pizzas
pizzas = ['margarita', 'seafood', 'hawaian']
friend_pizzas = pizzas[:]
pizzas.append('pepperoni')
friend_pizzas.append('chicken')
print(pizzas)
#['margarita', 'seafood', 'hawaian', 'pepperoni']
print(friend_pizzas)
#['margarita', 'seafood', 'hawaian', 'chicken']

# or prove through a for loop
print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza.title())
#My favorite pizzas are:
#['margarita', 'seafood', 'hawaian', 'pepperoni']

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza.title())
#My friend's favorite pizzas are:
#['margarita', 'seafood', 'hawaian', 'chicken']


##4.12 More Loops











