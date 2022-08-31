'''
The user enters three numbers, and the program finds which is the largest.
'''

import time

def three_numbers():
    '''
    Ask user for three numbers, and return the largest they enter.
    '''
    biggest_number = 0

    for i in range(3):
        number = int(input("Enter a number: "))
        if number > biggest_number:
            biggest_number = number
    return biggest_number

print("The biggest number you entered was: ", three_numbers())
time.sleep(5)
