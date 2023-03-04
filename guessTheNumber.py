from guessTheNumber_art import logo
import random

def guessTheNumber():
    cont = 'y'
    while(cont == 'y'):
        print(logo)
        print("Welcome to the number guessing game!!")
        print("I'm guessing of a number between 1 and 100.")
        difficulty = input("Choose a difficulty: 'easy' or 'hard' : ")
        number = random.randint(1,100)
        chances = 0
        if(difficulty == "hard"):
            chances = 5
        else:
            chances = 10
        while(chances>0):
            print(f"You have {chances} to guess the number")
            guess = int(input("Make a guess : "))
            if(guess == number):
                print(f"Amazing you have guessed the number, with {chances-1} chances left.")
                break
            elif(guess > number):
                print("Too high.")
            elif(guess < number):
                print("Too low.")
            chances-=1
            if(chances == 0):
                print("You have run out of guesses, You lose.")
                print(f"The answer is {number}")
            else:
                print("Guess again.")
        cont = input("Do you want to play again? 'y' or 'n': ")
guessTheNumber()
