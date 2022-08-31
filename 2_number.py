'''
Ask the user for a number.

Check if the number is odd.
'''

import time

def user_number(num = int(input("Enter a number: ")),
    check = int(input("Enter another number: "))):
    '''
    Ask the user for a number. Check if the number is divisible by 2 or four, and if so tell the user.
    '''
    if not num % 4:     # If modulo operator returns 0, 4 is a factor of num.
        print("Your first number, ", num, " is divisible by 4 and 2.")
    elif not num % 2:   # If modulo operator returns 0, 2 is a factor of num.
        print("Your first number, ", num, "i s divisible by 2.")
    else:
        print("Your first number, ", num, " is not divisible by 4 or 2.")

    if not num % check: # If modulo operator returns 0, check is a factor of num.
        print("Your second number, ", check, ", divides evenly into ", num, ".")
    else:
        print("Your second number, ", check, ", does not divide evenly into ", num, ".")


user_number()
time.sleep(5)
