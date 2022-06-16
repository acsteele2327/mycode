#! /usr/bin/env python3
""" ASCII Art Museum project by Aaron Steele | view a number of ascii art from an interface"""

#imports
import sys
import time
import threading
import os
import random

#import dictionary for ascii art
from wings import art

#print1by1 func for dramatic effect
def print1by1(text, delay=0.04):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)


#Help func will provide commands when called upon by help input also shown at the intro
def help():
    os.system('clear')
    print('''
===============================
    Commands:
      -------------------
      north or north wing
      west or west wing
      east or east wing
      south or south wing
      -------------------
      help or h
      quit or q  
===============================

''')
    input("Press enter to return\n>")



#gaze function runs to view the art for a limited time only, then returns to menu
def gaze():
    
    time.sleep(5.0)
    print1by1('Committing the piece\'s glory to memory... You look away with fleeting bliss... \n')
    time.sleep(1.5)
    os.system('clear') #will clear screen

S = threading.Timer(5.0, gaze) #5 seconds to look upon the lovely art

#Printing ascii function to display the bootiful arts lol
def print_ascii(fn):
    f=open(fn,'r')
    print(''.join([line for line in f]))

#Intro func will go here introducing the setting
def intro():
    os.system('clear') # start game with a fresh screen
    (print_ascii("entrance.txt")) #display picture of museum entrance
    input("Press enter to continue...\n>")


#leave func to exit program after user input
def leave():
    print("Are you sure you want to quit? Yes/No")
    quit_query = input('>')
    if quit_query.lower() in ['y', 'yes']:
            print("We hope you enjoyed your stay at the ASCII Museum!\nExiting...\n")
            sys.exit()
    else:
        pass


#Interface function
def menu_interface():
    print_ascii("hallway.txt") #ascii picture of museum hall
    print('''
 ====================================================
        Please enter the direction for the wing of 
        the museum you would like to enter:
        ---->  North Wing
        ---->  West Wing
        ---->  South Wing
        ---->  East Wing
 ====================================================
    
        ''')
        


def main():

    intro()

    while True:
        os.system('clear')
        menu_interface()
        main_input = input("\n>").lower()

        if main_input == "north" or main_input == "north wing":
            os.system('clear')
            print("Welcome to the North Wing")
            print1by1("As you peruse the lovely halls of the museum you turn your head and look upon an art piece that speaks to you on a molecular level")
            time.sleep(2.0)

            os.system('clear') # start game with a fresh screen
            print_ascii(art[0]["north"][random.randint(1,2)])
            gaze()
        
        elif main_input == "west" or main_input == "west wing":
            os.system('clear')
            print("Welcome to the West Wing")
            print1by1("As you peruse the lovely halls of the museum you turn your head and look upon an art piece that speaks to you on a molecular level")
            time.sleep(2.0)

            os.system('clear') # start game with a fresh screen
            print_ascii("chad.txt")
            gaze()

        elif main_input == "south" or main_input == "south wing":
            os.system('clear')
            print("Welcome to the South Wing")
            print1by1("As you peruse the lovely halls of the museum you turn your head and look upon an art piece that speaks to you on a molecular level")
            time.sleep(2.0)

            os.system('clear') # start game with a fresh screen
            print_ascii("dripgoku.txt")
            gaze()

        elif main_input == "east" or main_input == "east wing":
            os.system('clear')
            print("Welcome to the East Wing")
            print1by1("As you peruse the lovely halls of the museum you turn your head and look upon an art piece that speaks to you on a molecular level")
            time.sleep(2.0)

            os.system('clear') # start game with a fresh screen
            print_ascii(art[1]["east"][random.randint(1,2)])
            gaze()

        #quit feature using the leave func
        elif main_input == "quit" or main_input == "q":
            os.system('clear')
            leave()

        #help feature to display commands user can input
        elif main_input == "help" or main_input == "h":
            help()

        else:
            os.system('clear') # start game with a fresh screen
            print("Please enter a valid input")
            time.sleep(1.0)

        

if __name__ == "__main__":
    main()
