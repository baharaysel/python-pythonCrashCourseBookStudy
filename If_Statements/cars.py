
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
#Audi
#BMW
#Subaru
#Toyota

car = 'bmw'
car == 'bmw'
#True
car = 'audi'
car == 'bmw'
#False

##Case sensitivity for checking equality
car = 'Audi'
car == 'audi'
#False

car = 'Audi'
car.lower() == 'audi'
#True

