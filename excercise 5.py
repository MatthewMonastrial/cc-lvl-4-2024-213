# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 09:14:09 2024

@author: USER
"""

days = dict({
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
})#creates a dictionary for days

month = int(input("Enter the month number (1-12): "))#gets user input and saves it as a month

if 1 <= month <= 12:#checks if the number is withing 1-12 or not
    if month == 2:#checks if the user picked february which is 2 or not
        leap = input("Is it a leap year? (yes/no): ")#checks if the year is a leap year or not
        if leap == 'yes':
            print("February has 29 days.")#prints 29 days if it is a leap year or not
        else:
            print("February has 28 days.")#prints 28 days if not
    else:
        print("The month has " ,str(days[month]) + " days.")#prints the amount of days the month has from the dictionary
else:
    print("Invalid month number. Please enter a number between 1 and 12.")#prints an error message if the input is not within 1-12