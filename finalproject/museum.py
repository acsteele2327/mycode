#! /usr/bin/env python3
""" ASCII Art Museum project by Aaron Steele | view a number of ascii art from an interface"""

#imports
import sys
import time
import threading
import os

#print1by1 func for dramatic effect
def print1by1(text, delay=0.04):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

#Intro func will go here introducing the setting
def intro():
    os.system('clear') # start game with a fresh screen


#Help func will provide commands when called upon by help input also shown at the intro
#def help():
    



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

#testing out print func
#print_ascii('feelsokayman.txt')
#print_ascii('uknow.txt')



#Interface function
def menu_interface():
     print('''
        ====================================================
        Please enter the direction for the wing of the 
        museum you would like to enter:
        ---->  North Wing
        ---->  West Wing
        ---->  South Wing
        ---->  East Wing
        ====================================================
    
        ''')
        


def main():

    intro()

    while True:
        menu_interface()
        main_input = input("\n>").lower()

        if main_input == "north" or main_input == "north wing":
            print("Welcome to the North Wing")
            print1by1("As you peruse the lovely halls of the museum you turn your head and look upon an art piece that speaks to you on a molecular level")
            time.sleep(2.0)

            os.system('clear') # start game with a fresh screen
            print_ascii("feelsokayman.txt")
            gaze()
        
        elif main_input == "west" or main_input == "west wing":
            print("Welcome to the West Wing")
            print1by1("As you peruse the lovely halls of the museum you turn your head and look upon an art piece that speaks to you on a molecular level")
            time.sleep(2.0)

            os.system('clear') # start game with a fresh screen
            print_ascii("chad.txt")
            gaze()

        elif main_input == "south" or main == "south wing":
            print("Welcome to the South Wing")
            print1by1("As you peruse the lovely halls of the museum you turn your head and look upon an art piece that speaks to you on a molecular level")
            time.sleep(2.0)

            os.system('clear') # start game with a fresh screen
            print_ascii("dripgoku.txt")
            gaze()

        elif main_input == "east" or main_input == "east wing":
            print("Welcome to the East Wing")
            print1by1("As you peruse the lovely halls of the museum you turn your head and look upon an art piece that speaks to you on a molecular level")
            time.sleep(2.0)

            os.system('clear') # start game with a fresh screen
            print_ascii("gotem.txt")
            gaze()

        

if __name__ == "__main__":
    main()
