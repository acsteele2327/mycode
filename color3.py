#! /usr/bin/env python3
"""This code is for demonstrating the uses of the color module
        Aaron Steele -  """

import crayons

def main():
    """This function makes use of the crayons module"""
    print(crayons.magenta('Aaron is tired on this monday. Feelin kinda purple')) #coloring entire print line

    #Coloring with the variable and bold
    print('I am also feeling a little ' + crayons.blue('blue', bold=True))

    #using an f string to get multiple colors on a single line
    print(f"I am also a little {crayons.red('red')}, white and {crayons.blue('blue')} today!")

if __name__ == "__main__":
    main()

