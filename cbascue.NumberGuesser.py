#Guess the number course Project, Wk. 8, DeVry University, CIS115
#Codie Bascue
#10/24/19

#import random numbers
import random

def display_menu():
    print("1) Computer picks the random number and you try to guess")
    print("2) Computer tries to guess the number that you pick")
    print("3) End Program")
    print()

def main():
    #display title of program and welcome user
    print("Welcome to the Guess my Number Program! \n\n")
    while True:
        display_menu()
        choice = int(input("Which game would you like to play? "))
        if(choice == 1):
            user_guess()
        elif(choice == 2):
            comp_guess()
        else:
            print()
            #goodbye message
            print("Thank you for playing! Goodbye!")
            break

def user_guess():
    print()
    #set the range for the random number
    myNum = random.randint(1,10)
    #set number of tries
    count = 1
    userGuesses = []
    #create a loop where the program asks user for a number between 1-10, if the user is too high from the random number, display that, too low display that, guesses correct, display and end the loop.
    while True:
        #set a check for errors in input
        try:
            userGuess = int(input("Please guess a number between 1 and 10: "))
            while userGuess < 1 or userGuess > 10:
                print("Invalad entry")
                userGuess = int(input("Please guess a number between 1 and 10: "))
        except:
            print("Error, please enter only numbers!")
            continue
        userGuesses.append(userGuess)
        #set rules for results based on the user's guess
        if userGuess < myNum:
                print("Guess is too low, please try again!")
                count = count + 1
        elif userGuess > myNum:
                print("Guess is too high, please try again!")
                count = count + 1
        elif userGuess == myNum:
                print()
                print("You got it! Great job! You guessed it in " + str(count) + " attempts")
                print()
                print("You picked the following numbers: " + str(userGuesses))
                print()
                break

def comp_guess():
    #set up program to run game where computer tries to guess the user's number if the user chooses choice 2
    print()
    #Get the user's number that they want the computer to guess
    count = 1
    computerGuesses = []
    while True:
        try:
            userNum = int(input("Please enter the number you would like the computer to try and guess!: "))
            while userNum < 1 or userNum > 10:
                print("Invalad entry")
                userNum = int(input("Please enter the number you would like the computer to try and guess!: "))
        except:
            print("Error, please enter only numbers!")
            continue
        break

    minGuess = 1
    maxGuess = 10 
    while True:
        #set a check for errors in input
        #get random number between 1 and 10 from the computer
        compNum = random.randint(minGuess,maxGuess)
        computerGuesses.append(compNum)
        #set rules based on computer's guess and user's input
        if(compNum < userNum):
            print("The computer guessed ", compNum ," which is too low")
            minGuess = compNum + 1
            count = count + 1
        elif(compNum > userNum):
            print("The computer guessed ", compNum ," which is too high")
            maxGuess = compNum - 1
            count = count + 1
        elif(compNum == userNum):
            print()
            print("The computer guess ", compNum ," which was correct! The computer guessed it in ", count ," attempts.")
            print()
            print("The computer guessed the following numbers: " + str(computerGuesses))
            print()
            break


if __name__ == "__main__":
    main();
    
