 
items = []
#prices = []

choose = -1
while choose != 5:
    choose = int(input("\nMenu\n"
                   "1 - Add a new item\n"
                   "2 - Display the contents of the shopping cart\n"
                   "3 - Remove an item\n"
                   "4 - Compute the total\n"
                   "5 - Quit\n\n"))
    
    match choose:
        case 1:
             item = input("\nWhat item would you like to add? ")
             items.append(item)  
             #price = float(input(f"What is the price of '{item}'? "))
             #prices.append(price)
             print(f"'{item}' has been added to the cart.\n")
             input("Press enter to Continue.")
        case 2:
            print("\nThe contents of the shopping cart are:\n")
            index = 1
            for item in items:
                print(f"{index}. - {item}")
                index += 1
            input("\nPress enter to Continue.")
        case _:
            print("\nNot implmented yet. ")

