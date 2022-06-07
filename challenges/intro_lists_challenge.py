#! /usr/bin/env python3

import random

wordbank= ["four", "spaces"]

# TLG student list
tlgstudents= ["Aaron", "Casey", "Donny", "Emmanuel", "Eric", "Jaelen", "James", "Jay", "John", "Ken", "Maurice", "Mike", "Ryan", "Shamain", "Tuang", "Tyler", "Zhenqian", "Travis"]

#input asking for a number between 0 and 17
#num=int( input("Please input a number between 0 and 17: \n"))


#use the integer num to slice one of the elements from the list tlgstudents below
#choose=int(input("Please choose a student number between 0 and 17: \n"))
choose=random.randint(0,17)
student_name= tlgstudents[choose]

#print <student name> always uses four <spaces> to indent.
print(f"{student_name} always uses four {wordbank[1]} to indent.")

