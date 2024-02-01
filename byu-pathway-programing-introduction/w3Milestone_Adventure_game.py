#I have added a easter egg in the First scenario when the option "NARROW" is chosen I gave a hint with the word Upper
#on the text (Pool) the word pool is an option hided and if the player write pool he discover the ending hided.
#I have used while to control the user input that needs to be iqual the value expected.
#I showed it to my son and he played some scenarios and found some bugs that I could correct.

#Scenario 1: The Mysterious Cave

print("\n\n\t\tYou find yourself standing at the entrance of a mysterious cave.\n" 
      "\t\tThe air is chilly, and the only sound is the faint dripping of water from inside.\n"
       "\t\tTwo paths lead deeper into the cave. On your left is a dimly lit path, and on your right is\n" 
       "\t\ta path shrouded in darkness. Which path will you choose?")


scenario1_first = ""
scenario1_second = ""
scenario1_third = ""
scenario1_fourth = ""
ignoreWay = ("\n\t\tIgnoring the pleas of the trapped mythical creature, you decide to press on with your exploration of the cave. \n" 
            "\t\tAs you venture deeper, the path becomes treacherous, and eerie sounds surround you. Suddenly, you find yourself face to face with a hostile guardian,\n"
            "\t\ta formidable creature protecting the cave's inner sanctum.\n\n"
            "\t\tWithout the aid of the mythical creature you abandoned, the guardian sees you as a threat. \n"
            "\t\tDespite your attempts to defend yourself, the guardian proves too powerful. \n"
            "\t\tThe last thing you see is the glint of its menacing eyes before succumbing to the darkness.\n\n"
            "\t\tYour journey ends here. The cave keeps its secrets, and your story becomes another tale lost in its mysterious depths.\n")

while scenario1_first.upper() not in ("LEFT", "RIGHT"):   
    scenario1_first = input("\n\t\tGo LEFT into the dimly lit path. Go RIGHT into the path shrouded in darkness. ")

if scenario1_first.upper() == "LEFT":
    print("\n\t\tAs you proceed down the dimly lit path, you come across a fork in the cave.\n"
          "\t\tThe left tunnel looks narrow and unstable, while the right tunnel seems wider and more well-traveled.\n"
           "\t\tWhich path will you take?")
    while scenario1_second.upper() not in ("NARROW", "WIDE"):
         scenario1_second = input("\n\t\tTake the NARROW left tunnel. Take the WIDE right tunnel. ")

    if scenario1_second.upper() == "NARROW":
        print("\n\t\tThe narrow tunnel opens into a small cavern.\n"
                "\t\tIn the center there is a POOL, you see a glittering treasure chest.\n"
                 "\t\tHowever, you also notice a mysterious shadow lurking in the corner. What will you do?")
          
        while scenario1_third.upper() not in ("OPEN", "INVESTIGATE", "POOL"):
         scenario1_third = input("\n\t\tOPEN the treasure chest. INVESTIGATE the mysterious shadow. ")
       
        if scenario1_third.upper() == "OPEN":
            print("\n\t\tAs you open the chest, you find a valuable gem inside. Suddenly, \n"
                  "\t\tthe mysterious shadow reveals itself to be a nonfriendly cave spirit,\n"
                  "\t\tthat burns the cave and you die inside the cave.\n\t\tTHE END\n")
        elif scenario1_third.upper() == "INVESTIGATE":
            print("\n\t\tApproaching the mysterious shadow cautiously, \n"
                  "\t\tyou discover it's a camouflaged entrance to a hidden chamber. \n"
                  "\t\tInside, you find ancient inscriptions on the walls that tell the story of the cave's guardian spirit.\n"
                   "\t\tSuddenly, the guardian spirit materializes before you and defeat you in a duel.\n\t\tTHE END\n")
        else: #POOL
            print("\n\t\tCongratularions you discovered an easter egg.")
            print("\n\t\tYou jump at the pool...")
            print("\n\t\tAs you jumped at the pool, the real chest appears and you find a valuable gem inside.\n"
                  "\t\tSuddenly, the mysterious shadow reveals itself to be a friendly cave spirit, pleased with your honesty.\n"
                   "\t\tIt guides you out of the cave safely.\n\t\tTHE END\n")
    else: #WIDE
        print("\n\t\tThe dark path leads to a cavern filled with eerie sounds.\n"
               "\t\tYou notice a faint glow in the distance. As you approach, you see a swarm of mystical fireflies\n"
                "\t\tsurrounding an ancient, locked chest. What will you do?\n\t\tTHE END\n")
         
        while scenario1_second.upper() not in ("OPEN", "FOLLOW"):
         scenario1_second = input("\n\t\tOPEN the ancient chest. FOLLOW the fireflies.. ")

         if scenario1_second.upper() == "OPEN":
             print("\n\t\tOpening the ancient chest reveals a magical artifact that grants you the power to understand \n"
                   "\t\tthe language of animals. Just then, you hear the distant an creature that flies with you and takes you out of the cavern.\t\tTHE END\n")
         else: #FOLLOW
             print("\n\t\tAs you follow the mystical fireflies, they lead you to a hidden chamber filled with ancient runes.\n"
                   "\t\tIn the center of the chamber, you find an enchanted pedestal with a shimmering crystal. It falls in the floor causing \n"
                    "\t\tcausing a huge tremor destroying all the cave with you inside.\t\tTHE END\n")

