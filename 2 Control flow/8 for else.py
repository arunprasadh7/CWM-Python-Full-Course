# for else

successful = False
for i in range(3):
    print('Attempt')
    if successful:
        break
else:
    print('Attempted thrice and failed to send the email.')
