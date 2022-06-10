#! /usr/bin/env python3

# write a script that read in the content of the Dracula novel as a file object

def part1():

    with open("dracula.txt", "r") as dracula:
        for lines in dracula:
            print(lines, end="")

def part2():

    #write a for loop that only prints out the line if it has the word vampire in it

    with open("dracula.txt", "r") as dracula:

        for lines in dracula:
            lines = lines.rstrip('\n') #remove newline char

            if "vampire" in lines:
                print(lines)

def part3():

    #make sure the lines with vampire print regardless of case sensitivity

    with open("dracula.txt", "r") as dracula:

        for lines in dracula:
            lines = lines.rstrip('\n') #remove newline char

            if "vampire" in lines.lower():
                print(lines)



def part4():

    #count how many times the word vampire comes up

    with open("dracula.txt", "r") as dracula:

        #adding count variable to tally up word count of vampire
        count = 0

        for lines in dracula:
            lines = lines.rstrip('\n') #remove newline char

            if "vampire" in lines.lower():
                count += 1
        print(count)

def part5():

    #take the lines from draculat.txt that have campire in it and write them to a second file named vampytimes.txt

    with open("dracula.txt", "r") as dracula:

        for lines in dracula:
            lines = lines.rstrip('\n') #remove newline char

            if "vampire" in lines.lower():
                
                #with loop to open and write file
                with open("vampytimes.txt", "a") as foo:

                    foo.write(lines + "\n")

#part5()

def new_func():

    with open("dracula.txt", "r") as foo:

        for line in foo:
            line = line.rstrip('\n') #removes newline char

            if "Dracula" in line:
                print(line)

                with open("vampytimes.txt", "a") as slippy:

                    slippy.write(line + "\n")

new_func()