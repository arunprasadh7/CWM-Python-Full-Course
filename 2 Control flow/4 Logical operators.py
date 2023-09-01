# Logical operators - and, or, not

#and 

high_income = True
good_credit = True

if high_income and good_credit:
    print('Eligible for loan.')
else:
    print('Not eligible for loan.')

# or

income = True
credit = False

if income or credit:
    print('Eligible for loan at higher intrest rates.')
else:
    print('Not eligible.')

# not

student = True

if not student:
    print('Eligible for loan.')
else:
    print('Not eligible.')


#method4

high_income = False
good_credit = True
student = False

if not student and (high_income or good_credit):
    print('Eligible')
else:
    print('Not eligible.')