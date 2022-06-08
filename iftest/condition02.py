#! /usr/bin/env python3

hostname=input("What value should we set for hostname?")

#using the str.lower method to return a lowercase string

if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    input()

    print("hostname matches expected config")
    #user is informed of matching config from input above

##Inform user that script is over
print("Exiting the script at this time..")
