word = "Commitment"
favorite_letter = input("What is your favorite letter? ")

for letter in word:
    if(letter.upper() == favorite_letter.upper()):
        print("_", end="")
    else:
        print(letter.lower(), end="")