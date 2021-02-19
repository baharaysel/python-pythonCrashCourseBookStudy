 
 ## Adding Whitesoace to Strings with Tabs or Newlines##
 
print("Python")
#Python 
print("\tPython")
#	Python

## Adding Newline in a string
print("Languages:\nPython\nC\nJavaScript")
#Languages:
#Python
#C
#JavaScript

## Combininig tabs and newlines in a single string##
print("Languages:\n\tPython\n\tC\n\tJavaScript")
#Languages:
	#Python
	#C
	#JavaScript
	
	
## Stripping Whitespace temporarily( Mostly used to clean up user input before it's stored in a program.
favorite_language = 'python '
#' python '
favorite_language = favorite_language.rstrip() #rightspace strip
#'python '
favorite_language,lstrip()	                   #leftspace strip
#'python '
favorite_language.strip()                      #strip completely 
#'python'


