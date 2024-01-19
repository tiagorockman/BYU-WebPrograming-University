#Meal Price Calculator

child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))

sub_total_children = child_meal_price * children
sub_total_adults = adult_meal_price * adults
sub_total= sub_total_children + sub_total_adults


print(f"Subtotal: ${sub_total:.1f}")