grade = int(input("What is your grade percent? "))

if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

sign = ""
last_digit = grade % 10
if letter not in ("A", "F") and last_digit >= 7:
    sign = "+"
elif letter not in ("F") and last_digit < 3:
    sign = "-"

print(f"Your letter grade is: {letter}{sign}")

passed = grade >= 70
if passed:
    print("Congratulations, you passed!")
else:
    print("Try again and good luck next time!")
