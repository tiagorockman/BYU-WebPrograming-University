# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

"""
This program asks the user for
1) the name of a text file
2) a line number
and prints the text from that line of the file.
"""
def main():
    try:
        # Get a filename from the user.
        filename = input("Enter the name of text file: ")

        # Read the text file specified by the user into a list.
        text_lines = read_list(filename)

        # Get a line number from the user.
        linenum = int(input("Enter a line number: "))

        # Get the line that the user requested from the list.
        line = text_lines[linenum - 1]

        # Print the line that the user requested.
        print()
        print(line)

    except FileNotFoundError as not_found_err:
        # This code will be executed if the user enters
        # the name of a file that doesn't exist.
        print()
        print(type(not_found_err).__name__, not_found_err, sep=": ")
        print(f"The file {filename} doesn't exist.")
        print("Run the program again and enter the" \
                " name of an existing file.")

    except PermissionError as perm_err:
        # This code will be executed if the user enters the name
        # of a file and doesn't have permission to read that file.
        print()
        print(type(perm_err).__name__, perm_err, sep=": ")
        print(f"You don't have permission to read {filename}.")
        print("Run the program again and enter the name" \
                " of a file that you are allowed to read.")

    except ValueError as val_err:
        # This code will be executed if the user enters
        # an invalid integer for the line number.
        print()
        print(type(val_err).__name__, val_err, sep=": ")
        print("You entered an invalid integer for the line number.")
        print("Run the program again and enter an integer for" \
                " the line number.")

    except IndexError as index_err:
        # This code will be executed if the user enters a valid
        # integer for the line number, but the integer is greater
        # than the number of lines in the file.
        print()
        print(type(index_err).__name__, index_err, sep=": ")
        length = len(text_lines)
        if linenum < 0:
            print(f"{linenum} is a negative integer.")
        else:
            print(f"{linenum} is greater than the number" \
                    f" of lines in {filename}.")
            print(f"There are only {length} lines in {filename}.")
        print(f"Run the program again and enter a line number" \
                f" between 1 and {length}.")

    except Exception as excep:
        # This code will be executed if some
        # other type of exception occurs.
        print()
        print(type(excep).__name__, excep, sep=": ")


def read_list(filename):
    """Read the contents of a text file into a list
    and return the list that contains the lines of text.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Create an empty list named text_lines.
    text_lines = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as text_file:

        # Read the contents of the text
        # file one line at a time.
        for line in text_file:

            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()

            # Append the clean line of text
            # onto the end of the list.
            text_lines.append(clean_line)

    # Return the list that contains the lines of text.
    return text_lines


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()



# Run the get_line.py program five times and enter the input shown in the Sample Run section below. For each of the first four times that you run the program, find the lines of code in get_line.py that handled the exception that was raised.
# Sample Run
# > python get_line.py
# Enter the name of text file: notafile.csv
# FileNotFoundError: [Errno 2] No such file or directory: 'notafile.csv'
# The file notafile.csv doesn't exist.
# Run the program again and enter the name of an existing file.
# > python get_line.py
# Enter the name of text file: accidents.csv
# Enter a line number: hey
# ValueError: invalid literal for int() with base 10: 'hey'
# You entered an invalid integer for the line number.
# Run the program again and enter an integer for the line number.
# > python get_line.py
# Enter the name of text file: accidents.csv
# Enter a line number: -300
# IndexError: list index out of range
# -300 is a negative integer.
# Run the program again and enter a line number between 1 and 7.
# > python get_line.py
# Enter the name of text file: accidents.csv
# Enter a line number: 75
# IndexError: list index out of range
# 75 is greater than the number of lines in accidents.csv.
# There are only 7 lines in accidents.csv.
# Run the program again and enter a line number between 1 and 7.
# > python get_line.py
# Enter the name of text file: accidents.csv
# Enter a line number: 4
# 2012,33782,2362000,5615000,31006,3167,440,9420,6396,1262