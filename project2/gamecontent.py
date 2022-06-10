#! /usr/bin/env python3
 
#a dictionary linking a room to other rooms
# Import this file to mygame01.py

rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'north' : 'Boiler Room',
                  'desc'  : 'You appear to be in a cramped hall. The walls stand decrepit with exposed framework signifying a time long past.\nYou feel uneasy as if there is another presence lurking in the shadows.\nTo your south you see the doorway to what looks like a kitchen.\nTo the north is a shut door with an ominous energy.\nTo the east is another door half open...\n'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'gate key',
                  'desc'  : 'You arrive in the kitchen.\nThe sink is filled with dismembered body parts and the stench fills your being with dread.\nYou notice a key clutched in one of the rotting hands toppled in the sink\nThere are no other exits than the doorway you entered through\n'
                },
            'Dining Room' : {
                  'west'  : 'Hall',
                  'south' : 'Garden',
                  'item'  : 'telephone',
                  'desc'  : 'You arrive in a grand dining room.\nMultiple plates lay strewn across the great table and on them body parts, both human and unknown.\nOn the mantle you spot a telephone, the faint glow of its\'s screen catching your eye.\nTo the west is a half open door\nto the south is a glass entryway that appears to lead to a Garden.\n'
                },
            'Garden' : {
                  'north' : 'Dining Room',
                  'desc'  : 'You step out into the night, the area opening up to a large garden lined with an iron fence.\nThe walls appear to be inescapable but behind the overgrown shrubbery is a gate.\nShaking the handle you notice a bolt requiring some kind of key\nThe only other exit is the glass doorway from which you entered the garden.\n'
                },
            'Boiler Room' : {
                  'south' : 'Hall',
                  'item'  : 'Dark Figure',
                  'desc'  : 'You slowly open the door to a pitch black room.\n You hear the constant sound of the machinery dulling out your senses but your chest feels heavy.\n There is a presence in this room\nYou can only make out a figure in the darkness.\nThe darkness masks any other exits than the door you came through.\n'
            }

         }