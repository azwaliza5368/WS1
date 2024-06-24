import random

def main():
    """Start a number guessing game between 1 - 100"""
    print("Guess the number!")

    x = random.randint(1, 100)
    guess = None
    
    while x != guess:
        #try:
        guess = int(input("Pick a number between 1-100: "))
        #except ValueError:
            #print("Invalid input! Please enter a valid integer.")
            #continue
        
        if x == guess:
            print("You Genius!")
            #print("You guessed it right! The number was")
        elif x > guess:
            print("Try a bigger number.")
        else:
            print("Try a smaller number.")

    


main()