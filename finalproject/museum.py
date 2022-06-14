#! /usr/bin/env python3
""" ASCII Art Museum project by Aaron Steele | view a number of ascii art from an interface"""

#imports
import sys
import time
import threading
import os

#print1by1 func for dramatic effect
def print1by1(text, delay=0.05):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

#Intro func will go here introducing the setting


#Help func will provide commands when called upon by help input also shown at the intro

#Map func should be consistently present when moving throughout (maybe more just a list of places to go next)

#clear screen func to clear each time the user moves to another room or out of a painting

def gaze():
    #function runs to view the art for a limited time only then return to menu
    time.sleep(5.0)
    print1by1('Committing the piece\'s glory to memory... You look away with fleeting bliss... \n')
    time.sleep(1.5)
    os.system('clear') #will clear screen

S = threading.Timer(5.0, gaze) #5 seconds to input or prints decision func

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
        Please enter the a number for the wing of the 
        museum you would like to enter:
        Enter 1 for ---->  North Wing
        Enter 2 for ---->  West Wing
        Enter 3 for ---->  South Wing
        Enter 4 for ---->  East Wing
        - - - - - - - - - - - - - - - - - - - - - - - - - -
    
        ''')
        


def main():

    while True:
        menu_interface()
        main_input = int(input("\n>"))

        if main_input == 1:
            print("Welcome to the North Wing")
            print1by1("As you peruse the lovely halls of the museum you turn your head and look upon an art piece that speaks to you on a molecular level")
            time.sleep(2.0)

            os.system('clear') # start game with a fresh screen
            print_ascii("feelsokayman.txt")
            gaze()
        continue


main()