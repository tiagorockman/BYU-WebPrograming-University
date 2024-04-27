# I have used match that is like the switch used in another languages to control the options selected
# I used a While statement showing the name of the item and waiting for an yes or no answer from user to really remove or not the items from the lists.


items = []
prices = []

choose = -1
while choose != 5:
    print("\nMenu\n"
                   "1 - Add a new item\n"
                   "2 - Display the contents of the shopping cart\n"
                   "3 - Remove an item\n"
                   "4 - Compute the total\n"
                   "5 - Quit\n")
    choose = int(input("Type an Action from Menu above.\n\n"))
    
    match choose:
        case 1:
             item = input("\nWhat item would you like to add? ")
             items.append(item)  
             price = float(input(f"What is the price of '{item}'? "))
             prices.append(price)
             print(f"'{item}' has been added to the cart.\n")
             input("Press <ENTER> to Continue.")
        case 2:
            print("\nThe contents of the shopping cart are:\n")
            index = 1
            for item in items:
                print(f"{index}. {item} - ${prices[index-1]}")
                index += 1
            input("\nPress <ENTER> to Continue.")
        case 3:
           index_to_remove = int(input("Which item would you like to remove? "))
           
           if index_to_remove > len(prices):
               print("There is no item in the list with this ID informed.")
               input("\nPress <ENTER> to Continue.")
           else:
                index_to_remove -= 1
                item_to_be_removed = items[index_to_remove]
                print(f"Confirm if you want to delete the product {item_to_be_removed.upper()} from the chart.")
                option = -1
                while option not in range(1, 3):
                    option= int(input("1 - Yes, 2 - No: "))
                if option == 1:
                    prices.pop(index_to_remove)
                    items.pop(index_to_remove)
                    print(f"{item_to_be_removed.upper()} removed")
                input("\nPress <ENTER> to Continue.")
        case 4:
            print(f"The total price of the items in the shopping cart is ${sum(prices)}\n")
            input("\nPress <ENTER> to Continue.")
        case 5:
            print("\nThank you. Goodbye.")
        case _:
            print("\nIvalid Option. ")

