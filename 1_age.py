'''
Ask the user their name and age
and tell them the year that they turn 100.
We call this function with age()
'''


from datetime import date
import time

def age_pep8(
    name = input("Please enter your name: "),     # Ask the user for their name.
    age = int(input("Please enter your age: ")),  # Ask the user for their age.
    year = int(str(date.today())[:-6])):          # Get the year from date.today() (Given as YYYY-MM-DD, [:-6] removes the '-MM-DD' to isolate YYYY).
    '''
    Print the user's name and age, and the year in which they turn 100.
    # This is calculated as the current year minus their age (Birth year), then add 100, giving the year they turn 100.
    '''

    try:
        print(f"{name}, you are {age} years old, and you turn 100 in the year {year - age + 100 }")
    except ValueError:
        print("Error! You entered your age incorrectly.")
    else:
        print("Something went wrong...\n", Exception)


#def age_oneliner(name = input("Please enter your name: "), age = int(input("Please enter your age: ")), year = int(str(date.today())[:-6])): print(f"{name}, you are {age} years old, and you turn 100 in the year {year - age + 100 }")

age_pep8()
time.sleep(5)
