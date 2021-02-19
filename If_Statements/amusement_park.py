##The if-elif-else Chain page84
age = 12

if age< 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $5.")
else:
	print("Your admission cost is $10.")
#Your admission cost is $5.


## instead using all elif conditions and omit last else condition
#you'll gain extra confidence that your code will run under the correct conditions.


###TRY IT YOURSELF Page 88
##5.3 Alien Colors#1
alien_color = 'Green'
if alien_color.lower() == 'green' :
	print("The player just earned 5 points.")
#The player just earned 5 points.

alien_color = 'YEllOW'
if alien_color.lower() == 'green' :
	print("The player just aearned 5 points.")
#no output

##5.4 Alien Colors#2
alien_color = 'Red'
if alien_color.lower() == 'green' :
	print("The player just earned 5 points for shooting the alien.")
else:
	print("The player just earned 10 point.")
#The player just earned 10 point.

##5.5 Alien Colors#3
alien_color = 'green'
if alien_color == 'green' :
	print("The player earned 5 points.")
elif alien_color == 'yellow' :
	print("The player earned 10 points.")
elif alien_color == 'red' :
	print("The player earned 15 points.")
#The player earned 5 points.

alien_color = 'yellow'
if alien_color == 'green' :
	print("The player earned 5 points.")
elif alien_color == 'yellow' :
	print("The player earned 10 points.")
elif alien_color == 'red' :
	print("The player earned 15 points.")
#The player earned 10 points.

alien_color = 'red'
if alien_color == 'green' :
	print("The player earned 5 points.")
elif alien_color == 'yellow' :
	print("The player earned 10 points.")
elif alien_color == 'red' :
	print("The player earned 15 points.")
#The player earned 15 points.

alien_color = 'pink'
if alien_color == 'green' :
	print("The player earned 5 points.")
elif alien_color == 'yellow' :
	print("The player earned 10 points.")
elif alien_color == 'red' :
	print("The player earned 15 points.")
# no output


##5.6 Stages of Life page 89  
age = 3
if age < 2 :
	print("The person is a baby")
elif age >= 2 and age < 4 :
	print("The person is toddler.")
elif age >=4 and age < 13 :
	print("The person is kid.")
elif age >= 13 and age < 20 :
	print("The person is teenager")
elif age >=20 and age < 65 :
	print("The person is adult")
elif age >=65 :
	print("The person is elder")
#The person is toddler.
## !!! Think about conditions are out of range like -10, 200 , letter or character your code doesnt catch errors


##5.7 Favorite Fruit
fav_fruits = ['peach', 'plum', 'watermelon', 'grapes']
fav_fruit = 'peach'
for fruit in fav_fruits:
	if fruit == 'peach' :
		print('Peach is your favorite fruit.')
#Peach is your favorite fruit.

fav_fruit = 'xxxx'
for fruit in fav_fruits:
	if fruit == 'xxxx' :
		print('Xxxx is your favorite fruit.')
#No output

##other way to write same code without 'for in' statement

fav_fruits = ['peach', 'plum', 'watermelon', 'grapes']
if 'peach' in fav_fruits:
		print('Peach is your favorite fruit.')
#Peach is your favorite fruit.



  




