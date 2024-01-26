#I have added a easter egg in the First scenario when the option "NARROW" is chosen I gave a hint with the word capitalized
#on the text (Pool) the word pool is an option hided and if the player write pool he discover the ending hided.


#Scenario 1: The Mysterious Cave

print("You find yourself standing at the entrance of a mysterious cave.\n" 
      "The air is chilly, and the only sound is the faint dripping of water from inside.\n"
       "Two paths lead deeper into the cave. On your left is a dimly lit path, and on your right is\n" 
       "a path shrouded in darkness. Which path will you choose?")


scenario1_first = ""
scenario1_second = ""
scenario1_third = ""
while scenario1_first.upper() not in ("LEFT", "RIGHT"):   
    scenario1_first = input("\nGo LEFT into the dimly lit path. Go RIGHT into the path shrouded in darkness. ")

if scenario1_first.upper() == "LEFT":
    print("\nAs you proceed down the dimly lit path, you come across a fork in the cave.\n"
          "The left tunnel looks narrow and unstable, while the right tunnel seems wider and more well-traveled.\n"
           "Which path will you take?")
    while scenario1_second.upper() not in ("NARROW", "WIDE"):
         scenario1_second = input("\nTake the NARROW left tunnel. Take the WIDE right tunnel.")

    if scenario1_second.upper() == "NARROW":
        print("\n The narrow tunnel opens into a small cavern.\n"
                "In the center there is a Poll, you see a glittering treasure chest.\n"
                 "However, you also notice a mysterious shadow lurking in the corner. What will you do?")
          
        while scenario1_third.upper() not in ("OPEN", "INVESTIGATE", "POOL"):
         scenario1_third = input("\nOPEN the treasure chest. INVESTIGATE the mysterious shadow.")
       
        
        if scenario1_third.upper() == "OPEN":
            print("\nAs you open the chest, you find a valuable gem inside. Suddenly, \nthe mysterious shadow reveals itself to be a nonfriendly cave spirit, that burns the cave and you die inside the cave.")
        elif scenario1_third.upper == "INVESTIGATE":
            print("\nApproaching the mysterious shadow cautiously, \nyou discover it's a camouflaged entrance to a hidden chamber. \nInside, you find ancient inscriptions on the walls that tell the story of the cave's guardian spirit. Suddenly, the guardian spirit materializes before you and defeat you in a duel. ")
        else: #POOL
            print("\n Congratularions you discovered an easter egg.")
            print("\nYou jump at the pool...")
            print("\nAs you jumped at the pool, the real chest appears and you find a valuable gem inside. Suddenly, the mysterious shadow reveals itself to be a friendly cave spirit, pleased with your honesty. It guides you out of the cave safely.")
    else:
        print(" The dark path leads to a cavern filled with eerie sounds.\n"
               "You notice a faint glow in the distance. As you approach, you see a swarm of mystical fireflies\n"
                "surrounding an ancient, locked chest. What will you do?")
         
        while scenario1_second.upper() not in ("OPEN", "FOLLOW"):
         scenario1_second = input("\nOPEN the ancient chest. FOLLOW the fireflies..")

         if scenario1_second.upper() == "OPEN":
             print("Opening the ancient chest reveals a magical artifact that grants you the power to understand \n"
                   "the language of animals. Just then, you hear the distant an creature that flies with you and takes you out of the cavern.")
         else:
             print("As you follow the mystical fireflies, they lead you to a hidden chamber filled with ancient runes.\n"
                   "In the center of the chamber, you find an enchanted pedestal with a shimmering crystal. It falls in the floor causing \n"
                    "causing a huge tremor destroying all the cave with you inside.")

else:
    print("\nThe dark path leads to a cavern filled with eerie sounds.\n"
          "You notice a faint glow in the distance. As you approach, you see a swarm of mystical fireflies surrounding an ancient,\n"
           "locked chest. What will you do?")
    while scenario1_second.upper() not in ("OPEN", "FOLLOW"):
         scenario1_second = input("\nOPEN the ancient chest.FOLLOW the fireflies..")
    
    
    if scenario1_second.upper() == "OPEN":
        print(" Wait beeing developed")
    else:
        print(" Wait beeing developed")
          
        



