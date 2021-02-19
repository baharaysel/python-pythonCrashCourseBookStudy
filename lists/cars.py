
###Sort permanently sort()
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
#['audi', 'bmw', 'subaru', 'toyota']  # we can never revert to the original order

###Reverse sort
cars.sort(reverse=True)
print(cars)
#['toyota', 'subaru', 'bmw', 'audi']

###Sorting a list temporiraly with the sorted() function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
#['audi', 'bmw', 'subaru', 'toyota']
print("\nHere is the original list again:") 
print(cars)
#['bmw', 'audi', 'toyota', 'subaru'] ## back to original list

## printin in reverse order permanently
cars.reverse()
print(cars)
#['subaru', 'toyota', 'audi', 'bmw']  ## it reverse permanetly but you can revert to original

## Finding the length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
#4



##TRY IT YOURSELF page 50
#3.8 seeing the world
places_to_visit = ['dublin', 'switzerland', 'Cuba', 'malaysia', 'india', 'chinA'] 
print(places_to_visit)
#BE AWARE capital create problem in sorted order and sorted function sort temporarily
print(sorted(places_to_visit))
#['Cuba', 'chinA', 'dublin', 'india', 'malaysia', 'switzerland']
print(sorted(places_to_visit, reverse=True))
#['switzerland', 'malaysia', 'india', 'dublin', 'chinA', 'Cuba']
print(places_to_visit) ## checking if list is still original order


places_to_visit.reverse()  # it changes permanently
print(places_to_visit)

places_to_visit.reverse() #reverse again to original list
print(places_to_visit)

places_to_visit.sort()    # it change list permanently in alhabetically order
print(places_to_visit)

places_to_visit.sort(reverse=True)
print(places_to_visit)

###Dinner guests 3.9 page50
guest_list = ['Esra', 'aYse', 'Mehmet', 'Birsel', 'Nur', 'Burcin', 'Deniz', 'Figen']
print(str(len(guest_list)) + " guests are invited to my dinner party.")
#8 guests are invited to my dinner party.

###every function 3.10 page50
#i think list inside list what they are asking
house1 = ['3bedroom', '2 bathrooms', 'open plan', '£1850']
house2 = ['2bedroom', '2bathroom', 'seperate living room', '£1450']
house3 = ['studio', '1bathroom', '£950']
every_function = [house1,house2,house3]
print(every_function)
type_of_treatment = [['eye_surgery','liposuction'],['hair impplant', 'penis enlargement']]
print(type_of_treatment)




