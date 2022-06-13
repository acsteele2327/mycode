#! /usr/bin/env python3
""" ASCII Art Museum project by Aaron Steele | view a number of ascii art from an interface"""


#Intro func will go here introducing the setting


#Help func will provide commands when called upon by help input also shown at the intro

#Map func should be consistently present when moving throughout (maybe more just a list of places to go next)

#clear screen func to clear each time the user moves to another room or out of a painting

#Printing ascii function
def print_ascii(fn):
    f=open(fn,'r')
    print(''.join([line for line in f]))

#testing out print func
print_ascii('feelsokayman.txt')
print_ascii('uknow.txt')



#Interface function
#def interface():