import random

def main():
    number = random.randint(1, 100)
    guess = 0

    while guess != number:
        try:
            guess = int(input("Enter a number between 1-100 :"))

            if(guess > number):
                print("Too high")
            elif(guess < number):
                print("Too low")
            else:
                print("Congratulations! You have guessed it true.")
                break
        except ValueError:
            print("Please enter a number between 1-100")


main()
