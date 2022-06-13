#! /usr/bin/env python3


#setting a default value for y if none is provided
def slappy(x, y="awesome"):
    print(f"{x} is {y}!")

#keyword arguments
#slappy(y="awesome", x="python")

#slappy("Python", "awesome")

#calculator functions examples
def add(x,y):
    total= x + y
    return total

def sub(x,y):
    total= x - y
    return total


#def main():
    print(add(10,5))
    print(sub(10,5))

def oddoreven(x):
    if x % 2 == 0:
        return True
    else:
        return False

def main():
    num= int(input("Choose a number and the below will signify if number is even: "))
    print(oddoreven(num))

##########################################################################

#divide function    
def divide(x,y):
    total = x / y
    return total

#testing divide calculator func
def test():

    x=int(input("Calculator: Input number\n>"))
    y=int(input("Calculator: Input number to divide by\n>"))
    print(f"Calculator: Result\n>{divide()}")

test()
