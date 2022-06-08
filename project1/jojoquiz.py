#! /usr/bin/env python3


#import question bank from the questionbank.py file

from questionbank import quiz

def game():

    # Intro code to introduce quiz and rules as well as user input to continue
    print("Welcome to the JoJo quiz")
    input()
    print("For each question you will have 3 attempts")
    input()
    print("Press enter to continue")
    input()

    #check answer function to present question, answer, attempts and score
    def check_ans(question, answer, attempts, score):
        if quiz[question]['answer'].lower() == answer.lower(): #lower method to ensure user can input regardless of case sensitivity
            print(f"Your answer is correct! \n Your score is {score + 1}!")
            return True
        else:
            print(f"Sorry the answer you provided was incorrect.. :( \n You have {attempts - 1} attempts left. \n Please try another answer...")
            return False

    while True:
        score = 0
        for question in quiz:
            attempts = 3
            while attempts > 0:
                print(quiz[question]['question'])
                answer = input("Please enter your answer: \n")

                check = check_ans(question, answer, attempts, score)
                if check:
                    score += 1
                    break
                attempts -= 1
        break


    # Present score to user

    print(f"Your final score is {score} out of 4! \n Press enter to continue")
    input()

def main():
    while True:
        game()
        play_again= input("would you like to play again, Y/N?")
        if play_again.lower() == "n":
            break
        elif play_again.lower() == "y":
            print("Restarting Quiz...")
        else:
            print("Please type Y/N?")

main()
