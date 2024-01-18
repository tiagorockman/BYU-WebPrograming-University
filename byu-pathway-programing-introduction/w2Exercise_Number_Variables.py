# printing Number
days_in_fev = 8
print(str(days_in_fev) + ' days in Feb ')

first_number = '5'
second_number = '6'
print(first_number+second_number) #gonna print 56

#to calculate number as a number you need to convert it 
first_number = input('Enter first number ')
second_number = input('Enter the second number ')
print(int(first_number) + int(second_number))
print(float(first_number) + float(second_number))

#printing variable
number = 7
print(f"The number is {number}.")


#Exercise
print("\n\n\t\tExercise")

# Write a program that does the following:

# Prompt the user for their age. Convert it to a number, add one to it, and tell them how old they will be on their next birthday.

# Prompt the user for the number of egg cartons they have. Assume each carton holds 12 eggs, multiply their number by 12, and display the total number of eggs.

# Prompt the user for a number of cookies and a number of people. Then, divide the number of cookies by the number of people to determine how many cookies each person gets.

person_age = input("How old are you? ")
print("On your next birthday, you will be " + str(int(person_age)+1))


egg_cartoon = input("How many egg cartons do you have? ")
print(f"You have {int(egg_cartoon)*12} eggs")

cookies = input("How many cookies do you have? ")
people = input("How many people are there? ")
print(f"Each person may have {float(cookies)/float(people)} cookies")

#Number of Decimals to display
cars = 3
people = 8

people_per_car = people / cars

# Round to 1 decimal
print(f"There are {people_per_car:.1f} people in each car.")
# Output: There are 2.7 people in each car.

# Round to 2 decimals
print(f"There are {people_per_car:.2f} people in each car.")
# Output: There are 2.67 people in each car.

# Round to 3 decimals
print(f"There are {people_per_car:.3f} people in each car.")
# Output: There are 2.667 people in each car.


distance = 9 * 1205 * 18

# Scientific notation with 3 digits of precision
print(f"The distance is: {distance:.3e} meters.")
# Output: The distance is: 1.952e+05 meters.

# Scientific notation with 6 digits of precision
print(f"The distance is: {distance:.6e} meters.")
# Output: The distance is: 1.952100e+05 meters.

big_number = 123456789

# Display without formatting:
print(f"The number is: {big_number}")
# Output: The number is: 123456789

# Display with "," formatting:
print(f"The number is: {big_number:,}")
# Output: The number is: 123,456,789

# Display with "_" formatting:
print(f"The number is: {big_number:_}")
# Output: The number is: 123_456_789


import math

radius = 5
area = math.pi * (radius ** 2)
print(f"The area is: {area}")
# Output: The area is: 78.53981633974483


weight = 1.65

lower = math.floor(weight)
print(lower)
# Output: 1

higher = math.ceil(weight)
print(higher)
# Output: 2

#Exercise 2
print("\n\n\n\t\t\t Exercise 2")
fahrenheit = input("What is the temperature in Fahrenheit? ")
celsius = (float(fahrenheit) -32) * 5 / 9
print(f"The temperature in Celsius is {celsius:.1f} degrees.")