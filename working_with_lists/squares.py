
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

## clean the code to write more concisely  reduce the line of code
##sometimes it can make more difficult to read you concentrate on what you want to do clearly first
squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


###Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,0]
min(digits)     ##use print at the front to get output
#0
max(digits)
#9
sum(digits)
#45



##List Comprehensions    
squares = [value**2 for value in range(1,11)]
print(squares)
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



###TRY IT YOURSELF Page64
##4.3 Counting to twenty
for number in range(1,21):
	print(number)
	

##4.4 One million
numbers_million = []
for number in range(1,1000001):
	numbers_million.append(number)
#print(numbers_million)

##4.5 Summing a Million
print(min(numbers_million))
#1
print(max(numbers_million))
#1000000
print(sum(numbers_million))
#500000500000


##Odd Numbers
odd_numbers = list(range(1,21,2))
print(odd_numbers)
#[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
for number in odd_numbers:
	print(number)      ##It ll print numbers in the list of odd_numbers to one by one under each other

##4.7 Threes 3, 6, 9, 12
multiples_3 = list(range(3,31,3))
for value in multiples_3:
	print(value)


##4.8 Cubes a**3

cube_of_numbers = []
for number in range(1,11):
	cube = number*number*number
	print(cube)
	cube_of_numbers.append(cube)
print(cube_of_numbers)
#[1, 8, ......., 1000.etc]

##or to print individually lets try to write code differently
cube_of_numbers = []
for number in range(1,11):
	cube = number*number*number
	cube_of_numbers.append(cube)
for cube in cube_of_numbers:
	print(cube)  #it ll print one under other one


##4.9 Cube Comprehension
cubes = [value**3 for value in range(1,11)]
print(cubes)
#[1, 8, ......., 1000.etc]







	


