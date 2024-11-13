# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 09:14:49 2024

@author: USER
"""

Pass = "10101" #password is set to 10101
max_attempts = 5#the amount of attempts the player can use in the pass
attempts = 0#the amoount of attempts has been used

while attempts < max_attempts: #the code will keep running until attempts reaches max attempts
    Guess = input("Enter the password: ")#the guess of the user for the password
    
    if Guess == Pass: #checks if the guess is correct
        print("Access granted.")#prints
        break#breaks code
    else:
        attempts += 1#adds 1 to the amount of attempts
        remaining_attempts = max_attempts - attempts#remaining attempts is the max attempts- the attempts used
        if remaining_attempts > 0:#checks if the remaining attempts is higher than 0
            print("Incorrect password. You have",remaining_attempts,"attempts remaining.")#prints while the remaining attempts is higher than 0
        else:
            print("Maximum attempts reached. Authorities have been alerted.")#prints when remaining attempts reaches 0