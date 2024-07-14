#5 - Exceeds requirements - Great effort until the end of the day to deliver the test.

import csv
from datetime import datetime, time


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
  with open(filename, "rt") as csv_file:
    csv_content = csv.reader(csv_file)
    next(csv_content)
    dictionary = {item[key_column_index]: item[key_column_index:] for item in csv_content}
    return dictionary

KEY_COLUMN_ID = 0
QUANTITY_COLUM_ID = 1
NAME_COLUMN_ID = 1
PRICE_COLUMN_ID = 2
SALE_TAX = 0.06


COMPANY_NAME = "Top VShape Emporium"
def main():
  #FileNotFoundError, PermissionError, and KeyError.
  try:
    current_date = datetime.now()
    quantity_total = 0
    subtotal = 0
    print(COMPANY_NAME) #Store Name
    products_dict = read_dictionary("products.csv", KEY_COLUMN_ID)
    print(products_dict)
    with open("request.csv", "rt") as receipt_file:
      csv_read = csv.reader(receipt_file)
      next(csv_read)
      # Use the requested product number to find the corresponding item in the products_dict.
      # Print the product name, requested quantity, and product price.
      for line in csv_read:
        id = line[KEY_COLUMN_ID]
        quantity = int(line[QUANTITY_COLUM_ID])
        quantity_total = quantity_total + quantity
       # if id in products_dict.keys():
        value = products_dict[id]
        name = value[NAME_COLUMN_ID]
        price = float(value[PRICE_COLUMN_ID].replace("'", ""))

        
        #Exceeding Requirements
        #Write code to discount the product prices by 10% if today is Tuesday or Wednesday.
        #Write code to discount the product prices by 10% if the current time of day is before 11:00 a.m.
        price = check_discount(price, current_date)

        subtotal = subtotal + price*quantity
        print(f"{name}: {quantity} @ {price}")
      sale_tax = (subtotal * SALE_TAX)
      total = subtotal + sale_tax
      print(f"Number of Items: {quantity_total}")
      print(f"Subtotal: {subtotal:.2f}")
      print(f"Sales tax: {sale_tax:.2f}")
      print(f"Total: {total:.2f}")
      print(f"Thank you for shopping at the {COMPANY_NAME}.")
      print(f"{current_date: %A %I:%M %p}")
      print_coupon_code(subtotal, total, quantity, current_date)
      #Write code to print at the bottom of the receipt an invitation for the customer to complete an online survey.
      print(f"You now can help us to develop. check the link http://fiae")
  except FileNotFoundError as not_found_err:
    print(not_found_err)
  except PermissionError as perm_err:
    print(perm_err)
  except KeyError as k_error:
    print(f"unknown product ID in the request.csv file \n {k_error}")
  except Exception as exc:
    print(exc)

def check_discount(price, current_date):
  weekday = current_date.weekday()
  if(weekday == 2 or weekday == 5):
     price = price - (price*0.1)

  hour = current_date.time()
  nine_AM = time(9,0)
  if(hour < nine_AM):
    price = price - (price*0.1)

  return price

def print_coupon_code(subtotal, total, quantity, current_date):
  #Write code to print a coupon at the bottom of the receipt. Write the code so that it will always print a coupon for one of the products ordered by the customer.
  coupon = str(quantity) + "A"
  if(total > 1):
    coupon = coupon + str(total)[1] + str(total)[3]
    coupon = coupon + "S"
    coupon = coupon + str(subtotal)[0] + str(subtotal)[-1]
  coupon = coupon + str(current_date.year)
  print(f"\n\n Your coupn code: {coupon}")

if __name__ == "__main__":
    main()