# 5- The With Statement
# when an object supports __enter__, __exit__ the object supports content management protocol
# with statement can be used for objects with content management protocol

try:
	with open('app.py')	as file: #while using with file.close() is executed automatically
		print('file opened')
    age = int(input('Age:'))
    xfactor = 10/age
    
except (ValueError, ZeroDivisionError):
	print('You did\'nt enter a valid age.')
	

else:
	print('No exceptions were thrown.')
	

# finally:
# 	file.close() #finally block will executed on all times