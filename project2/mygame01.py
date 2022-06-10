#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

# Replace RPG starter project with this code when new instructions are live

#Imports
import time
import sys
import os
import threading
from random import randint
#importing gamecontent dictionaries from seperate file
from gamecontent import rooms

#3spooky5me print lol
def print1by1(text, delay=0.1):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    SPoopy Game: Don\'t get eaten by the scawy monstah
    ========
    Commands:
      go [direction]
      get [item]
      run
      help
      quit 
    ''')

def showStatus():
    """determine the current status of the player"""
    #print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")

def decision():
    #function runs to pressure player to input command or game over
    print1by1('You took too long to run...\nThe Dark Figure envelops you...\nYOU DIED\n')
    os._exit(os.EX_OK) #will force quit the program

S = threading.Timer(5.0, decision)


def escape():
    #random chance to escape if run command is input by player when in the boiler room with dark figure
    S.start() #starts the countdown timer to input the run command
    while True:
        print('You must escape!\n')
        move = ''
        while move == '':  
            move = input('>')
        move = move.lower().split(" ", 1)
        if move[0] == 'run': #
            S.cancel() #cancels the countdown timer after run command is input
            escape_chance= randint(1,10) #random int to determine if you will escape or not

            if escape_chance >= 5:
                print("You managed to leave before the Dark Figure enveloped you.\n")
                currentRoom = 'Hall'
                break

            if escape_chance < 5:
                print1by1('The Dark Figure envelops you and your existence fades away...\nYOU DIED\n')
                sys.exit()
            

#an inventory, which is initially empty
inventory = []


#start the player in the Hall
currentRoom = 'Hall'

os.system('clear') # start game with a fresh screen

showInstructions()

#loop forever
while True:
    if currentRoom == 'Hall':
        print(rooms['Hall']['desc'])
    showStatus()



    # If a player enters a room with the Dark Figure... game over
    if currentRoom == 'Boiler Room':
        escape()
       

    #get the player's next 'move'
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:
    #['go','east']
    move = ''
    while move == '':  
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    os.system('clear') # clear the screen
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
            #Provide description of current room
            if 'desc' in rooms[currentRoom]:
                print(rooms[currentRoom]['desc'])
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    if move[0] == 'run' and rooms[currentRoom] != 'Boiler Room':
        print('You can\'t run in here!')

    #if they type 'get' first
    if move[0] == 'get' :
        #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(f'You picked up the ' + move[1])
            #delete the item from the room
            del rooms[currentRoom]['item']
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')


    #Win conditions to complete game and break out of game script
    if currentRoom == 'Garden' and 'gate key' in inventory and 'telephone' in inventory:
        print('You unlocked the garden gate with the key you acquired...\nYou escaped the scary house using the gate key and telephone to call an uber out of there\nYOU WON\n')
        break

    #Lose conditions if you only have the gate key in inventory    
    if currentRoom == 'Garden' and 'gate key' in inventory and 'telephone' not in inventory:
        print('You unlocked the garden gate with the key you acquired...\nYou are stranded with no one to help you...\nThe Dark Figure appears behind you...\n')
        print1by1('The Dark Figure approaches you..\nYou hesitate..\n')
        print1by1('The Dark Figure envelops you and your existence fades away...\nYOU DIED\n')
        break

    #lose conditions if you only have the telephone in inventory
    if currentRoom == 'Garden' and 'gate key' not in inventory and 'telephone' in inventory:
        print('You approach the gate to exit the grounds but it is locked...\nYou use the telephone to call for help but no one can get through the locked gate...\nThe Dark Figure appears behind you...\n')
        print1by1('The Dark Figure approaches you..\nYou hesitate..\n')
        print1by1('The Dark Figure envelops you and your existence fades away...\nYOU DIED\n')
        break

    elif move[0] == 'help':
        showInstructions()

    elif move[0] in ['q', 'quit']:
        print("Are you sure you want to quit? Yes/No")
        quit_query = input('>')
        if quit_query.lower() in ['y', 'yes']:
            print("Thanks for playing!")
            sys.exit()
        else:
            pass