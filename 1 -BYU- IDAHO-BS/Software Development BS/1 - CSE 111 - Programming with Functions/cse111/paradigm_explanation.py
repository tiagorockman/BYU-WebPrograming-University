# Example 1 - Procedural
def main():
    numbers = [87, 95, 72, 92, 95, 88, 84]
    total = 0
    for x in numbers:
        total += x
    average = total / len(numbers)
    print(f"average: {average:.2f}")
# Call main to start this program.
if __name__ == "__main__":
    main()

# Example 2 - Declarative Programming
# SQL - SELECT AVG(numbers) FROM table;

# Example 3 - Functional Programming
from functools import reduce
def main():
    numbers = [87, 95, 72, 92, 95, 88, 84]
    func_add = lambda a, b: a + b
    total = reduce(func_add, numbers)
    average =  total / len(numbers)
    print(f"average: {average:.2f}")
# Call main to start this program.
if __name__ == "__main__":
    main()

# Example 4 - Object-Oriented
def main():
    numbers = [87, 95, 72, 92, 95, 88, 84]
    numbers.append(78)
    numbers.append(72)
    print(numbers)
# Call main to start this program.
if __name__ == "__main__":
    main()


#  In Python, lists are objects with attributes and methods, and a programmer can modify a list by calling those methods.
# Example 6 - Data List
def main():
    # Create a dictionary with student IDs as
    # the keys and student names as the values.
    students = {
        "42-039-4736": "Clint Huish",
        "61-315-0160": "Amelia Davis",
        "10-450-1203": "Ana Soares",
        "75-421-2310": "Abdul Ali",
        "07-103-5621": "Amelia Davis",
        "81-298-9238": "Sama Patel"
    }
    # Get a student ID from the user.
    id = input("Enter a student ID: ")
    # Lookup the student ID in the dictionary and
    # retrieve the corresponding student name.
    name = students.get(id)
    if name:
        # Print the student name.
        print(name)
        # Remove the student that the user
        # specified from the dictionary.
        students.pop(id)
    else:
        print("No such student")
    print()
    # Use a for loop to print each key value pair
    # in the dictionary. Of course, the code in
    # the body of a loop can do much more with
    # each key value pair than simply print it.
    for key, value in students.items():
        print(key, value)
# Call main to start this program.
if __name__ == "__main__":
    main()

''' Dictionary Methods
Method	    Description
d.clear()	Removes all the elements from the dictionary d.
d.copy()	Returns a copy of the dictionary d.
d.get(key)	Returns the value of the specified key. Calling the get method is almost equivalent to using square brackets ([ and ]) to find a key in a dictionary.
d.items()	Returns a list that contains the key value pairs that are in the dictionary d.
d.keys()	Returns a list that contains the keys that are in the dictionary d.
d.pop(key)	Removes the element with the specified key from the dictionary d.
d.update(other)	Updates the dictionary d with the key value pairs that are in the other dictionary.
d.values()	Returns a list that contains the values that are in the dictionary d.
'''

''' List Methods
Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''