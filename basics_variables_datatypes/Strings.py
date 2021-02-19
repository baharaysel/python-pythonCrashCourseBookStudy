
"This is a string."
'This is also string.'
'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monthy Python, not the snake."
"One of th Python's strengths is its diverse and supportive community."

# Changing a  Case in a String with Methods

name = "ada lovelace"
print(name.title()) # capitilaze the string 'A' Aand 'L'  
#Ada Lovelace
print(name)
#ada lovelace
# it is very useful as we want to our programme to recognise input values Ada, ADA, and ada as the same name and display all of them as Ada.

name = "Ada lovelace"
print(name.upper())
print(name.lower())

# Many times you won't want to trust the capitalization that your users provide, so you'll convert strings to lowercase before stroing them
#then use it as you need and capitilaze



# COMBINING OR CONCATENATING STRINGS

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " +last_name
print("Full name=" + full_name)

print("Hello, " + full_name.title() + "!") # this is cool 
#Hello, Ada Lovelace!

message = "Hello, " + full_name.title() + "!"
print(message)



 



