###TRY IT YOURSELF Page93
##5.8 Hello Admin
user_names = ['admin', 'ayesha', 'deniz', 'aysel.isik1983', 'baharaysel', 'Baharaysel', 'BAHARAYSEL']
for user_name in user_names:
	if user_name == 'admin':
		print("Hello admin, would you like to see a status report?")
	else:
		print("Hello " + user_name + ", thank you for logging in again.")
'''it brings all users and message'''

##5.9 No Users 
'''test make sure list is not empty'''
user_names =[]
if user_names:
	for user_name in user_names:
		if user_name == 'admin' :
			print("Hello admin, would you like to see a status report?")
		else:
			print("Hello " + user_name + ", thank you for logging in again.")	
else:
	print("We need to find some users!")
#We need to find some users!
'''because our user_names list is empty we get this result.'''

##5.10. Checking Usernames
'''Check everybody has a unique name'''
current_names = ['admin', 'ayesha', 'deniz', 'aysel.isik1983', 'baharaysel']
new_user_names = ['Baharaysel', 'BAHARAYSEL','ayesha.1', 'admin', 'dEniz']
for new_user_name in new_user_names:
	if new_user_name in current_names:
		print("Enter new username")
	else:
		print("User name " + new_user_name + " available.")


current_names = ['admin', 'ayesha', 'deniz', 'aysel.isik1983', 'baharaysel']
new_user_names = ['Baharaysel', 'BAHARAYSEL','ayesha.1', 'admin', 'dEniz']

for new_user_name in new_user_names:
	new_user_name = new_user_name.lower()
	if new_user_name in current_names:
		print("Enter new username")
	else:
		print("User name " + new_user_name + " available.")
	


