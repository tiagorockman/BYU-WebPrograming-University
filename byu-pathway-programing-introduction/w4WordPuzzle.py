

word = "mosiah"

print("Welcome to the word guessing game!")
print()

print("Your hint is: ", end="")
for hint in range(len(word)):
    print("_ ", end="")

print()

not_guessed = True
guess_quantity = 0
while not_guessed:
    print()
    guess = input("What is your guess? ")
    guess_quantity = guess_quantity +1
    if(len(guess) != len(word)):
        print("Sorry, the guess must have the same number of letters as the secret word.")
    elif guess.lower() !=  word:
        print("Your guess was not correct.")
    else:
        print("Congratulations! You guessed it!")
        print(f"It took {guess_quantity} guesses.")
        not_guessed = False
    print()
    
    
    

