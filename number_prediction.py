import random

number =random.randint(1,100)
guess=0

while guess!=number:
    print("Please enter the number between 1-100 !")

    guess=int(input("Enter a number between 1-100 :"))

    if(guess > number):
        print("Too high")
    elif(guess<number):
        print("Too low")
    else:
        print("Congratulations! You have guessed it true.")
              
    
