# 4- Cleaning Up

try:
	file = open('app.py')	#opening a file called app.py
    age = int(input('Age:'))
    xfactor = 10/age
    # file.close() #wont be executed incase of any exceptions in the above code
except (ValueError, ZeroDivisionError):
	print('You did\'nt enter a valid age.')
	# file.close() #this block will be executed only incase of excecption

else:
	print('No exceptions were thrown.')
	# file.close() #this will not be executed in case of execption

finally:
	file.close() #finally block will executed on all times