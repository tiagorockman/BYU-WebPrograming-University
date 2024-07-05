# Values and References
# In a Python program, the computer assigns values to variables differently based on their data type. Consider the small program in example 10 and the output of that program. The program in example 10 contains two integer variables named x and y. The program in example 10 does the following:

# The statement at line 3 stores the value 17 into the variable x.
# Line 4 copies the value that is in the variable x into the variable y.
# Line 5 prints the values of x and y which are both 17.
# Line 6 adds one to the value of x, making its value 18 instead of 17.
# Line 7 prints the values of x and y again. The value of x was changed to 18. The value of y remained unchanged.
# Why does line 6 (x += 1) change the value of x but not change the value of y ? Because line 4 copies the value that was in x into y. In other words, x and y are two separate variables, each with its own value.

# Example 10
def main():
    x = 17
    y = x
    print(f"Before changing x: x {x}  y {y}")
    x += 1
    print(f"After changing x:  x {x}  y {y}")
# Call main to start this program.
if __name__ == "__main__":
    main()
