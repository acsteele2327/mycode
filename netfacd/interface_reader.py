#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
    try:
        print('\n********Details of Interface - ' + i + ' ************')
        print('MAC: ', end='') 
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
        print('IP: ', end='') 
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address

    except:
        print('Could not collect adapter information')  #Prints error message if unable to output try

