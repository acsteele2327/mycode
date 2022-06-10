#! /usr/bin/env python3

#Looping with for Challenge

#farms list to use with for loop
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

farmsinputindex = {
        "NE Farm": ["sheep","cows","pigs","chickens", "llamas", "cats"],
        "W Farm": ["pigs", "chickens", "llamas"],
        "SE Farm": ["chickens", "carrots", "celery"]}

def farmNE():

    #for loop that returns all the animals from the NE Farm
    for farm in farms:
        print(f"All the animals in the NE Farm are:\n {farms[0]['agriculture']}")

def farm_input1():

#farm_input1 returns plants/animals raised depending on user input on which farm

    for farm in farms:
        print("o  ", farm["name"])
    choice=input("Input NE Farm, W Farm or SE Farm: \n")

    print("The plants/animals raised at this farm are: \n", farmsinputindex[choice])

def farm_input2():

    #farm_input3 returns only the animals raised at the user input farm

    for farm

#WAS NOT ABLE TO FINISH also I think I fucked up majorly and just hard coded like an idiot
