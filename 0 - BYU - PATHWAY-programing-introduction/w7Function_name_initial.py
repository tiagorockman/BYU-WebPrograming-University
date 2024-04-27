def initial_name(name, force_uppercase = True):
    initial = name[0:1]
    if (force_uppercase):
        initial = initial.upper()

    return initial

first_name = input("Enter your first name: ")
middle_name = input("Enter your middle name: ")
last_name = input("Enter your last name: ")

print("Your inital name is :" + initial_name(force_uppercase=False, name=first_name) \
      + initial_name(middle_name, False) \
        + initial_name(last_name))