else: #RIGHT
    print("\n\t\tThe dark path leads to a cavern filled with eerie sounds.\n"
          "\t\tYou notice a faint glow in the distance. As you approach, you see a swarm of mystical fireflies surrounding an ancient,\n"
           "\t\tlocked chest. What will you do?")
    while scenario1_second.upper() not in ("OPEN", "FOLLOW", "GO BACK"):
         scenario1_second = input("\n\t\tOPEN the ancient chest. Try to GO BACK to entrance or FOLLOW the fireflies..  ")
    
    if scenario1_second.upper() == "OPEN":
        print("\n\t\tOpening the ancient chest reveals a magical artifact that grants you the power to understand the language of animals.\n"
              "\t\tJust then, you hear the distant cries of a creature in distress. Will you FOLLOW the cries or IGNORE them and continue exploring?")
        
        while scenario1_third.upper() not in ("FOLLOW", "IGNORE", ):
         scenario1_third = input("\n\t\tFOLLOW the cries. IGNORE the cries and continue exploring. ")

        if scenario1_third.upper() == "FOLLOW":
             print("\n\t\tFollowing the cries leads you to a trapped mythical creature.\n"
                   "\t\tWith your newfound ability to understand its language, it requests your help to break free.\n"
                    "\t\tWill you HELP the creature, or LEAVE it and explore further?")
             
             while scenario1_fourth.upper() not in ("HELP", "LEAVE", ):
                   scenario1_fourth = input("\n\t\tHELP the creature. LEAVE the creature and explore further.. ")

             if scenario1_fourth.upper() == "HELP":
                   print("\n\t\tFollowing your instinct you try to help the dragon.\n"
                   "\t\tFastly you aproach to the dragon and free the dragon from the chains.\n"
                    "\t\tThe dragon is free and grateful but it cant go against its nature. And try to attack you.\n"
                    "\t\tAs you can talk with it, He is amazed with that and begins to serve you, and now you have a great power and one of the biggest allies you could never have imagined.\n\t\tTHE END\n")
                        
             else:#LEAVE
                 print(ignoreWay)
        else: #IGNORE
            print(ignoreWay)
    
    elif scenario1_second.upper() == "FOLLOW":

              print("\n\t\tYou have ignored a great power, but followed the creature cries, you found a mistic creature a Shadow Dragon.\n"
              "\t\tHe is a powerful dragon but he is suffering and you know how to help, you have a potion with you.\n"
              "\t\tBut you don't know what will be the Dragon reaction. What Will be your choice LEAVE the room or HELP the Dragon?")
              
              while scenario1_third.upper() not in ("LEAVE", "HELP"):
                  scenario1_third = input("\n\t\tHELP the Dragon. LEAVE the room. ")
                  
                  
              if scenario1_third.upper() == "HELP":
                   print("\n\t\tFollowing your instinct you try to help the dragon.\n"
                   "\t\tSudenly you aproach to the dragon and spread the potion over the dragon's hurt.\n"
                    "\t\tThe dragon is healed and grateful but he cant go against his nature. And try to attack you.\n"
                    "\t\tAs you are lucky, the angel Solar appears in middle of the scene and save you teleporting out of the cavern.\n\t\tTHE END\n")
              else: #LEAVE
                  print("\n\t\tAs you contemplate the situation, you decide not to interfere with the suffering Shadow Dragon.\n"
                        "\t\tSlowly backing away, you exit the chamber, leaving the majestic creature behind.\n"
                         "\t\tAs you continue your exploration of the cave, you find the exit but you can't shake the feeling of missed opportunity\n"
                          "\t\tand wonder about the fate of the dragon.\n\t\tTHE END\n")
    else: #GO BACK
        print("\n\t\tFeeling a sense of caution, you decide to backtrack and return to the entrance of the cavern.\n"
              "\t\tAs you step away from the mysterious glow and eerie sounds, the atmosphere lightens, and you find yourself back at the cavern's entrance.\n"
              "\t\tHowever, as you stand there contemplating your next move, you realize that the cavern has subtly shifted. \n"
              "\t\tThe once-clear path back to the entrance is now shrouded in darkness. Panic sets in as you struggle to find your way back.\n"
              "\t\tIn this moment of confusion, you hear a low growl echoing through the cavern. Out of the shadows emerges a pack of shadow creatures,\n"
              "\t\tdrawn to the disturbance you caused. With limited options, you must decide quickly:")
        
        while scenario1_third.upper() not in ("ATTEMPT", "SEARCH", ):
                   scenario1_third = input("\n\t\tATTEMPT to fight the shadow creatures. SEARCH for an alternative escape route. ")

        if scenario1_third.upper() == "ATTEMPT":
              print("\n\t\t Fueled by bravery, you decide to face the approaching shadow creatures head-on.\n"
              "\t\tHowever, these creatures prove to be formidable adversaries, their dark forms swirling around you, overwhelming your senses.\n"
              "\t\tDespite your best efforts, the shadows envelop you entirely. The last thing you feel is an eerie chill before being consumed by the darkness. \n"
              "\t\tYour adventure in the mysterious cavern comes to an abrupt and unfortunate end.\n"
              "\t\tThe shadows, having claimed another victim, continue their haunting presence within the cavern,\n"
              "\t\tleaving your fate forever entwined with the enigmatic depths of the cave.\t\tTHE END\n")
        else: #SEARCH
              print("\n\t\t Your eyes dart around, searching for a hidden path to escape the encroaching shadow creatures.\n"
              "\t\t As you desperately explore the cavern's twists and turns, you stumble upon a concealed passage that leads to a small chamber bathed in dim light.\n"
              "\t\tDespite your best efforts, the shadows envelop you entirely. The last thing you feel is an eerie chill before being consumed by the darkness. \n"
              "\t\t The artifact reveals a vision of the outside world, guiding you to safety. You find yourself magically transported to the entrance of the cavern,\n"
              "\t\t untouched by the shadow creatures. The mystical fireflies have returned, lighting your way.\n\t\tTHE END\n")
             


            








