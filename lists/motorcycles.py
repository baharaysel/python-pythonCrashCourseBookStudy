
## Changing / adding to list  append insert del  pop()

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
#['honda', 'yamaha', 'suzuki']

motorcycles[0] = 'ducati'
print(motorcycles)
#['ducati', 'yamaha', 'suzuki']

motorcycles.append('honda')
print(motorcycles)
#['ducati', 'yamaha', 'suzuki', 'honda']


motorcycles = []  # it is good to start with empty list then we can add or as users can fill the list or dpend on the purpose

print(motorcycles)
#[]
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
#['honda', 'yamaha', 'suzuki']



## inserting
motorcycles.insert(0, 'ducati')
print(motorcycles)
['ducati', 'honda', 'yamaha', 'suzuki']


## removing using del
del motorcycles[0]
print(motorcycles)
#['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)
#['honda', 'suzuki']



##removing using a pop() method   (it removes last item on the list and store it)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
#['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)
#['honda', 'yamaha']
print(popped_motorcycle)
#suzuki


motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")
#The last motorcycle I have owned was a Suzuki.
print(motorcycles)
#['honda', 'yamaha']


##Popping Items from any Position in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was ' + first_owned.title() + '.')
#The first motorcycle I owned was Honda.



##Removing an Item by Value   ####it removes only first occurrence
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)
#['honda', 'yamaha', 'suzuki']


##TRY IT YOURSELF page 46
guest_list = ['aYse', 'Halil', 'Birsel', 'Nur', 'Burcin']
print("I would like to invite " + guest_list[0].title() + " to New Year Party")
#I would like to invite Ayse to New Year Party

#Halil cant come to party change Halil to Mehmet
guest_list[1]= 'Mehmet'
print(guest_list)
#['aYse', 'Mehmet', 'Birsel', 'Nur', 'Burcin']


#add more guests page46
print(guest_list)
#['aYse', 'Mehmet', 'Birsel', 'Nur', 'Burcin']
guest_list.insert(0,'Esra')
print(guest_list)
#['Esra', 'aYse', 'Mehmet', 'Birsel', 'Nur', 'Burcin']

guest_list.insert(-1,'Deniz')
print(guest_list)
##['Esra', 'aYse', 'Mehmet', 'Birsel', 'Nur', 'Burcin', 'Deniz']
guest_list.append('Figen')
print(guest_list)
#['Esra', 'aYse', 'Mehmet', 'Birsel', 'Nur', 'Burcin', 'Deniz', 'Figen']


##shrinking guest list  page46
guest_list = ['Esra', 'aYse', 'Mehmet', 'Birsel', 'Nur', 'Burcin', 'Deniz', 'Figen']
print(len(guest_list))
#8
print(guest_list)    ### guest_list.pop works even inside print function first:)
print("Dear " + guest_list.pop() + "\nI don't want to see you in my dinner party! \nFuck off!")
print("Dear " + guest_list.pop() + "\nI don't want to see you in my dinner party! \nFuck off!")
print("Dear " + guest_list.pop() + "\nI don't want to see you in my dinner party! \nFuck off!")
print("Dear " + guest_list.pop() + "\nI don't want to see you in my dinner party! \nFuck off!")
print("Dear " + guest_list.pop() + "\nI don't want to see you in my dinner party! \nFuck off!")
print("Dear " + guest_list.pop() + "\nI don't want to see you in my dinner party! \nFuck off!")
print(guest_list)
#['Esra', 'aYse']
print("Dear " + guest_list[0] + "\nYou are invited to my awesome party.")
print("Dear " + guest_list[1].title() + "\nYou are invited to my awesome party.")







