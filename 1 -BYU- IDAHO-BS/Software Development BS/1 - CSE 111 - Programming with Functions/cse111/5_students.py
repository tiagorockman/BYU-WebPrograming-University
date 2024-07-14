import csv
KEY_INUMBER = 0

def read_dictionary(filename, key_column_index):
  """Read the contents of a CSV file into a compound
  dictionary and return the dictionary.
  Parameters
      filename: the name of the CSV file to read.
      key_column_index: the index of the column
          to use as the keys in the dictionary.
  Return: a compound dictionary that contains
      the contents of the CSV file.
  """
  dictionary = {}
  with open(filename, "rt") as csv_file:
    csv_read = csv.reader(csv_file)
    #ignore first row
    next(csv_read)
    dictionary = {int(item[key_column_index]): item[1] for item in csv_read}
  return dictionary

def main():
   user_dict = read_dictionary("students.csv", KEY_INUMBER)
   print(user_dict)
   i_number = int(input("Informe o Inumber do Estudante: "))
   if i_number in user_dict.keys():
      name = user_dict[i_number]
      print(f"Student name: {name}")
   else:
      print("No such student.")

if __name__ == "__main__":
    main()