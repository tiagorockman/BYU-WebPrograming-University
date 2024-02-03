#I have added to the game an introduction instruction and a welcome
#I gave the opportunity to see the list of word.
#The word is chosen randomly

import random
#brief introduction and Welcome
print("###################################################")
print("####### Welcome to the word guessing game! ########")
print("###################################################")
print()
print("------------ Instructions -------------------------")
print("If the secret word is Mosiah")
print("You gess it is Moroni")
print("Your hint will be -  M O _ o _ i ")
print("* M and O are in uppercase because is in same position of MOsiah (first and second letter).\n* o and i are lowercase because they are in the secret word but in another position.\n"
      "* _ means that the word isn't present in the secret word.")
print("---------------------------------------------------")
print()

wordList =  [
    "Prophet",
    "Temples",
    "Scriptures",
    "Restoration",
    "Doctrine",
    "Faith",
    "Devotion",
    "Education",
    "Elder",
    "Zion",
    "BYU",
    "Spirituality",
    "Scholarship",
    "Brigham",
    "Family",
    "Testimony",
    "Priesthood",
    "Graduation",
    "Fasting",
    "Deseret"
]

choice = input("Do you want to see the bank of secret words? Yes - No. ")

if(choice.upper() == "YES"):
    print(wordList)
    
print()
#secret Word chosen randomly
secrect_word = random.choice(wordList).lower()


#print first hint
print("Your hint is: ", end="")
for hint in range(len(secrect_word)):
    print("_ ", end="")

print(f" ({len(secrect_word)}) letters.")
print()

not_guessed = True
guess_quantity = 0

#application core
while not_guessed:
    print()
    guess = input("What is your guess? ")
    guess_quantity = guess_quantity +1
    if(len(guess) != len(secrect_word)):
        print("Sorry, the guess must have the same number of letters as the secret word.")
    elif guess.lower() !=  secrect_word:
        print("Your hint is: ", end="")
        index = 0
        for letter in guess.lower():
           if(letter == secrect_word[index]):
               print(f"{letter.upper()} ", end="")
           elif letter in secrect_word:
               print(f"{letter} ", end="")
           else:
               print("_ ", end="")
           index +=1
    else:
        print("\nCongratulations! You guessed it!")
        print(f"It took {guess_quantity} guesses.")
        not_guessed = False
    print()
    
    
    

