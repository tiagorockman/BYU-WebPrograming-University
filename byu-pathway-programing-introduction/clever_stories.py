#Something I have add to the program was \t it centralizes the information like a Title
#I also use " to break line in the code source but it doesn't reflect in the output

#Requesting information
print("\tPlease enter the following:\n\n")

adjective = input("Adjective: ")
animal = input("Animal: ")
verb = input("Verb: ")
exclamation = input("Exclamation: ")
second_verb = input("Verb: ")
third_verb = input("Verb: ")

print("Your story is:\n\n")

print(f"The other day, I was really in trouble. It all started when I saw a very \n{adjective} {animal} {verb} down the hallway."
        f"\"{exclamation.capitalize()}!\" I yelled. But all \nI could think to do was to {second_verb} over and over. Miraculously,\n"
        f"that caused it to stop, but not before it tried to {third_verb}\nright in front of my family.")
